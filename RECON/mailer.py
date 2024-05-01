####mailer
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from datetime import date as d
from datetime import timedelta
import pandas as pd
import os


dates = d.today() - timedelta(0)
times = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
captions = "Weekly Recon  status for {} at {}".format(dates, times)


######diff csv for 22 & 23 & 24 for success


df = pd.read_csv(
    "D:/PycharmProjects/pythonProject/recon_status.csv",
    sep=",",
    names=["dates", "Services", "Status", "Comments"],
)


text_column = 'Status'

def color_text(val):
    if 'Recon yet to be Done' in val:
        return 'color: red'
    # elif 'APR23' in val:
    #     return 'color: darkorange'
    elif 'Recon Done' in val:
        return 'color: green'
    else:
        return ''


styled_df = df.style.applymap(color_text, subset=[text_column])
#styled_df2 = df.style.to_excel('styled.xlsx',engine='openpyxl')
#styled_df
# df.set_index('')
# df.set_index('Services',inplace=True)

# df.style.set_caption(captions)
df.to_csv("recon_summary_test.csv", sep=",", index=False)



to_list = ["ritik904191@gmail.com"]

username = "rishubsharma81@gmail.com"
password = 'vave hdqf vhrt slre'
from_email = username
msg = MIMEMultipart("alternative")
msg["Subject"] = captions
msg["From"] = username
msg["To"] = "recon_team"


html = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(
    styled_df.to_html()
)


part1 = MIMEText(html, "html")
msg.attach(part1)
try:
    port = 587
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, to_list, msg.as_string())
        print("Mail Sent\n")


except Exception as e:
    print("Error : ", e)



