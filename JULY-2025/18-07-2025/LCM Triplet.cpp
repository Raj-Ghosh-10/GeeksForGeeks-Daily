
// User function Template for C++

class Solution {

  public:

    int gcd(int a, int b)

        {

        if (a == 0)

            return b;

        return gcd(b % a, a);

    }

  

    long long lcmTriplets(long long N) {

        long long y, x = N, f, s, c = 0;

        if(N == 2 || N == 1)

            return N;

        if(N&1)

            return (N)*(N-1)*(N-2);

        else {

                x -= 2;  y=x;

             while(1 && c < 1)

                {

                    if(gcd(x, N) == 1) {

                         f = x*N*(N-1);

                         ++c;

};

                         --x;

                }c=0;  N=N-1;  --y;

            while(1 && c < 1 ) {

                    if(gcd(y, N) == 1) {

                         s = y*N*(N-1);

                         ++c;}

                    --y;

        }

            

            return max(f, s);

        }

    }

};