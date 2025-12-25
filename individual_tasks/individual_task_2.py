#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    transactions = []

    while True:
        command = input(">>> ")

        match command:
            case "add":
                payer_account_number = int(input("Введите расчетный счет плательщика: "))
                recipient_account_number = int(input("Введите расчетный счет получателя: "))
                amount = int(input("Введите перечисляемую сумму в рублях: "))

                new_transaction = {
                    'payer': payer_account_number,
                    'recipient': recipient_account_number,
                    'amount': amount
                }

                transactions.append(new_transaction)

                if len(transactions) > 1:
                    transactions.sort(key=lambda x: x.get('payer', ''))

            case "list":
                print("Список операций:")

                for num, transaction in enumerate(transactions, 1):
                    print(f"Операция #{num}:")
                    print(f"\tРасчетный счет плательщика: {transaction.get('payer', '0')}")
                    print(f"\tРасчетный счет получателя: {transaction.get('recipient', '0')}")
                    print(f"\tПеречисляемая сумма в рублях: {transaction.get('amount', '0')}")

            case command if command.startswith("find"):
                target_payer = int(command.split()[1])

                amount = 0
                for transaction in transactions:
                    if transaction.get('payer', '') == target_payer:
                        amount += transaction.get('amount', 0)

                if amount == 0:
                    print("Операции снятия денег с данного расчетного счета не найдены!", file=sys.stderr)
                else:
                    print(f"С расчетного счёта плательщика №{target_payer} было снято всего {amount} руб.")

            case "exit":
                break

            case _:
                print("Неизвестная команда!", file=sys.stderr)
