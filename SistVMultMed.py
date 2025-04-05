import json
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
    def verNombre(self): return self.__nombre
    def verHistoria(self): return self.__historia
    def verTipo(self): return self.__tipo
    def verPeso(self): return self.__peso
    def verFecha(self): return self.__fecha_ingreso
    def verLista_Medicamentos(self): return self.__lista_medicamentos

    def asignarNombre(self, n): self.__nombre = n
    def asignarHistoria(self, nh): self.__historia = nh
    def asignarTipo(self, t): self.__tipo = t
    def asignarPeso(self, p): self.__peso = p
    def asignarFecha(self, f): self.__fecha_ingreso = f
    def asignarLista_Medicamentos(self, lista): self.__lista_medicamentos = lista
    
class sistemaV:
    def __init__(self):
        self.__archivo = "mascotas.json"
        self.__lista_mascotas = {"Caninos": [], "Felinos": []}
        self.cargar_datos()
        
    def verTodasLasMascotas(self):
        return self.__lista_mascotas

    def verificarExiste(self,historia):
        for lista in self.__lista_mascotas.values():
            for m in lista:
                if historia == m.verHistoria():
                    return True
        return False

        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas["Caninos"])+ len(self.__lista_mascotas["Felinos"])
    
    def ingresarMascota(self,mascota,tipo):
        self.__lista_mascotas[tipo].append(mascota) 
        self.guardar_datos()
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for lista in self.__lista_mascotas.values():
            for masc in lista:
                if historia == masc.verHistoria():
                    return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        for lista in self.__lista_mascotas.values():
            for masc in lista:
                if historia == masc.verHistoria():
                    return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for lista in self.__lista_mascotas.values():
            for masc in lista:
                if historia == masc.verHistoria():
                    lista.remove(masc)
                    self.guardar_datos()# Remover correctamente
                    return True
        return False 
    def guardar_datos(self):
        datos = {tipo: [m.to_dict() for m in lista] for tipo, lista in self.__lista_mascotas.items()}
        with open(self.__archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def cargar_datos(self):
        try:
            with open(self.__archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.__lista_mascotas = {
                    tipo: [Mascota.from_dict(m) for m in lista] for tipo, lista in datos.items()
                }
        except FileNotFoundError:
            self.__lista_mascotas = {"Caninos": [], "Felinos": []}
def rev_num(msj):
    while True:
        try:
            x=int(input(msj))
            return x
        except:
            print("Por favor ingrese un número entero.")
from datetime import datetime
def rev_dt(msj):
    fecha1=input(msj)
    while True:
        try:
            dt = datetime.strptime(fecha1, '%d/%m/%Y')
            return dt
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY")
            fecha1 = input("Ingrese una fecha valida (DD/MM/YYYY): ")
    
def main():
    Sistema = sistemaV()
    while True:
        print("""
        --- MENÚ DEL SISTEMA ---
        1. Ingresar una mascota
        2. Ver fecha de ingreso de una mascota
        3. Ver número total de mascotas
        4. Ver medicamentos de una mascota
        5. Eliminar una mascota
        6. Ver información completa de una mascota
        7. Ver todas las mascotas
        8. Salir
        """)
        menu=rev_num("Ingrese una opción: ")
        if menu==1: # Ingresar una mascota 
            if Sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=rev_num("Ingrese la historia clínica de la mascota: ")
            
            if Sistema.verificarExiste(historia) == True:
                print("La historia clínica ya existe.")
            else:
                while True:
                    nombre = input("Ingrese el nombre de la mascota: ").strip()
                    if nombre != "":
                        break
                    print("El nombre no puede estar vacío.")

                while True:
                    print("1.Canino \n2.Felino")
                    num=rev_num("Ingrese el tipo de mascota : ")
                    if num==1: 
                        tipo="Canino"
                        break
                    elif num==2:
                        tipo="Felino"
                        break
                    else:
                        print("Ingrese un numero valido.")
                while True:
                    peso = rev_num("Ingrese el peso de la mascota (kg): ")
                    if peso > 0:
                        break
                    else:
                        print("El peso debe ser un número positivo.")

                fecha=rev_dt("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=rev_num("Ingrese cantidad de medicamentos: ")
                lista_med=[]

                for _ in range(nm):
                    while True:
                        nombre_medicamentos = input("Ingrese el nombre del medicamento: ").strip()
                        if nombre_medicamentos == "":
                            print("El nombre del medicamento no puede estar vacío.")
                            continue
                        if any(med.verNombre() == nombre_medicamentos for med in lista_med):
                            print("El medicamento ya fue ingresado.")
                            continue
                        break
                    dosis = rev_num("Ingrese la dosis: ")
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)


                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                tipo_dict = {"Canino": "Caninos", "Felino": "Felinos"}
                Sistema.ingresarMascota(mas, tipo_dict[tipo])


        elif menu==2: # Ver fecha de ingreso
            q = rev_num("Ingrese la historia clínica de la mascota: ")
            fecha = Sistema.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=Sistema.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = rev_num("Ingrese la historia clínica de la mascota: ")
            medicamento = Sistema.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son:")
                for m in medicamento:   
                    print(f"- {m.verNombre()} (dosis: {m.verDosis()})")

            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: 
            q=rev_num("Ingrese el numero de la historia de la mascota a eliminar:")# Eliminar mascota
            nombre_mascota = None
            for i in Sistema.verTodasLasMascotas.values():
                for m in i:
                    if m.verHistoria() == q:
                        nombre_mascota = m.verNombre()
                        break

            if nombre_mascota:
                confirm = rev_num(f"¿Está seguro de que desea eliminar a {nombre_mascota}? (1.Si\n2.No): ")
                if confirm == 1:
                    if Sistema.eliminarMascota(q):
                        print("Mascota eliminada con éxito.")
                    else:
                        print("No se pudo eliminar.")
                elif confirm==2:
                    print("Operacion cancelada")
                else:
                    print("Haz ingresado una opcion no valida.")
            else:
                print("No se encontró esa historia clínica.")

        elif menu==6: # Ver Historia completa
            historia = rev_num("Ingrese la historia clínica: ")
            encontrado = False
            for lista in Sistema.verTodasLasMascotas.values():
                for m in lista:
                    if m.verHistoria() == historia:
                        print("\n--- Datos de la mascota ---")
                        print(f"Nombre: {m.verNombre()}")
                        print(f"Tipo: {m.verTipo()}")
                        print(f"Peso: {m.verPeso()} kg")
                        print(f"Fecha de ingreso: {m.verFecha().strftime('%d/%m/%Y')}")
                        print("Medicamentos:")
                        for med in m.verLista_Medicamentos():
                            print(f"- {med.verNombre()} (dosis: {med.verDosis()})")
                        encontrado = True
                        break
            if not encontrado:
                print("Mascota no encontrada.")

        elif menu == 7:
            todas = Sistema.verTodasLasMascotas()
            for tipo, lista in todas.items():
                print(f"\n{tipo}:")
                for m in lista:
                    print(f"- {m.verNombre()} (Historia: {m.verHistoria()})")
        elif menu==8:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

