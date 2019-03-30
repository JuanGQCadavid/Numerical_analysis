#include <bits/stdc++.h>

using namespace std;

double (*f)(double x) = cos;

double regula_falsi(double xl, double xh, double tolerance, unsigned int iterations) {
  if(xl <= xh) {
    if(tolerance >= 0) {
      double yl = f(xl), yh = f(xh);

      if(yl == 0) {
        return xl;
      } else if(yh == 0) {
        return xh;
      } else if(yl * yh < 0) {
        if(iterations > 0) {
          double xm = (xl + xh) / 2, ym = f(xm);

          double error = 1e100;
          int count = 1;

          while(ym != 0 && error > tolerance && count < iterations) {
            if(yl * ym < 0) {
              xh = xm, yh = ym;
            } else {
              xl = xm, yl = ym;
            }

            double tmp_xm = xm;
            xm = xl - (yl * (xh - xl) / (yh - yl)), ym = f(xm);
            error = abs(tmp_xm - xm);
            ++count;
          }

          if(ym == 0 || error <= tolerance) {
            return xm;
          } else {
            throw "ITERATIONS_LIMIT_EXCEEDED: no result found";
          }
        } else {
          throw "INVALID_PARAMETER: iterations = 0";
        }
      } else {
        throw "INVALID_PARAMETERS: yl * yh > 0";
      }
    } else {
      throw "INVALID_PARAMETER: tolerance < 0";
    }
  } else {
    throw "INVALID_PARAMETERS: xl > xh";
  }
}

int main() {
  double xl, xh, tolerance;
  int iterations;

  cout << "Enter <xl> <xh> <tolerance> <iterations>: ";
  cin >> xl >> xh >> tolerance >> iterations;

  try {
    double result = regula_falsi(xl, xh, tolerance, iterations);
    printf("x = %e => f(x) = %e\n", result, f(result));
  } catch(char const* exception) {
    cout << exception << endl;
  }
}
