import random
from fibHeapTimed import FibHeap

print('time test started')
timelog = []
values = list(range(1,50))
random.shuffle(values)
H = FibHeap()

print('\ninserting')
for v in values:
	t = H.insertNode(v, v)
	timelog = timelog + t 
for i in range(10):
	n = random.randint(50,100)
	values2 = list(range(n,100))
	random.shuffle(values2)
	H2 = FibHeap()
	for v in values2:
		H2.insertNode(v, v)
	t = H.mergeHeap(H2)
	timelog = timelog + t
print('\nextracting')
for i in range(10):
	v, k, t = H.extractMin()
	timelog = timelog + t
print('\nprinting results')
for row in timelog:
	print(row)
