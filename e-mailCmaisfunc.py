import smtplib #Biblioteca que permite a conex√o com o servidor do gmail.
from email.mime.text import MIMEText #Permite o envio de texto


#============================Vari√°veis===========================

smtp = "smtp.gmail.com" #servidor do seu provedor de e-mail

porta = 587 #Porta padr„o tls

remetente = "seu-email@gmail.com" 

password = "sua senha"

destinatarios=["email.outro@gmail.com"]

#===========================Mensagem=============================
#Menssagem escrita em um arquivo txt
msg = MIMEText(open('arquivoteste.txt', 'r').read())
msg['From'] = 'Leandro CustÛdio'
msg['to'] = 'Friends'
msg['Subject'] = 'Envio Teste'

msg = msg.as_string()

#============================Conex√£o===============================
#Conecta com o servidor
server = smtplib.SMTP(smtp, porta)

server.starttls()

server.login(remetente,password)

server.sendmail(remetente, destinatarios, msg)

server.quit()