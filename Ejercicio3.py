from Clase import Registro

def mostrarA (dias):
    d=1
    for hora in dias:
        h=0
        for comp in hora:
            print ('Para el dia', d, ', en la hora', h, ':')
            max, nombMax = comp.getMax ()
            min, nombMin = comp.getMin ()
            if nombMax == 'T':
                print ('La variable maxima es la Temperatura con', max, 'grados.')
            elif nombMax == 'H':
                print ('La variable maxima es la Humedad siendo un total de', max)
            elif nombMax == 'P':
                print ('La variable maxima es la Presion Atmosferica siendo un total de', max)
            if nombMin == 'T':
                print ('La variable minima es la Temperatura con', min, 'grados.')
            elif nombMin == 'H':
                print ('La variable minima es la Humedad siendo un total de:', min)
            elif nombMin == 'P':
                print ('La variable minima es la Presion Atmosferica siendo un total de:', min)
            h+=1
        d+=1
def mostrarB (dias):
    cont = 0
    for hora in dias:
        for comp in hora:
            cont = cont + comp.getTemp ()
    print ('La temperatura promedio de este mes es:', cont/720)
def mostrarC (dias, dia):
    i = 0
    for elem in dias[dia-1]:
        i = elem.mostrar(i)
if __name__=="__main__":
    dias = []
    with open ("Registro.txt", "+r") as archi:
        hora = []
        i=0
        for line in archi:
            t, h, p = line.split (',')
            hora.append (Registro (float(t), float(h), float(p)))
            i+=1
            if i == 24:
                dias.append (hora)
                i=0
                hora = []
    opcion = input ('a - Mostrar las menores y mayores variables de los dias y horas del mes.\nb - Mostrar temperatura promedio mensual por hora.\nc - Mostrar las variables de las horas de un dia determinado.\nOPCIÓN: ')
    if opcion == 'a':
        mostrarA (dias)
    elif opcion == 'b':
        mostrarB (dias)
    elif opcion == 'c':
        mostrarC (dias, int (input ('Ingrese dia: ')))
    else:
        print ('La opción ingresada es incorrecta.')
    print ('Fin del programa...')