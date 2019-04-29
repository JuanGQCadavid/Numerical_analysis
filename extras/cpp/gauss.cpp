#include <bits/stdc++.h>

using namespace std;
#define MAXN 100
#define print_variable(_x)                      \
  { cout << #_x " = " << _x << endl; }
#define print_vector(_vec, _n)                  \
  { cout << #_vec " = [";                       \
    for(int _i = 0; _i < _n; ++_i)              \
      cout << (_i? ", " : "") << _vec[_i];      \
    cout << "]" << endl; }
#define print_matrix(_mat, _n, _m)                      \
  { cout << #_mat " = [\n";                             \
    for(int _i = 0; _i < _n; ++_i) {                    \
      cout << "  [";                                    \
      for(int _j = 0; _j < _m; ++_j)                    \
        cout << (_j? ", " : "") << _mat[_i][_j];        \
      cout << "]\n"; }                                  \
    cout << "]" << endl; }

bool partial = false, total = false;

int marks[MAXN] = {};
double Ab[MAXN][MAXN + 1] = {};
double x[MAXN] = {};
int n = 0;

void partial_pivot(int k) {
  double max_val = Ab[k][k];
  int max_idx = k;

  for(int i = k + 1; i < n; ++i)
    if(Ab[i][k] > Ab[k][k])
      max_val = Ab[i][k], max_idx = i;

  if(max_idx != k)
    for(int i = k; i <= n; ++i)
      swap(Ab[k][i], Ab[max_idx][i]);

  cout << "* PARTIAL PIVOT *" << endl;
  if(max_idx != k) print_matrix(Ab, n, n + 1);
}

void total_pivot(int k) {
  double max_val = Ab[k][k];
  int max_idx_row = k;
  int max_idx_col = k;

  for(int i = k; i < n; ++i)
    for(int j = k; j < n; ++j)
      if(Ab[i][j] > max_val)
        max_val = Ab[i][j], max_idx_row = i, max_idx_col = j;

  if(max_idx_row != k)
    for(int i = k; i <= n; ++i)
      swap(Ab[k][i], Ab[max_idx_row][i]);

  if(max_idx_col != k) {
    for(int i = k; i < n; ++i)
      swap(Ab[i][k], Ab[i][max_idx_col]);
    swap(marks[k], marks[max_idx_col]);
  }

  cout << "* TOTAL PIVOT *" << endl;

  if(max_idx_row != k || max_idx_col != k) {
    print_vector(marks, n);
    print_matrix(Ab, n, n + 1);
  }
}

void gaussian_elimination() {
  cout << "* GAUSSIAN ELIMINATION *" << endl;

  for(int k = 0; k < n - 1; ++k) {
    if(total) total_pivot(k);
    else if(partial) partial_pivot(k);

    for(int i = k + 1; i < n; ++i) {
      double mik = Ab[i][k] / Ab[k][k];

      print_variable(mik);

      for(int j = k; j <= n; ++j)
        Ab[i][j] -= Ab[k][j] * mik;
    }

    print_matrix(Ab, n, n + 1);
  }
}

void regressive_clearance() {
  cout << "* REGRESSIVE CLEARANCE *" << endl;

  for(int i = n - 1; i >= 0; --i) {
    double sum = 0;

    for(int j = i + 1; j < n; ++j)
      sum += Ab[i][j] * x[marks[j]];

    x[marks[i]] = (Ab[i][n] - sum) / Ab[i][i];
    print_vector(x, n);
  }
}

int main(int argc, char** argv, char** env) {
  if(argc == 2 && string(argv[1]) == "help") {
    cout << "gauss [total | partial]" << endl;
    return 0;
  }

  for(int i = 1; i < argc; ++i) {
    string arg = argv[i];

    if(!total && arg == "partial")
      partial = true;
    else if(!partial && arg == "total")
      total = true;
  }

  for(int i = 0; i < MAXN; ++i) x[i] = NAN, marks[i] = i;

  cout << "Enter <n>: ";
  cin >> n;

  for(int i = 0; i < n; ++i) {
    cout << "Enter row #" << i + 1 << " of A|b: ";
    for(int j = 0; j <= n; ++j) cin >> Ab[i][j];
  }

  print_matrix(Ab, n, n + 1);

  gaussian_elimination();
  regressive_clearance();

  return 0;
}
