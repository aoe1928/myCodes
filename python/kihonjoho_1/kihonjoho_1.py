def Index(alphabet):
    return ord(alphabet) - 64


def GenarateBitMask(Pat, Mask):
    PatLen = len(Pat)
    for i in range(1, 27):
        Mask[i] = 0b0 # 初期化
    for i in range(1, PatLen):
        Mask[Index(Pat[i])] = 0b1 << (i - 1) | Mask[Index(Pat[i])]
    print(Mask)
    return PatLen


def BitapMatch(Text, Pat):
    TextLen = len(Text)
    PatLen = GenarateBitMask(Pat, Mask)
    Status = 0b0
    Goal = 0b1 << (PatLen - 2)
    for i in range(1, TextLen):
        Status = Status << 1 | 0b1
        Status = Status & Mask[Index(Text[i])]
        print(Status)
        if Status & Goal != 0b0:
            return i - PatLen + 2
    return -1


Text = list(' AACBBAACABABAB')
Pat = list(' ACABAB')
Mask = list(' ' * 27)
print(Mask)
a = GenarateBitMask(Pat, Mask)
print(a)
b = BitapMatch(Text, Pat)
print(b)