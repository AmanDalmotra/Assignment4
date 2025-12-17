txt_input = input("Enter text to write to the file :")

with open("output.txt", "w") as fh:
    fh.write(txt_input + "\n")

print("Data successfully written to output.txt. \n")

append_input = input("Enter additional text to append :")
with open("output.txt", "a") as fh:
    fh.write(append_input + "\n")

print("Data successfully appended. \n")

print("File content of output.txt :")
with open("output.txt", "r") as fh:
    data = fh.read()

print(data)
