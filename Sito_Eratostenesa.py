# print("Sieve of Eratosthenes")
# limit = int(input("Input the upper limit of the number:\n"))
# lista1 = []
#
# for i in range(2, limit+1):
#     lista1.append(i)
#     i = i + 1
#
#
# def sift(list1):
#     for k in range(2, limit+1):
#         for number in list1:
#             if number%k==0:
#                 if number != k:
#                         list1.remove(number)
#             else:
#                 continue
#
#     return list1
#
# def show(list2):
#
#
# print(f"The list of prime numbers in the range up to {limit} is \n{sift(lista1)}")

class SieveOfEratosthenes:
    def __init__(self, limit, list1=None):
        self.limit = limit
        self.list1 = list1 if list1 is not None else self.creating_list(limit)

    @staticmethod
    def creating_list(limit):
        list1 = []

        for i in range(2, limit + 1):
            list1.append(i)

        return list1

    def sift(self):
        for k in range(2, self.limit + 1):
            for number in self.list1:
                if number % k == 0:
                    if number != k:
                        self.list1.remove(number)
        return self.list1

    def check(self):
        non_prime_numbers = []
        for j in self.list1:
            if j <= 1:
                non_prime_numbers.append(j)
            elif j <= 3:
                continue
            elif j % 2 == 0 or j % 3 == 0:
                non_prime_numbers.append(j)
            else:
                i = 5
                while i * i <= j:
                    if j % i == 0 or j % (i + 2) == 0:
                        non_prime_numbers.append(j)
                        break
                    i += 6
        if non_prime_numbers:
            print("Non-prime numbers in the list:", non_prime_numbers)
        else:
            print("All numbers in the list are prime.")


#limit1 = int(input("Input the upper limit:\n"))
#sieve1 = SieveOfEratosthenes(limit1)
#print("Prime numbers up to", limit1, ":\n",sieve1.sift())
#print(sieve1.check())

sieve1 = SieveOfEratosthenes(20)
print(sieve1.sift())
print(sieve1.check())

