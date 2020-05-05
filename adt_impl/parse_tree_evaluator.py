from adt_impl.expression_parse_tree import ExpParseTree
import operator


class ParseTreeEvaluator:
    def __init__(self):
        super().__init__()
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

    def evalx(self, parse_tree: ExpParseTree):
        if parse_tree.left and parse_tree.right:
            math_func = self.operators[parse_tree.key]
            return math_func(self.evalx(parse_tree.left), self.evalx(parse_tree.right))
        else:
            return int(parse_tree.key)


exp = "((((47+392) * 50)-2) + ((3-1) / (136+14)))"
dandi = ExpParseTree("")
dandi.parse(exp)
dandi.appear()
evaluator = ParseTreeEvaluator()
parsed_eval = evaluator.evalx(dandi)
print(parsed_eval)
actual_result = (((47 + 392) * 50) - 2) + ((3 - 1) / (136 + 14))
assert parsed_eval == actual_result
