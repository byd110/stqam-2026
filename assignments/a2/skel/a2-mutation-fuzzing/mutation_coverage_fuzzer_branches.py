from typing import Dict, Tuple, Union, List, Any
import subprocess
import random
import time

from fuzzer import Fuzzer, Runner
from mutation_fuzzer import MutationFuzzer
from function_coverage_runner import FunctionCoverageRunner
from population_coverage import *
from crashme import crashme

class MutationCoverageFuzzerBranches(MutationFuzzer):
    """Fuzz with mutated inputs based on coverage"""

    def __init__(self, seeds: List[str],
                 min_mutations: int = 2,
                 max_mutations: int = 10) -> None:
        self.seeds = seeds
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.inputs = []
        self.reset()

    def reset(self) -> None:
        """Reset the initial population and seed index"""
        self.population = self.seeds
        self.seed_index = 0
        self.coverages_seen: Set[frozenset] = set()

    def run(self, runner: FunctionCoverageRunner) -> Any:
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome = super().run(runner)
        new_coverage = frozenset(runner.coverage())
        if outcome == Runner.PASS and new_coverage not in self.coverages_seen:
            # We have new coverage
            self.population.append(self.inp)
            self.coverages_seen.add(new_coverage)

        return result

    def fuzz(self) -> str:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.inp = self.seeds[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()

        self.inputs.append(self.inp)
        return self.inp

if __name__ == "__main__":
    seed_input = "good"
    mutation_coverage_fuzzer = MutationCoverageFuzzerBranches([seed_input])

    n = 30000
    start = time.time()
    mutation_coverage_fuzzer.runs(FunctionCoverageRunner(crashme), trials=n)
    end = time.time()
    print ("It took the mutation coverage fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n))

    _, mcf_coverage = population_coverage(mutation_coverage_fuzzer.inputs, crashme)
    mcf_max_coverage = max(mcf_coverage)
    print ("Our mutation coverage fuzzer covers %d branches." % (mcf_max_coverage))
