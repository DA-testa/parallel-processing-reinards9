def process():
  # in a nutshell, kods darbojas tā kā tetris
  threads = [0] * n_threads
  output = []
  for job_duration in jobs:
    # atrod piemērotāko threadu (ar vismazāko apstrādes ilgumu)
    thread_i = threads.index(min(threads))
    # saglabājam, kad darbs tiks sākts
    output.append((thread_i, threads[thread_i]))
    # pieskaita threadam darba ilgumu
    threads[thread_i] += job_duration

  assert n_jobs == len(output)

  print("\n".join([f"{thread_num} {starts_at}" for thread_num, starts_at in output]))

threads_and_jobs = input().split(" ")
n_threads = int(threads_and_jobs[0])
n_jobs = int(threads_and_jobs[1])
jobs = [int(job) for job in input().split(" ")]

process()

