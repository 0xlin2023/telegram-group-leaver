# Telegram 批量退群工具

这是一个使用 Python 编写的命令行工具，可以帮助你安全、方便地批量退出 Telegram 群组和频道。

## ✨ 功能特性

- **自动清理**：每次运行时，会自动检测并清理与"已注销账号" (Deleted Account) 的对话，保持你的对话列表整洁。
- **交互式选择**：通过键盘上下键和空格，在列表中轻松勾选想要退出的群组。
- **安全防封**：在每次退群操作后随机延迟 2-5 秒，模拟真人操作，有效规避账号被限制的风险。
- **配置简单**：将敏感的 `api_id` 和 `api_hash` 存储在本地的 `config.json` 文件中，不会上传到代码仓库，保护你的隐私安全。
- **清晰易用**：操作流程简单明了，并有清晰的进度提示和最终确认环节，防止误操作。

## ⚙️ 安装与配置

1.  **克隆或下载项目**
    将本项目所有文件下载到你的电脑上。

2.  **创建配置文件**
    在项目根目录下，创建一个名为 `config.json` 的文件，并填入以下内容。请将里面的值替换成你自己的信息（可以从 [my.telegram.org](https://my.telegram.org) 获取）。

    ```json
    {
      "api_id": 1234567,
      "api_hash": "0123456789abcdef0123456789abcdef"
    }
    ```

3.  **安装依赖**
    在你的终端或 PowerShell 中，进入项目目录，然后运行以下命令来安装所有必需的库：

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 如何运行

确保你的终端在项目目录下，然后运行以下命令：

```bash
python leave_telegram_groups.py
```

程序启动后，会提示你登录（首次运行或会话过期时），然后列出所有群组供你选择。

## ⚠️ 免责声明

- 本工具是基于 Telegram 官方 API 开发，但自动化操作本身存在被 Telegram 限制账号功能的风险，请自行承担使用后果。
- 本工具已内置随机延迟以降低风险，但仍建议不要一次性退出超大量的群组。
- 请勿将本项目用于任何非法用途。 