import flet as ft
import keyboard
import json
import time

# 設定ファイルを開く
with open("config.json", "r") as json_open:
    json_load = json.load(json_open)
hot_key = json_load['hot_key']
delay = json_load["delay"]
bg_image = json_load["bg_image"]

# 目標サイト
target_site = {
    "youtube": "k",
    "udemy": "enter"
}
play_key = target_site["youtube"]

# print(pyautogui.KEYBOARD_KEYS)
def click_target():
    # keyboardライブラリを使用してキーをシミュレーション
    keyboard.press('alt')
    keyboard.press_and_release('tab')
    keyboard.release('alt')
    time.sleep(delay)
    keyboard.press_and_release(play_key)
    keyboard.press('alt')
    keyboard.press_and_release('tab')
    keyboard.release('alt')

def main(page: ft.Page):
    page.title = "7thHeaven"
    page.window.width = 320
    page.window.height = 210
    page.padding = 0
    page.spacing = 0
    page.window.resizable = False  # ウインドウサイズ変更可否
    page.window.center()  # ウィンドウをデスクトップの中心に移動
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # 水平方向の中央寄せ
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 縦方向中央寄せ
    page.window.maximizable= False
    # page.window.title_bar_hidden=True

    YoutubeRef = ft.Ref[ft.TextButton]()
    UdemyRef = ft.Ref[ft.TextButton]()

    def setTarget(e):
        global play_key
        target = e.control.text
        match (target):
            case "Youtube":
                play_key = target_site["youtube"]
            case "Udemy":
                play_key = target_site["udemy"]
            case _:
                pass
        YoutubeRef.current.icon = (
            "CHECK" if(play_key==target_site["youtube"]) else "CHECK_BOX_OUTLINE_BLANK_SHARP"
        )
        UdemyRef.current.icon = (
            "CHECK" if(play_key==target_site["udemy"]) else "CHECK_BOX_OUTLINE_BLANK_SHARP"
        )
        control_button.update()

    control_button = ft.Row(
        [
            ft.TextButton("Youtube", icon="CHECK" if(play_key==target_site["youtube"]) else "CHECK_BOX_OUTLINE_BLANK_SHARP", on_click=setTarget, ref=YoutubeRef),
            ft.TextButton("Udemy", icon="CHECK" if(play_key==target_site["udemy"]) else "CHECK_BOX_OUTLINE_BLANK_SHARP", on_click=setTarget, ref=UdemyRef),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    content = ft.Column(
        [   
            ft.Text(f"ホットキー: {hot_key}",
                    style=ft.TextStyle(
                                size=20,
                                weight=ft.FontWeight.NORMAL,
                                foreground=ft.Paint(
                                    color=ft.colors.PURPLE_ACCENT_700,
                                    stroke_width=1,
                                    stroke_join=ft.StrokeJoin.ROUND,
                                    style=ft.PaintingStyle.STROKE,
                                ))
                    ),
            ft.Divider(height=1, color=ft.colors.PURPLE_600),
            control_button
        ],
        expand=1,
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(ft.Container(
            image_src=bg_image,
            image_fit=ft.ImageFit.COVER,
            image_opacity=0.9,
            expand=True,
            padding=10,
            content=content
        ))

    # suppress=True を設置することで、パソコンデフォルトのHotkeyの抑制可能
    # trigger_on_releaseこのオプションをTrueに設定すると、ホットキーの動作はキーが離されたときに実行されます(Hotkey抑制できない問題を完全に解決できる)
    keyboard.add_hotkey(hot_key, click_target, args=[], suppress=True, trigger_on_release=True)

ft.app(target=main)