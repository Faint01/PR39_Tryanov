from typing import Union
from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker, MDColorPicker

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')


class MainApp(MDApp):

    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)

    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "You Clicked Cancel!"

    def show_time_picker(self):
        from datetime import datetime

        default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()

        time_dialog = MDTimePicker()
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()

    def on_save(self, instance, value, date_range):
         self.root.ids.date_label.text = str(value)

    def on_cancel_date(self, instance, value):
        self.root.ids.date_label.text = "Вы закрыли окно выбора даты!"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel_date)
        date_dialog.open()

if __name__ == '__main__':
    MainApp().run()
