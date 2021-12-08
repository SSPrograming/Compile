# Generated from D:/2021autumn/Брвы/Compile/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .naiveCParser import naiveCParser
else:
    from naiveCParser import naiveCParser

# This class defines a complete generic visitor for a parse tree produced by naiveCParser.

class naiveCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by naiveCParser#r.
    def visitR(self, ctx:naiveCParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:naiveCParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#typeIdentifierPointer.
    def visitTypeIdentifierPointer(self, ctx:naiveCParser.TypeIdentifierPointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#sizeof.
    def visitSizeof(self, ctx:naiveCParser.SizeofContext):
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


    # Visit a parse tree produced by naiveCParser#expr.
    def visitExpr(self, ctx:naiveCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#conditionOperator.
    def visitConditionOperator(self, ctx:naiveCParser.ConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#conditionExpr.
    def visitConditionExpr(self, ctx:naiveCParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#assignment.
    def visitAssignment(self, ctx:naiveCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#definition.
    def visitDefinition(self, ctx:naiveCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#callProc.
    def visitCallProc(self, ctx:naiveCParser.CallProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#return.
    def visitReturn(self, ctx:naiveCParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by naiveCParser#param.
    def visitParam(self, ctx:naiveCParser.ParamContext):
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


    # Visit a parse tree produced by naiveCParser#loopBlock.
    def visitLoopBlock(self, ctx:naiveCParser.LoopBlockContext):
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