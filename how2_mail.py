#Simple Mail Transfer Protocol
import smtplib

# Conexao com gmail. Para outlook usar: smtp-mail.outlook.com (mesma porta)
conn = smtplib.SMTP('smtp.gmail.com', 587)

# Dizer "Oi" ao servidor
conn.ehlo()

# Start TLS
conn.starttls()

# Login (Usar senha específica para aplicativos) 
conn.login('seu_endereco@gmail.com', 'senha_para_aplicativos')

# Não use caracteres especiais
subject = 'Este e o Assunto.'
body = 'Texto do corpo do email sem caracteres especiais \nPodendo ter quebra de linhas.'

# Envia e-mail
conn.sendmail(
    # De
    'seu_endereco@gmail.com'
    # Para
    ,'seu_endereco@gmail.com'
    # Assunto e Corpo do email é separado por \n\n
    ,f"Subject: {subject}\n\n{body}"
)

# Encerra Conexao 
conn.quit()