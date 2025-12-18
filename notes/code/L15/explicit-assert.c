int main()
{
  int a = 5;
  __CPROVER_assert(a == 2, "a is not 2");
  return 0;
}

