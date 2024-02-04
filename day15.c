#include <stdlib.h> 
#include <string.h>
#include <stdio.h>

char *readline(FILE *file) {
    char c;
    size_t size = 512;
    size_t len = 0;
    char *buffer = calloc(size, sizeof(char));
    if (buffer == NULL) {
        perror("malloc");
        return NULL;
    }

    while ((c = fgetc(file)) != EOF && c != '\n') {
        if (len == size) {
            size *= 2;
            char *tmp = realloc(buffer, size);
            if (!tmp) {
                perror("malloc");
                free(buffer);
                return NULL;
            }
            buffer = tmp;
        }
        buffer[len] = c;
        len++;
    }

    buffer[len] = '\0';

    return buffer;
}

int hash_str(char *tok) {
  char *ptr = tok;
  int total = 0;
  while ((*ptr)) {
    total += *ptr;
    total *= 17;
    total = total % 256;
    ptr++;
  }
  return total;
}


int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "invalid parameters\n");
      return EXIT_FAILURE;
  } 
  FILE *file = fopen(argv[1], "r");
  if (!file) {
     perror("fopen");
    return EXIT_FAILURE;
  }

  char *line = readline(file);
  if (!line) {
    return EXIT_FAILURE;
  }

  char *tok = strtok(line, ",");
  int total = 0;
  while ((tok)) {
    total += hash_str(tok);
    tok = strtok(NULL, ",");
  }

  
  fclose(file);
  printf("result value: %d\n", total);

  return EXIT_SUCCESS;
}
