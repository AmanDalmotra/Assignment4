try :
    with open("sample.txt" , "rt") as fh:
        print("Reading file content :")
        line_no = 1
        for line in fh:
            print (f"Line {line_no} : {line.strip()}")
            line_no += 1

except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")