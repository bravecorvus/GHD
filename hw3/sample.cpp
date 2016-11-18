#include <iostream>
using namespace std;

double sample(double x, double y) {
  cout << "args are " << x << " and " << y << endl;
  return x + y;
}

int main() {
  double first;
  double second;
  cout << "What do you want to be the first value" << endl;
  cin >> first;
  cout << "What do you want to be the second value" << endl;
  cin >> second;
  cout << sample(first, second) << endl;
}