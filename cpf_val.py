n = input("Digite o número do CPF: ")

def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')     
     # remove pontos e traços

    if len(cpf) != 11 or not cpf.isdigit():
        return False 
        # CPF deve ter 11 dígitos numéricos

    cpf = list(map(int, cpf))
     # converte para lista de inteiros
     
    # Calcula o primeiro dígito verificador
    soma = sum(cpf[i] * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto
    # Calcula o segundo dígito verificador
    soma = sum(cpf[i] * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto
    return cpf[-2:] == [dv1, dv2] # CPF é válido se os dois últimos dígitos 
   
cpf = (n)
if valida_cpf(cpf):
    print(f'O CPF {cpf} é válido')
else:
    print(f'O CPF {cpf} não é válido')
