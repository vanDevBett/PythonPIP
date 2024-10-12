import matplotlib.pyplot as plt

def generate_piechart():
    labels = ['A', 'B', 'C']
    values = [200, 300, 400]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()