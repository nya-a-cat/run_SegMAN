from confusion_matrix import plot_confusion_matrix
import numpy as np

if __name__ == '__main__':
    cm = np.array([[9,1],[2,8]])
    plot_confusion_matrix(cm, ['class0','class1'], save_dir='.', show=False)
    print('Saved confusion_matrix.png')
