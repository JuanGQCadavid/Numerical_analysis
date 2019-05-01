#include <bits/stdc++.h>

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
  Matrix L, U;
  lu_factorization(A, L, U);

  for(int i = 0; i < n; ++i) {
    Vector b; b[i] = 1;
    Vector z = progressive_clearance(L, b);
    Vector x = regressive_clearance(U, z);
    for(int j = 0; j < n; ++j) A[j][i] = x[j];
  }

  return A;
}

Matrix multiply(Matrix A, Matrix B) {
  Matrix C;
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      for(int k = 0; k < n; ++k)
        C[i][j] += A[i][k] * B[k][j];
  return C;
}

Vector multiply(Matrix A, Vector b) {
  Vector c;
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      c[i] += A[i][j] * b[j];
  return c;
}

Matrix add(Matrix A, Matrix B) {
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      A[i][j] = A[i][j] + B[i][j];
  return A;
}

Vector add(Vector a, Vector b) {
  for(int i = 0; i < n; ++i)
    a[i] = a[i] + b[i];
  return a;
}

double norminf(Vector b) {
  double max_value = 0;
  for(int i = 0; i < n; ++i)
    max_value = std::max(max_value, b[i]);
  return max_value;
}

double norm1(Vector b) {
  double acum = 0;
  for(int i = 0; i < n; ++i)
    acum += std::abs(b[i]);
  return acum;
}

double norm2(Vector b) {
  double acum = 0;
  for(int i = 0; i < n; ++i)
    acum += b[i] * b[i];
  return std::sqrt(acum);
}

double norminf(Matrix A) {
  double max_value = 0;
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      max_value = std::max(max_value, A[i][j]);
  return max_value;
}

double norm1(Matrix A) {
  double acum = 0;
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
    acum += std::abs(A[i][j]);
  return acum;
}

double norm2(Matrix A) {
  Matrix (*transpose)(Matrix);
  double (*p)(Matrix);
  return std::sqrt(p(multiply(transpose(A), A)));
}

double normfrobenius(Matrix A) {
  double acum = 0;
  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      acum += A[i][j] * A[i][j];
  return std::sqrt(acum);
}

Vector relaxed_jacobi(Matrix A, Vector b, Vector x0, double lambda) {
  Vector x1;
  for(int i = 0; i < n; ++i) {
    double acum = 0;
    for(int j = 0; j < n; ++j) if(j != i) acum += A[i][j] * x0[j];
    x1[i] = lambda * ((b[i] - acum) / A[i][i]) + (1 - lambda) * x0[i];
  }

  return x1;
}

Vector relaxed_gauss_seidel(Matrix A, Vector b, Vector x0, double lambda) {
  for(int i = 0; i < n; ++i) {
    double acum = 0;
    for(int j = 0; j < n; ++j) if(j != i) acum += A[i][j] * x0[j];
    x0[i] = lambda * ((b[i] - acum) / A[i][i]) + (1 - lambda) * x0[i];
  }

  return x0;
}
