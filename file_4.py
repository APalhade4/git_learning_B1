class A:
    def even_odd(self):
        Even_numbers = []
        Odd_numbers = []
        for i in range(1, 40):
            if i % 2 == 0:
                Even_numbers.append(i)
            else:
                Odd_numbers.append(i)
        print("Even Numbers are : ", Even_numbers)
        print("Odd Numbers are : ", Odd_numbers)