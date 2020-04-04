#define flat charge for ground shipping
ground_flat = 20

#Create a variable for the cost of premium ground shipping.
premium_shipping = 125.00

#Write a function for the cost of ground shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.
def cost_ground(weight):
  cost = 0;
  if(weight <= 2):
    cost = weight * 1.5 + ground_flat
    return cost
  elif(weight > 2  and weight <= 6):
    cost = weight * 3.00 + ground_flat
    return cost
  elif(weight >6 and weight <= 10):
    cost = weight * 4.00 + ground_flat
    return cost
  else:
    cost = weight * 4.75 + ground_flat
    return cost
 
def cost_drone(weight):
  cost = 0;
  if(weight <= 2):
    cost = weight * 4.50
    return cost
  elif(weight > 2  and weight <= 6):
    cost = weight * 9.00
    return cost
  elif(weight >6 and weight <= 10):
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost

#A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
#print(cost_ground(8.4))

#A package that weighs 1.5 pounds should cost $6.75 to ship by drone
#print(cost_drone(1.5))

#Using those two functions for ground shipping cost and drone shipping cost, as well as the cost of premium ground shipping, write a function that takes one parameter, weight and prints a statement that tells the user
def total_cost(weight):
  if(cost_ground(weight) < cost_drone(weight) and cost_ground(weight) < premium_shipping ):
    return "Ground Shipping is cheaper and it will cost " + str(cost_ground(weight))
  elif(cost_ground(weight) > cost_drone(weight) and cost_drone(weight) < premium_shipping):
    return "Drone Shipping is cheaper and it will cost " + str(cost_drone(weight))
  else:
    return "Premium Shipping is cheaper and it will cost " + str(premium_shipping)
  
#What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
print(total_cost(4.8))

#What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
print(total_cost(41.5))