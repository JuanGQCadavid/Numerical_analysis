#include <iostream>

using namespace std;

int fact(int n) {
  if(n == 0) return 1;
  else return fact(n - 1) * n;
}

double pow(double x, int n) {
  if(n == 0) return 1.0;
  else if(n & 1) return x * pow(x, n - 1);
  else {
    double val = pow(x, n >> 1);
    return val * val;
  }
}

int main() {
  double x;

  cout << "We will calculate e ^ x with 4 significant digits. Enter <x>: ";
  cin >> x;

  double max_err = 5.0e-4;
  double c_val = 1.0, p_val = 1.0e10;

  for(int i = 1; abs((c_val - p_val) / c_val) >= max_err; ++i) {
    p_val = c_val;
    c_val += pow(x, i) / fact(i);
  }

  cout << c_val << endl;
}
