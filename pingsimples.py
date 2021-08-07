import  os # Importa o modulo O.S do sistema operacional

print('#' * 60)

# Criando uma variavel que recebe o usuario um ip
ip_ou_host = input('Digite o Ip ou host a ser verificado: ')

print('-' * 60)
# no windows use -n
os.system('ping -c 6 {}'.format(ip_ou_host))
print('-' * 60)
