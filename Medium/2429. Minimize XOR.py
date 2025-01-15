class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = ['0'] * len(bin(num1)[2:])

        count = bin(num2).count('1')
        n = bin(num1)[2:]
        for i in range(len(a)):
            if count and n[i] == '1':
                a[i] = '1'
                count -= 1
            elif count == 0:
                break
        if count > 0:
            for i in range(len(a) - 1, -1, -1):
                if count > 0:
                    if a[i] == '0':
                        a[i] = '1'
                        count -= 1
                else:
                    break
        if count > 0:
            for i in range(count):
                a.append('1')
        return int(''.join(a), 2)
