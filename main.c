#include <stdio.h>
#include <stdlib.h>
#define MAX_TIME 100000

void light(char **pole, int *T, int N, int D, int reverse) {
    int time = 0;
    for (int i = 0; i < N; i++) {
        int idx = reverse ? N - 1 - i : i;
        for (int d = -D; d <= D; d++) {
            int pos = idx + d;
            if (pos >= 0 && pos < N)
                for (int dt = 0; dt < T[idx]; dt++)
                    pole[pos][time + dt] = 1;
        }
        time += T[idx];
    }
}

int main() {
    int N, D1, D2;
    scanf("%d %d %d", &N, &D1, &D2);

    int *T1 = malloc(N * sizeof(int)), *T2 = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) scanf("%d", &T1[i]);
    for (int i = 0; i < N; i++) scanf("%d", &T2[i]);

    char **s1 = malloc(N * sizeof(char *)), **s2 = malloc(N * sizeof(char *));
    for (int i = 0; i < N; i++) {
        s1[i] = calloc(MAX_TIME, 1);
        s2[i] = calloc(MAX_TIME, 1);
    }

    light(s1, T1, N, D1, 0);
    light(s2, T2, N, D2, 1);

    int k_min = -1, k_max = -1;
    for (int i = 0; i < N; i++) {
        int o1 = 0, o2 = 0;
        for (int t = 0; t < MAX_TIME; t++) {
            if (s1[i][t] && s2[i][t]) o2++;
            else if (s1[i][t] || s2[i][t]) o1++;
        }
        int kvalita = 2 * o1 + 3 * o2;
        if (k_min == -1 || kvalita < k_min) k_min = kvalita;
        if (k_max == -1 || kvalita > k_max) k_max = kvalita;
    }

    printf("%d %d\n", k_min, k_max);

    for (int i = 0; i < N; i++) free(s1[i]), free(s2[i]);
    free(s1); free(s2); free(T1); free(T2);
    return 0;
}
