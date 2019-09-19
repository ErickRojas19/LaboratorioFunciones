def a_power_b(base,exp):
   
    try:
            
        if(exp==1):
            return(base)

        if(exp!=1):
            return(base*a_power_b(base,exp-1))
    except:

        print("Neeeeel Solo números.")


while True:
    a=int(input("Digite cualquier numero para continuar, 0 para kill: "))
    if a==0:
        print("Goodbye!")
        break
    else:
        base=int(input("Digite la base: "))
        exp=int(input("Digite el exponente: "))
        print("Resultado:",a_power_b(base,exp))

