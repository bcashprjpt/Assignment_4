

try:
    file = open('D:/Bikash learning/TuteDude_Assignment/Assignment_4/sample.txt','r')
    read = file.readlines()
    print("Reading the file")
    print("Line 1: ",read[0])
    print("Line 2: ",read[1])
    file.close()
except Exception:
    print("Error: The file sample.txt was not found.") 