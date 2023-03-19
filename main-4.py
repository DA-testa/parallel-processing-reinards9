import heapq

# Take input from the user
n, m = map(int, input().split())
job_times = list(map(int, input().split()))

# Assign jobs to threads
start_times = [None] * m
thread_heap = [(0, i) for i in range(n)]  # (finish time, thread index) heap
for i in range(m):
    job_time = job_times[i]
    finish_time, thread_idx = heapq.heappop(thread_heap)
    start_times[i] = (thread_idx, finish_time)
    heapq.heappush(thread_heap, (finish_time + job_time, thread_idx))

# Print output
for thread_idx, start_time in start_times:
    print(thread_idx, start_time)
