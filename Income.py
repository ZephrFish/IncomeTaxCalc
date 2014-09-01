# Income Tax Calculator

# Andrew Gill - 27/08/2013

# This is a mini program for calculating how much money I'll earn in a year
# Created while learning python, only for fun

# Declare Variables First
print """ 
  	Income Tax Calculator
	
	Author:    Andrew Gill
  	Created:   September 2014
	Revision:  0.1
	"""


wage_weekly =  raw_input("Please Enter The Amount You Get Paid Per Week: ") #Asks User for weekly wage
wage_monthly = int(wage_weekly) * 4  or raw_input("Please Enter Your Monthly Wage: ")# Calculates Monthly Wage based upon 4 weeks per month
wage_yearly = int(wage_monthly) * 12 #Calculates Monthly Wage based upon 12 months per year
basic_income_tax = int(wage_yearly) * 0.2  # Calculates Basic Income tax amount @ 20%
higher_income_tax = int(wage_yearly) * 0.4 # Calculates Higher Income tax amount @ 40%
print
# Begin If loop to calculate amount of income tax to be paid
if wage_yearly > 0 and wage_yearly < 32010:

    print str(basic_income_tax) + " is the basic amount of income tax you should be paying, this translates to 20%" 

    

elif wage_yearly > 32011 and wage_yearly < 150001:

   print str(higher_income_tax) + " is the higher amount of income tax you should be paying, this translates to 40%"

    

else: 

	print "You Earn Too Much!"

print	

print "You earn " + str(wage_weekly) + " Pounds Weekly" 

print "You earn " + str(wage_monthly) + " Pounds Monthly"

print "You earn " + str(wage_yearly) + " Pounds Yearly" + " before tax"


wageb_aftertax = int(wage_yearly) - int(basic_income_tax)

wageh_aftertax = int(wage_yearly) - int(higher_income_tax)

print "You will earn " + (str(wageb_aftertax) or str(wageh_aftertax)) + " pounds after tax"

raw_input("\n\nPress the Enter key to exit.")
