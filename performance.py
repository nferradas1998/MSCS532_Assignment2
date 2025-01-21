import time
import tracemalloc

def track_performance(func, arr):

    tracemalloc.start()
    start_time = time.time()
    start_snapshot = tracemalloc.take_snapshot()
    
    result = func(arr)
    
    end_snapshot = tracemalloc.take_snapshot()
    end_time = time.time()
    tracemalloc.stop()

    mem_used = start_snapshot - end_snapshot
    memory_diff = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_used = sum(stat.size_diff for stat in memory_diff)
    
    performance = {
        "Execution Time (seconds)": end_time - start_time,
        "Total memory used (bytes)": mem_used
    }
    
    return performance