import flet as ft
import datetime as dt

ft.Text

def main_page(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value='Hello, Flet!')
   
    name_input = ft.TextField(label="Введите ваше имя", max_length=40)

    greeting_history = []
    history_text = ft.Text('История приветствий:')
    # 2. Добавляем кнопку избранного и список избранных имен
    favorite_list = []
    history_favorites_text = ft.Text('Избранные имена:')
    # 1. Добавить сохранении истории
    try:
        with open('greeting_history.txt', 'r') as file:
            greeting_history = file.read().splitlines()
            history_text.value = 'История приветствий: \n-' + '\n-'.join(greeting_history)

    except FileNotFoundError:
        greeting_history = []

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

            # Задание 4: сохраняем историю приветствий, оставляем только последние 5
            greeting_history[:] = greeting_history[-5:]

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий: \n-' + '\n-'.join(greeting_history)
            
            # Задание 1: сохраняем историю приветствий в файл
            with open('greeting_history.txt', 'w') as file:
                file.write('\n'.join(greeting_history))

        else:
            hello_text.value = 'Error: введите ваше имя.'
            hello_text.color = ft.Colors.RED

    page.update()

    def clear_history(_):
        greeting_history.clear()
        favorite_list.clear()
        history_text.value = 'История приветствий:'
        history_favorites_text.value = 'Избранные имена:'
        page.update()
        # Задание 1: очищаем файл с историей приветствий
        with open('greeting_history.txt', 'w') as file:
            file.write('')
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def add_to_favorites(_):
        name = name_input.value.strip()
        if name:
            if name not in favorite_list:
                favorite_list.append(name)
                history_favorites_text.value = 'Избранные имена: \n-' + '\n-'.join(favorite_list)
                name_input.value = ''
                hello_text.value = f'{name} добавлено в избранные.'
                page.update()
            


    favorite_button = ft.IconButton(icon=ft.Icons.STAR, on_click=add_to_favorites)

    theme_button = ft.ElevatedButton('Change theme color', ft.Icons.BRIGHTNESS_6, on_click=on_button_click_change_theme_color)
    name_input = ft.TextField(label="Введите ваше имя", on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    #text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    #icon_button = ft.IconButton(icon=ft.Icons.SEND)

    page.add(hello_text, name_input, elevated_button, theme_button, clear_button, favorite_button, history_text, 
             history_favorites_text)



ft.run(main_page)
#ft.run(main_page, view=ft.AppView.WEB_BROWSER)


