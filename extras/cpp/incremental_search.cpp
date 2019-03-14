#include <cmath>
#include <cstdio>
#include <utility>
#include <cstdlib>
#include <iostream>

using namespace std;

double (*f)(double x) = sin;

pair<double, double> incremental_search(double x0, double delta, int iterations) {
  if(delta != 0) {
    if(iterations > 0) {
      double y0 = f(x0);

      if(y0 == 0) {
	return make_pair(x0, x0);
      }

      double x1 = x0 + delta, y1 = f(x1);
      double y0y1 = y0 * y1;

      for(int i = 1; y0y1 > 0 && i < iterations; ++i) {
	x0 = x1, y0 = y1;
	x1 = x0 + delta, y1 = f(x1);
	y0y1 = y0 * y1;
      }

      if(y0y1 < 0) {
	return make_pair(x0, x1);
      } else if(y0y1 == 0) {
	return make_pair(x1, x1);
      } else {
	throw "ITERATION_LIMIT_EXCEEDED: answer not found";
      }
    } else {
      throw "INVALID_PARAMETER: iterations can't be less than or equal to 0";
    }
  } else {
    throw "INVALID_PARAMETER: delta can't be zero";
  }
}

int main() {
  double x0, delta;
  int iterations;

  cout << "Enter <x0> <delta> <iterations>: ";
  cin >> x0 >> delta >> iterations;

  try {
    auto result = incremental_search(x0, delta, iterations);
    printf("[%e, %e]\n", result.first, result.second);
  } catch(char const* exception) {
    cout << exception << endl;
  }
}
