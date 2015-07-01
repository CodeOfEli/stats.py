import pandas as pd 
from scipy import stats

# Create Data: 
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56''' 

# Split the string: 
data = data.splitlines()

# List Comprehension: 
data = [i.split(', ') for i in data]

# Pull the first row to be the column names: 
column_names = data[0] #the first row
# Collect the following rows:
data_rows = data[1::]

#Now we create the actual dataframe right? 
df = pd.DataFrame(data_rows, columns=column_names)

# Convert entire column from a string to a float: 
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Print out the findings: 
print "The mean for the Alcohol and Tobacco set is {} and {} respectively".format(df['Alcohol'].mean(), df['Tobacco'].mean())
print "The median for the Alcohol and Tobacco set is {} and {} respectively".format(df['Alcohol'].median(), df['Tobacco'].median())
print "The mode for the Alcohol and Tobacco set is {} and {} respectively".format(stats.mode(df['Alcohol'])[0][0], stats.mode(df['Tobacco'])[0][0])
print "The mode for the Alcohol and Tobacco set is {} and {} respectively".format(stats.mode(df['Alcohol'])[0][0], stats.mode(df['Tobacco'])[0][0])
print "The range for the Alcohol and Tobacco set is {} and {} respectively".format(max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco']))
print "The variance for the Alcohol and Tobacco set is {} and {} respectively".format(df['Alcohol'].var(), df['Tobacco'].var())
print "The standard deviation for the Alcohol and Tobacco set is {} and {} respectively".format(df['Alcohol'].std(), df['Tobacco'].std())



