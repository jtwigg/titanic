__author__ = 'Twigg'

import csv as csv
import numpy as np
import matplotlib.pyplot as plt

csv_file_object = csv.reader(open('train.csv', 'rb'))       # Load in the csv file
header = csv_file_object.next()                             # Skip the fist line as it is a header
data=[]                                                     # Create a variable to hold the data

for row in csv_file_object:                 # Skip through each row in the csv file
    data.append(row)                        # adding each row to the data variable
data = np.array(data)                       # Then convert from a list to an array

dead = data[:,1].astype(np.int)

age_data =data[:,5];
age_data[age_data == ''] = 0


age_data = age_data.astype(np.float)
average_age = age_data.mean(axis=0)

ticket_price = data[:,9].astype(np.float)
plot_data = np.column_stack((dead, age_data,ticket_price))

alive = plot_data[plot_data[0::,0] == 1]
dead = plot_data[plot_data[0::,0] == 0]

#plt.scatter(plot_data[0:,0], plot_data[0:,1], s=20, c=colors, alpha=0.5)
plt.plot(alive[0::,1], alive[0::,2] , 'ro',c='#00FF00')
plt.plot(dead[0::,1],dead[0::,2] , 'ro',c='#FF0000')
plt.show()