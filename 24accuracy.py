def accuracy(tp, fp, tn, fn):
	a = (tp + tn) / (tp + fp + tn + fn)
	F1 = 2*(tp / (tp + fp))*(tp / (tp + fn)) / ((tp / (tp + fp)) + (tp / (tp + fn)))
	return a, F1

print('Accuracy and F1 score are:')
print(accuracy(1, 1, 1, 1))
print(accuracy(1, 2, 5, 1))
print(accuracy(1, 1, 6, 8))
print(accuracy(2, 3, 5, 9))
print(accuracy(17, 7, 13, 12))