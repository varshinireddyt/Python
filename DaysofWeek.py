def solution(S,K):
	days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	index_days=[0,1,2,3,4,5,6]
	print(days.index(S))
	target_index = days.index(S)+K

	return days[target_index%7]

print(solution('Sat',23))