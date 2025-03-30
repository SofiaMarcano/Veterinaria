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
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    def verNombre(self):#+
        return self.__nombre#+
    def verHistoria(self):#+
        return self.__historia
    def rev_medicamentos(self,nombre_medicamentos):
        for i in self.__lista_medicamentos:
            if i.verNombre() == nombre_medicamentos:
                return False
        return True
    
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = {"Felinos":[],"Caninos":[]}
        
    
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
                    lista.remove(masc)  # Remover correctamente
                    return True
        return False 
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
        print("""\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir """)
        menu=rev_num("Ingrese una opción: ")
        if menu==1: # Ingresar una mascota 
            if Sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=rev_num("Ingrese la historia clínica de la mascota: ")
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if Sistema.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
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
                peso=rev_num("Ingrese el peso de la mascota: ")
                fecha=rev_dt("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=rev_num("Ingrese cantidad de medicamentos: ")
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    for i in lista_med:
                        if nombre_medicamentos==i.VerMedicamento():
                            print("El medicamento ya existe.")
                            continue
                    dosis =rev_num("Ingrese la dosis: ")
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
                Sistema.ingresarMascota(mas,tipo +"s")
            else:
                print("Ya existe la mascota con el numero de histoira clinica")

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
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = Sistema.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

