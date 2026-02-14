from grammars import *
from grammar_fuzzer import GrammarFuzzer

# fill this in
def grammar_and_symbol_with_cost_7():
    # example:
    #return (EXPR_GRAMMAR, "<start>")
    return (None, None)
# --- end

grammar_7, symbol_7 = grammar_and_symbol_with_cost_7()
gf = GrammarFuzzer(grammar_7)
assert (gf.symbol_cost(symbol_7, set()) == 7)

# fill this in too
def second_grammar_and_symbol():
    # example:
    # return (EXPR_GRAMMAR, "<start>")
    return None

def symbol_cost_with_seen_Z():
    return set()

def symbol_cost_with_seen_Y():
    return set()
# --- end

(g2, sym) = second_grammar_and_symbol()
gf2 = GrammarFuzzer(g2)
z = symbol_cost_with_seen_Z()
y = symbol_cost_with_seen_Y()
assert gf2.symbol_cost(sym, z) != gf2.symbol_cost(sym, y)
