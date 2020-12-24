import csv
taxi = open("/Users/John Demetriades/Desktop/nyc_taxis.csv", "r")
taxi_list = list(csv.reader(taxi))
'''
Recap of Numpy library
'''
import numpy as np
array = np.array([[1,2],[3,4],[5,6]]) #create a 3x2 array
print(array[1,0])

'''
Single Instruction Multiple Data (SIMD) 
It helps to process multiple data by performing the same operation during a processor cycle
Vectorization
'''
taxi_list = taxi_list[1:]
overall = []
for row in taxi_list:
    each_row = []
    for item in row:
        each_row.append(item)
    overall.append(each_row)
taxi = np.array(overall) #create a numpy array of the csv file

print(taxi.shape) #prints shape of array
print(taxi[0])
print(taxi[1,2])
print(taxi[1][2])
print(taxi[1:3,1:3])
print(taxi[1:3][1:3]) #this is not the same as before, as this works only in lists and not in numpy arrays
print("Column:")
print(taxi[:,2])
print("Columns:")
print(taxi[:,[1,3,5]])

'''
Vectorised operation
'''
fare = taxi[:,9]
fees = taxi[:,10]
# total = np.array([fare[i] + fees[i] for i in range(len(fees))])
fare = fare.astype(np.float)
fees = fees.astype(np.float)
total = fare + fees

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]
trip_length_seconds = trip_length_seconds.astype(np.float)
trip_distance_miles = trip_distance_miles.astype(np.float)

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
trip_mph = trip_distance_miles/trip_length_hours

print(trip_mph.min())
print(np.min(trip_mph))
print(trip_mph.max()) #max, exists in 2 syntaxs
print(trip_mph.mean()) #mean, exists in 2 syntaxs
print(trip_mph.sum()) #sum, exists in 2 syntaxs
print(np.median(trip_mph)) #median can be found using this form only

columns = taxi[:,9:13]
columns = columns.astype(np.float)
print(columns.sum(axis=0)) #prints sum for each axis