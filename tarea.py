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
        print("pollo xuxetu")
        break
    if resp == 1 :
        print("-------------------------------------------------------\n")
        print("                     Crear Plan\n")
        print("-------------------------------------------------------\n")
        faenas=int(input("Introduce el numero de faenas(minas): "))
        dias=int(input("Introduce la cantidad de dias: "))
        #poner que si te pone una faena o un dia menor a 1 que te mande a la chucha
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
    elif resp == 2 and c1 == 1:
        #aca te pregunta las toneladas
        contador_relleno_faenas,contador_relleno_dias = [0] * 2
        relleno = []
        while contador_relleno_dias < dias:
            for i in range(0,faenas):
                for abcde in range(0,dias):
                    relleno.append(int(input(f"introduce la produccion del dia {contador_relleno_faenas+1}: ")))
                    print(f"{relleno[contador_relleno_faenas]} añadido al dia {contador_relleno_faenas+1}")
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
        #ahora toca calcular esta wea, y para eso vuelvo a tratar el relleno original con la linea de output y 
        #trabajo denuevo con rangos y probablemente tambien sumandole como contadores a las variables del rango
        while resp == 3 and c2 == 1:
            print("aca te printea la produccion total de una faena")
            print("aca te pregunta si quieres calcular la produccion de un dia en especifico")
            c3 += 1    
            while resp == 4 and c3 == 1:
                print("aca te pregunta que dia quieres calcular la faena total")
                print("aca te printea la produccion total de todas faenas del dia en especifico")
                print("aca te pregunta si quieres calcular otro dia o si en cambio quieres empezar denuevo")
                if resp == 1 or 2 or 5:
                    print("si quiere empezar denuevo resetea los confirmadores")
                    c1 -= 1
                    c2 -= 1
                    c3 -= 1