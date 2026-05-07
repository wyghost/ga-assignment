import json
import os
import random
import sys

import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ga import run_ga
from fitness import onemax_fitness, knapsack_fitness


def save_combined_curve(onemax_history, knapsack_history, title, output_path):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].plot(onemax_history)
    axes[0].set_title("OneMax Fitness Curve")
    axes[0].set_xlabel("Generation")
    axes[0].set_ylabel("Best Fitness")

    axes[1].plot(knapsack_history)
    axes[1].set_title("Knapsack Fitness Curve")
    axes[1].set_xlabel("Generation")
    axes[1].set_ylabel("Best Fitness")

    fig.suptitle(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def run_onemax():
    random.seed(42)

    chromosome_length = 100

    result = run_ga(
        chromosome_length=chromosome_length,
        population_size=100,
        generations=300,
        elitism_count=2,
        crossover_probability=0.9,
        mutation_probability=1 / chromosome_length,
        fitness_function=onemax_fitness,
    )

    print("=== FP GA - OneMax ===")
    print(f"Best fitness: {result['best_fitness']}")
    print(f"Runtime: {result['runtime_seconds']:.4f} seconds")

    return result


def run_knapsack():
    random.seed(42)

    n = 100
    values = [random.randint(10, 100) for _ in range(n)]
    weights = [random.randint(5, 20) for _ in range(n)]
    capacity = int(0.4 * sum(weights))

    result = run_ga(
        chromosome_length=n,
        population_size=100,
        generations=300,
        elitism_count=2,
        crossover_probability=0.9,
        mutation_probability=1 / n,
        fitness_function=lambda c: knapsack_fitness(c, values, weights, capacity),
    )

    print("\n=== FP GA - Knapsack ===")
    print(f"Best fitness: {result['best_fitness']}")
    print(f"Runtime: {result['runtime_seconds']:.4f} seconds")

    return result


def main():
    os.makedirs("reports", exist_ok=True)

    onemax_result = run_onemax()
    knapsack_result = run_knapsack()

    save_combined_curve(
    onemax_result["fitness_history"],
    knapsack_result["fitness_history"],
    "FP GA Report",
    "reports/fp_curve.png",
)

    all_results = {
        "onemax": onemax_result,
        "knapsack": knapsack_result,
    }

    with open("reports/results_fp.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)


if __name__ == "__main__":
    main()