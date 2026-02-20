import flet as ft
from db import main_db, queries

def main(page: ft.Page):

    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT

    tasks_view = ft.Column()

    def update_list(filter_name="all"):
        tasks_view.controls.clear()
    
        data = queries.get_items(filter_name)

        for item_id, text, status in data:
            tasks_view.controls.append(
                ft.Checkbox(
                    label=text,
                    value=bool(status),
                
                    on_change=lambda e, i=item_id: [main_db.toggle_item(i, e.control.value), update_list(filter_name)]
                )
            )
        page.update()

    def add_clicked(e):
        if input_field.value:
        
            queries.add_item(input_field.value)
            input_field.value = ""
            update_list()


    input_field = ft.TextField(hint_text="Что купить?", expand=True, on_submit=add_clicked)
    add_btn = ft.FilledButton("ADD", icon=ft.Icons.ADD, on_click=add_clicked)


    filters = ft.Row([
        ft.TextButton("Все", on_click=lambda _: update_list("all")),
        ft.TextButton("Не куплено", on_click=lambda _: update_list("unbought")),
        ft.TextButton("Куплено", on_click=lambda _: update_list("bought")),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(ft.Row([input_field, add_btn]), filters, tasks_view)
    update_list()

if __name__ == "__main__":

    main_db.init_db()
    ft.app(target=main)
