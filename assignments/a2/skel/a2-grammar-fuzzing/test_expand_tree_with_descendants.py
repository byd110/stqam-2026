from grammar_fuzzer import *
from grammars import *

import unittest

class DescendantTtests (unittest.TestCase):
    def test_expand_tree_with_descendants(self):
        gf = GrammarFuzzer(EXPR_GRAMMAR, "<start>")
        gf.expand_node = gf.expand_node_max_cost
        derivation_tree: DerivationTree = ("<start>",
                                           [("<expr>",
                                             [("<expr>", None),
                                              (" + ", []),
                                              ("<term>", None)]
                                             )])
        gf.expand_tree_once(derivation_tree)
        # How could you test this function that uses randomness?

