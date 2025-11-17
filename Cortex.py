import time 

def Pcortex(): #animal naming verbal fluency test
    enter = 0
    animals = set()
    while enter != "":
        enter = input("Press Enter to Start: ")
    start_time = time.time()

    while True:
        if len(animals) > 0:
            animal = input("Name another animal: ")
        else:
            animal = input("Name an animal: ")

        if time.time() - start_time <= 60:
            animals.add(animal)
        else:
            print("Too late, Times up!")
            break

    length = len(animals)
    if length == 1:
        s = "animal"
    else:
        s = "animals"
    print(f"You named {length} {s}.")
    if length >= 23:
        print("You have above average verbal naming fluency!")
    elif 13 < length < 23:
        print("You verbal naming fluency is healthy.")
    else:
        print("Consider improving your brain health.")

    if length > 0:
        print("Animals named:", ", ".join(animals))

if __name__ == "__main__":
    Pcortex()


