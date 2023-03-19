def process():
    # In a nutshell, this code works like Tetris
    threads = [0] * n_threads
    output = []
    
    for job_duration in jobs:
        # Find the thread with the shortest processing time
        thread_i = threads.index(min(threads))
        
        # Save when the job will start
        output.append((thread_i, threads[thread_i]))
        
        # Add the job duration to the thread's processing time
        threads[thread_i] += job_duration

    assert n_jobs == len(output)

    print("\n".join([f"{thread_num} {starts_at}" for thread_num, starts_at in output]))

threads_and_jobs = input().split(" ")
n_threads = int(threads_and_jobs[0])
n_jobs = int(threads_and_jobs[1])
jobs = [int(job) for job in input().split(" ")]

process()

