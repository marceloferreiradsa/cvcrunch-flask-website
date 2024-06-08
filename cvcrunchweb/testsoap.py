from zeep import Client

# URL do WSDL
wsdl = 'https://satnfe.sef.sc.gov.br/ws/distribuicao/nfedownloadV2.asmx?wsdl'

# Criar o cliente
client = Client(wsdl=wsdl)

# Listar serviços
for service in client.wsdl.services.values():
    print(f'Service: {service.name}')
    for port in service.ports.values():
        operations = port.binding._operations.values()
        for operation in operations:
            print(f'  Operation: {operation.name}')
            print(f'    Input: {operation.input.signature()}')
            print(f'    Output: {operation.output.signature()}')

# Listar tipos
print("\nTipos disponíveis:")
for type_name, type_obj in client.wsdl.types.items():
    print(f'  {type_name}: {type_obj}')
