class Solution{ 
    bool check(int N) { 
        map<int,int> mp;
        for(int i=2;i<=sqrt(N);i++) { 
            while(N%i==0) { 
                mp[i]++; 
                N=N/i; 
            }
        } 
        if(N!=1) mp[N]++;   
        if(mp.size()==1) { 
            auto it=mp.begin(); 
            if(it->second*2+1==9) return 1; 
            return 0;
        } 
        for(auto it:mp) {   
            if(it.second>1) return 0; 
        }
        if(mp[N]>1) return 0; 
        return mp.size()==2;
    }
public:
    long long int nineDivisors(long long int N){ 
        int dem=0;
       for(int i=2;i<=sqrt(N);i++) {  
           if(check(i)) dem++;
       } 
       return dem;
    }
};