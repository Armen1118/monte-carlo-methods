from re import A
import random
import math

def percenterror(data,actual):
  pe=abs((actual-data))*100 / abs(actual)
  return pe

#i will start by creating random points never mind where
#Create these points store them in the damn list, then ask ourselves if point is inside ellipse keep it and up a counter
#do the experiment 15 times, after each one take the value and append it into the list such that the

def random_generator():
  x=random.uniform(-2,2)
  y=random.uniform(-5,5)
  return (x,y)

def point_counter():
    total=0
    for i in range(10000):
      point=random_generator()
      x=point[0]
      y=point[1]
      if pow(x,2)/pow(2,2) + pow(y,2)/pow(5,2)<= 1:
        total=total+1
    return total

#from homework before
def mean(data):
  mean=sum(data)/len(data)
  return(mean)
#now i have a single experimented laid out
  #1) I must do it 15 times
  #2) each time i do it i must store it and eppend it to a list
  #3) i can take the average of the list to get a single number
  #4) use that number to findd the area
m=0
result=[]
while m<15:
  var=point_counter()
  result.append(var)
  m=m+1

average=mean(result)
# print(average)

def area_finder(inside_points):
  A= 40* (inside_points/10000)
  return A

montecarloarea=area_finder(average)

# print("This is the area of the ellipse per the monte carlo simulation:", montecarloarea)

# print("If we use the ellipse area formula, A=pi*a*b, we find that the", float(31.41593))

# print("We can find the accuracy of our model by looking at the percent error", percenterror(montecarloarea,31.41593))


# #Show how the uncertainty (the error) of the estimation scales with 𝑀 and with 𝑁. Fix
# 𝑁 to show the scaling with 𝑀 and fix 𝑀 to show the scaling with 𝑁.


#So lets first fix the N to 100000 and show the result if M is ran different times, we can do this by creating a list with different elements of M,
#i.e M=15,M=30 ... and each time i get to an M i update a list with the number of points specified


# for i in M:
#   newresult=[]
#   newpoint=point_counter()
#   newresult.append(newpoint)


from statistics import mean   # import function to compute the average of a list

# List of sample sizes: how many times we want to run point_counter()
M = [15, 25, 35, 45, 55]

# This will store the average result for each sample size in M
goodformath = []

# Loop over the indices of M (runs 5 times total)
for i in range(len(M)):

    n = M[i]          # number of times to run point_counter() in this experiment
    newpoints = []    # reset list to store results for THIS value of n only

    # Run the experiment n times
    for m in range(n):
        updated = point_counter()   # perform one Monte Carlo trial
        newpoints.append(updated)   # store the result

    newav = mean(newpoints)

    goodformath.append(newav)

# print(goodformath)



#im loopin 5 times,

#the loop im looping is in teh range of n which is teh index of each thing


listofstatistics=[]
for i in range(len(goodformath)):
  newstat=percenterror(area_finder(goodformath[i]), 31.41593 )
  listofstatistics.append(newstat)
print(listofstatistics)


