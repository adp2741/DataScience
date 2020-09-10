import bisect
from heapq import heappush, heappop, nsmallest

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print(heappop(a), heappop(a))

assert a[0] == nsmallest(1, a)[0] == 3

nsmallest(2, a)

x = list(range(10**6))
%timeit i = x.index(991234)
%timeit i = bisect.bisect_left(x, 991234)

bisect.bisect(x, 991234)
