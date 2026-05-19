def find_user(users: list[dict], target_id: int) -> dict | None:
    """Busca un usuario por su id en una lista de usuarios."""
    for i in range(len(users)):
        if users[i]['id'] == target_id:
            return users[i]
    return None

def find_duplicates(items: list) -> list:
    """Devuelve una lista con los elementos duplicados en la lista de entrada."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def search_sorted_list(sorted_list: list, target) -> bool:
    """Determina si un elemento está presente en una lista ordenada."""
    return target in sorted_list

def multiply_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Multiplica dos matrices y devuelve el resultado."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total = total + a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

def transpose(matrix: list[list]) -> list[list]:
    """Calcula la transpuesta de una matriz."""
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

def find_in_matrix(matrix: list[list], target) -> tuple[int, int] | None:
    """Busca un valor dentro de una matriz y devuelve sus coordenadas (fila, columna) o None si no se encuentra."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return None

def sort_users_by_age(users: list[dict]) -> list[dict]:
    """Ordena la lista de usuarios por edad en orden ascendente."""
    users.sort(key=lambda u: u['age'])
    return users

def get_top_n(scores: list[int], n: int) -> list[int]:
    """Devuelve los n puntajes más altos de la lista."""
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:n]

def is_sorted(arr: list) -> bool:
    """Verifica si la lista está ordenada en orden ascendente."""
    return arr == sorted(arr)