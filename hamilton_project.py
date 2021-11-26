'''
Sarah Yildirim
1/22/21
OMH
Project description: I have coded a fermi estimate. I decided to estimate how many tickets
to see Hamilton (the broadway show) are sold each year. I did this to see if the amount
of tickets sold are consistent. I enjoyed this project a lot and would definitely recommend it again.
I enjoyed applying previous topics I had learned from statistics
Sources:
https://www.hollywoodreporter.com/news/pumped-by-hamilton-broadway-box-office-hits-record-annual-high-1367-billion-959796
https://seatplan.com/new-york/richard-rodgers-theatre/
https://www.canva.com
'''

from numpy import random # this is the library used to generate data based on a normal distribution
import matplotlib.pyplot as plt # this is for graphing
import seaborn as sns # this is so the graphs are smoother


years = []

def orchestrasum(): # this is generating the orchestra seating for the theatre
	global orchestra
	orchestra = random.normal(loc=760, scale=18, size= 376) # this is the normal distribution with mean 760, sd 18, and size of 376 which is coming from 8 times 47 because there are 8 shows a week and with breaks the actors have, the show runs for only 47 weeks
	return sum(orchestra) # this returns the sum of all tickets sold in the orchestra section

def frontsum(): # this is generating the front mezzanine seating
	global front_mezzanine
	front_mezzanine = random.normal(loc=210, scale=23, size=376) # this is the normal distributoon with mean 210 (coming from an average of only 210 of the 252 seats being filled per show), sd of 23, and size of 376 (total shows a year)
	return sum(front_mezzanine) # this returns the sum of all tickets sold in the front mezzanine

def rearsum(): # this is generating the rear mezzanine seating
	global rear_mezzanine
	rear_mezzanine = random.normal(loc=190, scale=31, size=376) # this is the normal distribution with mean 190 (this is less than the front mezzanine because less people buy read mezzanine tickets), sd of 31 and size of 376
	return sum(rear_mezzanine) # this returns the sum of all tickets sold in the rear mezzanine


for x in range(1000): # this is for a total of 1000 years so we get a good estimate
	total_tickets = 0 #resetting
	total_tickets = orchestrasum() + frontsum() + rearsum() # adding up the three different sections in the theatre
	years.append(total_tickets) # adding the total tickets from one year to the list


sns.distplot(years,hist= False,color='gold') # using the seaborn to smooth the graph and I do not want a histogram printed, so false

'''
This is to make the graph of number of seats filled in the orchestra by the y axis of proportion of days in one year
'''
#sns.distplot(orchestra,hist= False,color='gold')
#plt.xlabel('Number of seats filled')
#plt.ylabel('Proportion of days in a year')

'''
This is to make the graph of number of seats filled in the front mezzanine by the y axis of proportion of days in one year
'''
#sns.distplot(front_mezzanine,hist= False,color='gold')
#plt.xlabel('Number of seats filled')
#plt.ylabel('Proportion of days in a year')

'''
This is to make the graph of number of seats filled in the rear mezzanine by the y axis of proportion of days in one year
'''
#sns.distplot(rear_mezzanine,hist= False,color='gold')
#plt.xlabel('Number of seats filled')
#plt.ylabel('Proportion of days in a year')

plt.show()

'''
Feedback:
Grace: Maybe use sns to make your graphs smoother
What I did: I imported sns in order for my graphs to look better

Ms. Healey: Make the numbers more realistic
What I did: I did not include the weeks broadway does not perform. So, instead of using 52 weeks (a whole year), I used the realistic number of 47

'''


