import flet as ft
import pyautogui
import keyboard
import json

json_open = open("config.json", "r")
json_load = json.load(json_open)

videoData = json_load["video_coordinates"]
keyData = json_load['hot_key']

def click_target():
    # 現在の座標を取得
    mouseX, mouseY = pyautogui.position()
    pyautogui.click(videoData["x"], videoData["y"])
    pyautogui.click(mouseX, mouseY)

def main(page: ft.Page):
    page.title = "LeaningProgram"
    page.window.width = 320
    page.window.height = 240
    page.padding = 10
    page.spacing = 0
    page.window.resizable = False  # ウインドウサイズ変更可否
    page.window.center()  # ウィンドウをデスクトップの中心に移動
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # 水平方向の中央寄せ
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 縦方向中央寄せ
    page.window.maximizable= False
    # page.window.title_bar_hidden=True

    # ---------画面サイズ取得---------
    x, y = pyautogui.size()
    screen_size = ft.Text(f"画面サイズ: x {x}px, y {y}px")
    
    video_coordinates = ft.Text(f"動画設定座標: x {videoData['x']}px, y {videoData['y']}px")
    hot_key = ft.Text(f"ホットキー: {keyData}")

    content = ft.Column(
        [   
            screen_size, 
            ft.Divider(height=1, color=ft.colors.PURPLE_400),
            video_coordinates,
            ft.Divider(height=1, color=ft.colors.PURPLE_400),
            hot_key
        ],
        # expand=1,
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(content)

    # suppress=True を設置することで、パソコンデフォルトのHotkeyの抑制可能
    keyboard.add_hotkey(keyData, click_target, args=[], suppress=True)

ft.app(target=main)