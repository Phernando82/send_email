import win32com.client

# criando integração com o outlook
outlook = win32com.client.Dispatch('outlook.application')

# criando um email
email = outlook.CreateItem(0)


def envia_email(quant, desc):
    arq = open("emails.txt")
    linhas = arq.readlines()
    emails = []
    for linha in linhas:
        emails.append(linha)
    emails = "".join(emails)
    email.To = emails
    email.Subject = "Email de cotação Python"
    email.HTMLBody = f"""
            <p> Estimado(a) Senhor(a)</p>

            <p>Gostaria de cotar os seguintes materiais:</p>
            <p>{desc}...... {quant} unidades</p>

            <p> Melhores Cumprimentos!</p>
            """
    email.Send()


