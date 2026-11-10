expenses = [
    {"category": "Еда", "amount": 1200},
    {"category": "Такси", "amount": 600},
    {"category": "Развлечения", "amount": 1500},
]


def get_total(expenses):
    return sum(
    expense["amount"]
    for expense in expenses
    )


print("Всего расходов:", get_total(expenses))


def get_max_expense(expenses):
    return max(
        expense["amount"]
        for expense in expenses
        )
