from grammars import *
from reducer import *
from ebnf import *
import random

ASSIGNMENT_2_EBNF_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": ["<float>", "<integer>", "<not-a-number>"],
    "<float>": ["<digits>.<digits>"],
    "<integer>": ["<digits>"],
    "<not-a-number>": ["NaN"],
    "<digits>": ["<digit>+"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

ASSIGNMENT_2_BNF_GRAMMAR = convert_ebnf_grammar(ASSIGNMENT_2_EBNF_GRAMMAR)

class A2Runner(Runner):
    def run(self, inp: str) -> Tuple[str, Outcome]:
        if inp == "NaN":
            return (inp, Runner.FAIL)
        else:
            return (inp, Runner.PASS)

class EvalA2Runner(A2Runner):
    def __init__(self) -> None:
        self.parser = EarleyParser(ASSIGNMENT_2_BNF_GRAMMAR)

    def run(self, inp: str) -> Tuple[str, Outcome]:
        try:
            tree, *_ = self.parser.parse(inp)
        except SyntaxError:
            return (inp, Runner.UNRESOLVED)

        return super().run(inp)

random.seed(260213)
float_input = "100.99"
eval_a2 = EvalA2Runner()
ggr = GenerativeGrammarReducer(
    eval_a2,
    EarleyParser(ASSIGNMENT_2_BNF_GRAMMAR),
    log_test=True, log_reduce=False)

print (ggr.reduce(float_input))
