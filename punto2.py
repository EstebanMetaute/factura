controlBln = True
televisorFlt = 1500000
computador_portatilFlt = 1200000
computador_escritorioFlt = 1300000
videobeamFlt = 800000
tabletasFlt = 750000
#Valores finales
cantidad_tv = 0
totales_tv = 0
cantidad_tablets = 0
totales_tablets = 0
cantidad_portatil = 0
totales_portatil = 0
cantidad_escritorio = 0
totales_escritorio = 0
cantidad_videobeam = 0
totales_videobeam = 0
import os
while controlBln == True:
    os.system('cls')
    opcionStr= input('1. Computador de escritorio\n2. Computador portatil\n3. Tabletas\n4. Videobeam\n5. Televisor\n6. FACTURAR\n7. Salir\n->  ')
    if opcionStr == '1':
        cantidad_escritorio+=1
        totales_escritorio+=computador_escritorioFlt
    if opcionStr == '2':
        cantidad_portatil+=1
        totales_portatil+=computador_portatilFlt
    if opcionStr == '3':
        cantidad_tablets+=1
        totales_tablets+=tabletasFlt
    if opcionStr == '4':
        cantidad_videobeam+=1
        totales_videobeam+=videobeamFlt
    if opcionStr == '5':
        cantidad_tv+=1
        totales_tv+=televisorFlt
    if opcionStr == '6':
        os.system('cls')
        print('Cantidad de computadores de escritorio......', cantidad_escritorio, ' $', totales_escritorio)
        print('Cantidad de computadores portatiles.........', cantidad_portatil, ' $' , totales_portatil)
        print('Cantidad de tablets.........................',cantidad_tablets, ' $' ,totales_tablets)
        print('Cantidad de tv..............................', cantidad_tv, ' $' , totales_tv)
        print('Cantidad videobeam..........................', cantidad_videobeam, ' $', totales_videobeam)
        print('Total de ventas $',(totales_videobeam + totales_escritorio + totales_portatil + totales_tv + totales_tablets))
        enter = input('\n<ENTER>')
        if opcionStr == '7':
            controlBln = False
