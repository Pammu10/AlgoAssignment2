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
    "quickfirst": "#1f77b4",
    "quickrandom": "#ff7f0e",
    "quickmedian": "#2ca02c"
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

# === Plotting with Matplotlib ===
def plot_case(case_type: str, df: pd.DataFrame, outfile: str):
    plt.figure(figsize=(8, 6))
    
    for algo in algorithms:
        algo_name = algo_names[algo]
        input_type_needed = case_map[algo][case_type]
        
        sub = df[(df["Algorithm"] == algo) & (df["InputType"] == input_type_needed)]
        if not sub.empty:
            sub = sub.sort_values("N")
            plt.plot(
                sub["N"],
                sub["AvgTimeMicroseconds"],
                marker="o",
                label=algo_name,
                color=algo_colors[algo],
                linewidth=2
            )
    
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input Size (N)", fontsize=14)
    plt.ylabel("Time (μs)", fontsize=14)
    plt.title(f"Quicksort Variants - {case_type.capitalize()} Case", fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(outfile, format=outfile.split(".")[-1])
    plt.close()

# Generate plots
plot_case("best", df, "quicksort_best.pdf")
plot_case("worst", df, "quicksort_worst.pdf")
plot_case("average", df, "quicksort_average.pdf")


print("plots saved")