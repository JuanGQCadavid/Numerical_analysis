#include <bits/stdc++.h>

using namespace std;

double (*f)(double x) = exp;

double minitrapezoid(double x0, double x1) {
  return (x1 - x0) * (f(x0) + f(x1)) / 2;
}

double trapezoid(double x0, double xn, int n) {
  double h = (xn - x0) / n;
  double acum = 0;

  for(int i = 1; i < n; ++i) {
    acum += f(x0 + h * i);
  }

  return (h / 2) * (f(x0) + 2 * acum + f(xn));
}

double minisimpson13(double x0, double x1, double x2, double h) {
  return (h / 3) * (f(x0) + 4 * f(x1) + f(x2));
}

double simpson13(double x0, double xn, int n) {
  double h = (xn - x0) / n;

  double oddacum = 0;
  double evenacum = 0;

  for(int i = 1; i < n; i += 2) {
    oddacum += f(x0 + h * i);
  }

  for(int i = 2; i < n; i += 2) {
    evenacum += f(x0 + h * i);
  }

  return (h / 3) * (f(x0) + 4 * oddacum + 2 * evenacum + f(xn));
}

double minisimpson38(double x0, double x1, double x2, double x3, double h) {
  return (3 * h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3));
}

double simpson38(double x0, double xn, int n) {
  double h = (xn - x0) / n;
  double acumno3 = 0;
  double acum3 = 0;

  for(int i = 1; i < n; ++i) {
    if(i % 3 == 0) {
      acum3 += f(x0 + h * i);
    } else {
      acumno3 += f(x0 + h * i);
    }
  }

  return (3 * h / 8) * (f(x0) + 3 * acumno3 + 2 * acum3 + f(xn));
}

int main() {
  double a, b;
  int n;
  cout << "Enter <a> <b> <n> for calculating INTEGRAL(exp, a, b): ";
  cin >> a >> b;
  cout << "trapezoid: " << trapezoid(a, b, n) << endl;
  cout << "simpson13: " << simpson13(a, b, n) << endl;
  cout << "simpson38: " << simpson38(a, b, n) << endl;
}
