// cbmc div-by-zero.c --function foo
unsigned int foo(unsigned int x, unsigned int y) {
  if (x > y)
    return x / y;
  else
    return y / x;
}
