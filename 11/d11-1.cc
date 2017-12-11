#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

static inline void rtrim(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(), [](int ch) {
        return !std::isspace(ch);
    }).base(), s.end());
}

int main( int argc, char *argv[] ) {

  if ( argc != 2 ){
    cout<<"usage: "<< argv[0] <<" <filename>\n";
    return 1;
  }
  
  ifstream file(argv[1]);
  if(!file.is_open()) {std::cout << "ERROR" << '\n';return 2;};
  string line;
  int x=0,y=0,z=0;
  while(getline(file,line,',')){
    rtrim(line);
    if(line=="n")
      {y++;z--;}
    else if(line=="ne")
      {x++;z--;}
    else if(line=="se")
      {x++;y--;}
    else if(line=="s")
      {y--;z++;}
    else if(line=="sw")
      {x--;z++;}
    else if(line=="nw")
      {x--;y++;}
    else{}
  }
  cout << "Answer:"<<(abs(x)+abs(y)+abs(z))/2<<'\n';
  return 0;
}
