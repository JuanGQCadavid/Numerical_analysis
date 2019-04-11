#include <bits/stdc++.h>

using namespace std;
#define MAXN 100

int debug = 0;

bool gauss = false,
  partial = false,
  total = false;

int marks[MAXN] = {};
double Ab[MAXN][MAXN + 1] = {};
double L[MAXN][MAXN + 1] = {};
double U[MAXN][MAXN + 1] = {};

int n = 0;

void print_help() {
  cout <<
    "matrix_solver [DEBUG | METHOD | MOD]+\n\n"

    "DEBUG:\n"
    "  1: print each matrix per operation\n"
    "  2: also print multipliers, pivots, etc...\n"
    "  by default only the resulting matrix is printed\n\n"

    "METHOD:\n"
    "  gauss\n\n"

    "MOD:\n"
    "  partial: partial pivot\n"
    "  total: total pivot\n"
       << endl;
}

void print_Ab() {
  cout << "[A|b]:\n";
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j <= n; ++j)
      cout << (j? " " : "") << Ab[i][j];
    cout << endl;
  }
}

void print_marks() {
  cout << "marks:\n";
  for(int i = 0; i < n; ++i)
    cout << (i? " " : "") << marks[i];
  cout << endl;
}

#define print_variable(x) cout << #x << " = " << x << endl

void partial_pivot(int k) {
  double max_val = Ab[k][k];
  int max_idx = k;

  for(int i = k + 1; i < n; ++i)
    if(Ab[i][k] > Ab[k][k])
      max_val = Ab[i][k], max_idx = i;

  if(max_idx != k)
    for(int i = k; i <= n; ++i)
      swap(Ab[k][i], Ab[max_idx][i]);
}

void total_pivot(int k) {
  double max_val = Ab[k][k];
  int max_idx_row = k;
  int max_idx_col = k;

  for(int i = k; i < n; ++i)
    for(int j = k; j < n; ++i)
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
}

void total_pivot_fix_cols() {

}

void gaussian_elimination() {
  for(int k = 0; k < n - 1; ++k) {

    if(total) total_pivot(k);
    else if(partial) partial_pivot(k);

    for(int i = k + 1; i < n; ++i) {
      double mik = Ab[i][k] / Ab[k][k];

      for(int j = k; j <= n; ++j) {
        Ab[i][j] -= Ab[k][j] * mik;
      }
    }
  }
}

void progressive_clearance() {

}

void regressive_clearance() {
}

int main(int argc, char** argv) {
  if(argc == 1) {
    print_help();
    return 0;
  }

  for(int i = 1; i < argc; ++i) {
    string arg = argv[i];

    if(arg == "gauss")
      gauss = true;
    else if(!total && arg == "partial")
      partial = true;
    else if(!partial && arg == "total") {
      total = true;

      for(int i = 0; i < n; ++i)
        marks[i] = i;
    } else if(debug == 0 && (arg == "1" || arg == "2"))
      debug = arg[0] - '0';
  }

  cout << "Enter <n>: ";
  cin >> n;

  for(int i = 0; i < n; ++i) {
    cout << "Enter row #" << i + 1 << " of [A|b]: ";

    for(int j = 0; j <= n; ++j) {
      cin >> Ab[i][j];
    }
  }

  if(gauss) {
    gaussian_elimination();

    if(total) {
      total_pivot_fix_cols();
    }
  }

  print_Ab();

  return 0;
}
