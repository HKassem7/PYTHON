# Hamza Kassem

shares = int(input('Enter numbers of shares purchased: ')) # turns user input (string) into int immediately
price_share = float(input('Enter the price per share [in dollars]: '))
pur_comission_per = float(input('Enter the purchase comission percentage paid broker [in %]: '))
num_sold = int(input('Enter the number of shares sold: '))
sales_price = float(input('Enter the sales price per share [in dollars]: '))
sales_comission_per = float(input('Enter the sales comission percentage paid broker [in %]: '))

print("Hamza Kassem's Stock Transaction App") #used double quotes here bc i needed to print a single quote

spent = round(float(shares*price_share), 3) #value of the stocks at buying price
print('Joe Paid: $', spent, sep='') #sep ='' means it doesn't print a space, round(x,y) rounds x number to y places (acts weird bc it doens't rly round, google how it works)

pur_com = round(float(spent*(.01 * pur_comission_per)), 3) #purchase comission
print('Purchase Comission: $', pur_com, sep='')

sold = round(float(num_sold * sales_price), 3)
print('Joe sold at: $', sold, sep='')

sales_com = round(float(sold*(.01 * sales_comission_per)), 3) #sales comission
print('Sales Comission: $', sales_com, sep='')

profit = sold - spent - sales_com - pur_com #to find profit
print("Joe's profit: $", profit, sep='')
