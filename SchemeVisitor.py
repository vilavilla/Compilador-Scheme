# Generated from Scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SchemeParser import SchemeParser
else:
    from SchemeParser import SchemeParser

# This class defines a complete generic visitor for a parse tree produced by SchemeParser.

class SchemeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SchemeParser#root.
    def visitRoot(self, ctx:SchemeParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#groupExpr.
    def visitGroupExpr(self, ctx:SchemeParser.GroupExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#variableExpr.
    def visitVariableExpr(self, ctx:SchemeParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#numberExpr.
    def visitNumberExpr(self, ctx:SchemeParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#stringExpr.
    def visitStringExpr(self, ctx:SchemeParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#trueExpr.
    def visitTrueExpr(self, ctx:SchemeParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#falseExpr.
    def visitFalseExpr(self, ctx:SchemeParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:SchemeParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#ifExpr.
    def visitIfExpr(self, ctx:SchemeParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#condExpr.
    def visitCondExpr(self, ctx:SchemeParser.CondExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#letExpr.
    def visitLetExpr(self, ctx:SchemeParser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#readExpr.
    def visitReadExpr(self, ctx:SchemeParser.ReadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#displayExpr.
    def visitDisplayExpr(self, ctx:SchemeParser.DisplayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#writeExpr.
    def visitWriteExpr(self, ctx:SchemeParser.WriteExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#newlineExpr.
    def visitNewlineExpr(self, ctx:SchemeParser.NewlineExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:SchemeParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#logicalExpr.
    def visitLogicalExpr(self, ctx:SchemeParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#carExpr.
    def visitCarExpr(self, ctx:SchemeParser.CarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#cdrExpr.
    def visitCdrExpr(self, ctx:SchemeParser.CdrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#consExpr.
    def visitConsExpr(self, ctx:SchemeParser.ConsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#nullExpr.
    def visitNullExpr(self, ctx:SchemeParser.NullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#lengthExpr.
    def visitLengthExpr(self, ctx:SchemeParser.LengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#appendExpr.
    def visitAppendExpr(self, ctx:SchemeParser.AppendExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#stringAppendExpr.
    def visitStringAppendExpr(self, ctx:SchemeParser.StringAppendExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#stringLengthExpr.
    def visitStringLengthExpr(self, ctx:SchemeParser.StringLengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#stringEqualsExpr.
    def visitStringEqualsExpr(self, ctx:SchemeParser.StringEqualsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:SchemeParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#listLiteralExpr.
    def visitListLiteralExpr(self, ctx:SchemeParser.ListLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#emptyListExpr.
    def visitEmptyListExpr(self, ctx:SchemeParser.EmptyListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#letBindingPair.
    def visitLetBindingPair(self, ctx:SchemeParser.LetBindingPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#condClauseExpr.
    def visitCondClauseExpr(self, ctx:SchemeParser.CondClauseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#condElseClause.
    def visitCondElseClause(self, ctx:SchemeParser.CondElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:SchemeParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:SchemeParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#block.
    def visitBlock(self, ctx:SchemeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#expressionStmt.
    def visitExpressionStmt(self, ctx:SchemeParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:SchemeParser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#ifStmt.
    def visitIfStmt(self, ctx:SchemeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#ifElseStmt.
    def visitIfElseStmt(self, ctx:SchemeParser.IfElseStmtContext):
        return self.visitChildren(ctx)



del SchemeParser