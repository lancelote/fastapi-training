import requests


def main() -> None:
    choice = input("[R]eport weather or [s]ee reports? ")
    while choice:
        command = choice.lower().strip()
        if command == "r":
            report_event()
        elif command == "s":
            see_events()
        else:
            print(f"Don't know what to do with {command}")

        choice = input("[R]eport weather or [s]ee reports? ")


def report_event():
    description = input("What is happening now? ")
    city = input("What city? ")
    data = {
        "description": description,
        "location": {
            "city": city,
        },
    }
    url = "http://127.0.0.1:8000/api/reports"
    response = requests.post(url, json=data)
    response.raise_for_status()
    result = response.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    for report in data:
        print(
            f"{report.get('location').get('city')} has "
            f"{report.get('description')}"
        )


if __name__ == "__main__":
    main()
