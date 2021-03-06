#Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

statement_one =not (4 + 5 <= 9)

statement_two =not (8 * 2) != 20 - 4


def graduation_reqs(gpa, credits):
  #If a student meets both requirements the function should return
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  
  #If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
  if ((gpa >= 2.0) and not(credits >= 120)):
    return "You do not have enough credits to graduate."
  
  #If they have enough credits but their GPA is less than 2.0 the function should return
  if (not(gpa >= 2.0) and (credits >= 120)):
    return "Your GPA is not high enough to graduate."
  
#If they do not have enough credits and their GPA is less than 2.0, the function should return
  if (not(gpa >= 2.0) and not(credits >= 120)):
    return"You do not meet either requirement to graduate!"

