def process_jobs():
    #
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
        print(f"Thread {thread_num} starts job at {starts_at} seconds")

# Get input from user
num_threads, num_jobs = input("Enter number of threads and jobs: ").split()
n_threads = int(num_threads)
n_jobs = int(num_jobs)
jobs = list(map(int, input("Enter job durations: ").split()))

# Process jobs and print output
process_jobs()

