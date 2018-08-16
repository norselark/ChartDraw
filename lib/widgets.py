"""A selection of widgets for use in the GUI"""
from functools import partial
from typing import Mapping, Optional, Callable

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview

from lib.utils import harmonics, truncate_rounding


def handler(spinbox, event):
    if event.keysym == 'Return':
        spinbox.apply_command()
    if event.keysym in ['Up', 'Down']:
        spinbox.spinbox_command()
    if event.keysym in ['a', 't', 'h']:
        return "break"


class TreeviewPanel(tk.Frame):
    def __init__(self, parent: tk.BaseWidget, data: Mapping, *args) -> None:
        super().__init__(parent, *args)
        self.display = 'trunc'
        self.harmonic = tk.StringVar(self)
        harmonic_label = tk.Label(self, textvariable=self.harmonic)
        harmonic_label.pack(side=tk.TOP)
        self.tv = Treeview(self, columns=('glyph', 'angle', 'trunc'),
                           show=[],
                           height=13, displaycolumn=['glyph', self.display])

        self.tv.column('glyph', anchor='center',
                       minwidth=40, width=40, stretch=False)
        self.tv.column('angle', anchor='center',
                       minwidth=120, width=120, stretch=False)
        self.tv.column('trunc', anchor='center',
                       minwidth=120, width=120, stretch=False)

        self.tv.pack(side=tk.TOP)

        self.button_panel = tk.Frame(self)
        self.button_panel.pack(side=tk.TOP)

        self.up = tk.Button(self.button_panel,
                            text=u'\u25b2', command=self.scroll_up)
        self.up.pack(side=tk.LEFT)
        self.toggle = tk.Button(self.button_panel,
                                text='Toggle', command=self.toggle_column)
        self.toggle.pack(side=tk.LEFT)
        self.down = tk.Button(self.button_panel,
                              text=u'\u25bc', command=self.scroll_down)
        self.down.pack(side=tk.LEFT)

        self.harm_panel = tk.Frame(self)
        self.harm_panel.pack(side=tk.TOP)

        self.harm_text = tk.Label(self.harm_panel, text='Harmonic:')
        self.harm_text.pack(side=tk.LEFT)
        self.harm = tk.Spinbox(self.harm_panel, from_=1, to=300, width=5)
        self.harm.pack(side=tk.LEFT, padx=5)
        self.harm.bind('<Key>', partial(handler, self))

        self.data = data
        self.fill_data(harmonic=1)

    def fill_data(self, harmonic: int) -> None:
        self.harmonic.set('Current harmonic: %d' % harmonic)
        for item in self.tv.get_children():
            self.tv.delete(item)
        harm_angles = harmonics(self.data['base_angles'], harmonic)
        trunc_angles = map(str, map(truncate_rounding, harm_angles))
        rounded_angles = map(lambda x: '%.2f°' % x, harm_angles)
        for row in zip(self.data['glyphs'], rounded_angles, trunc_angles):
            self.tv.insert('', tk.END, values=row)

    def spinbox_command(self):
        pass

    def toggle_column(self):
        if self.display == 'angle':
            self.display = 'trunc'
        else:
            self.display = 'angle'
        self.tv.configure(displaycolumn=['glyph', self.display])

    def scroll_down(self):
        last_item = self.tv.get_children()[-1]
        self.tv.move(last_item, '', 0)

    def scroll_up(self):
        first_item = self.tv.get_children()[0]
        self.tv.move(first_item, '', tk.END)

    def apply_command(self):
        val = self.harm.get()
        try:
            val = int(val)
            if val >= 1:
                self.fill_data(harmonic=val)
        except Exception:
            messagebox.showwarning(
                'Harmonic', 'The harmonic number must be a positive integer')


class HarmonicSelection(tk.Frame):
    def __init__(self, parent: tk.BaseWidget,
                 apply_command: Callable, *args) -> None:
        super().__init__(parent, *args)
        self.apply_command = apply_command
        tk.Label(self, text='Harmonic:').pack()

        box_frame = tk.Frame(self)
        box_frame.pack()
        self.spinbox = tk.Spinbox(box_frame, from_=1, to=300, width=5)
        self.spinbox.pack(side='left', padx=5)
        self.spinbox.bind('<Key>', partial(handler, self))

        self.ok_button = tk.Button(
            box_frame, text='Apply', command=apply_command)
        self.ok_button.pack(side='left')

    def set_spinbox_command(self, command: Callable):
        self.spinbox.configure(command=command)
        self.spinbox_command = command

    def get(self):
        if self.validate():
            return int(self.spinbox.get())
        else:
            return None

    def handler(self, event):
        if event.keysym == 'Return':
            self.apply_command()
        if event.keysym in ['Up', 'Down']:
            self.spinbox_command()
        if event.keysym in ['a', 't', 'h']:
            return "break"

    def reset(self):
        self.spinbox.delete(0, 'end')
        self.spinbox.insert(0, '1')

    def validate(self):
        val = self.spinbox.get()
        try:
            val = int(val)
            if val >= 1:
                return True
        except Exception:
            pass
        messagebox.showwarning(
            'Harmonic', 'The harmonic number must be a positive integer')
        return False


class CycleSelection(tk.Frame):
    def __init__(self, parent: tk.BaseWidget,
                 apply_command: Callable, *args) -> None:
        super().__init__(parent, *args)
        self.apply_command = apply_command

        tk.Label(self, text='Turned axis:').pack()

        box_frame = tk.Frame(self)
        box_frame.pack()
        self.spinbox = tk.Spinbox(box_frame, from_=1, to=12, width=5)
        self.spinbox.pack(side='left', padx=5)

        self.ok_button = tk.Button(
            box_frame, text='Apply', command=apply_command)
        self.ok_button.pack(side='left')

        self.spinbox.bind('<Key>', partial(handler, self))

    def set_spinbox_command(self, command: Callable):
        self.spinbox.configure(command=command)
        self.spinbox_command = command

    def get(self) -> Optional[int]:
        if self.validate():
            return int(self.spinbox.get())
        else:
            return None

    def reset(self):
        self.spinbox.delete(0, 'end')
        self.spinbox.insert(0, '1')

    def validate(self):
        val = self.spinbox.get()
        try:
            val = int(val)
            if val >= 1:
                return True
        except Exception:
            pass
        messagebox.showwarning(
            'Cycle', 'The cycle number must be a positive integer')
        return False
