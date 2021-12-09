# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/LLVM/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .naiveCParser import naiveCParser
else:
    from naiveCParser import naiveCParser

# This class defines a complete listener for a parse tree produced by naiveCParser.
class naiveCListener(ParseTreeListener):

    # Enter a parse tree produced by naiveCParser#prog.
    def enterProg(self, ctx:naiveCParser.ProgContext):
        pass

    # Exit a parse tree produced by naiveCParser#prog.
    def exitProg(self, ctx:naiveCParser.ProgContext):
        pass


    # Enter a parse tree produced by naiveCParser#r.
    def enterR(self, ctx:naiveCParser.RContext):
        pass

    # Exit a parse tree produced by naiveCParser#r.
    def exitR(self, ctx:naiveCParser.RContext):
        pass


    # Enter a parse tree produced by naiveCParser#TypeInt.
    def enterTypeInt(self, ctx:naiveCParser.TypeIntContext):
        pass

    # Exit a parse tree produced by naiveCParser#TypeInt.
    def exitTypeInt(self, ctx:naiveCParser.TypeIntContext):
        pass


    # Enter a parse tree produced by naiveCParser#TypeVoid.
    def enterTypeVoid(self, ctx:naiveCParser.TypeVoidContext):
        pass

    # Exit a parse tree produced by naiveCParser#TypeVoid.
    def exitTypeVoid(self, ctx:naiveCParser.TypeVoidContext):
        pass


    # Enter a parse tree produced by naiveCParser#TypeChar.
    def enterTypeChar(self, ctx:naiveCParser.TypeCharContext):
        pass

    # Exit a parse tree produced by naiveCParser#TypeChar.
    def exitTypeChar(self, ctx:naiveCParser.TypeCharContext):
        pass


    # Enter a parse tree produced by naiveCParser#typeIdentifierPointer.
    def enterTypeIdentifierPointer(self, ctx:naiveCParser.TypeIdentifierPointerContext):
        pass

    # Exit a parse tree produced by naiveCParser#typeIdentifierPointer.
    def exitTypeIdentifierPointer(self, ctx:naiveCParser.TypeIdentifierPointerContext):
        pass


    # Enter a parse tree produced by naiveCParser#sizeof.
    def enterSizeof(self, ctx:naiveCParser.SizeofContext):
        pass

    # Exit a parse tree produced by naiveCParser#sizeof.
    def exitSizeof(self, ctx:naiveCParser.SizeofContext):
        pass


    # Enter a parse tree produced by naiveCParser#boolExpr.
    def enterBoolExpr(self, ctx:naiveCParser.BoolExprContext):
        pass

    # Exit a parse tree produced by naiveCParser#boolExpr.
    def exitBoolExpr(self, ctx:naiveCParser.BoolExprContext):
        pass


    # Enter a parse tree produced by naiveCParser#idList.
    def enterIdList(self, ctx:naiveCParser.IdListContext):
        pass

    # Exit a parse tree produced by naiveCParser#idList.
    def exitIdList(self, ctx:naiveCParser.IdListContext):
        pass


    # Enter a parse tree produced by naiveCParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:naiveCParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by naiveCParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:naiveCParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by naiveCParser#TrueFalse.
    def enterTrueFalse(self, ctx:naiveCParser.TrueFalseContext):
        pass

    # Exit a parse tree produced by naiveCParser#TrueFalse.
    def exitTrueFalse(self, ctx:naiveCParser.TrueFalseContext):
        pass


    # Enter a parse tree produced by naiveCParser#MulDiv.
    def enterMulDiv(self, ctx:naiveCParser.MulDivContext):
        pass

    # Exit a parse tree produced by naiveCParser#MulDiv.
    def exitMulDiv(self, ctx:naiveCParser.MulDivContext):
        pass


    # Enter a parse tree produced by naiveCParser#AddSub.
    def enterAddSub(self, ctx:naiveCParser.AddSubContext):
        pass

    # Exit a parse tree produced by naiveCParser#AddSub.
    def exitAddSub(self, ctx:naiveCParser.AddSubContext):
        pass


    # Enter a parse tree produced by naiveCParser#Parens.
    def enterParens(self, ctx:naiveCParser.ParensContext):
        pass

    # Exit a parse tree produced by naiveCParser#Parens.
    def exitParens(self, ctx:naiveCParser.ParensContext):
        pass


    # Enter a parse tree produced by naiveCParser#GetP.
    def enterGetP(self, ctx:naiveCParser.GetPContext):
        pass

    # Exit a parse tree produced by naiveCParser#GetP.
    def exitGetP(self, ctx:naiveCParser.GetPContext):
        pass


    # Enter a parse tree produced by naiveCParser#Id.
    def enterId(self, ctx:naiveCParser.IdContext):
        pass

    # Exit a parse tree produced by naiveCParser#Id.
    def exitId(self, ctx:naiveCParser.IdContext):
        pass


    # Enter a parse tree produced by naiveCParser#ArrayVisit.
    def enterArrayVisit(self, ctx:naiveCParser.ArrayVisitContext):
        pass

    # Exit a parse tree produced by naiveCParser#ArrayVisit.
    def exitArrayVisit(self, ctx:naiveCParser.ArrayVisitContext):
        pass


    # Enter a parse tree produced by naiveCParser#MakP.
    def enterMakP(self, ctx:naiveCParser.MakPContext):
        pass

    # Exit a parse tree produced by naiveCParser#MakP.
    def exitMakP(self, ctx:naiveCParser.MakPContext):
        pass


    # Enter a parse tree produced by naiveCParser#Int.
    def enterInt(self, ctx:naiveCParser.IntContext):
        pass

    # Exit a parse tree produced by naiveCParser#Int.
    def exitInt(self, ctx:naiveCParser.IntContext):
        pass


    # Enter a parse tree produced by naiveCParser#FCall.
    def enterFCall(self, ctx:naiveCParser.FCallContext):
        pass

    # Exit a parse tree produced by naiveCParser#FCall.
    def exitFCall(self, ctx:naiveCParser.FCallContext):
        pass


    # Enter a parse tree produced by naiveCParser#conditionOperator.
    def enterConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        pass

    # Exit a parse tree produced by naiveCParser#conditionOperator.
    def exitConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        pass


    # Enter a parse tree produced by naiveCParser#CondExp.
    def enterCondExp(self, ctx:naiveCParser.CondExpContext):
        pass

    # Exit a parse tree produced by naiveCParser#CondExp.
    def exitCondExp(self, ctx:naiveCParser.CondExpContext):
        pass


    # Enter a parse tree produced by naiveCParser#Or.
    def enterOr(self, ctx:naiveCParser.OrContext):
        pass

    # Exit a parse tree produced by naiveCParser#Or.
    def exitOr(self, ctx:naiveCParser.OrContext):
        pass


    # Enter a parse tree produced by naiveCParser#And.
    def enterAnd(self, ctx:naiveCParser.AndContext):
        pass

    # Exit a parse tree produced by naiveCParser#And.
    def exitAnd(self, ctx:naiveCParser.AndContext):
        pass


    # Enter a parse tree produced by naiveCParser#CondOp.
    def enterCondOp(self, ctx:naiveCParser.CondOpContext):
        pass

    # Exit a parse tree produced by naiveCParser#CondOp.
    def exitCondOp(self, ctx:naiveCParser.CondOpContext):
        pass


    # Enter a parse tree produced by naiveCParser#CondParen.
    def enterCondParen(self, ctx:naiveCParser.CondParenContext):
        pass

    # Exit a parse tree produced by naiveCParser#CondParen.
    def exitCondParen(self, ctx:naiveCParser.CondParenContext):
        pass


    # Enter a parse tree produced by naiveCParser#assignment.
    def enterAssignment(self, ctx:naiveCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by naiveCParser#assignment.
    def exitAssignment(self, ctx:naiveCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by naiveCParser#definition.
    def enterDefinition(self, ctx:naiveCParser.DefinitionContext):
        pass

    # Exit a parse tree produced by naiveCParser#definition.
    def exitDefinition(self, ctx:naiveCParser.DefinitionContext):
        pass


    # Enter a parse tree produced by naiveCParser#callProc.
    def enterCallProc(self, ctx:naiveCParser.CallProcContext):
        pass

    # Exit a parse tree produced by naiveCParser#callProc.
    def exitCallProc(self, ctx:naiveCParser.CallProcContext):
        pass


    # Enter a parse tree produced by naiveCParser#returnLine.
    def enterReturnLine(self, ctx:naiveCParser.ReturnLineContext):
        pass

    # Exit a parse tree produced by naiveCParser#returnLine.
    def exitReturnLine(self, ctx:naiveCParser.ReturnLineContext):
        pass


    # Enter a parse tree produced by naiveCParser#ParamExpr.
    def enterParamExpr(self, ctx:naiveCParser.ParamExprContext):
        pass

    # Exit a parse tree produced by naiveCParser#ParamExpr.
    def exitParamExpr(self, ctx:naiveCParser.ParamExprContext):
        pass


    # Enter a parse tree produced by naiveCParser#ParamFunc.
    def enterParamFunc(self, ctx:naiveCParser.ParamFuncContext):
        pass

    # Exit a parse tree produced by naiveCParser#ParamFunc.
    def exitParamFunc(self, ctx:naiveCParser.ParamFuncContext):
        pass


    # Enter a parse tree produced by naiveCParser#ParamString.
    def enterParamString(self, ctx:naiveCParser.ParamStringContext):
        pass

    # Exit a parse tree produced by naiveCParser#ParamString.
    def exitParamString(self, ctx:naiveCParser.ParamStringContext):
        pass


    # Enter a parse tree produced by naiveCParser#paramList.
    def enterParamList(self, ctx:naiveCParser.ParamListContext):
        pass

    # Exit a parse tree produced by naiveCParser#paramList.
    def exitParamList(self, ctx:naiveCParser.ParamListContext):
        pass


    # Enter a parse tree produced by naiveCParser#defineParam.
    def enterDefineParam(self, ctx:naiveCParser.DefineParamContext):
        pass

    # Exit a parse tree produced by naiveCParser#defineParam.
    def exitDefineParam(self, ctx:naiveCParser.DefineParamContext):
        pass


    # Enter a parse tree produced by naiveCParser#defineParamList.
    def enterDefineParamList(self, ctx:naiveCParser.DefineParamListContext):
        pass

    # Exit a parse tree produced by naiveCParser#defineParamList.
    def exitDefineParamList(self, ctx:naiveCParser.DefineParamListContext):
        pass


    # Enter a parse tree produced by naiveCParser#block.
    def enterBlock(self, ctx:naiveCParser.BlockContext):
        pass

    # Exit a parse tree produced by naiveCParser#block.
    def exitBlock(self, ctx:naiveCParser.BlockContext):
        pass


    # Enter a parse tree produced by naiveCParser#loopBlock.
    def enterLoopBlock(self, ctx:naiveCParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by naiveCParser#loopBlock.
    def exitLoopBlock(self, ctx:naiveCParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by naiveCParser#breakLine.
    def enterBreakLine(self, ctx:naiveCParser.BreakLineContext):
        pass

    # Exit a parse tree produced by naiveCParser#breakLine.
    def exitBreakLine(self, ctx:naiveCParser.BreakLineContext):
        pass


    # Enter a parse tree produced by naiveCParser#continueLine.
    def enterContinueLine(self, ctx:naiveCParser.ContinueLineContext):
        pass

    # Exit a parse tree produced by naiveCParser#continueLine.
    def exitContinueLine(self, ctx:naiveCParser.ContinueLineContext):
        pass


    # Enter a parse tree produced by naiveCParser#statements.
    def enterStatements(self, ctx:naiveCParser.StatementsContext):
        pass

    # Exit a parse tree produced by naiveCParser#statements.
    def exitStatements(self, ctx:naiveCParser.StatementsContext):
        pass


    # Enter a parse tree produced by naiveCParser#returnStatemts.
    def enterReturnStatemts(self, ctx:naiveCParser.ReturnStatemtsContext):
        pass

    # Exit a parse tree produced by naiveCParser#returnStatemts.
    def exitReturnStatemts(self, ctx:naiveCParser.ReturnStatemtsContext):
        pass


    # Enter a parse tree produced by naiveCParser#whileBlock.
    def enterWhileBlock(self, ctx:naiveCParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by naiveCParser#whileBlock.
    def exitWhileBlock(self, ctx:naiveCParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by naiveCParser#ifBlock.
    def enterIfBlock(self, ctx:naiveCParser.IfBlockContext):
        pass

    # Exit a parse tree produced by naiveCParser#ifBlock.
    def exitIfBlock(self, ctx:naiveCParser.IfBlockContext):
        pass


    # Enter a parse tree produced by naiveCParser#ifLoopBlock.
    def enterIfLoopBlock(self, ctx:naiveCParser.IfLoopBlockContext):
        pass

    # Exit a parse tree produced by naiveCParser#ifLoopBlock.
    def exitIfLoopBlock(self, ctx:naiveCParser.IfLoopBlockContext):
        pass


    # Enter a parse tree produced by naiveCParser#functionCall.
    def enterFunctionCall(self, ctx:naiveCParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by naiveCParser#functionCall.
    def exitFunctionCall(self, ctx:naiveCParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by naiveCParser#functionDeclare.
    def enterFunctionDeclare(self, ctx:naiveCParser.FunctionDeclareContext):
        pass

    # Exit a parse tree produced by naiveCParser#functionDeclare.
    def exitFunctionDeclare(self, ctx:naiveCParser.FunctionDeclareContext):
        pass


    # Enter a parse tree produced by naiveCParser#functionDefine.
    def enterFunctionDefine(self, ctx:naiveCParser.FunctionDefineContext):
        pass

    # Exit a parse tree produced by naiveCParser#functionDefine.
    def exitFunctionDefine(self, ctx:naiveCParser.FunctionDefineContext):
        pass



del naiveCParser