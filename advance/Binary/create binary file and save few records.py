size_of_rec = 20
with open('Names.dat','wb') as f:
    ans= 'y'
    while ans.lower()=='y':
        name = input("enter Name:")
        l=len(name)
        name = name + (size_of_rec-1)*' '
        name = name.encode()
        f.write(name)
        ans=input("add More?")
