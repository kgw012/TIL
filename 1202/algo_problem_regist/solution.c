#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main() {
    int C_COST = 1;
    int Q_COST = 2;

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        char st[100000];
        scanf("%s", st);

        // 천지인 자판 확인
        int OFFSET = 'a';

        char prev = st[0];
        int c_cnt = ((int)prev - OFFSET) % 3 + 1;

        for (int i = 1; i < strlen(st); i++) {
            char c = st[i];
            if( ((int)prev - OFFSET) / 3 == ((int)c - OFFSET) / 3 ) {
                c_cnt++;
            }

            c_cnt += ((int)c - OFFSET) % 3 + 1;
            prev = c;
        }

        int c_cost = c_cnt * C_COST;

        // 쿼티 자판 확인
        int q_cnt = strlen(st);
        int q_cost = q_cnt * Q_COST;

        // 대소 비교 후 정답 출력
        if (c_cost < q_cost) {
            printf("#%d %s", t, "CHEONJIIN\n");
        }
        else if (c_cost > q_cost) {
            printf("#%d %s", t, "QWERTY\n");
        }
        else {
            printf("#%d %s", t, "DRAW\n");
        }
    }

    return 0;
}