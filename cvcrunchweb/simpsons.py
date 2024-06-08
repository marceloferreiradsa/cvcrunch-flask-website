from zeep import Client

# URL do WSDL
wsdl = 'https://satnfe.sef.sc.gov.br/ws/distribuicao/nfedownloadV2.asmx?wsdl'

# Criar o cliente
client = Client(wsdl=wsdl)

# Criar o XML de solicitação como uma string
xml_request = '''
<distNFeSC versao="2.00" xmlns="http://www.satnfe.sef.sc.gov.br/ws/distribuicao-v2">
    <tpAmb>1</tpAmb>
    <verAplic>appcliente 2.5</verAplic>
    <cUF>42</cUF>
    <CNPJ>46074917000131</CNPJ>
    <solRel>
        <indXML>1</indXML>
        <indAtor>9</indAtor>
        <ultNuNSU>0</ultNuNSU>
    </solRel>
</distNFeSC>
'''

# Fazer a chamada ao Web Service
response = client.service.NfeDownloadContab(xml_request)

# Printar a resposta
print(response)
