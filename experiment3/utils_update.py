import os
import json


# ファイルからデータを読み込む関数
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return json.load(file)  # JSONファイルを辞書形式で読み込む
            except json.JSONDecodeError:
                return []  # 空のリストを返す（ファイルが空の場合）
    return []  # ファイルが存在しない場合



def append_to_json(file_path, new_entry, proposed_prompt):
    # 現在のデータをロード
    data = load_json(file_path)
    if proposed_prompt not in data[-1]:
        data.append({proposed_prompt : []})
        
    # 新しいデータを追加
    data[-1][proposed_prompt].append(new_entry)
    # ファイルに書き戻す
    with open(file_path, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # JSONを整形して保存