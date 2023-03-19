def process_jobs():
    
    thread_times = [0] * n_threads
    job_start_times = []

    for job_duration in jobs:
        
        thread_index = thread_times.index(min(thread_times))

       
        job_start_times.append((thread_index, thread_times[thread_index]))

       
        thread_times[thread_index] += job_duration

    assert n_jobs == len(job_start_times)

    
    for thread_num, starts_at in job_start_times:
        print(f"{thread_num} {starts_at}")

# Get input from user
num_threads, num_jobs = input().split()
n_threads = int(num_threads)
n_jobs = int(num_jobs)
jobs = list(map(int, input().split()))

# Process jobs and print output
process_jobs()
