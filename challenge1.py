a = "C"
b = "D"
c = "E"
d = "F"
e = "G"
f = "H"
g = "I"
h = "J"
i = "K"
j = "L"
k = "M"
l = "N"
m = "O"
n = "P"
o = "Q"
p = "R"
q = "S"
r = "T"
s = "U"
t = "V"
u = "W"
v = "X"
w = "Y"
x = "Z"
y = "A"
z = "B"

#text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
#ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
text2 = """map"""

for letter in text2:
    if letter in globals():
        print(globals()[letter], end='')
    else:
        print(letter, end='')

