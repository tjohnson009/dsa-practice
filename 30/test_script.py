def label(station: str, celsius: int) -> str:
    return f"{station}: {celsius}°C"

def show(station: str, celsius: int):
    print(label(station, celsius))

# result = show("roof", 12)
# print(result)

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def format_reading(station: str, celsius: float) -> str:
    fahrenheit = to_fahrenheit(celsius)
    return f"{station}: {fahrenheit:.1f}"

# reading = format_reading("yard", 20)
# print(reading)

def format_duration(test_name: str, duration_ms: float) -> str:
    return f"{test_name}: {duration_ms:.1f} ms"

# print(format_duration("smoke", 120))

# duration_ms = None

# if duration_ms is None:
#     print(300)
# else:
#     print(duration_ms)

def classify_runtime(duration_ms: int | None, limit_ms: int = 500) -> str:
    match duration_ms:
        case None:
            return "missing"
        case _ if duration_ms < 0:
            return "invalid"
        case _ if duration_ms >= limit_ms:
            return "slow"
        case _: 
            return "ok"

for value in (None, -1, 0, 499, 500):
    print(value, classify_runtime(value))
