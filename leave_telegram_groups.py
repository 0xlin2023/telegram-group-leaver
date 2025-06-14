import json
import asyncio
import random
try:
    import questionary
except ImportError:
    print("错误：缺少 'questionary' 库。")
    print("请先在终端运行 'pip install questionary' 来安装它。")
    exit(1)

from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat

print("=== Telegram 批量退群工具 By ChatGPT ===\n")

# 从 config.json 读取 api_id 和 api_hash
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        api_id = config["api_id"]
        api_hash = config["api_hash"]
except Exception as e:
    print("读取 config.json 失败，请确保文件存在且格式正确！")
    print("示例内容：{\"api_id\": 123456, \"api_hash\": \"abcdefg123456\"}")
    exit(1)

async def main():
    async with TelegramClient('leave_telegram_session', api_id, api_hash) as client:
        print("正在获取对话列表...")
        dialogs = await client.get_dialogs()
        
        # 自动清理 "Deleted Account"
        deleted_count = 0
        for d in dialogs:
            if getattr(d.entity, 'deleted', False):
                print(f"检测到已注销账号，正在清理: {d.name} ...")
                await client.delete_dialog(d.id)
                deleted_count += 1
        
        if deleted_count > 0:
            print(f"\n已自动清理 {deleted_count} 个'已注销账号'的对话。\n")
            print("重新获取对话列表...")
            dialogs = await client.get_dialogs()

        groups = [d for d in dialogs if isinstance(d.entity, (Channel, Chat))]
        
        if not groups:
            print("未检测到任何群组/频道。")
            return

        print(f"\n共检测到 {len(groups)} 个群组/频道。\n")

        choices_map = {
            f"{idx+1:>4}: {g.name}  (ID: {g.id})": g
            for idx, g in enumerate(groups)
        }

        selected_choices = await questionary.checkbox(
            '请选择要退出的群组 (按[空格]勾选/取消, [回车]确认):',
            choices=list(choices_map.keys())
        ).ask_async()

        if not selected_choices:
            print("没有选择任何群组，程序退出。")
            return
            
        groups_to_leave = [choices_map[choice] for choice in selected_choices]
        
        print("\n你选择了以下群组准备退出：")
        for group in groups_to_leave:
            print(f"- {group.name}")
        
        confirm = await questionary.confirm("确认要退出这些群组吗?", default=False).ask_async()
        
        if confirm:
            total_to_leave = len(groups_to_leave)
            for i, group in enumerate(groups_to_leave):
                print(f"[{i+1}/{total_to_leave}] 正在退出: {group.name} ...", end="", flush=True)
                await client.delete_dialog(group.id)
                print(" ✔")

                if i < total_to_leave - 1:
                    delay = random.uniform(2, 5)
                    print(f"   └ 为规避风险，随机等待 {delay:.1f} 秒...")
                    await asyncio.sleep(delay)

            print("\n指定群组已全部退出！")
        else:
            print("操作已取消。")

if __name__ == "__main__":
    asyncio.run(main())
