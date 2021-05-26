file1=input("Enter the file name to read")
file2=input("Enter the file name to copy the data")
with open(file1, 'r') as inp:
    content=inp.read().upper()
with open(file2, 'a') as out:
    t=out.write(content)
if t:
    print("Data copied successfully")
