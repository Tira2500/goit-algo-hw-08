class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key  # в конспектах використовується self.val або self.key


def calculate_tree_sum(root):
    """
    Рекурсивна функція, яка обходить усе дерево 
    та обчислює суму всіх його значень.
    """
    # Базовий випадок: якщо вузол порожній (None), його внесок у суму дорівнює 0
    if root is None:
        return 0
    
    # Рекурсивно додаємо значення поточного вузла, лівого та правого піддерев
    return root.val + calculate_tree_sum(root.left) + calculate_tree_sum(root.right)


# Блок для перевірки виконання коду
if __name__ == "__main__":
    # Створюємо тестове дерево пошуку:
    #        15
    #       /  \
    #      10   20
    #     /
    #    8
    #
    # Очікувана сума: 15 + 10 + 20 + 8 = 53
    
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    
    # Обчислення суми
    total_sum = calculate_tree_sum(root)
    
    print("Код виконано успішно!")
    print(f"Сума всіх значень у дереві: {total_sum}")  # Виведе: 53