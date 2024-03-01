import os
os.system('cls')

cons_escritorioInt = 1500000
cons_portatilInt = 1200000
cons_tabletasInt = 800000
cons_videoInt = 780000
cons_tvInt = 3400000
var_totalGFlt = 0
var_nombreStr = input('nombre ->')
var_contactoStr = input('contacto ->')
var_direccionStr = input('direccion  ->')
var_presupuestoFlt = float(input('presupuesto ->'))
var_controlBln  = True
while var_controlBln == True:
    os.system('cls')
    print('CLIENTE: ', var_nombreStr)
    var_opcionStr = int(input('<<< MENU DE OPCIONES >>>\n\n1. computador de escritorio\n2. computador portatil\n3. tabletas\n4. videobeam\n5. tv\n6. SALIR\n ->'))
    if var_opcionStr >= 1 and var_opcionStr <= 5:
        var_cantidadInt = int(input('cantidad'))
    if var_opcionStr == 1:
        var_totalGFlt += (var_cantidadInt * cons_escritorioInt)
    if var_opcionStr == 2:
        var_totalGFlt += (var_cantidadInt * cons_portatilInt)
    if var_opcionStr == 3:
        var_totalGFlt += (var_cantidadInt * cons_tabletasInt)
    if var_opcionStr == 4:
        var_totalGFlt += (var_cantidadInt * cons_videoInt)
    if var_opcionStr == 5:
        var_totalGFlt += (var_cantidadInt * cons_tvInt)
    if var_opcionStr == 6:
        print('el total a pagar es $', var_totalGFlt)
        if var_presupuestoFlt >= var_totalGFlt:
            print('gracias por su compra')
        else:
            print('no tienes sufucuente saldo')
        var_controlBln = False
        print('\n resumen de compra:')
        print('computadores de escritorio: $', cons_escritorioInt)
        print('computador portatil $', cons_portatilInt)
        print('tabletas $', cons_tabletasInt)
        print('videobeam $', cons_videoInt)
        print('tv $', cons_tvInt)
        break