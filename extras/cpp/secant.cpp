#include <bits/stdc++.h>

using namespace std;

double f(double x) {
  return cos(x) + x;
}

double secant(double x0, double x1, double tolerance, unsigned int iterations) {
  if(tolerance >= 0) {
    if(iterations > 0) {
      double y0 = f(x0);
      double y1 = f(x1);

      if(y0 == 0) {
        return x0;
      } else if(y1 == 0) {
        return x1;
      } else {
        double error = abs(x1 - x0);
        int count = 0;

        while(y1 != 0 && error > tolerance && count < iterations) {
          double tmp = x1 - y1 * (x1 - x0) / (y1 - y0);
          x0 = x1;
          y0 = y1;
          x1 = tmp;
          y1 = f(x1);
          error = abs(x1 - x0);
          ++count;
        }

        if(y1 == 0 || error <= tolerance) {
          return x1;
        } else {
          throw "ITERATIONS_LIMIT_EXCEEDED: result not found";
        }
      }
    } else {
      throw "INVALID_PARAMETER: iterations = 0";
    }
  } else {
    throw "INVALID_PARAMETER: tolerance < 0";
  }
}

int main() {
  double x0, x1, tolerance;
  unsigned int iterations;

  cout << "Enter <x0> <x1> <tolerance> <iterations>: ";
  cin >> x0 >> x1 >> tolerance >> iterations;

  try {
    double result = secant(x0, x1, tolerance, iterations);
    printf("x = %e => f(x) = %e\n", result, f(result));
  } catch(char const* exception) {
    cout << exception << endl;
  }
}
