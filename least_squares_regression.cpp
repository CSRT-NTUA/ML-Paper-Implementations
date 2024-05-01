#include <bits/stdc++.h>

using namespace std;


void regression(vector<float> x, vector<float> y)
{
    int n = x.size();
    float mx = accumulate(x.begin(), x.end(), 0)/n;
    float my = accumulate(y.begin(), y.end(), 0)/n;
    
    float sx = accumulate(x.begin(), x.end(), 0);
    float sy = accumulate(y.begin(), y.end(), 0);
    float sx_sy = 0;
    float sx_x = 0;
    for(int i =0; i<n; i++)
    {
        sx_sy += x[i]*y[i];
        sx_x += x[i]*x[i];
    }
    float b = (n*sx_sy-sx*sy)/(n*sx_x-sx*sx);

    float a = my - b*mx;

    printf("y= %.3f + %.3f*x", a, b);
}

int main(void)
{
    vector<float> x = { 5, 7, 12, 16, 20 };
    vector<float> y = { 40, 120, 180, 210, 240 };
    regression(x,y);
    return 0;
}