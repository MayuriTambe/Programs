import os

print([f for f in os.listdir('/home/admin1')
       if os.path.isfile(os.path.join('/home/admin1', f))])