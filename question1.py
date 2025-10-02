import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("all_results_avg.csv")

# Mapping algorithm codes to pretty names
algo_names = {
    "bubble": "Bubble Sort",
    "insertion": "Insertion Sort",
    "merge": "Merge Sort",
    "quickmedian": "QuickSort (median pivot)",
    "heap": "Heap Sort",
    "radix": "Radix Sort"
}

input_colors = {
    "Random": "#1f77b4",   
    "Sorted": "#2ca02c",  
    "Reversed": "#d62728" 
}

input_markers = {
    "Random": "o",
    "Sorted": "s",
    "Reversed": "^"
}

def plot_algorithm(algo_code: str, df: pd.DataFrame, outfile: str):
    plt.figure(figsize=(8, 6))

    algo_name = algo_names[algo_code]
    sub = df[df["Algorithm"] == algo_code]

    for input_type in ["Random", "Sorted", "Reversed"]:
        s = sub[sub["InputType"] == input_type].sort_values("N")
        if not s.empty:
            plt.plot(
                s["N"],
                s["AvgTimeMicroseconds"],
                marker=input_markers[input_type],
                markersize=6,
                label=input_type,
                color=input_colors[input_type],
                linewidth=2
            )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)", fontsize=14)
    plt.ylabel("Execution Time (μs)", fontsize=14)
    plt.title(f"{algo_name} - Performance by Input Type", fontsize=16, weight="bold")
    plt.legend(title="Input Type", fontsize=11)
    plt.grid(True, which="both", linestyle="--", linewidth=0.7, alpha=0.6)
    plt.tight_layout()
    plt.savefig(outfile, format=outfile.split(".")[-1])
    plt.close()

for algo in algo_names.keys():
    plot_algorithm(algo, df, f"{algo}_cases.pdf")

print("Plots saved for question 1")