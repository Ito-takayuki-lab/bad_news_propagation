import tempfile
import os
from autogen import ConversableAgent
from utils import llm_config_list



class Agents:
    def __init__(self, rumor):
        self.llm_config = llm_config_list["gpt-4o-mini"]
        self.llm_name = "GPT"
        self.rumor = rumor
        kuroda_def="""
            黒田くんのプロフィール
            名前: 黒田 太一
            年齢: 27歳
            職業: 会社員（事務職）
            趣味: 読書（特にジャンルのこだわりはなし）、散歩（週末にすることが多い）
            黒田くんの特徴
            外見: 身長170cm。標準的な体型。黒髪で短髪。服装は無地のシャツやジーンズが中心。
            仕事: 指示された業務を決められた通りに行うことが多い。進捗は平均的。
            日常生活
            平日は定時で仕事をこなし、帰宅後は家で過ごすことが多い。
            特別な趣味や習慣はなく、休日には近所を散歩したり、スーパーで買い物をする程度。
            家庭用の家電や日用品は標準的なものを使用している。"""

        self.agent_A = ConversableAgent(
            "agent_A",
            system_message=kuroda_def + "黒田くんは" + self.rumor + "をしているという情報があります。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        
        self.agent_B = ConversableAgent(
            "agent_B",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_C = ConversableAgent(
            "agent_C",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_D = ConversableAgent(
            "agent_D",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_E = ConversableAgent(
            "agent_E",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_F = ConversableAgent(
            "agent_F",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_G = ConversableAgent(
            "agent_G",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_H = ConversableAgent(
            "agent_H",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.agent_I = ConversableAgent(
            "agent_I",
            system_message=kuroda_def + "あなたは黒田くんの知り合いです。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.tester = ConversableAgent(
            "tester",
            system_message= "あなたはテスターです。「はい」か「いいえ」でのみお答えください。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )