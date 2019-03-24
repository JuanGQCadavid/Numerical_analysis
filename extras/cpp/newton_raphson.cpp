#include <bits/stdc++.h>

using namespace std;

double f(double x) {
  return cos(x) + x;
}

double df(double x) {
  return x - f(x) / (-sin(x) + 1);
}

double fixed_point(double x0, double tolerance, unsigned int iterations) {
  if(tolerance >= 0) {
    if(iterations > 0) {
      double error = 1e100;
      int count = 1;
      double y0 = f(x0);

      while(y0 != 0 && error > tolerance && count < iterations) {
        double tmp = x0;
        x0 = df(x0);
        error = abs(tmp - x0);

        y0 = f(x0);
        ++count;
      }

      if(y0 == 0 || error <= tolerance) {
        return x0;
      } else {
        throw "ITERATIONS_LIMIT_EXCEEDED: result not found";
      }
    } else {
      throw "INVALID_PARAMETER: iterations = 0";
    }
  } else {
    throw "INVALID_PARAMETER: tolerance < 0";
  }
}

int main() {
  double x0, tolerance;
  unsigned int iterations;

  cout << "Enter <x0> <tolerance> <iterations>: ";
  cin >> x0 >> tolerance >> iterations;

  try {
    double result = fixed_point(x0, tolerance, iterations);
    printf("x = %e => f(x) = %e\n", result, f(result));
  } catch(char const* exception) {
    cout << exception << endl;
  }
}
