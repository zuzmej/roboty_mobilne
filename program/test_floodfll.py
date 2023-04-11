class Matrix:
    def __init__(self, values):
        self.values = values

    def znajdz_mniejszy_sasiad(self, col, row):
        # Pobierz wartość danego elementu
        target_value = self.values[col][row]

        # Sprawdź elementy w otoczeniu (góra, dół, prawo, lewo)
        otoczenie = [
            (col, row - 1),  # góra
            (col, row + 1),  # dół
            (col + 1, row),  # prawo
            (col - 1, row)   # lewo
        ]

        for c, r in otoczenie:
            # Sprawdź czy współrzędne są w granicach listy 2D
            if 0 <= r < len(self.values[0]) and 0 <= c < len(self.values):
                # Jeśli wartość sąsiada jest mniejsza o 1 od wartości elementu, zwróć współrzędne tego sąsiada
                if self.values[c][r] == target_value - 1:
                    return [c, r]

        # Jeśli nie znaleziono elementu o 1 mniejszego, zwróć None
        return None
# Przykład użycia klasy Matrix
matrix = Matrix([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [37, 36, 35, 34, 33, 32, 31, 30, 9, 10, 11, 12, 13, 14, 17, 16], [38, 37, 36, 37, 34, 33, 32, 29, 28, 27, 26, 25, 24, 15, 18, 19], [39, 38, 37, 38, 35, 36, 33, 34, 27, 26, 25, 24, 23, 16, 17, 18], [40, 39, 38, 39, 38, 37, 38, 35, 36, 27, 28, 29, 22, 21, 20, 19], [45, 40, 41, 40, 39, 38, 39, 2137, 37, 38, 41, 30, 23, 22, 21, 20], [44, 43, 42, 43, 40, 39, 62, 63, 2137, 39, 40, 31, 32, 33, 34, 35], [45, 46, 43, 44, 45, 46, 61, 2137, 63, 62, 41, 42, 43, 38, 37, 36], [46, 47, 44, 45, 48, 47, 60, 2137, 2137, 61, 60, 43, 44, 39, 40, 43], [47, 48, 47, 46, 49, 50, 59, 60, 61, 62, 59, 58, 45, 46, 41, 42], [48, 49, 48, 49, 52, 51, 58, 59, 2137, 2137, 58, 57, 56, 47, 48, 43], [49, 50, 51, 50, 53, 54, 57, 58, 63, 62, 59, 58, 55, 50, 49, 44], [50, 51, 52, 53, 54, 55, 56, 57, 62, 61, 60, 59, 54, 51, 46, 45], [51, 52, 55, 54, 55, 56, 57, 58, 61, 62, 2137, 2137, 53, 52, 47, 48], [52, 53, 54, 57, 56, 57, 58, 59, 60, 2137, 2137, 2137, 2137, 53, 50, 49], [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 2137, 2137, 52, 51, 52]])

col, row = 8,9 # współrzędne elementu, w otoczeniu którego szukamy
[col,row] = matrix.znajdz_mniejszy_sasiad(col, row)
print(col)
print(row)  # Output: [0, 1] (wartość 4 jest o 1 mniejsza niż wartość 5)

