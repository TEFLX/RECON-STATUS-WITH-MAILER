# -*- coding: utf-8 -*-
#script that creates the csv
from datetime import datetime
from datetime import date as d
from datetime import timedelta
print("start")
for i in range(0,30,1):
     # print(i)
     # dates = d.today()-timedelta(i)
     # print(dates)


     dates = d.today()-timedelta(i)
     times = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
     try:
         # with open('tbo_reco/logs/log_test' + str(dates) + '.txt', 'w') as f:
         #     f.write('\n')
         services2 = ['tbo_reco']
         for service in services2:
             core = 'tbo_reco/stat/stat-' + str(dates) + '.txt'
             missFiles = 'tbo_reco/error/missing-' + str(dates) + '.txt'
             # print(core)
             try:
                 with open(core, 'r') as f:
                     lines = f.read().splitlines()
                     f.close()
                 if ('1' in lines):
                     print('\n{} , {} ,  Recon Done,_'.format(dates, service))
                 else:
                     print('\n{} , {} ,  Recon yet to be Done'.format(dates, service), end='')

                     with open(missFiles, 'r') as f:
                         #add code to check if following file is emepty
                         # if yes read open error file read the last line having error and print it

                         lineList = f.read().splitlines()
                         print(',Files Missing - ', end='')
                         for line in lineList:
                             print(str(line), end=' ')

                         f.close()


             except Exception as e:
                # print("error",e)
                  pass

     except Exception as e:
        # print("error occur")
          pass