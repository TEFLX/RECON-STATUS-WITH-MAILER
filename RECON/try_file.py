import pandas as pd
from IPython.display import display, HTML
from datetime import datetime
from datetime import date as d
from datetime import timedelta
for i in range(0,8,1):
     print(i)
     dates = d.today()-timedelta(i)
     print(dates)


     dates = d.today()-timedelta(i)
     times = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
     with open('tbo_reco/logs/log_test'+str(dates)+'.txt', 'w') as f:
         f.write('\n')
     services2 = ['tbo_reco']
     for service in services2:
         core = 'tbo_reco/stat-''.txt'
         missFiles = 'tbo_reco/error-''.txt'
         # print(core)
         try:
             with open(core, 'r') as f:
                 lines = f.read().splitlines()
                 f.close()
             if('1' in lines):
                 print('\n{} , {} ,  Recon Done,_'.format(dates,service))
             else:
                 print('\n{} , {} ,  Recon yet to be Done'.format(dates,service),end='')


                 with open(missFiles, 'r') as f:
                     lineList = f.read().splitlines()
                     print(',Files Missing - ',end='')
                     for line in lineList:
                         print(str(line),end=' ')


                     f.close()


         except Exception as e:
             with open('tbo_reco/logs/logs_test'+str(dates)+'.txt', 'a+') as f:
                 f.write(str(e))
                 f.write('\n')

csv_file = 'Test.csv'
text_column = 'date'
df = pd.read_csv(csv_file)

def color_text(val):
    if '26MAY2023' in val:
        return 'color: red'
    elif 'APR23' in val:
        return 'color: darkorange'
    elif 'JUL' in val:
        return 'color: green'
    else:
        return ''


styled_df = df.style.applymap(color_text, subset=[text_column])
display(styled_df)
