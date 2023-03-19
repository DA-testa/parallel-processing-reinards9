
import heapq     

o, r = map ( int, input().split () )

t = list(map(int, input().split()  ) )

threads = [(0, n) for n in range(o)] 

heapq.heapify (  threads)

for n in range  (r):

  
    darb= t[n]
  
    laiks, index = heapq.heappop(threads)
  
    sākas = laiks
  
    laiks += darb
  
    print(index, sākas  )
  
    heapq.heappush(threads, (  laiks, index))
