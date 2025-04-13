
try:
    enter_data = input("Enter text to write to the file: ")
    file = open("D:/Bikash learning/TuteDude_Assignment/Assignment_4/output.txt",'w')
    file.write(enter_data+"\n")
    print("Data successfully written to the output file. \n")
    file.close()
    
    append_data = input("Enter additional text to append:  ")
    file = open("D:/Bikash learning/TuteDude_Assignment/Assignment_4/output.txt",'a')
    file.write(append_data)
    print("Data successfully append to the output file. \n")
    file.close()
except Exception:
    print("File not found. Please check the file path.") 
finally:
    print("Final content of the output.txt file:")  
    file = open("D:/Bikash learning/TuteDude_Assignment/Assignment_4/output.txt",'r')
    print(file.read())
    file.close()

      
