try:    
    f = open('lyrics.txt') #the default mode is the read mode, so if you don't define it, it will take it automatically
    try:
        f.write("This is to update the file")
    except:
        print("Something went wrong in writing the file")
    finally:
        f.close()

except:
    print("Something went wrong when opening the file")