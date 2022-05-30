import matplotlib.pyplot as plt


def plot_data(data: list[dict], city: str, date: str):
    y = [t['temp'] for t in data]
    x = [int(t['hour'][:2]) for t in data]

    plt.plot(x, y)
    plt.title(f"{city}  {date}")
    plt.xlabel("Time [hours]")
    plt.ylabel("Temperature [Celsius degrees]")
    plt.xlim(0, 23)
    plt.grid()
    plt.show()
