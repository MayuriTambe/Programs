'''First_list=["red","green","yellow","pink"]
Second_list=["black","brown","red","yellow"]

def commom(First_list,Second_list):
    if (set(First_list))&(set(Second_list)):
            return True
print(commom(First_list,Second_list))'''
list1 = ['cat', 'dog', 'panda', 'tiger']
list2 = ['tiger', 'lion', 'monkey', 'cat']

intersection = [i for i in list1 if i in list2]

print(intersection)