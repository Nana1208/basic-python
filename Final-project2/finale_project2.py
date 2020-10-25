## References: https://www.youtube.com/watch?v=bXRYJEKjqIM&t=187s


import smtplib

## Tanpa txt file, SUKSES
## Masalah yang muncul: keamanan email
## Problem solving: go to 'myaccount.google.com/lesssecureapps' and 'ALLOW LESS SECURE APPS' ON

# sender=input(str("email: "))
# password=input(str("Pass: "))
# receiver=input(str("email penerima: "))

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls ()
# server.login(sender, password)


# message = "Coba kirim email pakai python"
# server.sendmail (sender, receiver, message)
# server.quit ()


## Coba pakai txt file kirim ke 1 email, SUKSES
## Masalah yang muncul: 1) ERROR karena receiver; 2) "Username and Password not accepted"
## Problem solving: 1) tambahkan variable baru "receiver2=receiver.read"; 2) Di email yang masuk verifikasi kalau memang yang mengizinkan aplikasi kurang aman untuk login adalah kita sendiri
# sender=input(str("email: "))
# password=input(str("Pass: "))
# receiver=open("receiver_list.txt", "r")
# receiver2=receiver.read ()

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls ()
# server.login(sender, password)


# message = "Pesan dikirim dari python"
# server.sendmail(sender, receiver2, message)
# server.quit ()

## Bisa input pesan sendiri
# sender=input(str("email: "))
# password=input(str("Pass: "))
# receiver=open("receiver_list.txt", "r")
# receiver2=receiver.read ()

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls ()
# server.login(sender, password)

# pesan= input(str("Isi pesannya: "))
# message = pesan
# server.sendmail(sender, receiver2, message)
# print ("Email berhasil dikirimkan ke " + receiver2)
# server.quit ()


##Email subject dan attachment
##Masalah yang muncul: Setiap kali mengirim pesan, subject tidak muncul/no subject
##Problem solving: value pada variabel subject di pindahkan, langsung menjadi value msg ['Subject']
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# sender=input(str("email: "))
# password=input(str("Pass: "))
# receiver=open("receiver_list.txt", "r")
# receiver2=receiver.read ()
# # subject=input(str("Subject: "))
# pesan= input(str("Isi pesannya: "))


# msg=MIMEMultipart ()
# msg ['Subject'] = input(str("subject: "))
# msg ['From'] = sender
# msg ['To'] = receiver2



# body = pesan

# msg.attach (MIMEText (body, 'plain'))
# text = msg.as_string ()

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls ()
# server.login(sender, password)

# server.sendmail(sender, receiver2, text)
# print ("Pesan terkirim")
# server.quit ()


## Ini final
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender=input(str("email: "))
password=input(str("Pass: "))
#Pastikan nama file txt untuk list email sama "receiver.txt"
receiver=open("receiver_list.txt", "r")
receiver2=receiver.read ()
pesan= input(str("Isi pesannya: "))

msg=MIMEMultipart ()
msg ['Subject'] = input(str("subject: "))
msg ['From'] = sender
msg ['To'] = receiver2

body = pesan

msg.attach (MIMEText (body, 'html'))

namafile=input("Nama file atau path file yang akan dilampirkan: ")
attachment=open (namafile, 'rb')

part=MIMEBase('application', 'octet-stream')
part.set_payload (attachment.read ())
encoders.encode_base64(part)
part.add_header ('Content-Disposition', "attachment; filename= "+ namafile)

msg.attach(part)
text = msg.as_string ()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls ()
server.login(sender, password)

server.sendmail(sender, receiver2, text)
print ("Pesan terkirim")
server.quit ()