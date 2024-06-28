import streamlit as st 
from streamlit_gsheets import GSheetsConnection
from datetime import date
import pandas as pd 
from paymentremiander import send_email

st.write('## Welcome to your payment reminder program')
st.write('### Client Information' )


url = "https://docs.google.com/spreadsheets/d/1Pa8P5aZovswZAD1ynJVm-V8a9z5cehlGAoi28HbgRpo/edit?gid=0#gid=0"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[1, 2, ])
st.dataframe(data)

st.subheader('Top customers ')
sql = '''
SELECT 
      first_name,
      second_name
FROM invoice_data
WHERE amount > 10000
ORDER BY amount DESC;

'''
df_top_customers =  conn.query(spreadsheet=url,sql=sql)
st.dataframe(df_top_customers)
     



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
    count_email= 0
    for index, row in df.iterrows():
        if (present>=row['reminder_date'].date()) and (row['has_paid'] == 'no'):
            send_email(
            #    subject= f"[Coding is fun] Invoice:{row['invoice_no']}",
               name=row['name'],
               email_receiver= row['email'],
               due_date= row['due_date'].strftime('%d  %b %Y'),
               invoice_no= row['invoice_no'],
               amount= row['amount']
            )
            count_email += 1
    
    return f'Total emails sent: {count_email}'

df = load_fl(URL)
if st.button('Send Payment Reminders'):
    result = check_and_send(df)
    st.write(result)

    
