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

typedef struct {
    char cards[5];
    int bid;
} hand;

enum cards {
    JOKER, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE, CARD_COUNT
};

enum combinations {
    NONE, HIGH, PAIR, TWO_PAIR, THREE_KIND, FULL_HOUSE, FOUR_KIND, FIVE_KIND, COMB_COUNT
};

enum cards chr_to_card(char card) {
    switch (card) {
    case '2': return TWO;
    case '3': return THREE;
    case '4': return FOUR;
    case '5': return FIVE;
    case '6': return SIX;
    case '7': return SEVEN;
    case '8': return EIGHT;
    case '9': return NINE;
    case 'T': return TEN;
    case 'J': return JOKER; // change to jack
    case 'Q': return QUEEN;
    case 'K': return KING;
    case 'A': return ACE;
    default: return -1;
    }
}

enum combinations valueate(int count[CARD_COUNT]) {
    enum combinations comb = NONE;
    int real_cnt = count[0];

    for (int i = CARD_COUNT - 1; i >= 0; i--) {
        if ((count[i] + ((count[i] != 0 && i != 0) ? count[0] : 0)) == 5) {
            return FIVE_KIND;
        }
    }

    for (int i = CARD_COUNT - 1; i >= 0; i--) {
        if ((count[i] + ((count[i] != 0 && i != 0) ? count[0] : 0)) == 4) {
            return FOUR_KIND;
        }
    }

    for (int i = CARD_COUNT - 1; i >= 0; i--) {
        switch (count[i] + ((count[i] != 0 && i != 0) ? real_cnt : 0)) {
            case 3:
                if (comb == PAIR) {
                    return FULL_HOUSE;
                } else {
                    comb = THREE_KIND;
                    real_cnt -= (3 - count[i]);
                }
                break;
            case 2:
                if (comb == THREE_KIND) {
                    return FULL_HOUSE;
                } else if (comb == PAIR) {
                    comb = TWO_PAIR;
                } else {
                    comb = PAIR;
                }
                real_cnt -= (2 - count[i]);
                break;
            case 1:
                if (comb == NONE)
                    comb = HIGH;
                break;
            default:
                break;
        }
    }
    return comb;
}

int cmp_hand(const void *elem1, const void *elem2) {
    const hand *hand1 = (const hand *) elem1;
    const hand *hand2 = (const hand *) elem2;

    int count1[CARD_COUNT] = { 0 };
    int count2[CARD_COUNT] = { 0 };

    for (int i = 0; i < 5; i++) {
        count1[chr_to_card(hand1->cards[i])]++;
        count2[chr_to_card(hand2->cards[i])]++;
    }

    enum combinations comb1 = valueate(count1);
    enum combinations comb2 = valueate(count2);

    if (comb1 > comb2) {
        return 1;
    } else if (comb1 < comb2) {
        return -1;
    }
    for (int i = 0; i < 5; i++) {
        int rv = chr_to_card(hand1->cards[i]) - chr_to_card(hand2->cards[i]);
        if (rv != 0) {
            return rv;
        }
    }

    return 0;
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

    size_t len = 0;
    size_t size = 1024;
    hand *games = malloc(sizeof(hand) * size);
    if (!games) {
        perror("malloc");
        return -1;
    }

    char *buff;
    while ((buff = readline(file)) && strlen(buff) > 0) {
        if (len == size) {
            size *= 2;
            hand *tmp = realloc(games, size * sizeof(hand));
            if (!tmp) {
                perror("realloc");
                free(buff);
                free(games);
                return -1;
            }
            games = tmp;
        }

        strncpy(games[len].cards, buff, 5);
        games[len].bid = strtol(buff + 6, NULL, 10);
        len++;
        free(buff);
    }

    qsort(games, len, sizeof(hand), cmp_hand);

    int rv = 0;
    for (size_t i = 0; i < len; i++) {
        printf("%s -> %d\n", games[i].cards, games[i].bid);
        rv += (i+1) * games[i].bid;
    }

    fclose(file);
    free(games);
    printf("result value: %d\n", rv);

    return EXIT_SUCCESS;
}