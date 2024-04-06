filename = input("Enter a file name: ")
content = ""

try:
    with open(filename, 'r') as file:
        content = file.read()
except:
    print(f"File {filename} does not exist: ")

print(content)

#write to file
output_file = "Written_text.txt"
sentence = input("Enter your text: ")

try:
    with open(output_file, 'w') as file:
        file.write("sentence")
except FileNotFoundError:
    print(f"The file {output_file} does not exist.")

file.close()