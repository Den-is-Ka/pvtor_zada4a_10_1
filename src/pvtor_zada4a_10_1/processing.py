def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    result = []
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(operations: list[dict], descending: bool = True) -> list[dict]:
    sort_operations = sorted(operations, key=lambda item: item["date"], reverse=descending)

    return sort_operations


if __name__ == "__main__":
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = filter_by_state(operations)
    print(result)
    result = filter_by_state(operations, "CANCELED")
    print(result)
    result = sort_by_date(operations)
    print(result)
    result = sort_by_date(operations, False)
    print(result)
