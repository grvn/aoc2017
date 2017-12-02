#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
  //  ifstream file("test_input1");
  ifstream file("code");
  if(!file.is_open()) {std::cout << "ERROR" << '\n';return 2;};
  string line;
  int result = 0;
  while(getline(file,line)){
    stringstream ss(line);
    int data, high, low;
    bool first = true;
    while(ss >> data){
      if(high < data || first){high=data;}
      if(low > data || first){low=data;}
      first=false;
    }
    result += (high-low);
  }
  cout << "Checksum är: " << result << '\n';  
  return 0;
}
