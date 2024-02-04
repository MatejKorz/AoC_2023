#include <stdlib.h> 
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

#define MIN_POS 7 //200000000000000
#define MAX_POS 27 //400000000000000

typedef struct {
  long long pos_x;
  long long pos_y;
  long long pos_z;
  long long vel_x;
  long long vel_y;
  long long vel_z;
} Hailstone;

void init_hailstone(Hailstone *stone) {
  stone->pos_x = 0;
  stone->pos_y = 0;
  stone->pos_z = 0;
  stone->vel_x = 0;
  stone->vel_y = 0;
  stone->vel_z = 0;
}

bool paths_cross(Hailstone *h_a, Hailstone *h_b) {
  double tx = (h_b->pos_x - h_a->pos_x) / (h_a->vel_x - h_b->vel_x);
  double ty = (h_b->pos_y - h_a->pos_y) / (h_a->vel_y - h_b->vel_y);
  if (tx != ty) {
    return false;
  }
  long long x_pos = (h_a->pos_x + h_a->vel_x * tx);
  long long y_pos = (h_a->pos_y + h_a->vel_y * ty);

  return MIN_POS <= x_pos && x_pos <= MAX_POS && MIN_POS <= y_pos && y_pos <= MAX_POS;
}

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
  
  size_t size = 512;
  size_t len = 0;
  Hailstone **stone_list = malloc(size*sizeof(Hailstone *));
  if (!stone_list) {
    perror("malloc");
    return EXIT_FAILURE;
  }

  
  char *line = readline(file);
  while (strcmp(line, "") != 0) {
    char *delim = strstr(line, "@");
    *delim = ',';
    char *tok = strtok(line, ",");

    stone_list[len] = malloc(sizeof(Hailstone));
    if (!stone_list[len]) {
      perror("malloc");
      return EXIT_FAILURE;
    }

    for (int i = 0; i < 6; i++) {
      switch (i) {
        case 0: stone_list[len]->pos_x = strtoll(tok, NULL, 10); break;
        case 1: stone_list[len]->pos_y = strtoll(tok, NULL, 10); break;
        case 2: stone_list[len]->pos_z = strtoll(tok, NULL, 10); break;
        case 3: stone_list[len]->vel_x = strtoll(tok, NULL, 10); break;
        case 4: stone_list[len]->vel_y = strtoll(tok, NULL, 10); break;
        case 5: stone_list[len]->vel_z = strtoll(tok, NULL, 10); break;

      }
      tok = strtok(NULL, ",");
    }
    len++;
    line = readline(file);
  }

  int total = 0;
  for (size_t i = 0; i < len; i++) {
    for (size_t j = 0; i < len; j++) {
      if (i == j) {
      continue;
      }
      total += (paths_cross(stone_list[i], stone_list[j])) ? 1 : 0;
    }
  }

  printf("result value: %d\n", total);

  return EXIT_SUCCESS;
}

