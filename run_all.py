import subprocess
import glob
import os
import pandas as pd
# Algorithms
algorithms = ["bubble", "insertion", "merge", "quickmedian", "heap", "radix"]

input_files = sorted(glob.glob("inputs/*.txt"))
results = []
NUM_RUNS = 5

# Run all algorithms
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
            except:
                print("Error running", exe_path, infile)

        if times:
            avg_time = sum(times) / len(times)
            results.append([algo, n, inptype, avg_time])
            print(algo, n, inptype, "average time:", round(avg_time, 2))
        else:
            print(algo, n, inptype, "failed all runs")

# Save CSV
df = pd.DataFrame(results, columns=["Algorithm", "N", "InputType", "AvgTimeMicroseconds"])
df.to_csv("all_results_avg.csv", index=False)
print("Results saved to all_results_avg.csv")