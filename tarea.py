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
    if resp == 1 :
        print("-------------------------------------------------------\n")
        print("                     Crear Plan\n")
        print("-------------------------------------------------------\n")
        a=int(input("Introduce el numero de faenas(minas): "))
        b=int(input("Introduce la cantidad de dias: "))
        print("                     Plan de produccion")
        print("-------------------------------------------------------")
        contador = 1
        contador2 = 0
        while contador <= b: 
            print("         ",end="")
            print(f"{contador}",end="")
            contador += 1
        else:
            print("\n")
            while contador2 < a:
                print(f"faena {contador2} ","0         "*a)
                contador2 += 1
        print("-------------------------------------------------------\n")
        c1 = 1
        continue
    elif resp == 2 and c1 == 1:
        print("aca te pregunta las toneladas")
        print("aca te printea el menu pero con las toneladas incluidas")
        c2 = 1
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
else:
    print("pollo xuxetu")

#tengo un monton de comentarios dentro de prints, los deje ahi para no perderme mientras lo ejecutaba xD
#espero no perder el hilo para cuando vuelva
    
