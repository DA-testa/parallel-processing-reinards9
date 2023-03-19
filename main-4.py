def process_jobs():
    # Allocate jobs to threads 
    thread_times = [0] * n_threads
    job_start_times = []

    for job_duration in jobs:
        # Find the thread with the least amount of work
        thread_index = thread_times.index(min(thread_times))

        # Record when the job will start
        job_start_times.append((thread_index, thread_times[thread_index]))

        # Add the job duration to the thread's processing time
        thread_times[thread_index] += job_duration

    assert n_jobs == len(job_start_times)

    # Print the thread numbers and job start times
    for thread_num, starts_at in job_start_times:
        print(f"{thread_num} {starts_at}")

# Get input from user
n_threads, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))

# Process jobs and print output
process_jobs()


