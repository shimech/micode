#include <stdio.h>
#include "stack.h"

int main() {
  push('o');
  push('y');
  push('k');
  push('o');
  push('t');
  while (!empty_s()) {
    printf("%c ", pop());
  }
  printf("\n");
  return 0;
}
