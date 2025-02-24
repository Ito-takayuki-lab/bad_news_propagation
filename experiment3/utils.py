import os
import json
import random


# ファイルからデータを読み込む関数
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return json.load(file)  # JSONファイルを辞書形式で読み込む
            except json.JSONDecodeError:
                return []  # 空のリストを返す（ファイルが空の場合）
    return []  # ファイルが存在しない場合


def append_to_json(file_path, new_entry):
    # 現在のデータをロード
    data = load_json(file_path)
    # 新しいデータを追加
    data.append(new_entry)
    # ファイルに書き戻す
    with open(file_path, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # JSONを整形して保存

def append_count_to_json(file_path, new_entry):
    # 現在のデータをロード
    data = load_json(file_path)
    # 新しいデータを追加
    data.append(new_entry)
    # ファイルに書き戻す
    with open(file_path, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # JSONを整形して保存



llm_config_list = {
    "gpt-4o-mini": {
        "model": "gpt-4o-mini-2024-07-18",
        "api_key": os.environ['OPENAI_API_KEY'],
    },
    "gpt-4o": {
        "model": "gpt-4o-2024-08-06",
        "api_key": os.environ['OPENAI_API_KEY'],
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "api_key": os.environ['GEMINI_API_KEY'],
        "api_type": "google",
    },
    "claude-3-5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "api_key": os.environ['CLAUDE_API_KEY'],
        "api_type": "anthropic",
    }
}


input_file = "json/good_information_new.json"
output_file = "json/good_information_new_shuffle.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)
# nameの部分を抽出してシャッフル
names = [item["name"] for item in data["contents"]]
random.shuffle(names)

# シャッフルされたnameを元データに適用
for i, item in enumerate(data["contents"]):
    item["name"] = names[i]

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)