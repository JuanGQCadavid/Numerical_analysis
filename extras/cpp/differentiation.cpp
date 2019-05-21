#include <bits/stdc++.h>

using namespace std;

#define errfx2points (h / 2) * fxx(xi)
#define errfx3pointsleft h * h / 3 * fxxx(xi)
#define errfx3pointsmiddle h * h / 6 * fxxx(xi)
#define errfx3pointsright h * h / 3 * fxxx(xi)
#define errfx5pointsmiddle1 ((h * h) * (h * h)) / 30 * fxxxx(xi)
#define errfx5pointsforward ((h * h) * (h * h)) / 5 * fxxxxx(xi)

double (*f)(double x) = exp;


double fx2points(double x, double h) {
  return (f(x + h) - f(x)) / h;
}

double fx3pointsleft(double x, double h) {
  return (f(x - 2 * h) - 4 * f(x - h) + 3 * f(x)) / (2 * h);
}

double fx3pointsmiddle(double x, double h) {
  return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h);
}

double fx3pointsright(double x, double h) {
  return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h);
}

double fx5pointsmiddle1(double x, double h) {
  return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h);
}

double fx5pointsforward(double x, double h) {
  return (-25 * f(x) + 48 * f(x + h) - 36 * f(x + 2 * h) + 16 * f(x + 3 * h) - 3 * f(x + 4 * h)) / (12 * h);
}

int main() {
  double x, h;
  cout << "Enter <x> and <h> for evaluating the derivative of e^x: ";
  cin >> x >> h;
  cout << fx2points(x, h) << endl;
  cout << fx3pointsleft(x, h) << endl;
  cout << fx3pointsmiddle(x, h) << endl;
  cout << fx3pointsright(x, h) << endl;
  cout << fx5pointsmiddle1(x, h) << endl;
  cout << fx5pointsforward(x, h) << endl;
  cout << f(x) << endl;
}
