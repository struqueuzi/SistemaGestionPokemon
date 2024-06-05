import csv
import msvcrt
import os


pokemones = ''
with open('pokemon_primera_generacion(1).csv', newline='', endcoding='utf-8') as p:
    datos = csv.reader(p, delimeter=',' )
    pokemones = list(datos)

cinturon = []


while True:
    print('<<Press any key to continue :>>')
    msvcrt.getch()
    os.system('cls')
    print('''\033[31m Sistema de Gestion Cinturon Pokemon
             *********************************************\033[0m 
             1.	Mostrar todos los Pokémon disponibles.
             2.	Buscar un Pokémon por nombre.
             3.	Agregar un Pokémon al cinturón.
             4.	Mostrar los Pokémon en el cinturón.
             5.	Quitar un Pokémon en el cinturón.
             0.	Salir.''')
    
    n = (input('Seleccione una opcion :'))
    if n == "0" :
        break
    elif n == "1" :
        print("\033[33mListado de Pokemones\033[0m")
        for p in pokemones:
            print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")
    elif n == "2" :
        print("\033[33mBuscar Pokemon\033[0m")
        nombre = input("Ingrese nombre para buscar").capitalize()
        centinela = False
        for p in pokemones:
             if p[1] == nombre:
                 print(f"\033[32mENCONTRADO {p[0]}\t{p[1]}\t{p[2]}\tAltura :{p[3]}\t Peso: {p[4]} ")
                 centinela = True
                 break
             if not centinela:
                 print("\033[31mPokemon NO encontrado\033[0m")    
    elif n == "3" :
        print("\033[33mAgregar Cinturon\033[0m")
        if len (cinturon)<6:
            nombre = input("Ingrese nombre para buscar").capitalize()
        centinela = False
        for p in pokemones:
             if p[1] == nombre:
                 print(f"\033[32mENCONTRADO {p[0]}\t{p[1]}\t{p[2]}\tAltura :{p[3]}\t Peso: {p[4]} ")
                 repetido = False
                 for pok in cinturon:
                     if pok[1]==nombre:
                         repetido = True 
                 if not repetido:
                     cinturon.append(p)
                 else:
                     print("\033[31mPokemon Repetido\033[0m")
                 centinela = True
                 break
             if not centinela:
                 print("\033[31mPokemon NO encontrado\033[0m")
        else:
            print("\033[31mCinturon sin espacio disponible\033[0m")         
    elif n == "4" :
        print("\033[33mMostrar Cinturon\033[0m")
        if len(cinturon)>0:
            for i in range(len(cinturon)):
                print(f"{i+1} {cinturon[i][1]} {cinturon[i][2]} ")
        else:
            print("\033[31mCinturon Vacio\033[0m")
    elif n == "5" :
        print("\033[33mQuitar del Cinturon\033[0m")
        nombre = input("Ingrese nombre para quitar : ").capitalize()
        centinela = False
        for p[1] in cinturon:
            if p[1] == nombre:
                cinturon.remove(p)
                print("\033[32mPokemon quitado\033[0m")
                centinela = True
            print(cinturon)
        if not centinela:
            print("\033[31m Pokemon no encontrado\033[0m")
    elif n == "6" :
        
    else:
        print("\033[31mOpcion no valida\033[0m")