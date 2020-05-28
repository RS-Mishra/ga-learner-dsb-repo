# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter = ',',skip_header=1)
census = np.concatenate((data,new_record))


# --------------
#Code starts here
age = census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
age_std = np.std(age)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = race_0.__len__()
len_1 = race_1.__len__()
len_2 = race_2.__len__()
len_3 = race_3.__len__()
len_4 = race_4.__len__()

minority_race1 = [len_0,len_1,len_2,len_3,len_4]
minority_race = minority_race1.index(min(minority_race1))
print(minority_race)


# --------------
#Code starts here
#senior_citizen = census[:,0]
senior_citizens = census[census[:,0]>60]
print (senior_citizens)
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
avg_pay_high > avg_pay_low


