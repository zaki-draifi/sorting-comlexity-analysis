from __future__ import annotations

import random
import statistics
import time
from typing import Dict, List, Tuple

from .sorts import ALGORITHMS


def generate_data(n: int, seed: int) -> List[int]:
    rng = random.Random(seed)
    return [rng.randint(0, 10**6) for _ in range(n)]


def time_once(fn, data: List[int]) -> float:
    """Return elapsed time in milliseconds."""
    start = time.perf_counter()
    out = fn(data)
    end = time.perf_counter()
    # sanity check: ensure output is sorted (basic correctness)
    if out != sorted(data):
        raise ValueError("Sorting output is incorrect.")
    return (end - start) * 1000.0


def benchmark(
    sizes: List[int],
    repeats: int = 5,
    seed: int = 42,
) -> List[Tuple[str, int, float]]:
    results: List[Tuple[str, int, float]] = []

    # Pre-generate datasets per size for fairness across algorithms
    datasets: Dict[int, List[int]] = {n: generate_data(n, seed + n) for n in sizes}

    for algo in ALGORITHMS:
        for n in sizes:
            timings: List[float] = []
            data = datasets[n]
            for _ in range(repeats):
                timings.append(time_once(algo.fn, data))
            avg_ms = statistics.mean(timings)
            results.append((algo.name, n, avg_ms))
    return results


def main() -> None:
    # Keep sizes modest so the project runs fast on most machines.
    # Bubble/Insertion become slow at large n.
    sizes = [100, 300, 600, 1000, 2000]
    repeats = 5

    rows = benchmark(sizes=sizes, repeats=repeats)

    # Print as CSV-like output
    print("algorithm,n,avg_ms")
    for name, n, avg_ms in rows:
        print(f"{name},{n},{avg_ms:.3f}")


if __name__ == "__main__":
    main()
