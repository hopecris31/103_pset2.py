# Hope Crisafi
# Problem Set 2
# 4/11/2021

#NJW 25/26


#variable
#either single-quotes or double-quotes
#RAM
#the CPU
#17 = x


#NJW Don't comment out code that answers questions please

#1
#height = input('Enter height in inches: ')
#print('Your height is: ', height, 'inches.')

#NJW Good, but height is a number! (-1)

#2
#favoriteColor = input('Type your favorite color here: ')
#print(favoriteColor, 'is your favorite color?', favoriteColor, 'is the worst color ever!')


#3
#The result would be 11, because python follows the mathematic order of operations


#4
#python would display 5; the most recent variable assignment, because assignments are destructive


#5
#totalSales = float(input('Type projected amount of total sales here: '))
#annualProfit = .23 * totalSales
#print('The annual profit is ','{:.2f}'.format(annualProfit), 'dollars.')



#6
#acreSquareFeet = 43560
#userLandFeet = int(input('Enter total square feet: '))
#userAcres = userLandFeet / acreSquareFeet
#print('Your land is about', '{:.2f}'.format(userAcres), 'acre(s).')


#7

tax = 0.07
#subtotal = 
#itemsTotal = 
#totalTax = (itemsTotal * 0.07) + itemsTotal

#NJW You're better off using additional variables here:
#NJW one = total
#NJW two = one + newTotal
#NJW three = two + newTotal
#NJW stops variables running out of control

itemOnePrice = float(input('Item 1 Price: '))
print('subtotal: ','{:.2f}'.format(itemOnePrice))
print('tax: ','{:.2f}'.format(itemOnePrice * tax))
print('total: ','{:.2f}'.format(itemOnePrice + (itemOnePrice * tax)))

itemTwoPrice = float(input('Item 2 Price: '))
print('subtotal: ','{:.2f}'.format(itemOnePrice + itemTwoPrice))
print('tax: ','{:.2f}'.format((itemOnePrice + itemTwoPrice) * tax))
print('total: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + (itemOnePrice * tax) + (itemTwoPrice * tax)))

itemThreePrice = float(input('Item 3 Price: '))
print('total: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice))
print('tax: ','{:.2f}'.format((itemOnePrice + itemTwoPrice + itemThreePrice)* tax))
print('subtotal: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice + (itemOnePrice * tax) + (itemTwoPrice * tax) + (itemThreePrice * tax)))

itemFourPrice = float(input('Item 4 Price: '))
print('subtotal: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice))
print('tax: ','{:.2f}'.format((itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice)* tax))
print('total: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice + (itemOnePrice * tax) + (itemTwoPrice * tax) + (itemThreePrice * tax) + (itemFourPrice * tax)))

itemFivePrice = float(input('Item 5 Price: '))
print('subtotal: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice + itemFivePrice))
print('tax: ','{:.2f}'.format((itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice + itemFivePrice)* tax))
print('total: ','{:.2f}'.format(itemOnePrice + itemTwoPrice + itemThreePrice + itemFourPrice + itemFivePrice + (itemOnePrice * tax) + (itemTwoPrice * tax) + (itemThreePrice * tax) + (itemFourPrice * tax) + (itemFivePrice * tax)))




#8


#NJW DON'T do the math yourself, get the computer to do 9/5 

#tempCelcius = float(input('Enter temperature in Celcius: '))
#tempFahrenheit = (tempCelcius * 1.8) + 32
#print('Your temperature in Fahrenheit is: ',tempFahrenheit)


#9

#numShares = 2000
#amtPerShare = 40.00
#total = numShares * amtPerShare
#commission = total * 0.03
#grandTotal = total + commission
#stockInc = amtPerShare + 2.75
#stockIncTotal = stockInc * numShares
#newCommission = stockIncTotal * 0.03
#totalProfit = stockIncTotal -(newCommission + commission + total)


#print('Krista paid ','{:.2f}'.format(total), 'dollars for her stocks.')
#print('Krista paid ', '{:.2f}'.format(commission), 'dollars in commission.')
#print('Krista received ', '{:.2f}'.format(stockIncTotal), 'dollars when she sold all of her shares.')
#print('Krista paid ', '{:.2f}'.format(newCommission), 'dollars in commission when she sold.')
#print("Krista's total profit was",'{:.2f}'.format(totalProfit), "dollars.")






