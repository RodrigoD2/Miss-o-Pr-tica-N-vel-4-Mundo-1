from Pessoa import Pessoa

pessoa = Pessoa(
    nome="Vivian Souza",
    dataNascimento="07/11/1977",
    cpf="598.247.956-57",
    rg="92648175-1",
    status=False
)

print(f"Nome: {pessoa.nome}, Data de Nascimento: {pessoa.dataNascimento}, CPF: {pessoa.cpf}, RG: {pessoa.rg}, Status: {pessoa.status}")


try:
    pessoa.cpf = "000.001.002"
except ValueError as e:
    print(e)

pessoa.cpf = "598.247.956-57"
print(f"Nome: {pessoa.nome}, Data de Nascimento: {pessoa.dataNascimento}, CPF: {pessoa.cpf}, RG: {pessoa.rg}, Status: {pessoa.status}")