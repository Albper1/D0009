import lab2a
import lab2b

while True:
    print("1. kör bounce\n2. kör tvärsumman\n3. kör newton-rhapson\n4. Avsluta programmet")
    choice = input("Välj alternativ: ")
    if choice == '1':
        lab2a.bounce(int(input("Skriv in en parameter till bounce: ")))
    elif choice == '2':
        print(lab2a.tvarsumman(int(input("Skriv in en parameter till tvärsumman: "))))
    elif choice == '3':
        print(lab2b.solve(int(input("Skriv in en parameter till tvärsumman: "))**2-1,0.001))
    elif choice == '4':
        print("byebye")
        break
    else:
        print("Felinmatning, mata in 1-4.")

    print("\n----------------------------------\n")
