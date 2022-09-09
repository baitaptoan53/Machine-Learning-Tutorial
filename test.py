class Cuahang:
    def __init__(self, ten="", gia=0, soluong=0, size=0, mau="", khuyenmai="khong"):
        self.__ten = ten
        self.__gia = gia
        self.__soluong = soluong
        self.__size = size
        self.__mau = mau
        self.__khuyenmai = khuyenmai

    def Nhap(self):
        while(True):
            self.__ten = input("Moi ban nhap ten mat hang:")
            if(self.__ten != ""):
                break
            else:
                print("Ten mat hang phai khac rong")
        while(True):
            self.__size = input("Moi ban nhap kich thuoc:")
            if (self.__size != ""):
                break
            else:
                print("Kich thuoc phai khac rong")
        while(True):
            self.__mau = input("Moi ban nhap mau:")
            if(self.__mau != ""):
                break
            else:
                print("Moi ban nhap lai mau")
        while(True):
            try:
                self.__gia = float(
                    input("Moi ban nhap gia mat hang(Nghin dong):"))
                if(self.__gia > 0):
                    break
                else:
                    print("Gia tri mat hang phai lon hon 0")
            except ValueError:
                print("Gia tri mat hang nhap vao phai la so")
        while(True):
            try:
                self.__soluong = int(input("Moi ban nhap so luong mat hang:"))
                if(self.__soluong > 0):
                    break
                else:
                    print("So luong mat hang phai lon hon 0")
            except ValueError:
                print("So luong mat hang nhap vao phai la so")
        while(True):
            self.__khuyenmai = input(
                "Moi ban nhap chuong trinh khuyen mai('20/10','20/11','Noel','2/9','khong'):")
            if(self.__khuyenmai in ['20/10', '20/11', 'Noel', '2/9', 'khong']):
                break
            else:
                print("Khong co chuong trinh khuyen mai nao nhu ban vua nhap")

    def Tinh(self):
        if (self.__khuyenmai == '20/10'):
            return round(self.__gia-(self.__gia*(30/100)), 3)
        elif (self.__khuyenmai == '20/11'):
            return round(self.__gia-(self.__gia*(25/100)), 3)
        elif (self.__khuyenmai == 'Noel'):
            return round(self.__gia - (self.__gia * (35 / 100)), 3)
        elif (self.__khuyenmai == '2/9'):
            return round(self.__gia - (self.__gia * (50 / 100)), 3)
        elif(self.__khuyenmai == 'khong'):
            return self.__gia

    def __str__(self):
        return self.__ten  +"\t"+ str(self.Tinh())+"\t" + str(self.__size) + "\t" + self.__mau+"\t"+str(self.__soluong)

    def getKhuyenmai(self):
        return self.__khuyenmai

    def setKhuyenmai(self, value):
        self.__khuyenmai = value


class Danhsach:
    def __init__(self, ds=[]):
        self.__ds = ds

    def Nhap(self):
        while(True):
            c = Cuahang()
            c.Nhap()
            self.__ds.append(c)
            t = input("Ban có nhap tiep khong (Y/N)?")
            if (t not in ["Y", "y"]):
                break

    def HienThi(self):
        print("Ten mat hang\t Gia   \t Size \tMau \t So luong \n")
        for c in self.__ds:
            print(str(c))

    def HienThi1(self):
        print("Cac mat hang khuyen mai dip 2/9")
        print("Ten mat hang\t Gia KM\t Size \tMau \t So luong")
        for c in self.__ds:
            if c.getKhuyenmai() == '2/9':
                print(str(c))

    def Ghitep(self, tentep="MatHang.txt", isappend=True):
        if(isappend):
            f = open(tentep, "a")
        else:
            f = open(tentep, "w")
        for c in self.__ds:
            f.write(str(c))
        f.close()


d = Danhsach()
d.Nhap()
d.HienThi()
d.HienThi1()
d.Ghitep()