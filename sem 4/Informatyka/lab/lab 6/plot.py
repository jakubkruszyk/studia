import matplotlib.pyplot as plt


def plot_data(data: list[dict], value='t'):
    x = [record['timestamp'] for record in data]
    value = {'t': 'temperature', 'h': 'humidity', 'p': 'pressure'}[value]
    y = [record[value] for record in data]

    plt.plot(x, y)
    plt.show()
