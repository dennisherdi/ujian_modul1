# No. 1
#num=(input('Input your phone number: '))
def create_phone_number(num):

    a = [num]
    for i in a:
        if i.isalpha()==True:
            print('Invalid Input. No Alphabeth')
            return
        elif i.isnumeric()==False:
            print('Invalid input. No Symbols')
            return
        elif i.isnumeric()==True:
            if len(num)!=10:
                print('Digits must be in length of 10, not more or less.')
                return
            elif int(i) < 0:
                    print('Input only positive number.')
                    return
            else:
               
                phone_number = []
                for i in range(0,len(num)):
                    if i == 0:
                        phone_number.append('('+num[i])
                    elif i == 2:
                        phone_number.append(num[i]+') ')
                    elif i == 5:
                        phone_number.append(num[i]+'-')
                    else:
                        phone_number.append(num[i])

    hasil = ''.join(phone_number)
    # print(a)
    print(hasil)
create_phone_number(num)


# No. 2
# def move_zeros(urutan,n): 
#     x = 0 
#     for i in range(n): 
#         if urutan[i] != 0: 
#             urutan[x] = urutan[i] 
#             x+=1
#     while x < n: 
#         urutan[x] = 0
#         x += 1
# urutan1 = ['False', 1, 0, 1, 2, 0, 1, 3, 'a'] 
# n = len(urutan1) 
# move_zeros(urutan1,n)
# print("moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a'])")
# print(urutan1) 
# urutan2 = [0, 0, 0, 'Test', 0, 3, 'a', True, 'False'] 
# n = len(urutan2) 
# move_zeros(urutan2,n)
# print("moveZeros([0, 0, 0, 'Test', 0, 3, 'a', True, False])")
# print(urutan2) 
# urutan3 = [0, True, True, 'False', 'a', 'b', 1, 1, 1] 
# n = len(urutan3) 
# move_zeros(urutan3,n)
# print("moveZeros([0, True, True, False, 'a', 'b', 1, 1, 1])")
# print(urutan3) 


# No.3

class Statistik:
    def __init__(self,x):
        self.data = x
        self.jumlah_data = len(x)
        if (self.jumlah_data % 2)>0:
            self.jumlah_data_ganjil_genap = "Ganjil"
        else:
            self.jumlah_data_ganjil_genap = "Genap"
            self.data_tersortir = sorted(self.data)
            print("Data = "+str(self.data))
            print("Data tersortir = "+str(self.data_tersortir))
            print("Jumlah data = "+str(self.jumlah_data)+" ("+self.jumlah_data_ganjil_genap+")")
    def mean(self):
        j = 0
        for n in self.data:
            n = len(self.data)
            get_sum = sum(self.data) 
            mean = get_sum / n
            print("Mean = "+ str(j/self.jumlah_data))
    def median(self):
        if self.jumlah_data_ganjil_genap == "Ganjil":
            self.nilai_median = self.data_tersortir[(self.jumlah_data//2)] 
            print("Median = "+ str(self.nilai_median))
        else:
            b = self.jumlah_data//2
            a = b-1
            self.nilai_median = (self.data_tersortir[a]+self.data_tersortir[b])/2
            print("Median = ("+ str(self.data_tersortir[a]) + "+" + str(self.data_tersortir[b]) + ")/2 = " + str(self.nilai_median))
    def mode(self):
        y= [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8] 
        y.sort()  
        L1=[] 
        i = 0
        while i < len(y) :
            L1.append(y.count(y[i]))
            i += 1 
            d1 = dict(zip(y, L1)) 
            d2={k for (k,v) in d1.items() if v == max(L1) } 
    # def std(self):
    #     num_list = map(lambda n: n.rstrip("\n"), self.data)
    #     num_list = [int(x) for x in num_list]
    #     mean = sum(num_list)/len(num_list)
    #     print= (mean, max(num_list), min(num_list)
    #     for snDev in num_list:
    #         snDev = mean**(1.0/2)
    #         print snDev     
A = [2,1,4,5,6] 
B = Statistik(A)
B.mean()
B.median()   
     
 
