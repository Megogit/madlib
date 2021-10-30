#string concatenation(aka how to put strings together)
#suppose we want to create a string that says "never trust________"
untrusted="cats"# some string variable

#a few ways to do this

# print("never trust to "+ untrusted)
# print("never trust to {}".format(untrusted))
# print(f"subscribe to{untrusted}")
na= input("name:")
sur=input("surname:")
bir=input("birthdate:")

madlib = f"name: {na} \n surname:{sur}   \n birthdate:{bir}"

print (madlib)
