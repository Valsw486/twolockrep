class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
        # Инициализируем пустой словарь для товаров

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товара нет, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")


# Пример использования
if __name__ == "__main__":
    store = Store("Гастроном  №1", "Тверская 12")

    # Добавляем товары
    store.add_item("яблоки", 0.5)
    store.add_item("бананы", 0.75)

    # Получаем цену товара
    print(f"Цена яблок: {store.get_price('яблоки')}")

    # Обновляем цену товара
    store.update_price("яблоки", 0.6)

    # Удаляем товар
    store.remove_item("бананы")

    # Проверяем наличие товара
    print(f"Цена бананов: {store.get_price('бананы')}")


