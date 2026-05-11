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
    
    favorite_list = []
    history_favorites_text = ft.Text('Избранные имена:')
    
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

            
            greeting_history[:] = greeting_history[-5:]

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий: \n-' + '\n-'.join(greeting_history)
            
            
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

    def on_button_click_random_name(_):
        if greeting_history:
            import random
            random_name = random.choice(greeting_history)
            hello_text.color = ft.Colors.GREEN if random_name in greeting_history else None
            hello_text.value = f'Рандомное имя из истории: {random_name}'
            page.update()
            
    def on_button_click_hide_show_history(_):
        if history_text.visible:
            history_text.visible = False
            history_favorites_text.visible = False
        else:
            history_text.visible = True
            history_favorites_text.visible = True
        page.update()


    hide_show_history_button = ft.ElevatedButton('Показать/скрыть историю', on_click=on_button_click_hide_show_history)
    random_name_button = ft.ElevatedButton('Рандомное имя', on_click=on_button_click_random_name)
    favorite_button = ft.IconButton(icon=ft.Icons.STAR, on_click=add_to_favorites)
    theme_button = ft.ElevatedButton('Change theme color', ft.Icons.BRIGHTNESS_6, on_click=on_button_click_change_theme_color)
    name_input = ft.TextField(label="Введите ваше имя", on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    #text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    #icon_button = ft.IconButton(icon=ft.Icons.SEND)

    page.add(hello_text, name_input, elevated_button, theme_button, random_name_button, hide_show_history_button 
             , clear_button, favorite_button, history_text, history_favorites_text)



ft.run(main_page)
#ft.run(main_page, view=ft.AppView.WEB_BROWSER)


