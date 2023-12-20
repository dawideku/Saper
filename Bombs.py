class ReplaceFields:
    def __init__(self, dane):
        self.dane = dane

    def get_dane(self):
        return self.dane

    def change_top(self, x, y):
        dane = self.dane
        if dane[x - 1][y - 1] != '*':
            dane[x - 1][y - 1] = str(int(dane[x - 1][y - 1]) + 1)
        if dane[x - 1][y] != '*':
            dane[x - 1][y] = str(int(dane[x - 1][y]) + 1)
        if dane[x - 1][y + 1] != '*':
            dane[x - 1][y + 1] = str(int(dane[x - 1][y + 1]) + 1)
        self.dane = dane

    def change_mid(self, x, y):
        dane = self.dane
        if dane[x][y + 1] != '*':
            dane[x][y + 1] = str(int(dane[x][y + 1]) + 1)
        if dane[x][y - 1] != '*':
            dane[x][y - 1] = str(int(dane[x][y - 1]) + 1)
        self.dane = dane

    def change_bottom(self, x, y):
        dane = self.dane
        if dane[x + 1][y - 1] != '*':
            dane[x + 1][y - 1] = str(int(dane[x + 1][y - 1]) + 1)
        if dane[x + 1][y] != '*':
            dane[x + 1][y] = str(int(dane[x + 1][y]) + 1)
        if dane[x + 1][y + 1] != '*':
            dane[x + 1][y + 1] = str(int(dane[x + 1][y + 1]) + 1)
        self.dane = dane

    def update(self):
        dane = self.dane
        for i in range(0, len(dane)):
            for j in range(0, len(dane[0])):
                if dane[i][j] == '*':
                    if i == 0 and j == 0:
                        if dane[i][j + 1] != '*':
                            dane[i][j + 1] = str(int(dane[i][j + 1]) + 1)
                        if dane[i + 1][j] != '*':
                            dane[i + 1][j] = str(int(dane[i + 1][j]) + 1)
                        if dane[i + 1][j + 1] != '*':
                            dane[i + 1][j + 1] = str(int(dane[i + 1][j + 1]) + 1)
                    elif i == 0 and j == len(dane[0]) - 1:
                        if dane[i][j - 1] != '*':
                            dane[i][j - 1] = str(int(dane[i][j - 1]) + 1)
                        if dane[i + 1][j - 1] != '*':
                            dane[i + 1][j - 1] = str(int(dane[i + 1][j - 1]) + 1)
                        if dane[i + 1][j] != '*':
                            dane[i + 1][j] = str(int(dane[i + 1][j]) + 1)
                    elif i == 0 and j != 0 and j != len(dane[i]) - 1:
                        self.change_mid(i, j)
                        self.change_bottom(i, j)
                    elif i == len(dane) - 1 and j == 0:
                        if dane[i - 1][j] != '*':
                            dane[i - 1][j] = str(int(dane[i - 1][j]) + 1)
                        if dane[i - 1][j + 1] != '*':
                            dane[i - 1][j + 1] = str(int(dane[i - 1][j + 1]) + 1)
                        if dane[i][j + 1] != '*':
                            dane[i][j + 1] = str(int(dane[i][j + 1]) + 1)
                    elif i == len(dane) - 1 and j == len(dane[0]) - 1:
                        if dane[i - 1][j - 1] != '*':
                            dane[i - 1][j - 1] = str(int(dane[i - 1][j - 1]) + 1)
                        if dane[i - 1][j] != '*':
                            dane[i - 1][j] = str(int(dane[i - 1][j]) + 1)
                        if dane[i][j - 1] != '*':
                            dane[i][j - 1] = str(int(dane[i][j - 1]) + 1)
                    elif i == len(dane) - 1 and j != 0 and j != len(dane[i]) - 1:
                        self.change_top(i, j)
                        self.change_mid(i, j)
                    elif i != 0 and i != len(dane) - 1 and j == 0:
                        if dane[i - 1][j] != '*':
                            dane[i - 1][j] = str(int(dane[i - 1][j]) + 1)
                        if dane[i - 1][j + 1] != '*':
                            dane[i - 1][j + 1] = str(int(dane[i - 1][j + 1]) + 1)
                        if dane[i][j + 1] != '*':
                            dane[i][j + 1] = str(int(dane[i][j + 1]) + 1)
                        if dane[i + 1][j] != '*':
                            dane[i + 1][j] = str(int(dane[i + 1][j]) + 1)
                        if dane[i + 1][j + 1] != '*':
                            dane[i + 1][j + 1] = str(int(dane[i + 1][j + 1]) + 1)
                    elif i != 0 and i != len(dane) - 1 and j == len(dane[0]) - 1:
                        if dane[i - 1][j - 1] != '*':
                            dane[i - 1][j - 1] = str(int(dane[i - 1][j - 1]) + 1)
                        if dane[i - 1][j] != '*':
                            dane[i - 1][j] = str(int(dane[i - 1][j]) + 1)
                        if dane[i][j - 1] != '*':
                            dane[i][j - 1] = str(int(dane[i][j - 1]) + 1)
                        if dane[i + 1][j - 1] != '*':
                            dane[i + 1][j - 1] = str(int(dane[i + 1][j - 1]) + 1)
                        if dane[i + 1][j] != '*':
                            dane[i + 1][j] = str(int(dane[i + 1][j]) + 1)
                    else:
                        self.change_top(i, j)
                        self.change_mid(i, j)
                        self.change_bottom(i, j)
        self.dane = dane

    def scan(self, k, l):
        dane = self.dane
        lista_krotek = [(k, l)]
        koncowa_dl = 0
        while len(lista_krotek) != koncowa_dl:
            dl = len(lista_krotek)
            for el in lista_krotek:
                k = el[0]
                l = el[1]
                if k == 0 and l == 0:
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                    if dane[k + 1][l + 1] == '0':
                        if (k + 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l + 1))
                elif k == 0 and l == len(dane[0]) - 1:
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                    if dane[k + 1][l - 1] == '0':
                        if (k + 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l - 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                elif k == 0 and l != 0 and l != len(dane[k]) - 1:
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                    if dane[k + 1][l - 1] == '0':
                        if (k + 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l - 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                    if dane[k + 1][l + 1] == '0':
                        if (k + 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l + 1))
                elif k == len(dane) - 1 and l == 0:
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k - 1][l + 1] == '0':
                        if (k - 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l + 1))
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                elif k == len(dane) - 1 and l == len(dane[0]) - 1:
                    if dane[k - 1][l - 1] == '0':
                        if (k - 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l - 1))
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                elif k == len(dane) - 1 and l != 0 and l != len(dane[k]) - 1:
                    if dane[k - 1][l - 1] == '0':
                        if (k - 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l - 1))
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k - 1][l + 1] == '0':
                        if (k - 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l + 1))
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                elif k != 0 and k != len(dane) - 1 and l == 0:
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k - 1][l + 1] == '0':
                        if (k - 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l + 1))
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                    if dane[k + 1][l + 1] == '0':
                        if (k + 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l + 1))
                elif k != 0 and k != len(dane) - 1 and l == len(dane[0]) - 1:
                    if dane[k - 1][l - 1] == '0':
                        if (k - 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l - 1))
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                    if dane[k + 1][l - 1] == '0':
                        if (k + 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l - 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                else:
                    if dane[k - 1][l - 1] == '0':
                        if (k - 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l - 1))
                    if dane[k - 1][l] == '0':
                        if (k - 1, l) not in lista_krotek:
                            lista_krotek.append((k - 1, l))
                    if dane[k - 1][l + 1] == '0':
                        if (k - 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k - 1, l + 1))
                    if dane[k][l + 1] == '0':
                        if (k, l + 1) not in lista_krotek:
                            lista_krotek.append((k, l + 1))
                    if dane[k][l - 1] == '0':
                        if (k, l - 1) not in lista_krotek:
                            lista_krotek.append((k, l - 1))
                    if dane[k + 1][l - 1] == '0':
                        if (k + 1, l - 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l - 1))
                    if dane[k + 1][l] == '0':
                        if (k + 1, l) not in lista_krotek:
                            lista_krotek.append((k + 1, l))
                    if dane[k + 1][l + 1] == '0':
                        if (k + 1, l + 1) not in lista_krotek:
                            lista_krotek.append((k + 1, l + 1))
            koncowa_dl = len(lista_krotek)
            print(dl)
            print(lista_krotek)
            print(koncowa_dl)
            return lista_krotek

    def full_scan(self, scanned_krotki):
        dane = self.dane
        lista_krotek = scanned_krotki
        all_scanned = []
        for el in lista_krotek:
            k = el[0]
            l = el[1]
            if k == 0 and l == 0:
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
                if (k + 1, l + 1) not in all_scanned:
                    all_scanned.append((k + 1, l + 1))
            elif k == 0 and l == len(dane[0]) - 1:
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
                if (k + 1, l - 1) not in all_scanned:
                    all_scanned.append((k + 1, l - 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
            elif k == 0 and l != 0 and l != len(dane[k]) - 1:
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
                if (k + 1, l - 1) not in all_scanned:
                    all_scanned.append((k + 1, l - 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
                if (k + 1, l + 1) not in all_scanned:
                    all_scanned.append((k + 1, l + 1))
            elif k == len(dane) - 1 and l == 0:
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k - 1, l + 1) not in all_scanned:
                    all_scanned.append((k - 1, l + 1))
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
            elif k == len(dane) - 1 and l == len(dane[0]) - 1:
                if (k - 1, l - 1) not in all_scanned:
                    all_scanned.append((k - 1, l - 1))
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
            elif k == len(dane) - 1 and l != 0 and l != len(dane[k]) - 1:
                if (k - 1, l - 1) not in all_scanned:
                    all_scanned.append((k - 1, l - 1))
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k - 1, l + 1) not in all_scanned:
                    all_scanned.append((k - 1, l + 1))
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
            elif k != 0 and k != len(dane) - 1 and l == 0:
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k - 1, l + 1) not in all_scanned:
                    all_scanned.append((k - 1, l + 1))
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
                if (k + 1, l + 1) not in all_scanned:
                    all_scanned.append((k + 1, l + 1))
            elif k != 0 and k != len(dane) - 1 and l == len(dane[0]) - 1:
                if (k - 1, l - 1) not in all_scanned:
                    all_scanned.append((k - 1, l - 1))
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
                if (k + 1, l - 1) not in all_scanned:
                    all_scanned.append((k + 1, l - 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
            else:
                if (k - 1, l - 1) not in all_scanned:
                    all_scanned.append((k - 1, l - 1))
                if (k - 1, l) not in all_scanned:
                    all_scanned.append((k - 1, l))
                if (k - 1, l + 1) not in all_scanned:
                    all_scanned.append((k - 1, l + 1))
                if (k, l + 1) not in all_scanned:
                    all_scanned.append((k, l + 1))
                if (k, l - 1) not in all_scanned:
                    all_scanned.append((k, l - 1))
                if (k + 1, l - 1) not in all_scanned:
                    all_scanned.append((k + 1, l - 1))
                if (k + 1, l) not in all_scanned:
                    all_scanned.append((k + 1, l))
                if (k + 1, l + 1) not in all_scanned:
                    all_scanned.append((k + 1, l + 1))
        return all_scanned