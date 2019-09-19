def is_prime(number):
  
    try:           
        counter = 0
        for i in range(1,number+1):
            if (number% i)==0:
                counter = counter + 1
        if counter==2:
            
            print ("Si!!!")
        else:
            
            print ("NOOO!!!")
    except:
        
        print("-1")

counter=0
while True:
    a=int(input("Digite un número para saber si es primo, 0 para cerrar: "))
    if a<=0:
        print("Ending...")
        print("Se digito {} numeros primos :".format(counter))
        is_prime(counter)
        break
    else:
        if a > 0:
            counter=counter + 1
            number=int(input("Digite un número: "))
            print(("Su número es: {}".format(is_prime(number))))
