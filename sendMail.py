import smtplib , ssl
from email.mime.text import MIMEText
from email.utils import formataddr

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(reciever):
    sender_email = 'harry143lover@gmail.com'
    sender_name = 'SHRESTHA'

    # 'kotharisejal1998@gmail.com'
    reciever_email = reciever
    reciever_name = ''

    message_body = 'Your Analysis is completed and the Analysed image is attached below..'



    msg = MIMEMultipart()
    msg['To']= reciever_email
    msg['From']=sender_email
    msg['Subject'] = 'Analysed image ' +reciever_name

    msg.attach(MIMEText(message_body,'plain'))

    filename ='AnalysedImage.png'

    try:
        with open(filename,'rb') as attachment:
            part = MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())

        #encode file to be sent by email.
        encoders.encode_base64(part)

        #add header as key value pair to attachment
        part.add_header('Content-Disposition', 'attachment',
                                        filename=filename )

        msg.attach(part)
            
    except Exception as e:
            print(f'oh no {e}')  


    try:
        conn = smtplib.SMTP('smtp.gmail.com',587)

        # send internet traffic
        conn.ehlo()
        context = ssl.create_default_context()

        conn.starttls(context=context)
        conn.login(sender_email,'yjjvevhjgndifclw')

        conn.sendmail(sender_email,reciever_email,msg.as_string())
    except Exception as e:
        print(f'something bad happened!\n {e}')  
    finally:
        print('server is closing..')
        conn.quit()