class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_min_recursive(root):
    """
    Рекурсивна функція для знаходження вузла з найменшим значенням 
    у двійковому дереві пошуку (ДДП) або AVL-дереві.
    """
    # Базовий випадок: якщо дерево порожнє
    if root is None:
        return None
    
    # Якщо лівого нащадка немає, поточний вузол є найменшим
    if root.left is None:
        return root
    
    # Інакше занурюємося далі в ліве піддерево
    return find_min_recursive(root.left)


# Блок для перевірки працездатності коду
if __name__ == "__main__":
    # Створюємо тестове ДДП дерево:
    #        15
    #       /  \
    #      10   20
    #     /
    #    8
    
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    
    # Виклик функції
    min_node = find_min_recursive(root)
    
    if min_node:
        print(f"Код виконано успішно!")
        print(f"Найменше значення в дереві: {min_node.val}")  # Очікуваний результат: 8
    else:
        print("Дерево порожнє.")