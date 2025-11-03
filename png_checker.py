import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from datetime import datetime

# タイトル横アイコン
data = '''R0lGODlhIAAgAPMAAAAAALSLatSngaeH95+k992C7/2676jx7/7M7f/Y7AAAAAAA
        AAAAAAAAAAAAAAAAACH5BAEAAAAAIf8LWE1QIERhdGFYTVA8P3hwYWNrZXQgYmVn
        aW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pgo8eDp4bXBt
        ZXRhIHhtbG5zOng9J2Fkb2JlOm5zOm1ldGEvJyB4OnhtcHRrPSdJbWFnZTo6RXhp
        ZlRvb2wgMTIuNDAnPgo8cmRmOlJERiB4bWxuczpyZGY9J2h0dHA6Ly93d3cudzMu
        b3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMnPgoKIDxyZGY6RGVzY3JpcHRp
        b24gcmRmOmFib3V0PScnCiAgeG1sbnM6dGlmZj0naHR0cDovL25zLmFkb2JlLmNv
        bS90aWZmLzEuMC8nPgogIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50
        YXRpb24+CiA8L3JkZjpEZXNjcmlwdGlvbj4KPC9yZGY6UkRGPgo8L3g6eG1wbWV0
        YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAK
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        IAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
        ICAgICAgICAgICAgICAgICAgICAgICAgICAKPD94cGFja2V0IGVuZD0ndyc/PgH/
        /v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDP
        zs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmop6alpKOioaCf
        np2cm5qZmJeWlZSTkpGQj46NjIuKiYiHhoWEg4KBgH9+fXx7enl4d3Z1dHNycXBv
        bm1sa2ppaGdmZWRjYmFgX15dXFtaWVhXVlVUU1JRUE9OTUxLSklIR0ZFRENCQUA/
        Pj08Ozo5ODc2NTQzMjEwLy4tLCsqKSgnJiUkIyIhIB8eHRwbGhkYFxYVFBMSERAP
        Dg0MCwoJCAcGBQQDAgEAACwAAAAAIAAgAAAEtxDISam4WNTNa/5YJwJgeY2eKQxD
        iZJZIV8s64qfrK+1yZW6Wa0lIBgzG9OOZisaCchJxkBVZZ7QkGRKrVqd2Si3+7XC
        xuXMYR1Kl9dsTQaBcH/ghxOGXrdj4CB8dH5fgoQuh2UBZ4klAYsZCZJpj48fi1sC
        kpMYlZcTlZUWmpsJnRIBpxSiFamkplqZGi+oKqOztACuILe5qLsfsgKYuZaKvr/H
        yLrAII/Lv80Xz9CgoaHVG9fLEQA7
    '''

def check_image_properties(file_path, expected_width, expected_height, expected_dpi, size_limit_mb):
    try:
        image = Image.open(file_path)
        width, height = image.size
        dpi = image.info.get("dpi", (350, 350))[0]
        resolution_ok = (width, height) == (expected_width, expected_height)
        dpi_ok = round(dpi, 0) == expected_dpi
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        size_ok = file_size_mb <= size_limit_mb

        return resolution_ok, dpi_ok, size_ok, width, height, dpi, file_size_mb

    except Exception as e:
        raise Exception(f"エラー（{os.path.basename(file_path)}）: {e}")

def process_images(file_paths, expected_width, expected_height, expected_dpi, size_limit_mb):
    results = []
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        if not file_path.lower().endswith(".png"):
            results.append({
                "file": filename,
                "error": "【PNGファイルではありません】"
            })
            continue

        try:
            resolution_ok, dpi_ok, size_ok, width, height, dpi, file_size_mb = check_image_properties(
                file_path, expected_width, expected_height, expected_dpi, size_limit_mb
            )
            results.append({
                "file": filename,
                "resolution_ok": resolution_ok,
                "dpi_ok": dpi_ok,
                "size_ok": size_ok,
                "width": width,
                "height": height,
                "dpi": dpi,
                "file_size_mb": file_size_mb
            })
        except Exception as e:
            results.append({
                "file": filename,
                "error": str(e)
            })
    return results

