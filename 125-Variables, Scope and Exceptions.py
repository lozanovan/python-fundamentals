import os

userInput=input("Enter file path:")
directory = os.getcwd()

inputFile = open(userInput, 'r')
outputFile = open(os.path.join(directory, 'output.txt'), 'w')
inputData = inputFile.readlines()

for line in inputData:
    if('F' in line):
        buffer=int(line[:-2])
        buffer=round((buffer - 32) * 0.5556, 2)
        
        outputFile.write(str(buffer) + 'C'  + '\n')
        
outputFile.close()