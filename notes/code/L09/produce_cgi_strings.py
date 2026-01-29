from grammars import *
from simple_grammar_fuzzer import *

for i in range(10):
    print(simple_grammar_fuzzer(grammar=CGI_GRAMMAR, max_nonterminals=10))

