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

    def eval(self, parse_tree: ExpParseTree):
        if parse_tree.left and parse_tree.right:
            math_func = self.operators[parse_tree.key]
            return math_func(self.eval(parse_tree.left), self.eval(parse_tree.right))
        else:
            return int(parse_tree.key)


# TODO: Do unit tests
exp = "((((47 + 392) * 50) - 2)) + ((3 - 1) / (136 + 14))"
exp_tree = ExpParseTree("")
exp_tree.parse(exp)
exp_tree.appear()
evaluator = ParseTreeEvaluator()
parsed_eval = evaluator.eval(exp_tree)
print(parsed_eval)
actual_result = ((((47 + 392) * 50) - 2)) + ((3 - 1) / (136 + 14))
assert parsed_eval == actual_result
