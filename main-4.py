import heapq


n, m = map(int, input().split())
job_times = list(map(int, input().split()))


start_times = [0] * m
thread_heap = [(0, i) for i in range(n)]  
for i, job_time in enumerate(job_times):
    finish_time, thread_idx = heapq.heappop(thread_heap)
    start_times[i] = finish_time
    heapq.heappush(thread_heap, (finish_time + job_time, thread_idx))


for i, start_time in enumerate(start_times):
    print(i, start_time)

