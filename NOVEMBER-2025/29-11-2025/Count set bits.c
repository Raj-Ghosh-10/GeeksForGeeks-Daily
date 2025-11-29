int countSetBits(int n) {
    if (n == 0) return 0;
    int x = 0;
    while ((1 << x) <= n) x++;
    x--;
    int bitsUpTo2x = x * (1 << (x - 1));
    int msb2xToN = n - (1 << x) + 1;
    int rest = countSetBits(n - (1 << x));
    return bitsUpTo2x + msb2xToN + rest;
}