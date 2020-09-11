import bisect
from heapq import heappush, heappop, nsmallest
import decimal
from decimal import Decimal

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

rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)
rounded
