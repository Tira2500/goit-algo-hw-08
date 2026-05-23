import heapq

def min_cost_to_connect_cables(cables):
    """
    Знаходить мінімальні витрати на з'єднання кабелів за допомогою купи.
    """
    if not cables:
        return 0
    if len(cables) == 1:
        return 0
    
    # Створюємо мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Виконуємо з'єднання
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
        
    return total_cost

if __name__ == "__main__":
    # Приклад для тестування
    test_cables = [8, 4, 6, 12]
    print(f"Мінімальні витрати: {min_cost_to_connect_cables(test_cables)}")