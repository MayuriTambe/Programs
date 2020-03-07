#To concatenate the three Dictionaries in one dictinory
Data1={1:10, 2:20}
Data2={3:30, 4:40}
Data3={5:50,6:60}

#using **kwargs merge the Dictionaries

conactenate="The merging of Three Dictionaries is:",{**Data1,**Data2,**Data3}
print(conactenate)