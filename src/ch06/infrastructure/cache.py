import datetime

__cache = {}
LIFETIME_IN_HOURS = 1.0


def get_weather(
    city: str,
    state: str | None,
    country: str,
    units: str,
) -> dict | None:
    key = __create_key(city, state, country, units)
    data = __cache.get(key)

    if not data:
        return None

    last = data["time"]
    time_passed = datetime.datetime.now() - last
    hours_passed = time_passed / datetime.timedelta(minutes=60)

    if hours_passed < LIFETIME_IN_HOURS:
        return data["value"]

    del __cache[key]
    return None


def set_weather(
    city: str,
    state: str,
    country: str,
    units: str,
    forecast: dict,
):
    key = __create_key(city, state, country, units)
    data = {"time": datetime.datetime.now(), "value": forecast}
    __cache[key] = data
    __clean_out_of_data()


def __create_key(
    city: str, state: str, country: str, units: str
) -> tuple[str, str, str, str]:
    if not city or not country or not units:
        raise Exception("City, county, and units are required")
    return (
        city.strip().lower(),
        state.strip().lower(),
        country.strip().lower(),
        units.strip().lower(),
    )


def __clean_out_of_data():
    for key, data in __cache.items():
        time_passed = datetime.datetime.now() - data.get("time")
        hours_passed = time_passed / datetime.timedelta(minutes=60)
        if hours_passed > LIFETIME_IN_HOURS:
            del __cache[key]
