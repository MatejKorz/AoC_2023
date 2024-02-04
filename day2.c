#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define BUFF_SIZE 1024

#define RED 12
#define GREEN 13
#define BLUE 14

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

int parse_colors(char *line) {
    char *subtok = strtok(line, ",");
    while (subtok) {
        //printf("%s\n", subtok);
        char *substr = strstr(subtok, "red");
        if (substr) {
            int red = 0;
            sscanf(subtok, "%d", &red);
            if (red > RED) {
                return 1;
            }
        }
        substr = strstr(subtok, "green");
        if (substr) {
            int red = 0;
            sscanf(subtok, "%d", &red);
            if (red > GREEN) {
                return 1;
            }
        }
        substr = strstr(subtok, "blue");
        if (substr) {
            int red = 0;
            sscanf(subtok, "%d", &red);
            if (red > BLUE) {
                return 1;
            }
        }
        subtok = strtok(NULL, ",");
    }

    return 0;
}

int min_cubes(char *line) {
    int min_red = 0;
    int min_green = 0;
    int min_blue = 0;
    char *subtok = strtok(line, ",");
    while (subtok) {
        //printf("%s\n", subtok);
        char *substr = strstr(subtok, "red");
        if (substr) {
            int red = -1;
            sscanf(subtok, "%d", &red);
            if (red != -1) {
                min_red = (min_red == 0 || red > min_red) ? red : min_red;
            }
        }
        substr = strstr(subtok, "green");
        if (substr) {
            int red = -1;
            sscanf(subtok, "%d", &red);
            if (red != -1)
                min_green = (min_green == 0 || red > min_green) ? red : min_green;
        }
        substr = strstr(subtok, "blue");
        if (substr) {
            int red = -1;
            sscanf(subtok, "%d", &red);
            if (red != -1)
                min_blue = (min_blue == 0 || red > min_blue) ? red : min_blue;
        }
        subtok = strtok(NULL, ",");
    }

    return min_red * min_blue * min_green;
}

int game_cubes(FILE *file) {
    int result = 0;
    char *line;
    while ((line = readline(file))) {
        int len = strlen(line);
        if (len == 0) {
            break;
        }
        int id = 0;
        char collor_buff[1024] = { 0 };

        sscanf(line, "Game %d: %[^\n]", &id, collor_buff);

        char *ptr = collor_buff;
        while (*ptr != '\000') {
            if (*ptr == ';') {
                *ptr = ',';
            }
            ptr++;
        }
        //printf("%s\n", collor_buff);
        int pos = 0;
        pos = min_cubes(collor_buff);

        result += pos;

        free(line);
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
