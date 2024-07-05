import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os


# FileTreeApp クラス: アプリケーションのメインウィンドウを表す
# FileTreeApp class: Represents the main window of the application
class FileTreeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Directory Structure Generator")
        self.geometry("800x600")

        self.create_widgets()
        self.current_path = os.getcwd()
        self.update_tree_view()

    # ウィジェットの作成
    # Create widgets
    def create_widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        self.create_tree_view()
        self.create_input_area()
        self.create_buttons()
        self.create_path_entry()

    # ツリービューの作成
    # Create tree view
    def create_tree_view(self):
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree.heading('#0', text='File Structure', anchor=tk.W)

    # 入力エリアの作成
    # Create input area
    def create_input_area(self):
        self.input_label = ttk.Label(self.input_frame, text="Enter directory structure:")
        self.input_label.pack(fill=tk.X)

        self.input_text = tk.Text(self.input_frame, height=20)
        self.input_text.pack(fill=tk.BOTH, expand=True)

    # ボタンの作成
    # Create buttons
    def create_buttons(self):
        self.generate_button = ttk.Button(self.input_frame, text="Generate", command=self.generate_structure)
        self.generate_button.pack(fill=tk.X, pady=5)

        self.refresh_button = ttk.Button(self.input_frame, text="Refresh", command=self.refresh_tree)
        self.refresh_button.pack(fill=tk.X, pady=5)

    # パス入力欄の作成
    # Create path entry
    def create_path_entry(self):
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(self.main_frame, textvariable=self.path_var, state='readonly')
        self.path_entry.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))

    # ツリービューの更新
    # Update tree view
    def update_tree_view(self):
        self.tree.delete(*self.tree.get_children())
        self.path_var.set(self.current_path)
        self.populate_tree('', self.current_path)

    # ツリービューにディレクトリ構造を表示
    # Populate tree view with directory structure
    def populate_tree(self, parent, path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            item_id = self.tree.insert(parent, 'end', text=item, open=False)
            if os.path.isdir(item_path):
                self.tree.insert(item_id, 'end')

    # ディレクトリ構造の生成
    # Generate directory structure
    def generate_structure(self):
        structure = self.input_text.get("1.0", tk.END).strip()
        if not structure:
            messagebox.showerror("エラー", "ディレクトリ構造を入力してください。")
            return

        selected_item = self.tree.selection()
        base_path = self.current_path if not selected_item else os.path.join(self.current_path,
                                                                             self.tree.item(selected_item[0], 'text'))

        try:
            self.create_directory_structure(structure, base_path)
            messagebox.showinfo("成功", f"{base_path} にディレクトリ構造を作成しました。")
            self.refresh_tree()
        except Exception as e:
            messagebox.showerror("エラー", f"ディレクトリ構造の作成中にエラーが発生しました: {str(e)}")

    # 指定された構造に基づいてディレクトリとファイルを作成
    # Create directories and files based on the specified structure
    def create_directory_structure(self, structure, base_path='.'):
        lines = structure.strip().split('\n')
        current_path = base_path
        path_stack = []

        for line in lines:
            indent = len(line) - len(line.lstrip())
            name = line.strip()

            while len(path_stack) > indent // 4:  # インデントを4スペースとして扱う
                current_path = path_stack.pop()

            full_path = os.path.join(current_path, name)

            if name.endswith('/'):
                # ディレクトリの場合
                # If it's a directory
                os.makedirs(full_path, exist_ok=True)
                path_stack.append(current_path)
                current_path = full_path
            else:
                # ファイルの場合
                # If it's a file
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                open(full_path, 'a').close()

    # ツリービューを更新
    # Refresh tree view
    def refresh_tree(self):
        self.update_tree_view()


if __name__ == "__main__":
    app = FileTreeApp()
    app.mainloop()
