# a = [1, 11, 21, 1211, 111221, 
# len(a[30]) = ?
import itertools

a = ['1']
while len(a)<=30:
	next_num = ''
	for nums, ds in itertools.groupby(a[-1]):
		num = ''.join(ds)
		next_num += str(len(num)) + num[0]
	print len(next_num)
	a.append(next_num)

# 5808