// Problem :: problem has 3 variations. 

In Pascal triangle, each number is the sum of the two numbers

Variation 1 : Given row number r and column number c. print element at position(r,c) in pascal triangle


#include<bits/stdcc++.h>
using namespace std;
int nCr(int n, int r)
{
  long long rs = 1;
for(int i=0;i<r;i++){
rs = rs*(n-i);
rs = rs/(i+1);
}
return rs;
}
int main(){
  int r = 5;
  int c = 3;
  int elent = pascalTriangle(r,c);
  cout<<"element at (r,c) is : "<<elent;
  return 0;
}


VARIATION 2 : GIVEN ROW NUMBER N. PRITN THE NTH ROW OR PASCAL TRIANGLE.

  T.C = O(N*R) S.C = O(1)

  int nCr(int N, int R){
  long long rs = 1;
      for(int i=0;i<R;i++){
           rs = rs*(N-i);
           rs = rs/(i+1);
      }
   return rs;
}

int pascalTriangle(int n)
{
for(int c=1;c<=N;c++)
{
cout<<nCr(N-1, c-1);
}
cout<<endl;
}
int main()
{
  int N= 5;
  pascalTriangle(N);
  return 0;
}



OPTIMAL SOLUTION

T.C = O(n) S.C = O(1)

  void PT(int n)
{
  long long an = 1;
  count<<an<<" ";
  for(int i = 1; i<n;i++)
  {
  an = an*(n-i);
  an = an/i;
  cout<<an<<" ";
  }
  cout <<endl;
}

int main()
{
  int n = 5;
  PT(n);
  return 0;
}


VARIATION 3: GIVEN  NUMBER OF ROWS n. PRINT FIRST n ROWS OF PASCAL TRIANGLE.
  T.C = O(n*n*r) S.C = O(1)

  int nCr(int n, int r)
{
  long long an =1;
  for(int i=0; i<r; i++)
  {
  an = an*(n-i);
  an = an/(i+1);
  }
  return an;
}

vector<vector<int>>PT(int n)
{
  vector<vector<int>> rs;

//store entire pascal triangle

for(int r=1; r<=n; r++)
{
vector<int> temp;
for(int c =1; c<= r; c++)
  { 
  temp.push_back(nCr(r-1, c-1));
  }
  rs.push_back(temp);
}
return rs;
}


int main()
{
  int n = 5;
  vector<vector<int>> rs = PT(n);
  for(auto it: rs)
  {
  for (auto ele:it)
  { 
  cout<<ele<<" ";
  }
  cout<<endl;
 }
}



/// OPTIMAL SOLUTION

T.C = O(N*N)  S.C = O(1)

  vector<vector<int>> PT(int n)
{
  vector<vector<int>> rs;

  //store entire pascal triangle
  for(int r=0; r<=n; r++)
  {
  rs.push_back(generateRow(r));
  }
  return rs;
}

int main()
{
  int n = 5;
  vector<vector<int>> rs= PT(n);
    for(auto it: rs)
  {
  for( auto ele: it)
  {
    cout<<ele<<" ";
  }
  cout<<endl;
 }
}
