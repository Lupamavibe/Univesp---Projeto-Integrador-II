import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_test_email():
    try:
        # Configurações do servidor de e-mail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = 'lupamavibe2023@gmail.com'  # Substitua pelo seu e-mail
        smtp_password = 'Brasil500Familia600'  # Substitua pela sua senha

        # Configuração do e-mail
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = 'lupamavibe2023@gmail.com'
        msg['Subject'] = 'Teste de Conexão de E-mail'

        # Corpo do e-mail
        body = "Este é um teste de conexão de e-mail."
        msg.attach(MIMEText(body, 'plain'))

        # Enviando o e-mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Executar a função de teste de envio de e-mail
send_test_email()
