import subprocess
import glob
import pandas as pd
import os
import matplotlib.pyplot as plt

algorithms = ["quickfirst", "quickrandom", "quickmedian"]
algo_names = {
    "quickfirst": "QuickSort (first pivot)",
    "quickrandom": "QuickSort (random pivot)",
    "quickmedian": "QuickSort (median pivot)"
}
algo_colors = {
    "quickfirst": "#1f77b4",   # blue
    "quickrandom": "#ff7f0e",  # orange
    "quickmedian": "#2ca02c"   # green
}

input_files = sorted(glob.glob("inputs/*.txt"))
results = []

NUM_RUNS = 5
for algo in algorithms:
    exe_path = os.path.join("bin", f"{algo}.exe")
    for infile in input_files:
        fname = os.path.basename(infile)
        if "balanced" in fname:
            inptype = "Balanced"
        elif "notsorted" in fname:
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
            except Exception as e:
                print("Error running", exe_path, infile, ":", e)

        if times:
            avg_time = sum(times) / len(times)
            results.append([algo, n, inptype, avg_time])
            print(algo, n, inptype, "average time:", round(avg_time, 2))
        else:
            print(algo, n, inptype, "failed all runs")

df = pd.DataFrame(results, columns=["Algorithm", "N", "InputType", "AvgTimeMicroseconds"])
df.to_csv("quicksort_results_avg.csv", index=False)
print("Results saved to quicksort_results_avg.csv")

case_map = {
    "quickfirst": {"best": "Balanced", "worst": "Reversed", "average": "Random"},
    "quickrandom": {"best": "Sorted", "worst": "Random", "average": "Random"},
    "quickmedian": {"best": "Sorted", "worst": "Reversed", "average": "Random"}
}

# Marker shapes for clarity
markers = ["o", "s", "^"]
marker_map = {algo: markers[i % len(markers)] for i, algo in enumerate(algorithms)}

# === Styled plotting function ===
def plot_case(case_type: str, df: pd.DataFrame, outfile: str):
    plt.figure(figsize=(9, 7))
    
    for algo in algorithms:
        algo_name = algo_names[algo]
        input_type_needed = case_map[algo][case_type]
        
        sub = df[(df["Algorithm"] == algo) & (df["InputType"] == input_type_needed)]
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
                alpha=0.9
            )
    
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (N)", fontsize=14)
    plt.ylabel("Execution Time (μs)", fontsize=14)
    plt.title(f"Quicksort Variants - {case_type.capitalize()} Case", fontsize=16, weight="bold")
    plt.legend(fontsize=11)
    plt.grid(True, which="both", linestyle="--", linewidth=0.7, alpha=0.6)
    plt.tight_layout()
    plt.savefig(outfile, format=outfile.split(".")[-1])
    plt.close()

# Generate styled plots
plot_case("best", df, "quicksort_best.pdf")
plot_case("worst", df, "quicksort_worst.pdf")
plot_case("average", df, "quicksort_average.pdf")

print("Plots saved for question 3")
