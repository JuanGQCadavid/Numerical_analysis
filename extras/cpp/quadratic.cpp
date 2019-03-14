#include <iostream>
#include <utility>
#include <cmath>

using namespace std;

pair<double, double> quadratic(double a, double b, double c, double epsilon) {
  if(a == 0) {
    if(b == 0) {
      throw "INVALID_EQUATION: 0x^2 + 0x + c";
    } else {
      double x = (-c) / b;
      return make_pair(x, x);
    }
  } else {
    double determinant = b * b - 4 * a * c;

    if(determinant > 0) {
      determinant = sqrt(determinant);

      double x0, x1;

      if(abs((b - determinant) / b) <= epsilon) {
        x0 = (-b - determinant) / (2 * a);
        x1 = (2 * c) / (-b - determinant);
      } else if(abs(a) <= epsilon) {
        x0 = (2 * c) / (-b + determinant);
        x1 = (2 * c) / (-b - determinant);
      } else {
        x0 = (-b - determinant) / (2 * a);
        x1 = (2 * c) / (-b - determinant);
      }

      return make_pair(x0, x1);
    } else if(determinant == 0) {
      double x;

      if(abs(a) <= epsilon) {
        x = (2 * c) / (-b);
      } else {
        x = (-b) / (2 * a);
      }

      return make_pair(x, x);
    } else {
      throw "NO_SOLUTION_FOUND: determinant less than 0";
    }
  }
}

int main() {
  cout << "Enter <a> <b> <c> for solving ax2+bx+c: ";
  double a, b, c;
  cin >> a >> b >> c;

  try {
    auto result = quadratic(a, b, c, 0.001);
    double x0 = result.first, x1 = result.second;

    printf("x0 = %e => f(x0) = %e\n", x0, (a * x0 + b) * x0 + c);
    printf("x1 = %e => f(x1) = %e\n", x1, (a * x1 + b) * x1 + c);
  } catch(char const* exception) {
    cout << exception << endl;
  }
}
