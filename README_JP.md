# Directory Structure Generator: 包括的ガイド

## 目次
1. [はじめに](#はじめに)
2. [機能概要](#機能概要)
3. [インストールと設定](#インストールと設定)
4. [使用方法](#使用方法)
5. [コードの詳細解説](#コードの詳細解説)
6. [エラーハンドリング](#エラーハンドリング)
7. [トラブルシューティング](#トラブルシューティング)
## はじめに

Directory Structure Generatorは、Pythonで書かれたGUIアプリケーションで、ユーザーが指定したディレクトリ構造を視覚化し、実際のファイルシステム上に生成することができます。このツールは、プロジェクト構造の計画や、生成AIが提案したディレクトリ構造の迅速な実装に特に有用です。

## 機能概要

1. **ファイルシステムのツリービュー表示**: 現在のディレクトリ構造をグラフィカルに表示
2. **ディレクトリ構造の入力**: テキストエリアでカスタム構造を定義
3. **構造の生成**: 指定された構造に基づいてディレクトリとファイルを作成
4. **リアルタイム更新**: 生成後のファイルシステムの変更をリアルタイムで反映

## インストールと設定

### 必要条件
- Python 3.6以上
- tkinter（多くの場合、Pythonに標準で含まれています）

### 仮想環境の設定

```bash
# プロジェクトディレクトリの作成
mkdir directory_structure_generator
cd directory_structure_generator

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Unix系の場合
venv\Scripts\activate  # Windowsの場合

# 必要なパッケージのインストール（tkinterが別途必要な場合）
pip install tk
```

### アプリケーションのインストール

```bash
# リポジトリをクローン（実際のリポジトリURLに置き換えてください）
git clone https://github.com/yourusername/directory-structure-generator.git

# プロジェクトディレクトリに移動
cd directory-structure-generator

# 依存関係のインストール（requirements.txtがある場合）
pip install -r requirements.txt
```

## 使用方法

1. アプリケーションの起動:
   ```bash
   python directory_generator.py
   ```

2. GUIウィンドウが開きます。左側にファイルシステムのツリービュー、右側にディレクトリ構造入力エリアが表示されます。

3. ディレクトリ構造の入力:
   ```
   project/
       src/
           main.py
       tests/
           test_main.py
       docs/
           README.md
   ```

4. "Generate" ボタンをクリックして構造を生成します。

5. "Refresh" ボタンで、ツリービューを更新して新しい構造を確認できます。

## コードの詳細解説

### クラス: FileTreeApp

#### __init__(self)
- アプリケーションウィンドウの初期化
- ウィジェットの作成と初期ディレクトリの設定

#### create_widgets(self)
- メインフレーム、ツリーフレーム、入力フレームの作成
- 各ウィジェット（ツリービュー、入力エリア、ボタン、パス入力欄）の配置

#### create_tree_view(self)
- ファイルシステムを表示するツリービューの作成
- スクロールバーの追加

#### create_input_area(self)
- ディレクトリ構造入力用のテキストエリアの作成

#### generate_structure(self)
- 入力されたディレクトリ構造の検証
- `create_directory_structure` メソッドの呼び出し
- 成功・エラーメッセージの表示

#### create_directory_structure(self, structure, base_path='.')
- 指定された構造に基づいてディレクトリとファイルを再帰的に作成
- インデントを利用して階層構造を解析

## エラーハンドリング

1. **無効な入力**: 空の入力や不正な文字が含まれる場合、エラーメッセージを表示
2. **権限エラー**: ディレクトリ作成時に権限がない場合、具体的なエラーメッセージを表示
3. **既存のファイル/ディレクトリ**: 同名のものが存在する場合、警告メッセージを表示（オプション）

## トラブルシューティング

1. **GUIが表示されない**
   - Tkinterが正しくインストールされているか確認
   - 仮想環境を使用している場合、有効化されているか確認

2. **ディレクトリ生成に失敗する**
   - 書き込み権限があるか確認
   - パスの長さがOSの制限を超えていないか確認

3. **ツリービューが更新されない**
   - "Refresh" ボタンをクリック
   - アプリケーションを再起動



