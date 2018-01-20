import tkinter as tk
from tkinter.ttk import Treeview
from aq_functions import truncate_rounding

letters = ['S', 'L', 'H', 'V', 'M', 'J', 'D', 'U', 'N', 'P', 'X', 'C', 'A']
angles = ['292.24327', '242.66082', '271.75037', '293.01350',
          '231.33463', '228.76548', '272.72153', ' 24.61269',
          '342.18475', '289.17087', '135.16396', '306.3983',
          '087.37077']
truncs = list(map(truncate_rounding, angles))


class TreeviewPanel(tk.Frame):
    def __init__(self, *args):
        super().__init__(*args)
        self.display = 'angle'
        self.tv = Treeview(self, columns=('letter', 'angle', 'trunc'),
                           show=[],
                           height=13, displaycolumn=['letter', self.display])
        self.tv.heading('letter', text='Letter')
        self.tv.heading('angle', text='Angle')
        self.tv.heading('trunc', text='Trunc')

        self.tv.column('letter', anchor='center',
                       minwidth=20, width=20, stretch=False)
        self.tv.column('angle', anchor='center',
                       minwidth=120, width=120, stretch=False)
        self.tv.column('trunc', anchor='center',
                       minwidth=120, width=120, stretch=False)

        for l, a, t in zip(letters, angles, truncs):
            self.tv.insert('', tk.END, values=(l, a, t))

        self.tv.pack(side=tk.TOP)

        self.button_panel = tk.Frame(self)
        self.button_panel.pack(side=tk.BOTTOM)

        self.up = tk.Button(self.button_panel,
                            text=u'\u2bc5', command=self.scroll_up)
        self.up.pack(side=tk.LEFT)
        self.toggle = tk.Button(
            self.button_panel, text='Toggle', command=self.toggle_column)
        self.toggle.pack(side=tk.LEFT)
        self.down = tk.Button(
            self.button_panel, text=u'\u2bc6', command=self.scroll_down)
        self.down.pack(side=tk.LEFT)

    def toggle_column(self):
        if self.display == 'angle':
            self.display = 'trunc'
        else:
            self.display = 'angle'
        self.tv.configure(displaycolumn=['letter', self.display])

    def scroll_down(self):
        last_item = self.tv.get_children()[-1]
        self.tv.move(last_item, '', 0)

    def scroll_up(self):
        first_item = self.tv.get_children()[0]
        self.tv.move(first_item, '', tk.END)


if __name__ == '__main__':
    app = TreeviewPanel()
    app.pack()
    app.mainloop()
