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
        

        self.proposed_prompt="""
        **役割**
        あなたは人間の情報伝播をシミュレーションするためのエージェントです。必ず人間を模倣してください。
        
        **ルール**
        1. あなたは人間です。
        2. 必ず日本語を話してください。

        **指示**
        フィードバックがない場合は、普通に出力を行ってください。
        <フィードバック>は聞き手の反応です。そのフィードバックをもとに、より聞き手が興味を持つような出力を行ってください。

        """

        self.feed_back_agent_prompt="""
        **役割**
        あなたは受け取った情報に対して、リアクションをしてください。

        もし(ユーザープロンプトに「〜黒田くんについて知っていることを話してください。」という文言が入っている場合):
            空白を出力してください。

        他に(黒田くんに関する情報を他のエージェントからもらった場合):
            1. フィードバックを行う際の出力はフィードバックタブで挟んでください。出力例：<フィードバック> ~~~ <\フィードバック>
            2. 自分が知らなかった情報に対して、強くリアクションしてください。
        """

        self.feed_back_agent= ConversableAgent(
            "feed_back_agent",
            system_message=kuroda_def + self.feed_back_agent_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        nested_chats = [

            {
                "recipient": self.feed_back_agent,
                "max_turns": 2,
                "summary_method": "reflection_with_llm",
                "summary_prompt": "フィードバックをもとに、出力を作り直してください。",
            }
        ]

        self.starter= ConversableAgent(
            "starter",
            system_message=kuroda_def + "黒田くんは" + self.rumor + "をしているという情報があります。" + self.proposed_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.starter.register_nested_chats(
            nested_chats,
            # The trigger function is used to determine if the agent should start the nested chat
            # given the sender agent.
            # In this case, the arithmetic agent will not start the nested chats if the sender is
            # from the nested chats' recipient to avoid recursive calls.
            trigger=lambda sender: sender not in [self.feed_back_agent],
        )     
        self.ichirou = ConversableAgent(
            "ichirou",
            system_message=kuroda_def + "あなたはstarterから話を聞き、jirouに話します。" + self.proposed_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.ichirou.register_nested_chats(
            nested_chats,
            # The trigger function is used to determine if the agent should start the nested chat
            # given the sender agent.
            # In this case, the arithmetic agent will not start the nested chats if the sender is
            # from the nested chats' recipient to avoid recursive calls.
            trigger=lambda sender: sender not in [self.feed_back_agent],
        )
        self.jirou = ConversableAgent(
            "jirou",
            system_message=kuroda_def + "あなたはichirouから話を聞き、saburouに話します。" + self.proposed_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.jirou.register_nested_chats(
            nested_chats,
            # The trigger function is used to determine if the agent should start the nested chat
            # given the sender agent.
            # In this case, the arithmetic agent will not start the nested chats if the sender is
            # from the nested chats' recipient to avoid recursive calls.
            trigger=lambda sender: sender not in [self.feed_back_agent],
        )
        self.saburou = ConversableAgent(
            "saburou",
            system_message=kuroda_def + "あなたはjirouから話を聞き、shirouに話します。" + self.proposed_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.saburou.register_nested_chats(
            nested_chats,
            # The trigger function is used to determine if the agent should start the nested chat
            # given the sender agent.
            # In this case, the arithmetic agent will not start the nested chats if the sender is
            # from the nested chats' recipient to avoid recursive calls.
            trigger=lambda sender: sender not in [self.feed_back_agent],
        )
        self.shirou = ConversableAgent(
            "shirou",
            system_message=kuroda_def + "あなたはsaburouから話を聞き、testerに話します。" + self.proposed_prompt,
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        self.shirou.register_nested_chats(
            nested_chats,
            # The trigger function is used to determine if the agent should start the nested chat
            # given the sender agent.
            # In this case, the arithmetic agent will not start the nested chats if the sender is
            # from the nested chats' recipient to avoid recursive calls.
            trigger=lambda sender: sender not in [self.feed_back_agent],
        )
        self.tester = ConversableAgent(
            "tester",
            system_message="あなたはテスターです。「はい」か「いいえ」でのみお答えください。",
            llm_config={"config_list": [self.llm_config]},
            human_input_mode="NEVER",  # Never ask for human input.
        )
        