def display_results(results, export_txt, show_ok):
    output_lines = []
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    result_window = tk.Toplevel()
    result_window.title("チェック結果")
    result_window.tk.call('wm', 'iconphoto', result_window._w, tk.PhotoImage(data=data))

    text = tk.Text(result_window, wrap=tk.WORD, width=100, height=30)
    text.pack(padx=10, pady=10)

    for result in results:
        if "error" in result:
            line = f"{result['file']}: エラー - {result['error']}"
            text.insert(tk.END, line + "\n", "error")
            output_lines.append(line)
        else:
            status = []
            if not result["resolution_ok"]:
                status.append("画像サイズが異なります")
            if not result["dpi_ok"]:
                status.append("DPIが一致しません")
            if not result["size_ok"]:
                status.append(f"ファイルサイズが上限を超えています（{result['file_size_mb']:.2f}MB）")

            if not status:
                if not show_ok:
                    continue
                # OK表示（ファイル名 + OK を青色、残りは黒）
                text.insert(tk.END, f"{result['file']}: OK", "ok")
                text.insert(tk.END, f"\n  サイズ: {result['file_size_mb']:.2f}MB | 解像度: {result['width']}×{result['height']} | DPI: {result['dpi']}\n")
                line = f"{result['file']}: OK\n  サイズ: {result['file_size_mb']:.2f}MB | 解像度: {result['width']}×{result['height']} | DPI: {result['dpi']}"
            else:
                # NG表示（エラー文字列 + カンマも赤文字）
                text.insert(tk.END, f"{result['file']}: 【", "error")
                for i, s in enumerate(status):
                    text.insert(tk.END, s, "error")
                    if i < len(status) - 1:
                        text.insert(tk.END, ", ", "error")  # ← カンマも赤
                text.insert(tk.END, f"】", "error")
                text.insert(tk.END, f"\n  サイズ: {result['file_size_mb']:.2f}MB | 解像度: {result['width']}×{result['height']} | DPI: {result['dpi']}\n")
    line = f"{result['file']}: 【{', '.join(status)}】\n  サイズ: {result['file_size_mb']:.2f}MB | 解像度: {result['width']}×{result['height']} | DPI: {result['dpi']}"


    text.tag_config("error", foreground="red")
    text.tag_config("ok", foreground="blue")
    text.config(state=tk.DISABLED)

    # テキストファイル出力
    if export_txt:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            initialfile=f"チェック結果_{timestamp}.txt",
            title="結果ファイルの保存先を選択"
        )
        if save_path:
            try:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(output_lines))
            except Exception as e:
                messagebox.showerror("エラー", f"ファイル保存エラー: {e}")

def select_files():
    files = filedialog.askopenfilenames(
        title="画像ファイルを選択",
        filetypes=[("画像ファイル", "*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.tiff")]
    )
    if files:
        file_list_var.set("; ".join([os.path.basename(f) for f in files]))
        selected_files.clear()
        selected_files.extend(files)

def start_checking():
    if not selected_files:
        messagebox.showerror("エラー", "画像ファイルを選択してください。")
        return

    try:
        expected_width = int(width_var.get())
        expected_height = int(height_var.get())
        expected_dpi = int(dpi_var.get())
        size_limit_mb = float(size_limit_var.get())
    except ValueError:
        messagebox.showerror("エラー", "幅、高さ、DPI、サイズ上限は数値で入力してください。")
        return

    try:
        results = process_images(selected_files, expected_width, expected_height, expected_dpi, size_limit_mb)
        display_results(results, export_txt_var.get(), show_ok_var.get())
    except Exception as e:
        messagebox.showerror("エラー", f"チェック中にエラーが発生しました: {e}")

# GUIセットアップ
app = tk.Tk()
app.title("PNG画像プロパティチェッカー")

app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(data=data))

selected_files = []

# ファイル選択
tk.Label(app, text="選択中のファイル:").grid(row=0, column=0, padx=10, pady=5, sticky="nw")
file_list_var = tk.StringVar()
tk.Entry(app, textvariable=file_list_var, width=60, state="readonly").grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="参照", command=select_files).grid(row=0, column=2, padx=10, pady=5)

# チェック条件
tk.Label(app, text="幅 (px):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
width_var = tk.StringVar(value="2894")
tk.Entry(app, textvariable=width_var, width=10).grid(row=1, column=1, sticky="w", padx=10)

tk.Label(app, text="高さ (px):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
height_var = tk.StringVar(value="4093")
tk.Entry(app, textvariable=height_var, width=10).grid(row=2, column=1, sticky="w", padx=10)

tk.Label(app, text="DPI:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
dpi_var = tk.StringVar(value="350")
tk.Entry(app, textvariable=dpi_var, width=10).grid(row=3, column=1, sticky="w", padx=10)

tk.Label(app, text="ファイルサイズ上限 (MB):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
size_limit_var = tk.StringVar(value="10")
tk.Entry(app, textvariable=size_limit_var, width=10).grid(row=4, column=1, sticky="w", padx=10)

# チェックボックス
export_txt_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="結果をテキストファイルに保存", variable=export_txt_var).grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

show_ok_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="OKのファイルも表示する", variable=show_ok_var).grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# 実行ボタン
tk.Button(app, text="チェック開始", command=start_checking, width=20).grid(row=7, column=0, columnspan=3, pady=20)

app.mainloop()


# 本コメント以下の内容は修正・削除しないでください。
###############
# VLL活動範囲内でのみ、本プログラムおよび本プログラムから作成したアプリケーション(pngChecker.exe)の自由な利用・複製・改変・それら加工物を含む配布を、無償に限り認めます。
# 作成者：ChatGPT, なりはる(2023年度・2024年度VLLイラスト班班長)
# 作成：2025-04-06