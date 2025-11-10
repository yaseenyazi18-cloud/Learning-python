"""
Reading a File with Exception Handling
Create a text file named data.txt and put some lines of text in it.
Write a Python program that attempts to open and read from data.txt. Use try / except to catch FileNotFoundError (if file doesn’t exist), 
and in the exception handler print a user-friendly message.
Also use finally to close the file or print “Done reading file” regardless of success/failure.

"""
def Exeption_Handling(filename):
    file_object = None
    try:
       file_object = open(filename )
       condent = file_object.read()
       print(f"File : {filename}  condent : {condent}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' not founded. Please ensure it exists in the currect directory ") 
    except Exception as e:
        print(f"An unexepted error occured: {e}") 
    finally:
        if file_object:
            file_object.close()
            print("\n--------file clossed.------------")  
        else:
            print("Done reding flie (no flie was opened)" )         



         
Exeption_Handling("module_Exception.txt")










       