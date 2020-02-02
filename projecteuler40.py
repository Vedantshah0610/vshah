#include<iostream>
#include <sstream>
#include <cstring>
#include <stdlib.h>
using namespace std;
int main()
{
    int num;
    long long int mul;
    string result;
    cin>>num;
    stringstream str1;
    for(int i=2;i<=num;i++)
    {
    str1 << i;
    string geek = str1.str();
    char s[1000001]={'1'};
    result= s + geek;
    }
    long long int x;
    for(int i=1;i<1000000+1 ;)
    {
        i=i-1;
        cout<<"loop"<<result[i];
        int k=atoi( (result[i]+"") );

       cout<<endl<<"|"<<k<<"|";
        x=x*k;
        i=i+1;
        i=i*10;
    }	
    return 0;
}

