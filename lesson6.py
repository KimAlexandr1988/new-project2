size = int(input('Введите кол-во уровней: '))

for row in range(1, size + 1):
	for col in range(1, row + 1):
		print(row, end=' ')
    
	print()
print ('Happy end')
print ('Go to sleep')
