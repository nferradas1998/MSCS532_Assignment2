import mergesort
import quicksort
import performance
import random


arr = list(range(1000000, 0, -1))
    
merge_sort_perf = performance.track_performance(mergesort.mergesort, arr)
print("Merge Sort Performance Metrics:", merge_sort_perf)

quick_sort_perf = performance.track_performance(quicksort.quicksort, arr)
print("Quick Sort Performance Metrics:", quick_sort_perf)


