# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the previously saved results
# df = pd.read_csv("all_results_avg.csv")

# # Define the comparison counts function
# def comparison_counts(algo_name, n):
#     if algo_name == "Bubble Sort":
#         best = n - 1
#         avg = n*(n-1)/2  
#         worst = n*(n-1)/2
#     elif algo_name == "Insertion Sort":
#         best = n - 1
#         avg = (n**2 + 3*n - 4) / 4   
#         worst = n*(n-1)/2
#     elif algo_name == "Merge Sort":
#         best = avg = worst = n*np.log2(n)*10**2
#     elif algo_name == "Heap Sort":
#         best = avg = worst = n*np.log2(n)*10**2
#     elif algo_name == "Radix Sort":
#         k = np.log10(n)
#         best = avg = worst = n * k*10**2
#     elif algo_name in ["QuickSort (last pivot)", "QuickSort (first pivot)"]:
#         best = (n*np.log2(n)-n+1)*10**2
#         avg = (2*(n+1)*(np.log(n)+0.5772) - 4*n)*10**2   
#         worst = n*(n-1)/2
#     elif algo_name == "QuickSort (random pivot)":
#         best = (n*np.log2(n)-n+1)*10**2
#         avg = (2*(n+1)*(np.log(n)+0.5772) - 4*n)*10**2   
#         worst = n*(n-1)/2
#     else:
#         best = avg = worst = n
#     return best, avg, worst

# # Map InputType to case
# input_to_case = {
#     "Random": "avg",
#     "Sorted": "best",
#     "Reversed": "worst"
# }

# # Compute time per comparison
# df["Case"] = df["InputType"].map(input_to_case)
# df["TimePerComp"] = df.apply(
#     lambda row: row["AvgTimeMicroseconds"] / comparison_counts(row["Algorithm"], row["N"])[
#         {"best":0, "avg":1, "worst":2}[row["Case"]]
#     ], axis=1
# )

# # Define colors for algorithms
# algo_colors = {
#     "Bubble Sort": "#1f77b4",
#     "Insertion Sort": "#ff7f0e",
#     "Merge Sort": "#2ca02c",
#     "Heap Sort": "#9467bd",
#     "Radix Sort": "#8c564b",
#     "QuickSort (last pivot)": "#d62728",
#     "QuickSort (first pivot)": "#8c564b",
#     "QuickSort (random pivot)": "#e377c2"
# }

# # Plot Time / Comparisons vs N
# plt.figure(figsize=(10, 7))

# for algo in df["Algorithm"].unique():
#     sub = df[df["Algorithm"] == algo].sort_values("N")
#     plt.plot(sub["N"], sub["TimePerComp"], marker="o", label=algo, color=algo_colors.get(algo, "#333333"))

# plt.xscale("log")
# plt.yscale("log")
# plt.xlabel("Input size (N)", fontsize=14)
# plt.ylabel("Time per comparison (μs/comparison)", fontsize=14)
# plt.title("Time per Comparison vs Input Size", fontsize=16)
# plt.grid(True, which="both", linestyle="--", linewidth=0.5)
# plt.legend(fontsize=12)
# plt.tight_layout()
# plt.savefig("time_per_comparison.pdf")
# plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSVs
all_results = pd.read_csv("all_results_avg.csv")
quicksort_results = pd.read_csv("quicksort_results_avg.csv")

# Standardize algorithm names
qs_name_map = {
    "quickfirst": "QuickSort (first pivot)",
    "quickrandom": "QuickSort (random pivot)",
    "quickmedian": "QuickSort (median pivot)"
}
quicksort_results["Algorithm"] = quicksort_results["Algorithm"].replace(qs_name_map)

# Standardize input type names
all_results["InputType"] = all_results["InputType"].str.capitalize()
quicksort_results["InputType"] = quicksort_results["InputType"].str.capitalize()

# Merge datasets
df = pd.concat([all_results, quicksort_results], ignore_index=True)

# Your comparison count function
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

# Compute average comparisons
df["AvgComparisons"] = df.apply(lambda row: comparison_counts(row["Algorithm"], row["N"])[1], axis=1)

# Compute time per comparison
df["TimePerComparison"] = df["AvgTimeMicroseconds"] / df["AvgComparisons"]

# Filter for Random input only
df_random = df[df["InputType"]=="Random"]

# Plot
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



