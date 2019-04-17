def recurs(a):
    if a==0:
        return 1
    else:
        return a*(recurs(a-1)+1)

print(recurs(4))
