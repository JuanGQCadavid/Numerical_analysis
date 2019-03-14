#include <cstdio>

int main() {
  double curr, prev;

  prev = curr = 0.5;
  while(curr + 1.0 != 1.0) prev = curr, curr /= 2.0;

  printf("+ 1: %e\n", prev);

  prev = curr = 0.5;
  while(curr != 0.0) prev = curr, curr /= 2.0;

  printf(": %e\n", prev);
}
