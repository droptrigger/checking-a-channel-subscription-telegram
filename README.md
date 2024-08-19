[Russian](ruREAMDE.md)

<div align="center">

# Сhecking channel subscriptions
Easy Telegram bot that __works only after subscribing__ to all the necessary channels  
My TG channel - [Click](https://t.me/CreateTrigger)

<img src='https://github.com/user-attachments/assets/0e89d09a-3298-42df-856c-380e512f0ec9' width=50%/>
</div>

## 📖 Description

To work, you will need access to the necessary channels and a bot.

Which groups you need to subscribe to can be written in the code, or you can get them from the database.

## 🤖 Launching the bot

### 1. First, you will need to clone the repository to your computer via Git Bash.

```git
git clone https://github.com/droptrigger/checking-a-channel-subscription-telegram.git
```

### 2. We will install all the necessary libraries:

```pip
pip install aiogram
```

### 3. Go to https://t.me/BotFather and we create a bot. We allow you to invite him to the channels (It should be written `enabled`).
<div align="center">
<img src='https://github.com/user-attachments/assets/d82aff71-41dd-43c0-a41e-5344f8a6b404' width=50%/>
</div>

### 4. In the same BotFather, we copy the API token.
<div align="center">
<img src="https://github.com/user-attachments/assets/16d2b471-2818-49c9-a248-4a8e77b37685" width=60% height=50%>
</div>

### 5. In [config](bot/data/config.py ) enter this token instead of a pass.

### 6. Add the bot to the channel, copy the link to this channel.
<div align="center">
<img src="https://github.com/user-attachments/assets/d942e00f-f281-437d-ba9e-5e9331aa9a72">
</div>

### 7. The link to the channel can be found in various groups [user handlers](bot/handlers/user_handlers.py).
<div align="center">
<img src="https://github.com/user-attachments/assets/a1b40606-b288-46d0-90a9-2392c5c473c5">
</div>

## ✅ Well done! Everything should be working now.
