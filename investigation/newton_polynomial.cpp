#include <iostream>

using namespace std;
#define MAXN 100

int n = MAXN;
double xs[MAXN];
double ys[MAXN];
double div_diffs[MAXN][MAXN];

void build_div_diffs() {
  for(int i = 0; i < n; ++i) {
    div_diffs[i][0] = ys[i];
  }

  for(int i = 1; i < n; ++i) {
    for(int j = 0; j < n - i; ++j) {
      double num = div_diffs[j][i - 1] - div_diffs[j + 1][i - 1];
      double den = xs[j] - xs[i + j];
      div_diffs[j][i] = num / den;
    }
  }
}

double N(double x) {
  double result = 0;

  for(int i = n - 1; i > 0; --i) {
    result = (result + div_diffs[0][i]) * (x - xs[i - 1]);
  }

  result += div_diffs[0][0];

  return result;
}

int main() {
  cout << "Enter the number of points <n>: ";
  cin >> n;

  for(int i = 0; i < n; ++i) {
    cout << "Point #" << i << ". Enter <x> <y>: ";
    cin >> xs[i] >> ys[i];
  }

  build_div_diffs();

  int m;
  cout << "Enter the number of tests <m>: ";
  cin >> m;

  for(int i = 0; i < m; ++i) {
    double x;
    cout << "Evaluation #" << i << ". Enter <x>: ";
    cin >> x;
    cout << "f(" << x << ") = " << N(x) << endl;
  }
}
