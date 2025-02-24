import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from utils import llm_config_list



class Agents:
    def __init__(self, rumor):
        # self.llm_config = llm_config_list["gemini-2.0-flash-exp"]
        # self.llm_name = "GEMINI-2.0-flash"
        self.llm_config = llm_config_list["gpt-4o-mini"]
        self.llm_name = "GPT-4O-MINI"
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

        self.starter= ConversableAgent(
            "starter",
            system_message=kuroda_def + "黒田くんは" + self.rumor + "をしているという情報があります。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        
        self.ichirou = ConversableAgent(
            "ichirou",
            system_message=kuroda_def + "あなたはstarterから話を聞き、jirouに話します。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        
        self.jirou = ConversableAgent(
            "jirou",
            system_message=kuroda_def + "あなたはichirouから話を聞き、saburouに話します。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.saburou = ConversableAgent(
            "saburou",
            system_message=kuroda_def + "あなたはjirouから話を聞き、shirouに話します。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.shirou = ConversableAgent(
            "shirou",
            system_message=kuroda_def + "あなたはsaburouから話を聞き、testerに話します。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.tester = ConversableAgent(
            "tester",
            system_message="あなたはテスターです。「はい」か「いいえ」でのみお答えください。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        