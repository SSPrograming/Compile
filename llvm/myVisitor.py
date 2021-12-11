import re

from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_output import *
from utils.llvm_construct import *
from utils.string import *
from utils.SymbolTable import *


class MyVisitor(naiveCVisitor):
    def __init__(self):
        self.ST = SymbolTable()
        self.module = ir.Module()
        self.builder = ir.IRBuilder()
        self.while_block = None
        init_io(self.module)
        init_memory(self.module)
        init_system(self.module)

    def _getIdentifier(self, ctx, real=True):
        if real:
            if ctx.realTypeID():
                typeIdentifier = self.visit(ctx.realTypeID())
            elif ctx.realTypeIDPointer():
                typeIdentifier = self.visit(ctx.realTypeIDPointer())
            else:
                raise Exception('panic: _getIdentifier')
        else:
            if ctx.typeIdentifier():
                typeIdentifier = self.visit(ctx.typeIdentifier())
            elif ctx.typeIdentifierPointer():
                typeIdentifier = self.visit(ctx.typeIdentifierPointer())
            else:
                raise Exception('panic: _getIdentifier')
        pointer_count = typeIdentifier.count('*')
        ir_type = str2irType[typeIdentifier.replace('*', '')]
        for i in range(pointer_count):
            ir_type = ir.PointerType(ir_type)
        return ir_type

    def write(self, filename: str) -> None:
        write_ir(filename, str(self.module))

    def visitRealTypeID(self, ctx: naiveCParser.RealTypeIDContext):
        if ctx.TypeInt():
            token = ctx.TypeInt()
        elif ctx.TypeChar():
            token = ctx.TypeChar()
        elif ctx.TypeLL():
            token = ctx.TypeLL()
        elif ctx.TypeDouble():
            token = ctx.TypeDouble()
        else:
            raise Exception('panic: visitRealTypeID')
        return token.getSymbol().text

    def visitRealTypeIDPointer(self, ctx: naiveCParser.RealTypeIDPointerContext) -> str:
        realTypeIdentifier = self.visit(ctx.realTypeID())
        return realTypeIdentifier + '*'

    def visitTypeIdentifier(self, ctx: naiveCParser.TypeIdentifierContext):
        if ctx.TypeInt():
            token = ctx.TypeInt()
        elif ctx.TypeChar():
            token = ctx.TypeChar()
        elif ctx.TypeVoid():
            token = ctx.TypeVoid()
        elif ctx.TypeLL():
            token = ctx.TypeLL()
        elif ctx.TypeDouble():
            token = ctx.TypeDouble()
        else:
            raise Exception('panic: visitTypeIdentifier')
        return token.getSymbol().text

    def visitTypeIdentifierPointer(self, ctx: naiveCParser.TypeIdentifierPointerContext) -> str:
        typeIdentifier = self.visit(ctx.typeIdentifier())
        return typeIdentifier + '*'

    def visitDefinition(self, ctx: naiveCParser.DefinitionContext) -> None:
        ir_type = self._getIdentifier(ctx, real=True)
        identity = ctx.ID().getSymbol().text
        if ctx.LeftBracket() and ctx.RightBracket():
            size = int(ctx.PositiveINT().getSymbol().text)
            l_value = self.builder.alloca(ir.ArrayType(ir_type, size), name=identity)
        else:
            l_value = self.builder.alloca(ir_type, name=identity)
        self.ST.insert(identity, l_value)
        # 如果有初值
        if ctx.AssignOperator():
            r_value = self.visit(ctx.expr())
            self.builder.store(r_value, l_value)

    def visitCommonAssign(self, ctx: naiveCParser.CommonAssignContext):
        identity = ctx.ID().getSymbol().text
        l_value = self.ST.get(identity)
        if not l_value:
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '未定义的标识符: ' + identity
            print(position + error)
            raise Exception('panic: visitAssignment')
        r_value = self.visit(ctx.expr())
        self.builder.store(r_value, l_value)

    def visitTypeCast(self, ctx: naiveCParser.TypeCastContext):
        ir_type = self._getIdentifier(ctx, real=True)
        l_value = self.visit(ctx.expr())
        if isinstance(ir_type, ir.PointerType) and isinstance(l_value.type, ir.PointerType):
            cast = self.builder.bitcast(l_value, ir_type)
        elif isinstance(ir_type, ir.PointerType) and isinstance(l_value.type, ir.IntType):
            cast = self.builder.inttoptr(l_value, ir_type)
        elif isinstance(ir_type, ir.IntType) and isinstance(l_value.type, ir.PointerType):
            cast = self.builder.ptrtoint(l_value, ir_type)
        elif isinstance(ir_type, ir.IntType) and isinstance(l_value.type, ir.IntType):
            if ir_type.width < l_value.type.width:
                cast = self.builder.trunc(l_value, ir_type)
            elif ir_type.width > l_value.type.width:
                cast = self.builder.sext(l_value, ir_type)
            else:
                cast = l_value
        elif isinstance(ir_type, ir.DoubleType) and isinstance(l_value.type, ir.IntType):
            cast = self.builder.sitofp(l_value, ir_type)
        else:
            raise Exception('panic: visitTypeCast')
        return cast

    def visitArrayAssign(self, ctx: naiveCParser.ArrayAssignContext):
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if not symbol:
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '未定义的标识符: ' + identity
            print(position + error)
            raise Exception('panic: visitAssignment')
        index = self.visit(ctx.expr(0))
        if isinstance(symbol.type.pointee, ir.ArrayType):
            # 数组
            l_value = self.builder.gep(symbol, [ir.Constant(int32, 0), index])
        else:
            # 指针
            symbol = self.builder.load(symbol)
            l_value = self.builder.gep(symbol, [index])
        r_value = self.visit(ctx.expr(1))
        self.builder.store(r_value, l_value)

    def visitMulDiv(self, ctx: naiveCParser.MulDivContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left.type != right.type:
            position = 'line ' + str(ctx.start.line) + ': '
            error = '类型不匹配 -- ' + 'can\'t compute between ' + left.type + ' and ' + right.type
            print(position + error)
            raise Exception('panic: visitMulDiv')
        if ctx.op.type == naiveCParser.MUL:
            if isinstance(left.type, ir.DoubleType):
                return self.builder.fmul(left, right)
            return self.builder.mul(left, right)
        else:
            if isinstance(left.type, ir.DoubleType):
                return self.builder.fdiv(left, right)
            return self.builder.sdiv(left, right)

    def visitAddSub(self, ctx: naiveCParser.AddSubContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # 特殊处理指针加法
        if isinstance(left.type, ir.PointerType) and isinstance(left.type.pointee, ir.IntType) and \
                isinstance(right.type, ir.IntType):
            temp_l = self.builder.ptrtoint(left, int64)
            if right.type.width < 64:
                temp_r = self.builder.sext(right, int64)
            else:
                temp_r = right
            temp = self.builder.add(temp_l, self.builder.mul(ir.Constant(int64, left.type.pointee.width // 8), temp_r))
            return self.builder.inttoptr(temp, left.type)
        if left.type != right.type:
            position = 'line ' + str(ctx.start.line) + ': '
            error = '类型不匹配 -- ' + 'can\'t compute between ' + str(left.type) + ' and ' + str(right.type)
            print(position + error)
            raise Exception('panic: visitAddSub')

        if ctx.op.type == naiveCParser.ADD:
            if isinstance(left.type, ir.DoubleType):
                return self.builder.fadd(left, right)
            return self.builder.add(left, right)
        else:
            if isinstance(left.type, ir.DoubleType):
                return self.builder.fadd(left, right)
            return self.builder.sub(left, right)

    def visitNegative(self, ctx: naiveCParser.NegativeContext) -> ir.Value:
        value = self.visit(ctx.expr())
        if isinstance(value.type, ir.DoubleType):
            return self.builder.fneg(value)
        return self.builder.neg(value)

    def visitGetP(self, ctx: naiveCParser.GetPContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return symbol
        else:
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '未定义的标识符: ' + identity
            print(position + error)
            raise Exception('panic: visitGetP')

    def visitMakP(self, ctx: naiveCParser.MakPContext) -> ir.Value:
        r_value = self.visit(ctx.expr())
        if not isinstance(r_value.type, ir.PointerType):
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '不是指针类型，解引用失败'
            print(position + error)
            raise Exception('panic: visitMakP')
        return self.builder.load(r_value)

    def visitPositiveINT(self, ctx: naiveCParser.PositiveINTContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.PositiveINT().getSymbol().text))

    def visitChar(self, ctx: naiveCParser.CharContext):
        symbol = ctx.Char().getSymbol().text
        return ir.Constant(char, ord(convert_char(symbol)))

    def visitInt(self, ctx: naiveCParser.IntContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.INT().getSymbol().text))

    def visitId(self, ctx: naiveCParser.IdContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return self.builder.load(symbol)
        else:
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '未定义的标识符: ' + identity
            print(position + error)
            raise Exception('panic: visitId')

    def visitSizeOf(self, ctx: naiveCParser.SizeOfContext) -> ir.Constant:
        identifier = self.visit(ctx.typeIdentifier())
        ir_type = str2irType[identifier]
        return ir.Constant(int32, ir_type.width)

    def visitArrayVisit(self, ctx: naiveCParser.ArrayVisitContext):
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            index = self.visit(ctx.expr())
            if isinstance(symbol.type.pointee, ir.ArrayType):
                # 数组
                l_value = self.builder.gep(symbol, [ir.Constant(int32, 0), index])
            else:
                # 指针
                symbol = self.builder.load(symbol)
                l_value = self.builder.gep(symbol, [index])
            return self.builder.load(l_value)
        else:
            position = 'line ' + str(ctx.start.line) + ': '
            error = position + '未定义的标识符: ' + identity
            print(position + error)
            raise Exception('panic: visitId')

    def visitParens(self, ctx: naiveCParser.ParensContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitBoolExpr(self, ctx: naiveCParser.BoolExprContext) -> ir.Constant:
        if ctx.TRUE():
            return ir.Constant(boolean, True)
        elif ctx.FALSE():
            return ir.Constant(boolean, False)
        raise Exception('panic: visitBoolExpr')

    def visitConditionOperator(self, ctx: naiveCParser.ConditionOperatorContext) -> str:
        return ctx.getChild(0).getSymbol().text

    def visitAnd(self, ctx: naiveCParser.AndContext) -> boolean:
        value0 = self.visit(ctx.conditionExpr(0))
        value1 = self.visit(ctx.conditionExpr(1))
        return self.builder.and_(value0, value1)

    def visitOr(self, ctx: naiveCParser.OrContext) -> boolean:
        value0 = self.visit(ctx.conditionExpr(0))
        value1 = self.visit(ctx.conditionExpr(1))
        return self.builder.or_(value0, value1)

    def visitCondParen(self, ctx: naiveCParser.CondParenContext) -> boolean:
        return self.visit(ctx.conditionExpr())

    def visitCondOp(self, ctx: naiveCParser.CondOpContext) -> boolean:
        value0 = self.visit(ctx.expr(0))
        value1 = self.visit(ctx.expr(1))
        return self.builder.icmp_signed(self.visit(ctx.conditionOperator()), value0, value1)

    def visitCondExp(self, ctx: naiveCParser.CondExpContext) -> boolean:
        value = self.visit(ctx.expr())
        return self.builder.icmp_signed('!=', value, ir.Constant(value.type, 0))

    def visitReturnLine(self, ctx: naiveCParser.ReturnLineContext) -> None:
        if ctx.expr():
            value = self.visit(ctx.expr())
            self.builder.ret(value)
        else:
            self.builder.ret_void()

    def visitParamExpr(self, ctx: naiveCParser.ParamExprContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitParamFunc(self, ctx: naiveCParser.ParamFuncContext) -> ir.Value:
        return self.visit(ctx.functionCall())

    def visitParamString(self, ctx: naiveCParser.ParamStringContext) -> ir.Value:
        string = ctx.String().getSymbol().text
        g_string = add_global_string_constant(self.module, convert_str(string))
        return self.builder.gep(g_string, [ir.Constant(int32, 0), ir.Constant(int32, 0)], inbounds=True)

    def visitParamList(self, ctx: naiveCParser.ParamListContext) -> []:
        if not ctx.param():
            return []
        param = self.visit(ctx.param())
        if ctx.paramList():
            paramList = self.visit(ctx.paramList())
            paramList.append(param)
            return paramList
        else:
            return [param]

    def visitDefineParam(self, ctx: naiveCParser.DefineParamContext):
        typeIdentifier = self._getIdentifier(ctx, real=False)
        identity = ctx.ID().getSymbol().text
        return {'type': typeIdentifier, 'name': identity}

    def visitDefineParamList(self, ctx: naiveCParser.DefineParamListContext):
        if not ctx.defineParam():
            return []
        param = self.visit(ctx.defineParam())
        if ctx.defineParamList():
            paramList = self.visit(ctx.defineParamList())
            paramList.append(param)
            return paramList
        else:
            return [param]

    def visitFunctionCall(self, ctx: naiveCParser.FunctionCallContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        func = self.module.get_global(identity)
        _paramsList = self.visit(ctx.paramList())
        paramsList = []
        for param in _paramsList:
            if isinstance(param.type, ir.ArrayType):
                _identity = re.findall('%"(.*?)"', str(param))[1]
                symbol = self.ST.get(_identity)
                if not symbol:
                    position = 'line ' + str(ctx.start.line) + ': '
                    error = position + '未定义的标识符: ' + _identity
                    print(position + error)
                    raise Exception('panic: visitId')
                paramsList.append(self.builder.gep(symbol, [ir.Constant(int32, 0), ir.Constant(int32, 0)]))
            else:
                paramsList.append(param)
        try:
            ret = self.builder.call(func, paramsList)
        except TypeError:
            position = 'line ' + str(ctx.start.line) + ': '
            error = '参数类型不匹配'
            print(position + error)
            raise 'panic: visitFunctionCall'
        return ret

    def visitFunctionDeclare(self, ctx: naiveCParser.FunctionDeclareContext) -> None:
        typeIdentifier = str2irType[self.visit(ctx.typeIdentifier())]
        identity = ctx.ID().getSymbol().text
        self.ST = SymbolTable(self.ST)
        paramList = self.visit(ctx.defineParamList())
        paramListType = [item['type'] for item in paramList]
        func_ty = ir.FunctionType(typeIdentifier, paramListType)
        if self.module.get_unique_name(identity) == identity:
            ir.Function(self.module, func_ty, name=identity)
        else:
            func = self.module.get_global(identity)
            if func.ftype != func_ty:
                position = 'line ' + str(ctx.start.line) + ': '
                error = '函数类型不匹配 -- ' + 'expect "' + str(func.ftype) + '" but get "' + str(func_ty) + '"'
                print(position + error)
                raise Exception('panic: visitFunctionDeclare')

    def visitFunctionDefine(self, ctx: naiveCParser.FunctionDefineContext) -> None:
        typeIdentifier = str2irType[self.visit(ctx.typeIdentifier())]
        identity = ctx.ID().getSymbol().text
        self.ST = SymbolTable(self.ST)
        paramList = self.visit(ctx.defineParamList())
        paramListType = [item['type'] for item in paramList]
        func_ty = ir.FunctionType(typeIdentifier, paramListType)
        if self.module.get_unique_name(identity) == identity:
            func = ir.Function(self.module, func_ty, name=identity)
        else:
            func = self.module.get_global(identity)
            if func.ftype != func_ty:
                position = 'line ' + str(ctx.start.line) + ': '
                error = '函数类型不匹配 -- ' + 'expect "' + str(func.ftype) + '" but get "' + str(func_ty) + '"'
                print(position + error)
                raise Exception('panic: visitFunctionDefine')
        block = func.append_basic_block(name='entry')
        if len(paramList) != len(func.args):
            print('系统错误！')
            raise Exception('panic: visitFunctionDefine')
        self.builder.position_at_end(block)
        for i in range(len(func.args)):
            param = self.builder.alloca(func.args[i].type)
            self.builder.store(func.args[i], param)
            self.ST.insert(paramList[i]['name'], param)
        self.visit(ctx.block())
        self.ST = self.ST.prev()

    def visitBlock(self, ctx: naiveCParser.BlockContext) -> None:
        self.ST = SymbolTable(self.ST)
        self.visit(ctx.statements())
        self.ST = self.ST.prev()

    def _visitIfBlock(self, ctx: naiveCParser.IfBlockContext, i) -> None:
        if i == len(ctx.conditionExpr()):
            if ctx.block(i):
                self.visit(ctx.block(i))
            return
        cond = self.visit(ctx.conditionExpr(i))
        with self.builder.if_else(cond) as (then, otherwise):
            with then:
                self.visit(ctx.block(i))
            with otherwise:
                self._visitIfBlock(ctx, i + 1)

    def visitIfBlock(self, ctx: naiveCParser.IfBlockContext) -> None:
        self._visitIfBlock(ctx, 0)

    def visitWhileBlock(self, ctx: naiveCParser.WhileBlockContext) -> None:
        while_cond = self.builder.append_basic_block(name='while_cond')
        while_begin = self.builder.append_basic_block(name='while_begin')
        while_end = self.builder.append_basic_block(name='while_end')
        self.while_block = {
            'cond': while_cond,
            'begin': while_begin,
            'end': while_end,
            'outer': self.while_block
        }
        self.builder.branch(while_cond)
        self.builder.position_at_start(while_cond)
        cond = self.visit(ctx.conditionExpr())
        self.builder.cbranch(cond, while_begin, while_end)
        self.builder.position_at_start(while_begin)
        self.visit(ctx.block())
        cond = self.visit(ctx.conditionExpr())
        self.builder.cbranch(cond, while_begin, while_end)
        self.builder.position_at_end(while_end)
        self.while_block = self.while_block['outer']

    def visitBreakLine(self, ctx: naiveCParser.BreakLineContext) -> None:
        if not self.while_block:
            position = 'line ' + str(ctx.start.line) + ': '
            error = '此处不允许使用break'
            print(position, error)
            raise Exception('panic: visitBreakLine')
        else:
            self.builder.branch(self.while_block['end'])

    def visitContinueLine(self, ctx: naiveCParser.ContinueLineContext):
        if not self.while_block:
            position = 'line ' + str(ctx.start.line) + ': '
            error = '此处不允许使用continue'
            print(position, error)
            raise Exception('panic: visitContinueLine')
        else:
            self.builder.branch(self.while_block['begin'])
