def nao_entre_em_panico():

    limite = 100

    c = 1
    p = 1
    numero = 3

    primos = "2,"

    while p < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if(ehprimo):
            primos = primos + str(numero) + ","
            p += 1
            if(p % 10 == 0):
                primos = primos + "<br>"
        numero+=1

    return primos
