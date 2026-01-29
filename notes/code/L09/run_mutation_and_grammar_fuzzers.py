from grammars import *
from simple_grammar_fuzzer import *
from mutation_fuzzer import *

number_of_seeds = 10
seeds = [
    simple_grammar_fuzzer(
        grammar=URL_GRAMMAR,
        max_nonterminals=10) for i in range(number_of_seeds)]
print (seeds)
m = MutationFuzzer(seeds)
print ([m.fuzz() for i in range(20)])
