#include <bits/stdc++.h>

using namespace std;
#define MAXN 100

int debug = 0;

bool gauss = false,
  partial = false,
  total = false,
  lu = false;

int marks[MAXN] = {};
double Ab[MAXN][MAXN + 1] = {};
double L[MAXN][MAXN] = {};
double U[MAXN][MAXN] = {};
double answers[MAXN] = {};

int n = 0;

void print_help() {
  cout <<
    "matrix_solver [DEBUG | METHOD | MOD]+\n\n"

    "DEBUG:\n"
    "  1: print each matrix per operation\n"
    "  2: also print multipliers, pivots, etc...\n"
    "  by default only the resulting matrix is printed\n\n"

    "METHOD:\n"
    "  gauss: solve with gauss\n"
    "  lu: solve with lu factorization\n\n"

    "MOD:\n"
    "  partial: solve with partial pivot\n"
    "  total: solve with total pivot\n"
       << endl;
}

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

void partial_pivot(int k) {
  double max_val = Ab[k][k];
  int max_idx = k;

  for(int i = k + 1; i < n; ++i)
    if(Ab[i][k] > Ab[k][k])
      max_val = Ab[i][k], max_idx = i;

  if(max_idx != k)
    for(int i = k; i <= n; ++i)
      swap(Ab[k][i], Ab[max_idx][i]);

  if(debug >= 2) {
    cout << "* PARTIAL PIVOT *" << endl;

    if(max_idx != k) print_matrix(Ab, n, n + 1);
  }
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

  if(debug >= 2) {
    cout << "* TOTAL PIVOT *" << endl;

    if(max_idx_row != k || max_idx_col != k) {
      print_vector(marks, n);
      print_matrix(Ab, n, n + 1);
    }
  }
}

void gaussian_elimination() {
  if(debug >= 2) cout << "* GAUSSIAN ELIMINATION *" << endl;

  for(int k = 0; k < n - 1; ++k) {
    if(total) total_pivot(k);
    else if(partial) partial_pivot(k);

    for(int i = k + 1; i < n; ++i) {
      double mik = Ab[i][k] / Ab[k][k];

      if(debug >= 2) print_variable(mik);

      for(int j = k; j <= n; ++j)
        Ab[i][j] -= Ab[k][j] * mik;
    }

    if(debug >= 2) print_matrix(Ab, n, n + 1);
  }

  if(debug == 1) print_matrix(Ab, n, n + 1);
}

void regressive_clearance() {
  if(debug >= 2) cout << "* REGRESSIVE CLEARANCE *" << endl;

  for(int i = n - 1; i >= 0; --i) {
    double sum = 0;

    for(int j = i + 1; j < n; ++j)
      sum += Ab[i][j] * answers[marks[j]];

    answers[marks[i]] = (Ab[i][n] - sum) / Ab[i][i];
    if(debug >= 1) print_vector(answers, n);
  }
}

void build_LU() {
  if(debug >= 2) cout << "* LU FACTORIZATION *" << endl;

  for(int k = 0; k < n; ++k) {
    double sum = 0;

    for(int p = 0; p < k; ++p) sum += L[k][p] * U[p][k];
    L[k][k] = U[k][k] = sqrt(Ab[k][k] - sum);

    for(int i = k + 1; i < n; ++i) {
      sum = 0;
      for(int p = 0; p < k; ++p) sum += L[i][p] * U[p][k];
      L[i][k] = (Ab[i][k] - sum) / U[k][k];
    }

    for(int j = k + 1; j < n; ++j) {
      sum = 0;
      for(int p = 0; p < k; ++p) sum += L[k][p] * U[p][j];
      U[k][j] = (Ab[k][j] - sum) / L[k][k];
    }

    if(debug >= 2) {
      print_matrix(L, n, n);
      print_matrix(U, n, n);
    }
  }

  if(debug == 1) {
    print_matrix(L, n, n);
    print_matrix(U, n, n);
  }
}

int main(int argc, char** argv, char** env) {
  if(argc == 1) {
    print_help();
    return 0;
  }

  for(int i = 1; i < argc; ++i) {
    string arg = argv[i];

    if(!lu && arg == "gauss")
      gauss = true;
    else if(!gauss && arg == "lu")
      lu = true;
    else if(!total && arg == "partial")
      partial = true;
    else if(!partial && arg == "total")
      total = true;
    else if(debug == 0 && (arg == "1" || arg == "2"))
      debug = arg[0] - '0';
  }

  for(int i = 0; i < MAXN; ++i) answers[i] = NAN;
  for(int j = 0; j < MAXN; ++j) marks[j] = j;

  cout << "Enter <n>: ";
  cin >> n;

  for(int i = 0; i < n; ++i) {
    cout << "Enter row #" << i + 1 << " of A|b: ";
    for(int j = 0; j <= n; ++j) cin >> Ab[i][j];
  }

  if(debug >= 1) print_matrix(Ab, n, n + 1);

  if(gauss) {
    gaussian_elimination();
    regressive_clearance();

    if(debug == 0) {
      print_matrix(Ab, n, n + 1);
      print_vector(answers, n);
    }
  } else if(lu) {
    build_LU();
  }

  return 0;
}
