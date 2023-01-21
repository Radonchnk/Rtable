import hashlib
import os

def SortHashGenerator(amount):
    iterationsfile = open('Counter.txt', 'r')
    iterations = int(iterationsfile.readline())
    i = iterations
    iterationsfile.close()

    fp = open('DataBase.txt')
    DBDump = [line.strip('\n') for line in open('DataBase.txt')]

    while i < (iterations+amount):
        result = hashlib.md5(str(i).encode()).hexdigest()[0:4] + ':' + str(i)

        index = int(result[0], 16) * 16 * 16 * 16 + int(result[1], 16) * 16 * 16 + int(result[2], 16) * 16 + int(result[3], 16)
        if DBDump[index] == "":
            print(index)
            print(result)
            DBDump[index] = result

        i += 1

    fp.close()
    fp = open('DataBase.txt', 'w')
    fp.write("\n".join(DBDump))
    fp.close()

    iterationsfile = open('Counter.txt', 'w')
    iterationsfile.write(str(i))
    iterationsfile.close()

def findHash(hash):
    DBDump = [line.strip('\n') for line in open('DataBase.txt')]

    index = int(hash[0], 16) * 16 * 16 * 16 + int(hash[1], 16) * 16 * 16 + int(hash[2], 16) * 16 + int(hash[3],16)

    data = DBDump[index]

    if data == "":
        return("No hash in DB")
    return("Key:" + data[5:])


if not os.path.exists("DataBase.txt"):
    fp = open('DataBase.txt', 'w')
    for i in range(65536):
        #4294967296 - 8 nums
        #340282366920938463463374607431768211456 - md5
        fp.write("\n")

if not os.path.exists("Counter.txt"):
    iterationsfile = open('Counter.txt', 'w')
    iterationsfile.write('0')
    iterationsfile.close()

while True:

    userOutput = int(input("What you wanna to do? 0 - find a hash, 1 - generate a hash: "))

    if userOutput:
        amount = int(input("How many hashes do you wanna generate: "))

        SortHashGenerator(amount)
    else:
        hash = input("What hash you wanna find: ")

        print(findHash(hash))