import random
randomnumber = random.randrange(1, 100)
file = open("output.txt", "a")
file.write(str(randomnumber) + "\n")
file.close()
