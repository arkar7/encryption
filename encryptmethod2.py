class Encrypt:
    def __init__(self,eName):
        self.name = eName
        self.encryptList=[]

        self.decryptList=[]

    def ascii(self):
        print("The data to encrypt is",self.name)
        for i in self.name:
            encryptMethod=ord(i) + 2
            self.encryptList.append(encryptMethod)

        print("Encrypted Value are:>",self.encryptList)
        for i in self.encryptList:
            data = chr(i)
            print("Encrypted data",data)

    def Decrypt(self):
        for i in self.encryptList:
            dData = i - 2
            self.decryptList.append(chr(dData))
        print("decrypted Data",''.join(self.decryptList))


if __name__ =='__main__':
    eName=input("Please enter your name to encrypt:>")
    encrypt = Encrypt(eName)
    encrypt.ascii()
    encrypt.Decrypt()