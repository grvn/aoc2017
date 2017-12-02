#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int find_modulo(const std::vector<int>& ints){
  for(auto &i : ints){
    for(auto &j : ints){
      if((i != j) && ((i%j)==0)){
	  return i/j;
      }
    }
  }
  return 0;
}

int main() {
  //  ifstream file("test_input2");
  ifstream file("code");
  if(!file.is_open()) {std::cout << "ERROR" << '\n';return 2;};
  string line;
  int result = 0;
  while(getline(file,line)){
    stringstream ss(line);
    vector<int> ints;
    int data;
    while(ss >> data){ints.push_back(data);}
    result += find_modulo(ints);
  }
  cout << "Checksum är: " << result << '\n';  
  return 0;
}
