#include <iostream>

#define read_variable(_x)                               \
  { std::cout << "Enter " #_x ": "; std::cin >> _x; }
#define read_vector(_vec)                                       \
  { std::cout << "Enter vector " #_vec ": ";                    \
    for(int _i = 0; _i < n; ++_i) std::cin >> _vec[_i]; }
#define read_matrix(_mat)                                       \
  { std::cout << "Enter matrix " #_mat ":\n";                   \
    for(int _i = 0; _i < n; ++_i)                               \
      for(int _j = 0; _j < n; ++_j) std::cin >> _mat[_i][_j]; }
#define read_matrix_vector(_mat, _vec)                          \
  { std::cout << "Enter matrix " #_mat #_vec ":\n";             \
    for(int _i = 0; _i < n; ++_i) {                             \
      for(int _j = 0; _j < n; ++_j) std::cin >> _mat[_i][_j];   \
      std::cin >> _vec[_i]; }}

#define print_variable(_x)                              \
  { std::cout << #_x " = " << _x << std::endl; }
#define print_vector(_vec)                      \
  { std::cout << #_vec " = [";                  \
    for(int _i = 0; _i < n; ++_i)               \
      std::cout << (_i? ", " : "") << _vec[_i]; \
    std::cout << "]" << std::endl; }
#define print_matrix(_mat)                              \
  { std::cout << #_mat " = [\n";                        \
    for(int _i = 0; _i < n; ++_i) {                     \
      std::cout << "  [";                               \
      for(int _j = 0; _j < n; ++_j)                     \
        std::cout << (_j? ", " : "") << _mat[_i][_j];   \
      std::cout << "]\n"; }                             \
    std::cout << "]" << std::endl; }
#define print_matrix_vector(_mat, _vec)                 \
  { std::cout << #_mat #_vec " = [\n";                  \
    for(int _i = 0; _i < n; ++_i) {                     \
      std::cout << "  [";                               \
      for(int _j = 0; _j < n; ++_j)                     \
        std::cout << (_j? ", " : "") << _mat[_i][_j];   \
      std::cout << "]\n"; }                             \
    std::cout << "]" << std::endl; }
