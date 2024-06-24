from datetime import date
import pandas as pd 
# from .paymentremiander import send_email
# # import sys
# # sys.path.append('../paymentremiander')
# # from paymentremiander import send_email



# public Googlesheets url - not secure. 
# convert public googlesheets to csv

SHEET_ID = '1Pa8P5aZovswZAD1ynJVm-V8a9z5cehlGAoi28HbgRpo'
SHEET_NAME= 'SHEET1'
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_fl(url):
    parse_dates=['due_date','reminder_date']
    df = pd.read_csv(URL,parse_dates=parse_dates)
    return df 

print(load_fl(URL))


def check_and_send(df):
    present = date.today()
    count_email=0
    for row in df.iterrows():
        if (present>=row['remainder_date'].date()) and (row['has_paid'] == 'no'):
            send_email(
               name="John doe ",
               email_receiver='lereko4539@egela.com',
               due_date='11 Aug 2022',
               invoice_no='inv-21-12-009',
               amount='5'
            )
        count_email+=1
    return f'Total emails sent: {count_email}'
    
    
