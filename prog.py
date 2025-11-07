import numpy as np
import pandas as pd

reference = pd.DataFrame({"x":[0], "y":[0]})
robot_point = pd.DataFrame({"x":[0], "y":[0]})

while True:
    ip = input("""
    1. UP
    2. Down
    3. Left
    4. Right
    !. Exit""")
    
    if ip == "!":
        break

    ip = int(ip)
    if ip == 1:
        mvment = float(input("Enter movement go to UP: "))
        robot_point.loc[0, "y"]+= mvment
    elif ip == 2:
        mvment = float(input("Enter movement go to Down: "))
        robot_point.loc[0, "y"]-= mvment
    elif ip == 3:
        mvment = float(input("Enter movement go to Left: "))
        robot_point.loc[0, "x"]-= mvment
    elif ip == 4:
        mvment = float(input("Enter movement go to Right: "))
        robot_point.loc[0, "x"]+= mvment
    else:
        print("Invalid Input")

print("Distance of Robot from reference:", "\n", np.sqrt(np.sum((robot_point - reference)**2, axis=1))[0])
    
