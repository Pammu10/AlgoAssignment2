import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_results = pd.read_csv("all_results_avg.csv")
quicksort_results = pd.read_csv("quicksort_results_avg.csv")

qs_name_map = {
    "quickfirst": "QuickSort (first pivot)",
    "quickrandom": "QuickSort (random pivot)",
    "quickmedian": "QuickSort (median pivot)"
}
quicksort_results["Algorithm"] = quicksort_results["Algorithm"].replace(qs_name_map)

all_results["InputType"] = all_results["InputType"].str.capitalize()
quicksort_results["InputType"] = quicksort_results["InputType"].str.capitalize()

df = pd.concat([all_results, quicksort_results], ignore_index=True)

def comparison_counts(algo_name, n):
    if algo_name == "Bubble Sort":
        best = n - 1
        avg = n*(n-1)/2  
        worst = n*(n-1)/2
    elif algo_name == "Insertion Sort":
        best = n - 1
        avg = (n**2 + 3*n - 4) / 4   
        worst = n*(n-1)/2
    elif algo_name == "Merge Sort":
        best = avg = worst = n*np.log2(n)*10**2
    elif algo_name == "Heap Sort":
        best = avg = worst = n*np.log2(n)*10**2
    elif algo_name == "Radix Sort":
        best = avg = worst = 0
    elif algo_name == "QuickSort (first pivot)":
        best = (n*np.log2(n)-n+1)*10**2
        avg = (2*(n+1)*(np.log(n)+0.5772) - 4*n)*10**2   
        worst = n*(n-1)/2
    elif algo_name == "QuickSort (median pivot)":
        best = (n*np.log2(n)-n+1)*10**2
        avg = (n * np.log2(n) - n + 1) * 10**2
        worst = (n*np.log2(n)-n+1)*10**2
    elif algo_name == "QuickSort (random pivot)":
        best = (n*np.log2(n)-n+1)*10**2
        avg = (2*(n+1)*(np.log(n)+0.5772) - 4*n)*10**2   
        worst = n*(n-1)/2
    else:
        best = avg = worst = n
    return best, avg, worst

df["AvgComparisons"] = df.apply(lambda row: comparison_counts(row["Algorithm"], row["N"])[1], axis=1)

df["TimePerComparison"] = df["AvgTimeMicroseconds"] / df["AvgComparisons"]

df_random = df[df["InputType"]=="Random"]

plt.figure(figsize=(10,6))
for algo in df_random["Algorithm"].unique():
    subset = df_random[df_random["Algorithm"]==algo]
    plt.plot(subset["N"], subset["TimePerComparison"], marker='o', label=f"{algo}")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Input size N")
plt.ylabel("Time per comparison (µs/comparison)")
plt.title("Time per comparison vs N (Random Input Only)")
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.savefig("time_per_comparison.pdf")
plt.show()



