import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataframe=pd.DataFrame(exam_data,labels)
print("The Original Dataframe is:\n",dataframe)

sorted_by_name=dataframe.sort_values(by=["name"],ascending=False)
print("The name of Dataframe in Descending order is:\n",sorted_by_name)

sorted_by_Score=dataframe.sort_values(by=["score"],ascending=True)
print("The score of Dataframe in Ascending order is:\n",sorted_by_Score)