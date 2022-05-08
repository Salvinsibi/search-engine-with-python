from googlesearch import search
a=input("Search Here: ")
for i in search(a, stop=8):
    print(i)
