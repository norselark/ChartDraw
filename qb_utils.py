import numpy as np

class TextBuffer:
    def __init__(self):
        self.buffer = np.repeat(' ', 60 * 80).reshape((60, 80))
        self.row = 0
        self.col = 0
    
    def print(self, text):
        l = len(text)
        self.buffer[self.row, self.col:self.col + l] = list(text)
        self.row += 1
    
    def locate(self, row, col):
        self.row = row - 1
        self.col = col - 1
    
    def display(self):
        with open('bufferdisplay.txt', 'w') as outfile:
            for row in range(self.buffer.shape[0]):
                outfile.write(''.join(self.buffer[row, :]) + '\n')
        print('Written to bufferdisplay.txt')
    
    def cls(self):
        self.buffer = np.repeat(' ', 60 * 80).reshape((60, 80))
