import pickle
def CountRec():
    fobj= open("STUDENT.DAT","rb")
    num=0
    try:
        while true:
            rec= pickle.load(fobk)
            print(rec[0],rec[1],rec[2],sep="\t")
            num= num+1
            except:
                fobj.close()
                return num 
