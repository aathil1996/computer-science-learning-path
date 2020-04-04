hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create a variable total_price, and set it to 0.

total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print(average_price)

#Use a list comprehension to make a list called new_prices, which has each element in prices minus 5
new_prices = [price - 5 for price in prices]

#Print new_prices.
print(new_prices)

#Create a variable called total_revenue and set it to 0

total_revenue = 0

#Use a for loop to create a variable i that goes from 0 to len(hairstyles)

for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i]
  
#After your loop, print the value of total_revenue
print(total_revenue)

#find the average revenue
average_daily_revenue = total_revenue/7

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30]

#print cuts_under_30
print(cuts_under_30)

