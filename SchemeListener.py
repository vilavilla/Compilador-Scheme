# Generated from Scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SchemeParser import SchemeParser
else:
    from SchemeParser import SchemeParser

# This class defines a complete listener for a parse tree produced by SchemeParser.
class SchemeListener(ParseTreeListener):

    # Enter a parse tree produced by SchemeParser#root.
    def enterRoot(self, ctx:SchemeParser.RootContext):
        pass

    # Exit a parse tree produced by SchemeParser#root.
    def exitRoot(self, ctx:SchemeParser.RootContext):
        pass


    # Enter a parse tree produced by SchemeParser#groupExpr.
    def enterGroupExpr(self, ctx:SchemeParser.GroupExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#groupExpr.
    def exitGroupExpr(self, ctx:SchemeParser.GroupExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#variableExpr.
    def enterVariableExpr(self, ctx:SchemeParser.VariableExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#variableExpr.
    def exitVariableExpr(self, ctx:SchemeParser.VariableExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#numberExpr.
    def enterNumberExpr(self, ctx:SchemeParser.NumberExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#numberExpr.
    def exitNumberExpr(self, ctx:SchemeParser.NumberExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#stringExpr.
    def enterStringExpr(self, ctx:SchemeParser.StringExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#stringExpr.
    def exitStringExpr(self, ctx:SchemeParser.StringExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#trueExpr.
    def enterTrueExpr(self, ctx:SchemeParser.TrueExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#trueExpr.
    def exitTrueExpr(self, ctx:SchemeParser.TrueExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#falseExpr.
    def enterFalseExpr(self, ctx:SchemeParser.FalseExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#falseExpr.
    def exitFalseExpr(self, ctx:SchemeParser.FalseExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:SchemeParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:SchemeParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#ifExpr.
    def enterIfExpr(self, ctx:SchemeParser.IfExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#ifExpr.
    def exitIfExpr(self, ctx:SchemeParser.IfExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#condExpr.
    def enterCondExpr(self, ctx:SchemeParser.CondExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#condExpr.
    def exitCondExpr(self, ctx:SchemeParser.CondExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#letExpr.
    def enterLetExpr(self, ctx:SchemeParser.LetExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#letExpr.
    def exitLetExpr(self, ctx:SchemeParser.LetExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#readExpr.
    def enterReadExpr(self, ctx:SchemeParser.ReadExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#readExpr.
    def exitReadExpr(self, ctx:SchemeParser.ReadExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#displayExpr.
    def enterDisplayExpr(self, ctx:SchemeParser.DisplayExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#displayExpr.
    def exitDisplayExpr(self, ctx:SchemeParser.DisplayExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#writeExpr.
    def enterWriteExpr(self, ctx:SchemeParser.WriteExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#writeExpr.
    def exitWriteExpr(self, ctx:SchemeParser.WriteExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#newlineExpr.
    def enterNewlineExpr(self, ctx:SchemeParser.NewlineExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#newlineExpr.
    def exitNewlineExpr(self, ctx:SchemeParser.NewlineExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:SchemeParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:SchemeParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#logicalExpr.
    def enterLogicalExpr(self, ctx:SchemeParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#logicalExpr.
    def exitLogicalExpr(self, ctx:SchemeParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#carExpr.
    def enterCarExpr(self, ctx:SchemeParser.CarExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#carExpr.
    def exitCarExpr(self, ctx:SchemeParser.CarExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#cdrExpr.
    def enterCdrExpr(self, ctx:SchemeParser.CdrExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#cdrExpr.
    def exitCdrExpr(self, ctx:SchemeParser.CdrExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#consExpr.
    def enterConsExpr(self, ctx:SchemeParser.ConsExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#consExpr.
    def exitConsExpr(self, ctx:SchemeParser.ConsExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#nullExpr.
    def enterNullExpr(self, ctx:SchemeParser.NullExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#nullExpr.
    def exitNullExpr(self, ctx:SchemeParser.NullExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:SchemeParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:SchemeParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#listLiteralExpr.
    def enterListLiteralExpr(self, ctx:SchemeParser.ListLiteralExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#listLiteralExpr.
    def exitListLiteralExpr(self, ctx:SchemeParser.ListLiteralExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#emptyListExpr.
    def enterEmptyListExpr(self, ctx:SchemeParser.EmptyListExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#emptyListExpr.
    def exitEmptyListExpr(self, ctx:SchemeParser.EmptyListExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#letBindingPair.
    def enterLetBindingPair(self, ctx:SchemeParser.LetBindingPairContext):
        pass

    # Exit a parse tree produced by SchemeParser#letBindingPair.
    def exitLetBindingPair(self, ctx:SchemeParser.LetBindingPairContext):
        pass


    # Enter a parse tree produced by SchemeParser#condClauseExpr.
    def enterCondClauseExpr(self, ctx:SchemeParser.CondClauseExprContext):
        pass

    # Exit a parse tree produced by SchemeParser#condClauseExpr.
    def exitCondClauseExpr(self, ctx:SchemeParser.CondClauseExprContext):
        pass


    # Enter a parse tree produced by SchemeParser#condElseClause.
    def enterCondElseClause(self, ctx:SchemeParser.CondElseClauseContext):
        pass

    # Exit a parse tree produced by SchemeParser#condElseClause.
    def exitCondElseClause(self, ctx:SchemeParser.CondElseClauseContext):
        pass


    # Enter a parse tree produced by SchemeParser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:SchemeParser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by SchemeParser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:SchemeParser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by SchemeParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:SchemeParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by SchemeParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:SchemeParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by SchemeParser#block.
    def enterBlock(self, ctx:SchemeParser.BlockContext):
        pass

    # Exit a parse tree produced by SchemeParser#block.
    def exitBlock(self, ctx:SchemeParser.BlockContext):
        pass


    # Enter a parse tree produced by SchemeParser#expressionStmt.
    def enterExpressionStmt(self, ctx:SchemeParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by SchemeParser#expressionStmt.
    def exitExpressionStmt(self, ctx:SchemeParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by SchemeParser#assignmentStmt.
    def enterAssignmentStmt(self, ctx:SchemeParser.AssignmentStmtContext):
        pass

    # Exit a parse tree produced by SchemeParser#assignmentStmt.
    def exitAssignmentStmt(self, ctx:SchemeParser.AssignmentStmtContext):
        pass


    # Enter a parse tree produced by SchemeParser#ifStmt.
    def enterIfStmt(self, ctx:SchemeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SchemeParser#ifStmt.
    def exitIfStmt(self, ctx:SchemeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SchemeParser#ifElseStmt.
    def enterIfElseStmt(self, ctx:SchemeParser.IfElseStmtContext):
        pass

    # Exit a parse tree produced by SchemeParser#ifElseStmt.
    def exitIfElseStmt(self, ctx:SchemeParser.IfElseStmtContext):
        pass



del SchemeParser