#second time around, define all the functions i will be using

def mean(data):
  mean=sum(data)/len(data)
  return(mean)

def variance(data):
  mu=mean(data)
  total=0
  for x in data:
    total=total+(x-mu)**2
  return total/ len(data)

def kurtosis(data):
  mu=mean(data)
  var=variance(data)
  total=0
  for x in data:
    kurt=(x-mu)**4
    total=total+kurt
  return total / (len(data) * (var)**2)

def skewness(data):
  mu=mean(data)
  var=variance(data)
  total=0
  for x in data:
    kurt=(x-mu)**3
    total=total+kurt
  return total / (len(data) * (var)**(3/2) )

def percenterror(data,actual):
  pe=abs((actual-data))*100 / abs(actual)
  return pe


#a)

import numpy
import random
import matplotlib.pyplot as plt

elist=[]
for i in range (10**6):
  prng=random.random()
  elist.append(prng)

plt.hist(elist, bins=300, density=True)
plt.xlabel("Random Number")
plt.ylabel("Probability")

#b) At this point im just applying the functions ive defined on the list i created in a)
print("The mean is", mean(elist))
print("The variance is", variance(elist))
print("The skewness is", skewness(elist))
print("The kurtosis is", kurtosis(elist))

print("The percent error for the mean, variance and kurtosis is respectively",
percenterror(mean(elist),0.5),
percenterror(variance(elist), (1/12)),
percenterror(kurtosis(elist), (9/5)))

#c) using the percent error function defined above I get the values printed below. So pretty close to the actual.
#

#d)
#So this is the one i was confused for, let us pick some starting sample size 1e3 for example, then do the experiment once-> i.e find
#statistics. Then do it again for larger sample size, and repeat. At the end take the deviation and compare.

sample_size=[10**3, 10**4, 10**6]

list=[]
meandatalist=[]
variancedatalist=[]
skewnessdatalist=[]
kurtosisdatalist=[]

for i in sample_size:
 data=[random.random() for _ in range(i)]

 meandatalist.append(mean(data))
 variancedatalist.append(variance(data))
 skewnessdatalist.append(skewness(data))
 kurtosisdatalist.append(kurtosis(data))


def deviations(predicted, actual):
    return [abs(x - actual) for x in predicted]

mean_dev = deviations(meandatalist, 0.5)
var_dev  = deviations(variancedatalist, 1/12)
skew_dev = deviations(skewnessdatalist, 0.0)   # exact skew = 0
kurt_dev = deviations(kurtosisdatalist, 9/5)

print(mean_dev)
print(var_dev)
print(skew_dev)
print(kurt_dev)

import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_point_on_unit_sphere():

    u= random.random()
    v = random.random()


    theta = math.acos(1 - 2*u)
    phi = 2 * math.pi * v


    x = math.sin(theta) * math.cos(phi)
    y = math.sin(theta) * math.sin(phi)
    z = math.cos(theta)

    return (x, y, z)


points = [random_point_on_unit_sphere() for i in range(400)]

x_p=[point[0] for point in points]
y_p=[point[1] for point in points]
z_p=[point[2] for point in points]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_p, y_p, z_p, s=1)
ax.set_title('Random Points on a Unit Sphere')
plt.show()
