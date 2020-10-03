# Hamza Kassem

def main():
	infile = open('GirlNames.txt', 'r')
	Girl_Name = infile.readlines()
	
	infile = open('BoyNames.txt', 'r')
	Boy_Name = infile.readlines()
	
	infile.close()
	
	index = 0 
	while index < len(Girl_Name, Boy_Name):
		Girl_Name[index] = Girl_Name[index].rstrip('\n')
		Boy_Name[index] = Boy_Name[index].rstrip('\n')
		index += 1
	print(Girl_Name)
	print(Boy_Name)
	
	Girl_Name = ['1', '201']
	Boy_Name = ['1', '201'] 
	
	search = input('Enter G or g for Girls name, or B or b for Boys name: ')
	name = input('Enter a name: ')
	
	if name in Girl_Name:
		print(name, 'was one of the most popular.')
	else:
		print(name, 'was not one of the most popular.')

main()
exit = input('')
