import sys
import pandas as pd

if __name__ == '__main__':
    filename = ''

    if len(sys.argv) > 1:
        filename = (sys.argv[1])
    else:
        filename = 'files/utilisation.txt'

    data = pd.read_csv(filename, sep="|", header=None)
    data.columns = ['Cluster', 'Login', 'Name', 'Account', 'Used', 'Energy']
    print(data.shape)
    print('Active Users')
    print(data.Login.unique())
    print(f'Total usage: {data.Used.sum()}')

    with open('files/output.txt', 'w') as f:
        f.write(f'Shape: {data.shape}\n')
        f.write(f'Active Users: {len(data.Login.unique())}\n')
        f.writelines(f'Total usage: {data.Used.sum()}')
        f.close()


