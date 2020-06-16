#===========================Biliotecas============================

# Faz conexão com o gmail e envia o e-mail
import smtplib
#Adiciona vários tipos de conteúdos em um mesmo e-mail. 
from email.mime.multipart import MIMEMultipart
#Adiciona texto
from email.mime.text import MIMEText 
#Adiciona o anexo.
from email.mime.base import MIMEBase 

from email.mime.application import MIMEApplication

#encoda o anexo.
from email import encoders 

import mimetypes

#===========================Variáveis=============================

remetente = "seu-email@gmail.com"

password = "sua-senha"

destinatario = "destinatario" # Qualquer e-mail.

#===========================Mensagens=============================

msg = MIMEMultipart()

msg['From'] = remetente
msg['to'] = destinatario
msg['Subject'] = 'Arquivo Anexado'

corpo_texto = '''Prezados(as). 
            Estamos enviando o seu anexo conforme solicitado
            Atenciosamente
            Coordenação do PROMAC'''

msg.attach(MIMEText(corpo_texto))


filename = 'vitoria_elis.pdf'
attachment = open('vitoria_elis.pdf', "rb")


# buscar a lista de Mimetypes 
#https://www.freeformatter.com/mime-types-list.html#mime-types-list

mimetype_anexo = mimetypes.guess_type('vitoria_elis.pdf')[0].split('/')
part = MIMEBase(mimetype_anexo[0],mimetype_anexo[1])


part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content-disposition", "attachment;filename= %s" %filename)

msg.attach(part)

attachment.close()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remetente, password)
text = msg.as_string()
server.sendmail(remetente,destinatario,text)
server.quit()