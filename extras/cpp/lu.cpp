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

double A[MAXN][MAXN] = {};
double b[MAXN] = {};

double L[MAXN][MAXN] = {};
double U[MAXN][MAXN] = {};

double z[MAXN] = {};
double x[MAXN] = {};

int n = 0;

void lu_factorization() {
  cout << "* LU FACTORIZATION *" << endl;

  for(int k = 0; k < n; ++k) {
    double sum = 0;

    for(int p = 0; p < k; ++p) sum += L[k][p] * U[p][k];
    L[k][k] = U[k][k] = sqrt(A[k][k] - sum);

    for(int i = k + 1; i < n; ++i) {
      sum = 0;
      for(int p = 0; p < k; ++p) sum += L[i][p] * U[p][k];
      L[i][k] = (A[i][k] - sum) / U[k][k];
    }

    for(int j = k + 1; j < n; ++j) {
      sum = 0;
      for(int p = 0; p < k; ++p) sum += L[k][p] * U[p][j];
      U[k][j] = (A[k][j] - sum) / L[k][k];
    }

    print_matrix(L, n, n);
    print_matrix(U, n, n);
  }
}

void regressive_clearance() {
  cout << "* REGRESSIVE CLEARANCE *" << endl;

  for(int i = n - 1; i >= 0; --i) {
    double sum = 0;

    for(int j = i + 1; j < n; ++j)
      sum += U[i][j] * z[j];

    z[i] = (b[i] - sum) / U[i][i];
    print_vector(z, n);
  }
}

void progressive_clearance() {
  cout << "* PROGRESSIVE CLEARANCE *" << endl;

  for(int i = 0; i < n; ++i) {
    double sum = 0;

    for(int j = 0; j < i; ++j)
      sum += L[i][j] * x[j];

    x[i] = (z[i] - sum) / L[i][i];
    print_vector(x, n);
  }
}

int main(int argc, char** argv, char** env) {
  cout << "Enter <n>: ";
  cin >> n;

  for(int i = 0; i < n; ++i) {
    cout << "Enter row #" << i + 1 << " of A|b: ";
    for(int j = 0; j < n; ++j) cin >> A[i][j];
    cin >> b[i];
  }

  print_matrix(A, n, n);
  print_vector(b, n);

  lu_factorization();
  regressive_clearance();
  progressive_clearance();

  return 0;
}
