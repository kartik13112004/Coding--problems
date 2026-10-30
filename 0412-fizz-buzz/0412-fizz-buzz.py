class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        k = []
        for i in range(1, n + 1):
            k.append(str(i))
        for i in range(len(k)):
            if int(k[i]) % 3 == 0 and int(k[i]) % 5 == 0:
                k[i] = "FizzBuzz"
            elif int(k[i]) % 3 == 0:
                k[i] = "Fizz"
            elif int(k[i]) % 5 == 0:
                k[i] = "Buzz"
        return k

          
        