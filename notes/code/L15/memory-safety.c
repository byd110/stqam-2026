#define SIZE 20
char buffer[SIZE];

char read_buffer(int i)  { return buffer[i];     }
char read_pointer(int i) { return *(buffer + i); }

int main() {
  int index;
  read_buffer(index);
  read_pointer(index);
}
