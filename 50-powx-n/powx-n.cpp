class Solution {
private:
    double get(double x, int n){
        if(n == 1) return x;
        if(n == 0) return 1;

        double half = get(x, n / 2);
        if(n % 2 == 0) return half * half;
        return half * half * x;
    }
public:
    double myPow(double x, int n) {

        bool sign = true;
        if(n < 0) sign = false;
        double ans = get(x, n);
        if (sign) return ans;
        return 1/ans;
    }
};