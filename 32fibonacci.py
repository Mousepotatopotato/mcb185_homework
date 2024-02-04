F1 = 0
F2 = 1
F3 = 0
print(F1)
print(F2)
for i in range(8):
	F3 = F1 + F2
	F1 = F2
	F2 = F3
	print(F3)
	