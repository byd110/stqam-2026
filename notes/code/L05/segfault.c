#include <stdlib.h>

int main()
{
  int * q = malloc(5*sizeof(int));
  q[2000000] = 4;
}
