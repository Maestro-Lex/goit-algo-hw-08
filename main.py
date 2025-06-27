import heapq


def get_total_min_connection_cost(cables: list) -> float:
    '''
    Розрахунок мінімальної вартості з'єднання кабелів
    '''
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Обираємо перші 2 мінімальні елементи з купи з їх видаленням з купи для з'єднання
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        connection_cost = first + second # вартість з'єднання
        total_cost += connection_cost
        # замість видалених двох найкоротших кабелів вставляємо в купу їх з'єднання
        heapq.heappush(cables, connection_cost)        
        print(f"Витрати на об'єднання {first} та {second} кабелів становить {connection_cost}")
        print(f"Відредагований набір кабелів: {cables}")
        print("-------------------------")

    print(f"Мінімальні загальні витрати: {total_cost}")
    return total_cost


def merge_k_lists(k: list[list]) -> list:
    '''
    Додаткове завдання
    '''
    heap = []
    result = []

    # Додаємо перші елементи кожного списку у купу (значення, індекс списку, індекс елемента)
    for i, lst in enumerate(k):
        heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        # Якщо в тому ж списку ще є елементи, додаємо наступний
        if element_idx + 1 < len(k[list_idx]):
            next_val = k[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return result


def main():
    cables = [12, 11, 13, 5, 6, 7]
    get_total_min_connection_cost(cables)

    print("-------------------------")
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()