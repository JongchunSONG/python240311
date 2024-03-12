# DemoStr.py

#print(dir(str))
 
strA = "python is very powerful"
strB = "파이썬은 매우 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
data = "<<< spam and ham >>>"
result = data.strip("<>")
print(data)
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))