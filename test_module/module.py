import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class MyClass:
    def __init__(self, name):
        self.name = name

    def cleanDataExample(self):
        data = pd.read_csv('C:/Users/logan/MachineLearningTutorials/test_data.csv')
        # Check for duplicate rows
        duplicates = data.duplicated()
        print(f"Number of duplicate rows: {duplicates.sum()}")
        # Drop duplicate rows
        data = data.drop_duplicates()
        # Check for missing values
        missing = data.isnull().sum()
        print(f"Number of missing values:\n{missing}")
        # Drop rows with missing values
        data = data.dropna()
        # Correct inconsistent data (e.g. convert strings to lowercase)
        data['Name'] = data['Name'].str.lower()
        # Remove irrelevant columns
        #data = data.drop(['Name'], axis=1)

        #data.to_csv('C:/Users/logan/MachineLearningTutorials/test_module/cleaned_data.csv', index=False)
        print(data)

    def StandardScalerExample(self):
        # Feature Scaling using StandardScaler
        data = np.array([[10, 2, 5], [20, 4, 10], [30, 6, 15]])
        #data = np.array([[10, 2, 5, 27], [20, 4, 10, 84], [30, 6, 15, 62], [45, 43, 34, 92]])
        # calculate mean of each feature column
        mean = np.mean(data, axis=0)
        # prints [20.  4. 10.]
        # where the first value is the mean of the first column, the second value is the mean of the second column, etc.

        # calculate standard deviation of each feature column

        # standard deviation calculation 

        # columns of data np.array([[10, 2, 5], [20, 4, 10], [30, 6, 15]])
        # 10,20,30  2,4,6   5,10,15
        
        #Get average of each column set
        # (10+20+30)/3 = 20 ,  (2+4+6)/3 = 4, (5+10+15)/3 = 10

        # Get the difference of means of each column
        # [(10-20),(20-20), (30-20)] , [(2-4),(4-4),(6-4)], [(5-10),(10-10),(15-10)]
        # [-10, 0, 10], [-2, 0, 2], [-5, 0, 5]

        # Square each difference of means
        # [(-10)^2, (0)^2, (10)^2], [(-2)^2, (0)^2, (2)^2], [(-5)^2, (0)^2, (5)^2]
        # [100, 0, 100], [4, 0, 4], [25, 0, 25]

        # The standard deviation is equal to the square root of the mean of difference of means
        # sqr((100+0+100)/3) = 8.16496581, sqr((4+0+4)/3) = 1.63299316, sqr((25+0+25)/3) = 4.0824829


        std = np.std(data, axis=0)
        # prints [8.16496581 1.63299316 4.0824829]
        # where the first value is the standard deviation of the first column, the second value is the standard deviation of the second column, etc.

        # standardize the data using mean and standard deviation
        data_scaled = (data - mean) / std
        # prints the standardized data where each value is (value - mean) / standard deviation
        # array([[-1.22474487, -1.22474487, -1.22474487],
        #        [ 0.        ,  0.        ,  0.        ],
        #        [ 1.22474487,  1.22474487,  1.22474487]])
        print(data_scaled)

    #(data - min) / (max - min)
    def MinMaxScalaerExample(self):
        # Feature Scaling using MinMaxScaler
        data = np.array([[10, 2, 5], [20, 4, 10], [30, 6, 15]])
        #data = np.array([[10, 2, 5, 27], [20, 4, 10, 84], [30, 6, 15, 62], [45, 43, 34, 92]])
        scaler = MinMaxScaler()
        data_scaled = scaler.fit_transform(data)
        print("\nMin-Max Scaled Data:")
        print(data_scaled)









#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#c = a + b
#print(c) 
#print("")
#data = {'name': ['Alice', 'Bob', 'Charlie'],
#'age': [25, 30, 35],
#'country': ['USA', 'Canada', 'UK']}
#df = pd.DataFrame(data)
#print(df.head())
# Load data from a CSV file