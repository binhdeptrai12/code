from sys import argv

script, filename = argv
print("script %s" % script)
# khai bao variable txt, run pydoc file
txt = open(filename)
# in ra filename and read file
print("Here is your file %r:" % filename)
print(txt.readline())
# nhap lai file name
print("Type the filename again:")
file_again = input(">")
# run pydoc
txt_again = open(file_again)

print(txt_again.read())

