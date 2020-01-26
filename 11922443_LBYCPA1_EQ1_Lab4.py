def start():
    while True:
        print(" E N G I N E E R I N G  F O R M U L A S")
        print("Please pick the formula needed.")

        print(" [1] Slope of a line: y = mx + b")
        print(" [2] Kinematic: Xf = Xi + Vit + 1/2at^2")
        print(" [q] quit ")
        print(" [b] back")

    
        Equation = input( "Please choose a formula: ")

        if Equation == "1":
            print(" Slope of a line: y = mx + b ")
            missing = input(" Please enter the missing variable ")
            if missing == "y":
                print("Fill in the given")
                slope1 = input(" m = ")
                slope2 = input(" x = ")
                slope3 = input(" b = ")
                slopefinal = int(slope1) * int(slope2) + int(slope3)
                print(" Y = " + str(slopefinal))
        
           
            elif missing == "m":
                print("Fill in the given")
                slope1 = input(" y = ")
                slope2 = input(" x = ")
                slope3 = input(" b = ")
                slopefinal2 = int(slope1) - int(slope3) / int(slope2)
                print(" M = " +str(slopefinal2))

            elif missing == "x":
                print("Fill in the given")
                slope1 = input(" y = ")
                slope2 = input(" m = ")
                slope3 = input(" b = ")
                slopefinal3 = int(slope1) - int(slope3) / int(slope2)
                print(" X = " +str(slopefinal3))

            elif missing == "b":
                print("Fill in the given")
                slope1 = input(" m = ")
                slope2 = input(" x = ")
                slope3 = input(" y = ")
                slopefinal4 = int(slope3) - int(slope1) * int(slope2) 
                print(" B = " +str(slopefinal4))


        elif Equation == "2":
            print(" Kinematics: Xf = Xi + Vit + 1/2at^2 ")

            MissingK = input("Please enter the missing variable ")

            if MissingK == "Xf":
                Xo = input(" X initial = ")
                Vo = input(" V initial =  ")
                t = input(" Time = ")
                a = input(" Acceleration = ")
                KinematicFinal = int(Xo) + int(Vo) * int(t) + 1/2 * int(a) * int(t) ** 2
                print(" Xf =" + "  " + str(KinematicFinal))

            elif MissingK == "a":
                Xo = input(" X initial = ")
                Vo = input(" V initial =  ")
                t = input(" Time = ")
                X = input(" X final = ")
                KinematicFinal2 = int(X) - int(Xo) - int(Vo) * int(t) / 1/2 * int(t)
                print(" A =" + "  " + str(KinematicFinal2))

            elif MissingK == "t":   
                Xo = input(" X initial = ")
                Vo = input(" V initial =  ")
                a = input(" Acceleration = ")
                X = input(" X final = ")
                KinematicFinal3 = int(X) - int(Xo) - int(Vo) / .5 * int(a)
                print(" t = " + "  " + str(KinematicFinal3))

            elif MissingK == "Xo": 
                t = input(" time = ")
                Vo = input(" V initial =  ")
                a = input(" Acceleration = ")
                X = input(" X final = ")
                KinematicFinal4 = int(X) - int(Vo) - .5 * int(a) * int(t)
                print(" Xo = " + "  " + str(KinematicFinal4))

            elif MissingK == "Vo":
                t = input(" time = ")
                Xo = input(" X initial =  ")
                a = input(" Acceleration = ")
                X = input(" X final = ")
                KinematicFinal5 = int(X) - int(Xo) - .5 * int(a) * int(t)
                print(" Vo = " + "  " + str(KinematicFinal5))
        
        if Equation == "q":
            print("Quitting the Program")
            exit()
        if Equation =="b":
            start()
            
                
start()