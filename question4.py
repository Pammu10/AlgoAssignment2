import subprocess
import glob
import pandas as pd
import os
import matplotlib.pyplot as plt

algorithms = ["bubble", "insertion", "merge", "quickmedian", "heap", "radix"]

input_files = sorted(glob.glob("inputs/*.txt"))
results = []
NUM_RUNS = 5

# Run all algorithms
for algo in algorithms:
    exe_path = os.path.join("bin", f"{algo}.exe")
    for infile in input_files:
        fname = os.path.basename(infile)
        if "notsorted" in fname:
            inptype = "Random"
        elif "sortedincreasing" in fname:
            inptype = "Sorted"
        elif "sorteddecreasing" in fname:
            inptype = "Reversed"
        else:
            inptype = "Unknown"

        n = int(fname.split("_")[-1].split(".")[0])
        times = []

        for run in range(NUM_RUNS):
            print(f"Running {algo} on {fname} (run {run+1}/{NUM_RUNS})")
            try:
                out = subprocess.check_output([exe_path, infile], text=True).strip()
                times.append(int(out))
            except:
                print("Error running", exe_path, infile)

        if times:
            avg_time = sum(times) / len(times)
            results.append([algo, n, inptype, avg_time])
            print(algo, n, inptype, "average time:", round(avg_time, 2))
        else:
            print(algo, n, inptype, "failed all runs")

df = pd.DataFrame(results, columns=["Algorithm", "N", "InputType", "AvgTimeMicroseconds"])
df.to_csv("all_results_avg.csv", index=False)
print("Results saved to all_results_avg.csv")

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

def plot_case(case: str, df: pd.DataFrame, outfile: str):
    plt.figure(figsize=(8, 6))

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
                marker="o",
                label=algo_name,
                color=algo_colors[algo],
                linewidth=2,
                linestyle=dash_map.get(arr_type_needed, "solid")
            )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (n)", fontsize=14)
    plt.ylabel("Time (μs)", fontsize=14)
    plt.title(f"All Algorithms - {case.capitalize()} Case", fontsize=16)
    plt.legend(fontsize=10)
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(outfile, format=outfile.split(".")[-1])
    plt.close()


# Generate plots
plot_case("best", df, "all_best.pdf")
plot_case("worst", df, "all_worst.pdf")
plot_case("avg", df, "all_avg.pdf")

print("PDF plots saved: all_best.pdf, all_worst.pdf, all_avg.pdf")
