import heapq
import os

# Read input values
n, m = map(int, input().split())
jobs = list(map(int, input().split()))

# Initialize variables
threads = [(0, i) for i in range(n)]
start_times = [0] * m
heapq.heapify(threads)

# Process jobs
for i in range(m):
    time, thread = heapq.heappop(threads)
    start_times[i] = time
    heapq.heappush(threads, (time + jobs[i], thread))

# Output results
output = '\n'.join([f"{i} {start_times[i]}" for i in range(m)])
with open(os.environ['OUTPUT_PATH'], 'w') as f:
    f.write(output)

