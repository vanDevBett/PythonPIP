import matplotlib.pyplot as plt

def generate_barchart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_piechart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,200,300]
    # generate_barchart(labels, values)
    generate_piechart(labels, values)