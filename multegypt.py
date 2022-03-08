def multegypt(n,p):

    resultat = 0
    
    while n != 0:
        if (n%2==1) : 
            resultat += p
        n //= 2 
        p += p 
    return resultat

print("entrez le multiplicateur ")
a = int( input())
print("entrez le multiplicande ")
b = int(input())
print("le resultat de la multiplication egyptienne est :4")
print(multegypt(a,b))