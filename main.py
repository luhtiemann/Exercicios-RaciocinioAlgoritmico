"""
#1. Faça um algoritmo que leia um número inteiro e escreva seu antecessor e sucesso.
numeroInt = int(input("Insira um número inteiro: "))
ante = numeroInt - 1
suce = numeroInt + 1
print("Seu antecessor é: ", ante, ", e seu sucessor é: ", suce)

#2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade que completará em 2022.
anoNascimento = int(input("Insira seu ano de nascimento: "))
idade = 2022 - anoNascimento
print("Você completará ", idade, "anos em 2022.")

#3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salários-mínimos ele recebe.
salario = float(input("Insira seu salário: "))
salariosMin = salario/1212
print("Você recebe ", salariosMin, " salários mínimos.")

#4. Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
#(1) a vista com 5% de desconto;
#(2) o valor da parcela em 2x;
#(3) o valor da parcela em 3x com acréscimo de 5%.
valorProduto = float(input("Insira o valor do produto: "))
aVista = valorProduto * 0.95
parcela = valorProduto/2
both = (valorProduto/3) + (valorProduto*0.05)
print("O valor do produto a vista com 5% de desconto é de: ", aVista)
print("O valor da parcela em 2x é de: ", parcela)
print("O valor da parcela em 3x com com acréscimo de 5% é de: ", both )

#5. Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l),
#solicitando como entrada a distância total percorrida (KM) e o volume de combustível consumido para percorrê-la (litros).
distance = float(input("Insira a distância total percorrida em km: "))
gas = float(input("Insira o volume de combustível em litros consumido para perorre-la: "))
average = distance/gas
print("O consumo médio do automóvel em km/l é de: ", average)

#6. Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar um tanque cilindro,
#em que são fornecidas sua altura e raio, sabendo que:
#a. A lata de tinta custa R$ 50,00
#b. Cada lata contém 5 litros
#c. Cada litro de tinta pinta 3 metros quadrados
#d. Entrada do programa: altura e raio do cilindro e. Saída: valor em reais e quantidade de latas
altura = float(input("Insira a altura do cilindro: "))
raio = float(input("Insira o raio do cilindro: "))
area = 2*3.14*raio*(altura+raio)
litros = area/3
latas = litros/5
valor = latas*50
print("A quantidade de latas é: ", latas)
print("O valor em reais é: ", valor)

#Escreva um programa que recebe como entrada 3 numeros e os exibe ordenado
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
if n1<n2 and n1<n3:
    if n2<n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2<n1 and n2<n3:
    if n1<n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
else:
    if n1<n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)

#Escreva um algoritmo que dado o peso de um boxeador, informe a categoria a qual ele pertence, segundo a tabela abaixo
peso = float(input("Coloque seu peso em Kg: "))
if peso < 50:
    print("Voce pertence a palha")
elif peso == 50 ou peso <= 59.9:
    print("Voce pertence a Pluma")
elif peso == 60 or peso <= 75.9:
    print("Voce pertence a Leve")
elif peso == 76 or peso <= 87.9:
    print("Voce pertence a Pesado")
elif peso == 88 or peso <= 88:
    print("Voce pertence a Superpesado")
else:
    print(Coloque o peso certo!)
print("Fim")

#Elabore um algoritmo que leia um numero inteiro e verifique se ele eh par ou impar
numeroInt = int(input("Digite um número inteiro: "))
if numeroInt%2==1:
    print("Seu número é ímpar.")
else:
    print("Seu número é par.")

#Pode ou não fazer carteira de motorista
anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = 2022-anoNascimento
if idade >= 18:
    print("Pode fazer a carteira de motorista.")
else:
    print("Não pode fazer carteira de motorista")
print("Sua idade é: ", idade)

#Raiz quadrada
numeroInt = int(input("Digite um número inteiro: "))
if numeroInt<0:
    print("Número invalido")
raiz = numeroInt ** 0.5
print("Sua raiz é: ",raiz)

#Diametro normal ou errado de uma abobora kkk
diametro = float(input("Informe o diâmetro da abóbora: "))
if diametro >= 15 and diametro < 20:
    print("Abóbora Média.")
else:
    print("Produto fora das medidas.")

#Quantidade e valor de copias
copia = int(input("Digite a quantidade de cópias: "))
if copia < 100:
    valor = copia * 0.25
else copia >=100:
    valor = copia * 0.20
print("Valor do serviço: ", valor)

#Peso ideal
altura = float(input("Digite sua altura em metros: "))
sexo = int(input("Insira seu sexo, se masculino digite 1, e se feminino digite 2: "))
if sexo == 1:
    peso = (72.7*altura)-58
elif sexo == 2:
    peso = (62.1*altura)-44.7
print("Seu peso ideal é: ", peso)

#IMC
massa = float(input("Insira sua massa em Kg: "))
altura = float(input("Insira sua altura em metros: "))
IMC = massa/altura**2
if IMC>=18.5 and IMC<25:
    print("IMC normal.")
else:
    massaMax=24.9*(altura**2)
    print("Sua massa máxima considerada normal é: ", massaMax)

#Estacionamento valor
minutos = int(input("Insira quantos minutos o carro ficou estacionado: "))
resto = minutos%15
minutosX = minutos-60
fracionado = (minutosX-resto)/15
valorFracionado = fracionado*1.5
if minutos<75:
    print("O valor total é: ", 8)
elif minutos>=75:
    print("O valor total é: ", 8+valorFracionado)

minutos = int(input("Quantos minutos"))
if minutos > 60:
    valorExtra = 1.5*((minutos-60)/15)
    valorPagar = round(8+valorExtra)
    print(valorPagar)
else:
    valorPagar = 8
    print(valorPgar)

#Idade para votar
idade = int(input("Digite sua idade: "))
if idade<16:
    print("Não votante")
elif idade>=16 and idade<18 or idade>65:
    print("Eleitor facultativo")
elif idade>=18 and idade<=65:
    print("Eleitor obrigatório")

#IMC
massa = float(input("Insira sua massa em Kg: "))
altura = float(input("Insira sua altura em metros: "))
IMC = massa/altura**2
if IMC<18.5:
    print("Abaixo do peso.")
elif IMC>=18.5 and IMC<25:
    print("Peso normal.")
elif IMC>=25 and IMC<=30:
    print("Acima do peso.")
elif IMC>30:
    print("Obeso.")

#Categoria
idade = int(input("Insira sua idade: "))
if idade>=5 and idade<=7:
    print("Infantil A.")
elif idade>=8 and idade<=10:
    print("Infantil B")
elif idade>=11 and idade<=13:
    print("Juvenil A")
elif idade>=14 and idade<=17:
    print("Juvenil B")
elif idade>=18:
    print("Adulto")

#Kg para libras e categoria
peso = float(input("Insira seu peso em Kg: "))
pesoLibras = peso*2.2046
print("Seu peso em libras é: ",pesoLibras)
if pesoLibras>201:
    print("Peso-pesado")
elif pesoLibras>=176 and pesoLibras<=200:
    print("Cruzador")
elif pesoLibras>=169 and pesoLibras<=175:
    print("Meio-pesado")
elif pesoLibras>=161 and pesoLibras<=168:
    print("Super-médio")
else:
    print("Categoria inferior a Super-médio")

#Opção de valor de venda
preco = float(input("Insira o valor do produto: "))
opcao = int(input("Insira a opção escolhida, 1 sendo à vista, 2 sendo em 2x, 3 sendo em 3x, e 4 sendo em 4x: "))
if opcao == 1:
    valor = preco * 0.92
elif opcao == 2:
    valor = preco * 0.96 / 2
elif opcao == 3:
    valor = preco / 3
elif opcao == 4:
    valor = preco*1.04 / 4
print("O valor final do seu produto é: ", valor)

#Maior numero
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
if n1>=n2 and n1>=n3:
    print("O maior número é: ",n1)
elif n2>=n1 and n2>=n3:
    print("O maior número é: ",n2)
elif n3>=n1 and n3>=n3:
    print("O maior número é: ",n3)

#Sequencia decrescente
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
if n1>n2 and n1>n3:
    if n2>n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2>n1 and n2>n3:
    if n1>n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
else:
    if n1>n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)

#Nota valida ou nao
nota=float(input("Digite a sua nota: "))
while nota<7:
    print("Sua nota não é valida.")
    nota = float(input("Digite sua nota: "))
print("Sua nota é valida.")

#Media
num = int(input("Digite um número: "))
soma = 0
while num != -1:
    soma = soma + num
    media = soma/2
    num = int(input("Digite outro número: "))
print("Sua média é:",media)

#Soma
num = int(input("Digite um número: "))
soma = 0
while num >=1:
    soma = soma+num
    num = int(input("Digite outro número: "))
print("Sua soma é:",soma)

#Quantidade numeros pares e impares
numSoma = 1
par = 0
impar = 0
while numSoma <=10:
    num = int(input("Digite um número: "))
    numSoma = numSoma + 1
    if num%2==0:
        num = par
        par = par+1
    else:
        num = impar
        impar = impar +1
print("A quantidade de números pares lidos é:", par)
print("A quantidade de números ímpares lidos é:", impar)

#Vetor
n=10;
vet=[];
for i in range(0,n,1):
    vet.append(10+i);
print("\nO vetor: ", end="");
print(vet);
print("\nNovamente o vetor impresso em 2 modos: ")
i=0
for item in vet:
    print("(%2d,%2d)"%(item,vet[i]), end="");
    i+=1;
print();
***

#Vetor valores inteiros
valoresInteiros = [0,0,0,0,0,0,0,0,0,0]
contador = 0
while contador<10:
    numero=int(input("Digite um número: "))
    valoresInteiros[contador]=numero
    contador+=1
print(valoresInteiros)
print("Fim do programa")

#Printa vogais
i=0
j=0
string = str(input("Digite alguma coisa: "))
for i in string:
    if(i=='A' or i=='a'
    or i=='E' or i=='e'
    or i=='I' or i=='i'
    or i=='O' or i=='o'
    or i=='U' or i=='u'):
        j+=1
print("Vogais: ", j)
#coloca string=string.lower()

#Random apostas de 6 numeros
import random
apostaUsuario = [0,0,0,0,0,0]
numerosSorteados = [0,0,0,0,0,0]
indice = 0
while indice < len(apostaUsuario):
    numeroDigitado = int(input("Digite um número: "))
    apostaUsuario[indice] = numeroDigitado
    numerosSorteados[indice]
    numerosSorteados[indice]=random.randint(1,60)
    indice+=1
print("Aposta usuário: ", apostaUsuario)
print("Números sorteados: ", numerosSorteados)
acertos=0
contadorApostaUsuario = 0
while contadorApostaUsuario < len(apostaUsuario):
    numeroApostado = apostaUsuario[contadorApostaUsuario]
    contadorNumeroSorteado = 0
    while contadorNumeroSorteado < len(numerosSorteados):
        numeroSorteado= numerosSorteados[contadorNumeroSorteado]
        if numeroApostado == numeroSorteado:
            acertos += 1
        contadorNumeroSorteado +=1
    contadorApostaUsuario += 1
print("Acertos: ", acertos)

#Ex da prova copiar 0,1,4,9,16
num = int(input("Digite um número: "))
count = 0
while count <= num:
    print(count*count)
    count+=1

#Escreva um algoritmo que leia um vetor com 4 valores e apresente sua média
valoresInteiros = [0,0,0,0]
contador = 0
while contador<4:
    numero=int(input("Digite um número: "))
    valoresInteiros[contador]=numero
    contador+=1
print(sum(valoresInteiros)/contador)
print("Fim do programa")

numeros = []
contador = 0
somatorio = 0
while contador < 4:
    num = int(input("Insira um número: "))
    numeros.append(num)
    contador += 1
contador = 0
while contador < len(numeros):
    somatorio += numeros[contador]
    contador += 1
media = sum(numeros)/len(numeros)
print(media)

#Escreva um algoritmo que crie uma lista de tamanho 5
e imprima seus valores e em seguida a soma dos valores pares e ímpares

valoresInteiros = [0,0,0,0,0]
contador = 0
contadorP = 0
contadorI = 0
while contador<5:
    numero=int(input("Digite um número: "))
    valoresInteiros[contador]=numero
    contador+=1
    if numero %2 == 0:
        contadorP+=1
    else:
        contadorI+=1
print(valoresInteiros)
print("Soma dos valores pares: ",contadorP)
print("Soma do valores ímpares: ",contadorI)

numeros = []
contador = 0
somatorio = 0
while contador < 4:
    num = int(input("Insira um número: "))
    numeros.append(num)
    contador += 1
contador = 0
somaPares = 0
somaImpares = 0
while contador < len(numeros):
    numero = numeros[contador]
    if numero %2==0:
        somaPares += numero
    else:
        somaImpares += numero
    contador+=1
print(somaImpares,somaPares)

#Random cartas
import random
cartas = list(range(1,53))
print(cartas)
random.shuffle(cartas)
print(cartas)

#Ordene um vetor de 100 números inteiros gerados aleatoriamente.

import random
numeros = list(range(1,501))
lista = list(range(1,101))
contador = 0
while contador < len(lista):
    lista[contador] = random.choice(numeros)
    contador+=1
print(lista)

import random
contador = 0
numeros = []
while contador < 100:
    aleatorio = random.randint(0,500)
    numeros.append(aleatorio)
    contador+=1
print(numeros)
numeros.sort()
print(numeros)

#Lista
nome = "Luana Tiemann Halicki Cordeiro"
lista = list(nome)
print(nome)
print(lista)

#Lista
lista = list(range(0,100,2))
print(lista)
for contador in range (-10,10,2):
    print(contador)

#1
frutas = ['maça','uva','morango','abacaxi','acerola']
for i in range (len(frutas)):
    fruta = frutas[i]
    print(fruta)

#2
frutas = ['maça','uva','morango','abacaxi','acerola']
for elemento in frutas:
    print(elemento)

#3
frutas = ['maça','uva','morango','abacaxi','acerola']
cont = 0
while cont < len(frutas):
    fruta = frutas[cont]
    cont+=1

#Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)
for i in range(1,11):
    print("Tabuada do ", i)
    for j in range(11):
        print(i, "x", j, "=", i * j)

#Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
numero = 1
multi = 1
while multi<11:
    resultado = numero*multi
    print(numero, "X", multi, "=", resultado)
    numero+=1
    if numero == 11:
        multi += 1
        numero = 1

#Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.
numero = [0,0,0]
i=0
while i<len(numero):
    numero[i] = int(input("Digite um número: "))
    i+=1
if numero[0] > numero [1] + numero [2]:
    print(numero[0], "é maior que a soma dos outros dois.")
else:
    print(numero[0], "não é maior que a soma dos outros dois.")

#Leia dois valores reais do teclado, calcular e imprimir na tela:
#a) A soma destes valores b) O produto deles c) O quociente entre eles
numero=[0,0]
i = 0
while i <len(numero):
    numero[i]=int(input("Digite um número: "))
    i+=1
soma = numero[0] + numero[1]
print("Sua soma é: ", soma)
produto = numero[0]*numero[1]
print("Seu produto é: ", produto)
quociente = numero[0]/numero[1]
print("Seu quociente é: ", quociente)

#Ler 4 números inteiros e calcular a soma dos que forem par.
soma = 0
contador = 0
for i in range (1,5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma += numero
        contador +=1
print("A soma dos numeros pares é: ", soma)

#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
#Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
numero = int(input("Digite um número: "))
i=1
while i * (i+1) * (i+2) < numero:
    i=+1
if i*(i+1)*(i+2)==numero:
    print("É triangular.")
else:
    print("Não é triangular.")

#Matrix
matriz = [[8,7,6],
          [10,3,2],
          [17,15,3],
          [10,10,10]]
colunas = len(matriz[0])
for i in range (len(matriz)):
    for j in range(3):
        print(matriz[i][j])

#Matriz
matriz = [[1,2,3], [4,5,6], [7,8,9]]
quantidadeLinhas = len(matriz)
quantidadeColunas = len(matriz[0])
i = 0
while i < quantidadeLinhas:
    j = 0
    while j < quantidadeColunas:
        print(matriz[i][j])
        j += 1
i += 1

#Matriz
import random
matrizConceitoCorreto = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(matrizConceitoCorreto)):
    for j in range (len(matrizConceitoCorreto[0])):
        matrizConceitoCorreto[i][j] = random.randint(0,300)
print(matrizConceitoCorreto)

#Matriz
import random
matrizPython = []
for i in range(3):
    vetor = []
    for j in range (3):
        vetor.append(random.randint(0,300))
    matrizPython.append(vetor)
print(matrizPython)

#Matriz
import random
matrizPython = []
for i in range(4):
    vetor = []
    for j in range (4):
        vetor.append(random.randint(0,300))
    matrizPython.append(vetor)
print(matrizPython)
for i in range(4):
    for j in range(4):
        if i==j:
            print(matrizPython[i][j])

#Matriz
import random
matrizPython = []
for i in range(3):
    vetor = []
    for j in range (3):
        vetor.append(random.randint(0,300))
    matrizPython.append(vetor)
print(matrizPython)

#Matriz soma
import random
matriz = []
soma = 0
for i in range(3):
    vetor = []
    for j in range (3):
        vetor.append(random.randint(0,300))
    matriz.append(vetor)
print(matriz)
for i in range(3):
    for j in range(3):
        soma+=matriz[i][j]
print(soma)

#Matriz
import random
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
maior = []
lista = []
for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        matriz[i][j] = random.randint(0,300)
for i in range (len(matriz)):
    for j in range (len(matriz[0])):

#Def read integer
def ReadInteger():
    number = int(input("Type a number: "))
    return number

#Def sucessor
def successor(value):
    result = value + 1
    return result

#Def random
def GenerateRandomNumber(LowerLimit, HigherLimit):
    number = random.randint(LowerLimit,HigherLimit)
    return(number)

#Def create matrix
import random
def CreateMatrix(rows, collunms):
    matrix = []
    for i in range(rows):
        vector = []
        for j in range(collunms):
            vector.append(random.randint(0,100))
        matrix.append(vector)
    return matrix
def PrintMatrix(matrix):
    for vector in matrix:
        print(vector)
    
#Converter binário para decimal fácil
print("Bom dia, simbora!")
number = input("Enter a Binary number: ")
dec_number = int(number, 2)
print("The decimal conversion is: ", dec_number)

#Converter binário para decimal difícil
binario = input("Digite um número binário: ")
tamanho = len(binario)
soma = 0
for i in binario:
    tamanho = tamanho - 1
    if i=='1':
         aux = (int(i))*(2**tamanho)
         soma = soma + aux
    elif i=='0':
        aux = 0
        soma = soma + aux
    else:
        soma = "Número inválido."
        break
print(soma)
"""
