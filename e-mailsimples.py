import smtplib #Biblioteca que permite o envio do e-mail.

#=========================Variáveis=========================

remetente = "seu-email@gmail.com"

destinatario = "email-do-destinatario@gmail.com"

password = 'sua senha'

smtp = "smtp.gmail.com" #Servidor com o qual nos conectaremos.

#=======================Início do Código====================

#Inicia a instância da função smtp onde especificamos o servidor e a porta.

server = smtplib.SMTP(smtp,587) #Porta padrão. Pode se tentar também a porta 465 ou 25

server.starttls() #Define conexão tls

server.login(remetente,password) #Realiza o login no servidor

msg = "Vai dar tudo certo!" #Corpo do e-mail

server.sendmail(remetente, destinatario, msg) #Envia o e-mail.

server.quit() #Fecha a conexão.



