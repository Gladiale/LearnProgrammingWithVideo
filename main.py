import flet as ft
import keyboard
import json
import time

# 設定ファイルを開く
with open("config.json", "r") as json_open:
    json_load = json.load(json_open)
hot_key = json_load['hot_key']

# 目標サイト
target_site = {
    "youtube": "k",
    "udemy": "enter"
}
play_key = ""

# print(pyautogui.KEYBOARD_KEYS)
def click_target():
    if (play_key):
        # keyboardライブラリを使用してキーをシミュレーション
        keyboard.press('alt')
        keyboard.press_and_release('tab')
        keyboard.release('alt')
        time.sleep(0.5)
        keyboard.press_and_release(play_key)
        keyboard.press('alt')
        keyboard.press_and_release('tab')
        keyboard.release('alt')
    else:
        pass

def main(page: ft.Page):
    page.title = "HelperCodingLearning"
    page.window.width = 320
    page.window.height = 180
    page.padding = 10
    page.spacing = 0
    page.window.resizable = False  # ウインドウサイズ変更可否
    page.window.center()  # ウィンドウをデスクトップの中心に移動
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # 水平方向の中央寄せ
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 縦方向中央寄せ
    page.window.maximizable= False
    # page.window.title_bar_hidden=True

    def radiogroup_changed(e):
        global play_key
        play_key = e.control.value
    
    radio = ft.RadioGroup(
        ft.Row(
            [
            ft.Radio(value=target_site["youtube"] ,label="Youtube", splash_radius=10, fill_color=ft.colors.PURPLE_ACCENT_400),
            ft.Radio(value=target_site["udemy"], label="Udemy", splash_radius=10, fill_color=ft.colors.PURPLE_ACCENT_400),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_change=radiogroup_changed
    )

    content = ft.Column(
        [   
            ft.Text(f"ホットキー: {hot_key}"),
            ft.Divider(height=1, color=ft.colors.PURPLE_400),
            radio
        ],
        expand=1,
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(content)

    # suppress=True を設置することで、パソコンデフォルトのHotkeyの抑制可能
    # trigger_on_releaseこのオプションをTrueに設定すると、ホットキーの動作はキーが離されたときに実行されます(Hotkey抑制できない問題を完全に解決できる)
    keyboard.add_hotkey(hot_key, click_target, args=[], suppress=True, trigger_on_release=True)

ft.app(target=main)