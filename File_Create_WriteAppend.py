def main():
    try:
        fobj = open("Demo.txt","a")
        print("File Gets Opened")
        
        fobj.write(" Pune Maharashtra")

        fobj.close()
        print("File gets close")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    
if __name__=="__main__":
    main()