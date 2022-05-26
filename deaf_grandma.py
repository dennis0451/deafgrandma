def deaf_grandma():
    print('Hey Kid!')
    my_intput = input()
    goodbye_count = 0
    while goodbye_count <= 2:
        if my_intput == "":
            print ("WHAT?!")
            my_intput = input()
        elif  my_intput == my_intput.lower():
            print ("SPEAK UP, KID!")
            my_intput = input()
        elif my_intput == my_intput.upper() and my_intput != "GOODBYE!":
            print ("NO, NOT SINCE 1946!")
            my_intput = input()
        elif my_intput == my_intput.upper() and my_intput == "GOODBYE!" and goodbye_count < 1:
            print ("LEAVING SO SOON?")
            goodbye_count += 1
            my_intput = input()
        elif my_intput == my_intput.upper() and my_intput == "GOODBYE!" and goodbye_count == 1 :
            print ("LATER, SKATER!")
            goodbye_count += 1
            return

    



print(deaf_grandma())
