# Generated from D:/2021autumn/Брвы/Compile/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .naiveCParser import naiveCParser
else:
    from naiveCParser import naiveCParser

# This class defines a complete listener for a parse tree produced by naiveCParser.
class naiveCListener(ParseTreeListener):

    # Enter a parse tree produced by naiveCParser#r.
    def enterR(self, ctx:naiveCParser.RContext):
        pass

    # Exit a parse tree produced by naiveCParser#r.
    def exitR(self, ctx:naiveCParser.RContext):
        pass


    # Enter a parse tree produced by naiveCParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx:naiveCParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by naiveCParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx:naiveCParser.TypeIdentifierContext):
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


    # Enter a parse tree produced by naiveCParser#expr.
    def enterExpr(self, ctx:naiveCParser.ExprContext):
        pass

    # Exit a parse tree produced by naiveCParser#expr.
    def exitExpr(self, ctx:naiveCParser.ExprContext):
        pass


    # Enter a parse tree produced by naiveCParser#conditionOperator.
    def enterConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        pass

    # Exit a parse tree produced by naiveCParser#conditionOperator.
    def exitConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        pass


    # Enter a parse tree produced by naiveCParser#conditionExpr.
    def enterConditionExpr(self, ctx:naiveCParser.ConditionExprContext):
        pass

    # Exit a parse tree produced by naiveCParser#conditionExpr.
    def exitConditionExpr(self, ctx:naiveCParser.ConditionExprContext):
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


    # Enter a parse tree produced by naiveCParser#return.
    def enterReturn(self, ctx:naiveCParser.ReturnContext):
        pass

    # Exit a parse tree produced by naiveCParser#return.
    def exitReturn(self, ctx:naiveCParser.ReturnContext):
        pass


    # Enter a parse tree produced by naiveCParser#param.
    def enterParam(self, ctx:naiveCParser.ParamContext):
        pass

    # Exit a parse tree produced by naiveCParser#param.
    def exitParam(self, ctx:naiveCParser.ParamContext):
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