import re

def verify_card_number(card_number: str) -> str:
    normalized = re.sub(r'\D', '', card_number)
    account_number = [int(x) for x in normalized]

    processed = []

    for position, digit in enumerate(reversed(account_number)):
        if position % 2 == 0:
            processed.append(digit)
        elif digit * 2 < 10:
            processed.append(digit * 2)
        else:
            processed.append(digit * 2 - 9)

    print(account_number)
    print(processed)
    print(sum(processed))

    return 'VALID!' if sum(processed) % 10 == 0 else 'INVALID!'

print(verify_card_number('4111-1111-1111-1111'))