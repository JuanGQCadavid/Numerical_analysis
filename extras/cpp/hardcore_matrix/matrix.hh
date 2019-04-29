#include <cmath>

#define MAXN 10

extern int n;

struct Matrix {
  double values[MAXN][MAXN] = {};
  double* operator[](int i) {
    return values[i];
  }
};

struct Vector {
  double values[MAXN] = {};
  double& operator[](int i) {
    return values[i];
  }
};

Vector progressive_clearance(Matrix A, Vector b) {
  Vector x;

  for(int i = 0; i < n; ++i) {
    double sum = 0;
    for(int j = 0; j < i; ++j) sum += A[i][j] * x[j];
    x[i] = (b[i] - sum) / A[i][i];
  }

  return x;
}

Vector regressive_clearance(Matrix A, Vector b) {
  Vector x;

  for(int i = n - 1; i >= 0; --i) {
    double sum = 0;
    for(int j = i + 1; j < n; ++j) sum += A[i][j] * x[j];
    x[i] = (b[i] - sum) / A[i][i];
  }

  return x;
}

void lu_factorization(Matrix A, Matrix& L, Matrix& U) {
  for(int k = 0; k < n; ++k) {
    double sum = 0;
    for(int p = 0; p < k; ++p) sum += L[k][p] * U[p][k];
    L[k][k] = U[k][k] = std::sqrt(A[k][k] - sum);

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
  }
}

double det(Matrix A) {
  Matrix L, U;
  lu_factorization(A, L, U);

  double prod = 1;
  for(int i = 0; i < n; ++i) prod *= L[i][i] * U[i][i];

  return prod;
}

Matrix inverse(Matrix A) {  
  Matrix result, L, U;
  lu_factorization(A, L, U);

  Vector b;
  for(int i = 0; i < n; ++i) {
    b[i] = 1; if(i > 0) b[i - 1] = 0;
    Vector z = progressive_clearance(L, b);
    Vector x = regressive_clearance(U, z);
    //where does the vector go? as a column or as a row?
  }

  return result;
}
