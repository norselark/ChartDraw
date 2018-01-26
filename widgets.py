import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import Dialog
from tkinter.ttk import Treeview
from aq_functions import truncate_rounding


class TreeviewPanel(tk.Frame):
    def __init__(self, parent, data, *args):
        super().__init__(parent, *args)
        self.display = 'trunc'
        self.tv = Treeview(self, columns=('letter', 'angle', 'trunc'),
                           show=[],
                           height=13, displaycolumn=['letter', self.display])

        self.tv.column('letter', anchor='center',
                       minwidth=40, width=40, stretch=False)
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
                            text=u'\u25b2', command=self.scroll_up)
        self.up.pack(side=tk.LEFT)
        self.toggle = tk.Button(self.button_panel,
                                text='Toggle', command=self.toggle_column)
        self.toggle.pack(side=tk.LEFT)
        self.down = tk.Button(self.button_panel,
                              text=u'\u25bc', command=self.scroll_down)
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


class HarmonicSelection(Dialog):
    def body(self, parent):
        w = tk.Frame(self)
        w.pack()

        self.su = tk.IntVar()

        self.spinbox = tk.Spinbox(w, from_=1, to=300)
        self.spinbox.pack()
        self.spinbox.focus_set()

        checkbox = tk.Checkbutton(w, text='Superimposed', variable=self.su)
        checkbox.pack()
        return w

    def apply(self):
        self.result = {'harmonic': int(self.spinbox.get()),
                       'superimposed': True if self.su.get() else False}

    def validate(self):
        val = self.spinbox.get()
        try:
            val = int(val)
            if val >= 1:
                return True
        except Exception:
            pass
        messagebox.showwarning('Harmonic', 'The harmonic number must be a positive integer')
        return False


class CycleSelection(Dialog):
    def body(self, parent):
        w = tk.Frame(self)
        w.pack()

        self.spinbox = tk.Spinbox(w, from_=1, to=12)
        self.spinbox.pack()
        self.spinbox.focus_set()

        return w

    def apply(self):
        self.result = int(self.spinbox.get())

    def validate(self):
        val = self.spinbox.get()
        try:
            val = int(val)
            if val >= 1:
                return True
        except Exception:
            pass
        messagebox.showwarning('Cycle', 'The cycle number must be a positive integer')
        return False


if __name__ == '__main__':
    app = TreeviewPanel(None, {})
    app.pack()
    app.mainloop()
