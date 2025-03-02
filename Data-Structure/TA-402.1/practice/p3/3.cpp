//1
for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
        for (k = 1; k <= n; k++) {
            x++;
        }
        j = 1;
        while (j <= n) {
            x++;
            j *= 2;
        }
    }
}


//2
for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
        x++;
        for (k = 1; k <= n; k *= 2) {
            for (l = 1; l <= k; l++) {
                x++;
            }
        }
    }
}

//3
for (i = 1; i <= n; i++) {
    for (j = i; j <= n; j++) {
        x++;
    }

    for (k = 1; k <= n; k++) {
        int m = 1;
        while (m < k) {
            x++;
            m *= 3;
        }
    }
}

//4
for (i = 1; i <= n; i++) {
    for (j = 1; j <= i * i; j++) {
        for (k = 1; k <= j; k++) {
            x++;
        }
    }
    int m = 1;
    while (m < n) {
        x++;
        m *= 5;
    }
}

//5
for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
        for (k = 1; k <= n; k++) {
            for (l = 1; l <= n; l++) {
                if (l % 2 == 0) {
                    x++;
                }
            }
        }
    }
}