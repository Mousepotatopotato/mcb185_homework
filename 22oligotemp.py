def oligotemp(A, T, C, G):
    if ((A + T + C + G) <= 13):
        Tm = (A + T)*2 + (G + C)*4
    else:
        Tm = 64.9 + 41*(C +G - 16.4) / (A + T + G +C)
    return Tm

print(oligotemp(1, 1, 1, 1))
print(oligotemp(10, 10, 10, 10))