#include <bits/stdc++.h>

using namespace std;

double (*f)(double x) = exp;

double trap(double a, double b) {
  return (b - a) * (f(a) + f(b)) / 2;
}

double bigtrap(double a, double b, int n) {
  double acum = 0;
  for(int i = 1; i < n; ++i) {
    acum += f(a + ((b - a) / n) * i);
  }

  return ((b - a) / n) * (f(a) + f(b) + 2 * acum);
}

double minisimpson13(double x0, double x1, double x2, double h) {
  return (h / 3) * (f(x0) + 4 * f(x1) + f(x2));
}

double simpson13(double x0, double xn, int n) {
  double h = (xn - x0) / n;
  double oddacum = 0;
  double evenacum = 0;

  for(int i = 1; i < n; i+=2) {
    oddacum += f(x0 + h * i);
  }

  for(int i = 2; i < n; i+=2) {
    evenacum = f(x0 + h * i);
  }

  return (h / 3) * (f(x0) + f(xn) + 4 * oddacum + 2 * evenacum);
}

double minisimpson38(double x0, double x1, double x2, double x3, double h) {
  return (3 * h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3));
}

double simpson38(double x0, double xn, int n) {
  double acumno3 = 0;
  double acum3 = 0;
  double h = (xn - x0) / n;
  
  for(int i = 1; i < n; ++i) {
    if(i % 3 == 0) {
      acum3 += f(x0 + h * i);
    } else {
      acumno3 += f(x0 + h * i);
    }
  }
  
  return (3 * h / 8) * (6 * acumno3 + 2 * acum3 + f(x0) + f(xn));
}

int main() {
  double a, b;
  int n;
  cout << "Enter <a> <b> <n> for calculating INTEGRAL(exp, a, b): ";
  cin >> a >> b;
  cout << trap(a, b) << endl;
  cout << bigtrap(a, b, n) << endl;
}
