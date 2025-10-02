import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_results_avg.csv")
algorithms = ["bubble", "insertion", "merge", "quickmedian", "heap", "radix"]

algo_names = {
    "bubble": "Bubble Sort",
    "insertion": "Insertion Sort",
    "merge": "Merge Sort",
    "quickmedian": "QuickSort (median pivot)",
    "heap": "Heap Sort",
    "radix": "Radix Sort"
}

algo_colors = {
    "bubble": "#1f77b4",
    "insertion": "#ff7f0e",
    "merge": "#2ca02c",
    "quickmedian": "#d62728",
    "heap": "#9467bd",
    "radix": "#8c564b"
}

dash_map = {"Random": "solid", "Sorted": "dashed", "Reversed": "dotted"}

case_map = {
    "Bubble Sort": {"best": "Sorted", "worst": "Reversed", "avg": "Random"},
    "Insertion Sort": {"best": "Sorted", "worst": "Reversed", "avg": "Random"},
    "Merge Sort": {"best": "Sorted", "worst": "Reversed", "avg": "Random"},
    "Heap Sort": {"best": "Random", "worst": "Reversed", "avg": "Random"},
    "Radix Sort": {"best": "Random", "worst": "Reversed", "avg": "Random"},
    "QuickSort (median pivot)": {"best": "Sorted", "worst": "Reversed", "avg": "Random"},
}

markers = ["o", "s", "^", "D", "P", "X"]
marker_map = {algo: markers[i % len(markers)] for i, algo in enumerate(algorithms)}

def plot_case(case: str, df: pd.DataFrame, outfile: str):
    plt.figure(figsize=(9, 7))

    for algo in algorithms:
        algo_name = algo_names[algo]
        arr_type_needed = case_map.get(algo_name, {}).get(case)
        if not arr_type_needed:
            continue

        sub = df[(df["Algorithm"] == algo) & (df["InputType"] == arr_type_needed)]
        if not sub.empty:
            sub = sub.sort_values("N")
            plt.plot(
                sub["N"],
                sub["AvgTimeMicroseconds"],
                marker=marker_map[algo],
                markersize=6,
                label=algo_name,
                color=algo_colors[algo],
                linewidth=2,
                linestyle=dash_map.get(arr_type_needed, "solid"),
                alpha=0.9
            )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)", fontsize=14)
    plt.ylabel("Execution Time (μs)", fontsize=14)
    plt.title(f"Sorting Algorithms - {case.capitalize()} Case", fontsize=16, weight="bold")
    plt.legend(fontsize=11, loc="best")
    plt.grid(True, which="both", linestyle="--", linewidth=0.7, alpha=0.6)
    plt.tight_layout()
    plt.savefig(outfile, format=outfile.split(".")[-1])
    plt.close()

# Generate plots
plot_case("best", df, "all_best.pdf")
plot_case("worst", df, "all_worst.pdf")
plot_case("avg", df, "all_avg.pdf")

print("Plots saved for question 4")
