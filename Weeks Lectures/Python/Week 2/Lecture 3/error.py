#first func
def divide(a,b):
    return a/b

#second func
def main():
    result = divide(10, 2)
    print(result)

main()

#random user defined function
def string_build(word1, word2, word3, word4):
    return f"{word1}-{word2}-{word3}{word4}"

random_text = string_build("Python version", 3.14, "is gr", str(8))
print(random_text) 