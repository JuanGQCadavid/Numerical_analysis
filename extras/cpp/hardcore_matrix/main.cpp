#include "matrix.hh"
#include "utils.hh"

int n;

int main() {
  read_variable(n);
  Matrix A; read_matrix(A);
  Matrix Ainv = inverse(A);
  print_matrix(multiply(A, Ainv));
}
