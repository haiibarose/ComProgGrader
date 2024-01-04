def total(pocket):
    money = [key*value for key, value in pocket.items()]
    return sum(money)

def take(pocket, money_in):
    for key, value in money_in.items():
        if key in pocket:
            pocket[key] += value
        else:
            pocket[key] = value
    return pocket

def pay(pocket, amt):
    backup = dict(pocket)
    key = sorted(backup.keys())
    ans = dict()
    for value in sorted(key, reverse=True):
        while True:
            if value <= amt and backup[value] >= 1:
                amt -= value
                backup[value] -= 1
                if value in ans:
                    ans[value] += 1
                else:
                    ans[value] = 1
            else:
                break
    if amt != 0:
        return {}
    pocket = (backup)
    return ans

exec(input().strip())