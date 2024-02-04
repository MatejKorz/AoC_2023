#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

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

#define WRD_CNT 9
int find_n_replace(char *line, int dir) { // 0 = front, 1 = back
    const char *word[WRD_CNT] = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    int pos = (dir) ? 0 : strlen(line);
    char *small = NULL;
    int index = -1;
    for (int i = 0; i < WRD_CNT; i++) {
        char *substr = strstr(line, word[i]);
        if (!substr) {
            continue;
        }

        if (dir) {
            char *prev = line;
            while ((substr = strstr(prev + 1, word[i]))) {
                prev = substr;
            }
            substr = prev;
        }


        if ((dir) ? (substr - line >= pos) : (substr - line <= pos)) {
            pos = substr - line;
            index = i;
            small = substr;
        }
    }
    if (index != -1)
        memset(small, '0' + 1 + index, strlen(word[index]));
    return 0;
}

int game_cubes(FILE *file) {
    int result = 0;
    char *line;
    while ((line = readline(file))) {
        int len = strlen(line);
        if (len == 0) {
            break;
        }
        int num = 0;
        find_n_replace(line, 0);
        find_n_replace(line, 1);
        for (int i = 0; i < len; i++) {
            if (line[i] <= '9' && line[i] >= '0') {
                num += ((int) (line[i] - '0')) * 10;
                break;
            }
        }
        for (int i = len - 1; i >= 0; i--) {
            if (line[i] <= '9' && line[i] >= '0') {
                num += ((int) (line[i] - '0'));
                break;
            }
        }
        free(line);
        result += num;
    }

    return result;
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

    int rv = game_cubes(file);
    fclose(file);
    printf("result value: %d\n", rv);

    return EXIT_SUCCESS;
}