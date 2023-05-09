#Matias Aburto 21.797.621-9

c1, c2, c3, c4, resp = [0] * 5
print("SISTEMA DE PLANIFICACION DE LA PRODUCCION")
print("-------------------------------------------------------\n")
print("1-Crear plan")
print("2-Ingresar datos de produccion")
print("3-Calcular produccion total de una faena especifica")
print("4-Calcular procuccion total dia X de todas las faenas")
print("5-Salir\n")
while resp < 5:
    if c1 or c2 or c3 == 1:
        print("1-Crear plan 2-Ingresar datos de produccion 3-Calcular produccion total de una faena especifica 4-Calcular procuccion total dia X de todas las faenas 5-Salir")
    resp = int(input(":"))
    if resp < 1:
        print("\nNUMERO INVALIDO\n")
        print("1-Crear plan 2-Ingresar datos de produccion 3-Calcular produccion total de una faena especifica 4-Calcular procuccion total dia X de todas las faenas 5-Salir")
        continue
    if resp == 1 :
        print("-------------------------------------------------------\n")
        print("                     Crear Plan\n")
        print("-------------------------------------------------------\n")
        faenas=int(input("Introduce el numero de faenas(minas): "))
        dias=int(input("Introduce la cantidad de dias: "))
        if faenas < 1 or dias < 1:
            print("NUMERO INVALIDO")
            break
        print("                     Plan de produccion")
        print("-------------------------------------------------------")
        contador = 1
        contador2 = 0
        while contador <= dias: 
            print("         ",end="")
            print(f"{contador}",end="")
            contador += 1
        else:
            print("\n")
            separacion = "         "
            while contador2 < faenas:
                print(f"faena {contador2} ",f"0{separacion}"*faenas)
                contador2 += 1
        print("-------------------------------------------------------\n")
        c1 = 1
        continue
    if resp == (2,3,4) and c1 != 1:
        print("Plan de produccion no encontrado")
        continue
    if resp == 2 and c1 == 1:
        contador_relleno_faenas,contador_relleno_dias = [0] * 2
        relleno = []
        while contador_relleno_dias < dias:
            for i in range(0,faenas):
                for abcde in range(0,dias):
                    relleno.append(int(input(f"introduce la produccion del dia {contador_relleno_faenas+1}: ")))
                    contador_relleno_faenas += 1
                    contador_relleno_dias += 1
                    if contador_relleno_faenas == faenas:
                        contador_relleno_faenas = 0
        c2 = 1
        contador = 1
        print("                     Plan de produccion")
        print("-------------------------------------------------------")
        while contador <= dias: 
            print("         ",end="")
            print(f"{contador}",end="")
            contador += 1
        else:
            print("\n")
            largo = len(str(relleno[0]))
            separacion = " "*(8-largo)
            contador2 = 0
            for i in range(faenas):
                ini_range = 0
                fin_range = dias
                while contador2 < faenas:
                    n=1
                    output=(relleno[i:i + n] for i in range(ini_range, fin_range, n))
                    output2 = f"{separacion}".join(map(str, output))
                    print(f"faena {contador2} " + f"{output2}")
                    contador2 += 1  
                    ini_range = ini_range + dias
                    fin_range = fin_range + dias
        print("\n-------------------------------------------------------\n")
        continue
    if resp == 3 and c2 == 1:
        faena_cal = int(input("faena a calcular: "))
        rango1 = int(faena_cal*faenas)
        rango2 = int((faena_cal*faenas)+dias)
        rango_cal = relleno[rango1:rango2]
        produccion_total_faena = sum(relleno[rango1:rango2])
        print(f"la produccion total de la faena {faena_cal} es: {produccion_total_faena}\n")
        c3 = 1
        continue
    if resp == 4 and c2 == 1:
        dia_cal = int(input("dia a calcular: "))
        poto = []
        r1 = 1
        while dia_cal >= r1:
            poto.append(relleno[(r1*dia_cal)-1])
            r1 += 1
        produccion_total_dia = sum(poto)
        print(f"la produccion total del dia {dia_cal} es: {produccion_total_dia}\n")
        c4 = 1
        continue
    if resp == 5:
        print("hasta luego")
        break
    elif resp > 5:
        print("\nNUMERO INVALIDO\n")