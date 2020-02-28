import os
UserId=("The User ID: ",os.getuid())
print(UserId)
GroupId=("The Group ID: ",os.getegid())
print(GroupId)
Realgroup=("The Real Group ID: ",os.getgid())
print(Realgroup)
Supplement=("The Supplement ID: ",os.getgroups())
print(Supplement)