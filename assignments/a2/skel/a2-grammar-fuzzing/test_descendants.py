from grammar_fuzzer import *
from grammars import *

import unittest

class DescendantTtests (unittest.TestCase):
    def test_descendants(self):
        gf = GrammarFuzzer(EXPR_GRAMMAR, "<start>")
        derivation_tree: DerivationTree = ("<start>",
                       [("<expr>",
                         [("<expr>", None),
                          (" + ", []),
                          ("<term>",
                            [("<factor>", None),
                             (" * ", []),
                             ("<term>", None)])]
                         )])
        d = gf.descendants(derivation_tree, None)
        assert d == [(('<expr>', [('<expr>', None), (' + ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)])]), ('<start>', [('<expr>', [('<expr>', None), (' + ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)])])]), 0), (('<expr>', None), ('<expr>', [('<expr>', None), (' + ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)])]), 0), ((' + ', []), ('<expr>', [('<expr>', None), (' + ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)])]), 1), (('<term>', [('<factor>', None), (' * ', []), ('<term>', None)]), ('<expr>', [('<expr>', None), (' + ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)])]), 2), (('<factor>', None), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)]), 0), ((' * ', []), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)]), 1), (('<term>', None), ('<term>', [('<factor>', None), (' * ', []), ('<term>', None)]), 2)]

    def test_descendants_aliasing_structure(self):
        gf = GrammarFuzzer(EXPR_GRAMMAR, "<start>")
        derivation_tree: DerivationTree = ("<start>",
                       [("<expr>",
                         [("<expr>", None),
                          (" + ", []),
                             ("<term>", None)]
                         )])
        d = gf.descendants(derivation_tree, None)
        # mutate something from a descendant
        d[3][1][1][2]=("<TERM>", None)
        assert derivation_tree == ('<start>', [('<expr>', [('<expr>', None), (' + ', []), ('<TERM>', None)])])
        # mutate something from the first children call
        d[0][1][1][0]=('<EXPR>', d[0][1][1][0][1])
        assert derivation_tree == ('<start>', [('<EXPR>', [('<expr>', None), (' + ', []), ('<TERM>', None)])])
