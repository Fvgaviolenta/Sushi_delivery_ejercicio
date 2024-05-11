seguir_comprando = True
finalizar_compra = 0

while finalizar_compra == 0:
    pikachu_roll = 0
    otaku_roll = 0
    pulpo_venenoso_roll = 0
    anguila_electrica_roll = 0
    total_compra = 0
    rolls_compra = 0
    monto_desc = 0
    total_compra_desc = 0

    while seguir_comprando == True:
        print("Bienvenido a Super Sushi")
        print("************************")   
        print("          MENU          ")
        print("1. Pikachu roll $4500")
        print("2. Otaku roll $5000")
        print("3. Pulpo Venenoso roll $5200")
        print("4. Anguila Electrica roll $4800")
        try:
            seleccion_roll = int(input("Ingrese el rol que desea comprar: "))
            if seleccion_roll >= 1 and seleccion_roll <=4:
                if seleccion_roll == 1:
                    rolls_compra = rolls_compra + 1
                    pikachu_roll = pikachu_roll + 1
                    total_compra = total_compra + 4500
                    print("Usted selecciono un pikachu roll, $4500 fueron agregados al total de su compra")
                    while True:
                        try:
                            pedido_completo = input("Desea seguir comprando? ").upper()
                            if pedido_completo == "SI":
                                break
                            elif pedido_completo == "NO":
                                seguir_comprando = False
                                break
                            else:
                                print("Ingrese una opcion valida")
                        except ValueError:
                            print("Ingrese una opcion valida")
                elif seleccion_roll == 2:
                    rolls_compra = rolls_compra + 1
                    otaku_roll = otaku_roll + 1
                    total_compra = total_compra + 5000
                    print("Usted selecciono un Otaku roll, $5000 fueron agregados al total de su compra")
                    while True:
                        try:
                            pedido_completo = input("Desea seguir comprando? ").upper()
                            if pedido_completo == "SI":
                                break
                            elif pedido_completo == "NO":
                                seguir_comprando = False
                                break
                            else:
                                print("Ingrese una opcion valida")
                        except ValueError:
                            print("Ingrese una opcion valida")
                elif seleccion_roll == 3:
                    rolls_compra = rolls_compra + 1
                    pulpo_venenoso_roll = pulpo_venenoso_roll + 1
                    total_compra = total_compra + 5200
                    print("Usted selecciono un Pulpo Venenoso roll, $5200 fueron agregados al total de su comrpa")
                    while True:
                        try:
                            pedido_completo = input("Desea seguir comprando? ").upper()
                            if pedido_completo == "SI":
                                break
                            elif pedido_completo == "NO":
                                seguir_comprando = False
                                break
                            else:
                                print("Ingrese una opcion valida")
                        except ValueError:
                            print("Ingrese una opcion valida")
                elif seleccion_roll == 4:
                    rolls_compra = rolls_compra + 1
                    anguila_electrica_roll = anguila_electrica_roll + 1
                    total_compra = total_compra + 4800
                    print("Usted selecciono un Angula Electrica roll, $4800 fueron agregados al total de su compra")
                    while True:
                        try:
                            pedido_completo = input("Desea seguir comprando? ").upper()
                            if pedido_completo == "SI":
                                break
                            elif pedido_completo == "NO":
                                seguir_comprando = False
                                break
                            else:
                                print("Ingrese una opcion valida")
                        except ValueError:
                            print("Ingrese una opcion valida")
            else:
                print("Ingrese una opcion valida")     
        except ValueError:
            print("Ingrese una opcion valida")
            
    while True:
        print("Tu compra esta casi lista...")
        try:
            cupon_desc = input("Ingrese a continuacion su codigo de descuento, si no posee uno precione 'x': ")
            if cupon_desc == "soyotaku":
                print(f"Codigo valido, se aplica un descuento del 10% de tu comprara de ${total_compra}")
                monto_desc = total_compra * 0.1
                total_compra_desc = total_compra - monto_desc
                print("*****************************")
                print(f"TOTAL PRODUCTOS: {total_compra}")
                print("*****************************")
                print(f"Pikachu roll: {pikachu_roll}")
                print(f"Otaku roll: {otaku_roll}")
                print(f"Pulpo Venenoso roll: {pulpo_venenoso_roll}")
                print(f"Anguila Electrica roll: {anguila_electrica_roll}")
                print("*****************************")
                print(f"Subtotal a pagar: {total_compra}")
                print(f"Descuento por codigo: {monto_desc}")
                print(f"TOTAL: {total_compra_desc}")
                break
            elif cupon_desc == "x":
                print("*****************************")
                print(f"TOTAL PRODUCTOS: {total_compra}")
                print("*****************************")
                print(f"Pikachu roll: {pikachu_roll}")
                print(f"Otaku roll: {otaku_roll}")
                print(f"Pulpo Venenoso roll: {pulpo_venenoso_roll}")
                print(f"Anguila Electrica roll: {anguila_electrica_roll}")
                print("*****************************")
                print(f"Subtotal a pagar: {total_compra}")
                print("Descuento por codigo: $0")
                print(f"TOTAL: {total_compra}")
                break
            else:
                print("Ingrese una opcion valida porfavor")
        except ValueError:
            print("Ingrese un codigo valido porfavor")

    while True:
        try:
            pedido_completo = input("Desea realizar una nueva compra? (SI/NO): ").upper()
            if pedido_completo == "SI":
                seguir_comprando = True
                break
            elif pedido_completo == "NO":
                seguir_comprando = False
                finalizar_compra = 1
                print("Gracias por su compra")
                break
        except ValueError:
            print("Ingrese una opcion valida")  


