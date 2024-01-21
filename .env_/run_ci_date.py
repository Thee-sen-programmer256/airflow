from datetime import datetime

with open('./airflowlogs.txt','w') as f:
   f.write('CI/CD executed at {} + \n'.format(datetime.today()))