#include <stdlib.h>
#include "element.h"
ELEM *root_s = NULL;

int empty_s () {
  return (root_s == NULL);
}

void push(char x) {
  ELEM *e;
  e = (ELEM *)malloc(sizeof(ELEM));
  if (e != NULL) {
    e->v = x;
    e->p = root_s;
    root_s = e;
  }
}

char pop() {
  char r = 0;
  if (!empty_s()) {
    ELEM *e;
    e = root_s;
    r = root_s->v;
    root_s = e->p;
    free(e);
  }
  return r;
}
