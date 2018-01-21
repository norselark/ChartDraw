import tkinter as tk
from tkinter.ttk import Treeview
from aq_functions import truncate_rounding


class TreeviewPanel(tk.Frame):
    def __init__(self, parent, data, *args):
        super().__init__(parent, *args)
        self.display = 'trunc'
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

        for row in zip(data['letters'], data['angles'], data['truncated_angles']):
            self.tv.insert('', tk.END, values=row)

        self.tv.pack(side=tk.TOP)

        self.button_panel = tk.Frame(self)
        self.button_panel.pack(side=tk.BOTTOM)

        self.up = tk.Button(self.button_panel,
                            text=u'\u2bc5', command=self.scroll_up)
        self.up.pack(side=tk.LEFT)
        self.toggle = tk.Button(self.button_panel,
                                text='Toggle', command=self.toggle_column)
        self.toggle.pack(side=tk.LEFT)
        self.down = tk.Button(self.button_panel,
                              text=u'\u2bc6', command=self.scroll_down)
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


class ChartSelection(tk.Toplevel):
    def __init__(self, parent, *args):
        super().__init__(parent, *args)
        self.transient(parent)
        self.parent = parent
        self.result = None
        self.val = tk.IntVar()

        body = tk.Frame(self)
        body.pack()

        tk.Radiobutton(body, text='1', variable=self.val, value=1).pack()
        tk.Radiobutton(body, text='2', variable=self.val, value=2).pack()
        tk.Radiobutton(body, text='3', variable=self.val, value=3).pack()

        tk.Button(body, text='Ok', command=self.apply).pack()

        self.wait_window(self)

    def apply(self):
        self.result = self.val.get()
        self.parent.focus_set()
        self.destroy()


if __name__ == '__main__':
    app = TreeviewPanel()
    app.pack()
    app.mainloop()
