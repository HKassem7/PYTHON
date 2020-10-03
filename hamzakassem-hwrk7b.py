# Hamza Kassem

def main():
	infile = open('rainfall.txt', 'r')
	rainfall = infile.readlines()
	
	infile = open('months.txt', 'r')
	month = infile.readlines()
	
	infile.close()
	
	index = 0 
	while index < len(rainfall, month):
		rainfall[index] = int(rainfall[index])
		month[index] = int(month[index])
		index += 1
	print(rainfall)
	print(month) 
	
	rainfall = ['3.18', '3.99', '3.06', '1.53', '0.53', '0.26', '0.01', '0.00', '0.16', '1.22','2.17', '5.63']
	month = ['Janurary', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	total = 0.0 
	
	for average in numbers:
		total += value 
		average = total / len(rainfall)
		print('The average monthly rainfall of the year:')
		
	print('The total rainfall of the year: ')
	print('The month in which the maximum rainfall occurs: ', max(rainfall))
	print('The month in which the minimum rainfall occurs:' , min(rainfall))
	
main()
exit - input('')
	
        


    

    

     
    
    
