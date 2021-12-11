# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/LLVM/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .naiveCParser import naiveCParser
else:
    from naiveCParser import naiveCParser

# This class defines a complete generic visitor for a parse tree produced by naiveCParser.

class naiveCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by naiveCParser#prog.
    def visitProg(self, ctx:naiveCParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#r.
    def visitR(self, ctx:naiveCParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#realTypeID.
    def visitRealTypeID(self, ctx:naiveCParser.RealTypeIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#realTypeIDPointer.
    def visitRealTypeIDPointer(self, ctx:naiveCParser.RealTypeIDPointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:naiveCParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#typeIdentifierPointer.
    def visitTypeIdentifierPointer(self, ctx:naiveCParser.TypeIdentifierPointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#boolExpr.
    def visitBoolExpr(self, ctx:naiveCParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#idList.
    def visitIdList(self, ctx:naiveCParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:naiveCParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#PositiveINT.
    def visitPositiveINT(self, ctx:naiveCParser.PositiveINTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#TrueFalse.
    def visitTrueFalse(self, ctx:naiveCParser.TrueFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#MulDiv.
    def visitMulDiv(self, ctx:naiveCParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#AddSub.
    def visitAddSub(self, ctx:naiveCParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Parens.
    def visitParens(self, ctx:naiveCParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Int.
    def visitInt(self, ctx:naiveCParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Negative.
    def visitNegative(self, ctx:naiveCParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Char.
    def visitChar(self, ctx:naiveCParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#SizeOf.
    def visitSizeOf(self, ctx:naiveCParser.SizeOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#GetP.
    def visitGetP(self, ctx:naiveCParser.GetPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#TypeCast.
    def visitTypeCast(self, ctx:naiveCParser.TypeCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Id.
    def visitId(self, ctx:naiveCParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ArrayVisit.
    def visitArrayVisit(self, ctx:naiveCParser.ArrayVisitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#MakP.
    def visitMakP(self, ctx:naiveCParser.MakPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#FCall.
    def visitFCall(self, ctx:naiveCParser.FCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#conditionOperator.
    def visitConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#CondExp.
    def visitCondExp(self, ctx:naiveCParser.CondExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#Or.
    def visitOr(self, ctx:naiveCParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#And.
    def visitAnd(self, ctx:naiveCParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#CondOp.
    def visitCondOp(self, ctx:naiveCParser.CondOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#CondParen.
    def visitCondParen(self, ctx:naiveCParser.CondParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#CommonAssign.
    def visitCommonAssign(self, ctx:naiveCParser.CommonAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#MemoryAssign.
    def visitMemoryAssign(self, ctx:naiveCParser.MemoryAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ArrayAssign.
    def visitArrayAssign(self, ctx:naiveCParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#definition.
    def visitDefinition(self, ctx:naiveCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#callProc.
    def visitCallProc(self, ctx:naiveCParser.CallProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#returnLine.
    def visitReturnLine(self, ctx:naiveCParser.ReturnLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ParamExpr.
    def visitParamExpr(self, ctx:naiveCParser.ParamExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ParamFunc.
    def visitParamFunc(self, ctx:naiveCParser.ParamFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ParamString.
    def visitParamString(self, ctx:naiveCParser.ParamStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#paramList.
    def visitParamList(self, ctx:naiveCParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#defineParam.
    def visitDefineParam(self, ctx:naiveCParser.DefineParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#defineParamList.
    def visitDefineParamList(self, ctx:naiveCParser.DefineParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#block.
    def visitBlock(self, ctx:naiveCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#breakLine.
    def visitBreakLine(self, ctx:naiveCParser.BreakLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#continueLine.
    def visitContinueLine(self, ctx:naiveCParser.ContinueLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#statements.
    def visitStatements(self, ctx:naiveCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#whileBlock.
    def visitWhileBlock(self, ctx:naiveCParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#ifBlock.
    def visitIfBlock(self, ctx:naiveCParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#functionCall.
    def visitFunctionCall(self, ctx:naiveCParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#functionDeclare.
    def visitFunctionDeclare(self, ctx:naiveCParser.FunctionDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#functionDefine.
    def visitFunctionDefine(self, ctx:naiveCParser.FunctionDefineContext):
        return self.visitChildren(ctx)



del naiveCParser