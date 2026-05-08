import flet as ft
import datetime as dt

ft.Text

def main_page(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value='Hello, Flet!')
   
    name_input = ft.TextField(label="Введите ваше имя", max_length=40)

    def on_button_click_change_theme_color(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT


    def on_button_click(_):
        print(name_input.value)

        name = name_input.value.strip()
        datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

        if name:
            hello_text.color = None
            hello_text.value = f'{datetime} Привет, {name}!'
            name_input.value = ''
        else:
            hello_text.value = 'Error: введите ваше имя.'
            hello_text.color = ft.Colors.RED

    page.update()

    theme_button = ft.ElevatedButton('Change theme color', ft.Icons.BRIGHTNESS_6, on_click=on_button_click_change_theme_color)
    name_input = ft.TextField(label="Введите ваше имя", on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    #text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    #icon_button = ft.IconButton(icon=ft.Icons.SEND)

    page.add(hello_text, name_input, elevated_button, theme_button)



ft.run(main_page)
#ft.run(main_page, view=ft.AppView.WEB_BROWSER)
