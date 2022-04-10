

def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다. ".format(balance - money))
        return balance - money
    else:
        print("출금이 실패. 잔액은 {0}원 입니다. ".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()


balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
print(balance)


commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원 이고, 잔액은 {balance}입니다.")