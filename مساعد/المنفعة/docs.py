# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton)

intro = "**📚 Docs**\n\n"

USERGE_THUMB = "https://imgur.com/download/Inyeb1S"
USER_THUMB = "https://i.imgur.com/h6ZyB71.png"
BOT_THUMB = "https://i.imgur.com/zRglRz3.png"
DUAL_THUMB = "https://i.imgur.com/ZTcIANz.png"
CONTENT_THUMB = "https://i.imgur.com/v1XSJ1D.png"
REPO_THUMB = "https://i.imgur.com/hoRVXM3.png"
GC_THUMB = "https://i.imgur.com/lDpSgmg_d.png"

DECORATORS_THUMB = "https://i.imgur.com/xp3jld1.png"
DEPLOYMENT_THUMB = "https://i.imgur.com/S5lY8fy.png"
VARS_THUMB = "https://i.imgur.com/dw1lLBX.png"
EXAMPLE_THUMB = "https://i.imgur.com/NY4uasQ.png"
FAQS_THUMB = "https://i.imgur.com/b33rM21.png"
ERRORS_THUMB = "https://i.imgur.com/hv2r4nm.png"

userge_wiki = "https://theuserge.github.io/"
decorators = "https://theuserge.github.io/decorators.html"
deployment = "https://theuserge.github.io/deployment.html"
vars = f"{deployment}#list-of-available-vars"
modes = f"{deployment}#userge-modes"
examples = "https://theuserge.github.io/examples.html"
faqs = "https://theuserge.github.io/faq.html"
errors = "https://theuserge.github.io/errors.html"

HELP = (
    "🤖 **Assistant**\n\n"


    "You can use this bot in inline mode to search for UserGe Docs and FAQs"
    f" and All Methods available in [Docs](t.me//NNN1Ny).\n\n"

    "**__Search__**\n"
    "`@Bot <query>`\n\n"

    "**__List of Queries__**\n"
    "`Decorators`\n"
    "`Deployment`\n"
    "`Vars`\n"
    "`Modes`\n"
    "`Example`\n"
    "`Faqs`\n"
    "`Errors`"
)

USERGE = [
    InlineQueryResultArticle(
        title="About UserGe",
        input_message_content=InputTextMessageContent(
            "**👑 UserGe**\n\n"
            "**[UserGe](https://github.com/usergeteam/userge) **"
            "**is a Powerful , Pluggable Telegram UserBot written in **"
            "**[Python](https://www.python.org/) using **"
            "**[Pyrogram](https://github.com/pyrogram).**",
            disable_web_page_preview=True
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👥 Community", url="https://t.me/NNn1ny")
                ],
                [
                    InlineKeyboardButton("🗂 GitHub", url="https://github.com/Gaoc3"),
                    InlineKeyboardButton("📂 Docs", url="https://github.com/Gaoc3")
                ]
            ]
        ),
        description="UserGe is a Powerful , Pluggable Telegram UserBot.",
        thumb_url=USERGE_THUMB
    ),
    InlineQueryResultArticle(
        title="About UserGe Assistant",
        input_message_content=InputTextMessageContent(
            HELP, disable_web_page_preview=True, parse_mode="markdown"
        ),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "🗂 Source Code",
                url="https://github.com/Gaoc3"
            ),
            InlineKeyboardButton(
                "😎 Use Inline!",
                switch_inline_query=""
            )
        ]]),
        description="How to use UserGe Assistant Bot.",
        thumb_url=BOT_THUMB,
    ),
    InlineQueryResultArticle(
        title="Quick Links",
        input_message_content=InputTextMessageContent(
            "📚 **UserGe Docs**\n\n"
            "`Quick Links.`",
            disable_web_page_preview=True,
        ),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Online Docs 📚", url="t.me//NNn1ny"#quick-links"
            )
        ]]),
        description="See Contents available in UserGe wiki.",
        thumb_url=CONTENT_THUMB
    ),
    InlineQueryResultArticle(
        title="UserGe-Repository",
        input_message_content=InputTextMessageContent(
            "📚 **UserGe Docs**\n\n"
            "`UserGe-Repositories.`",
            disable_web_page_preview=True,
        ),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Github 🗂", url=f"https://github.com/Gaoc3"
            )
        ]]),
        description="All UserGe-Repositories.",
        thumb_url=REPO_THUMB
    ),
    InlineQueryResultArticle(
        title="Groups and Channels",
        input_message_content=InputTextMessageContent(
            "📚 ** Docs**\n\n"
            "`Join Our Updates Channel and Support Group.`",
            disable_web_page_preview=True,
        ),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Groups and Channels 👥",
                url="NNn1ny"
            )
        ]]),
        description="Join UserGe support Group and Updates Channel.",
        thumb_url=GC_THUMB
    )
]

DECORATORS = [
    (
        "UserGe Callback Decorators.",
        "Userge have it's own custom decorators.",
        f"[UserGe Callback Decorators.]({decorators}#userge-callback-decorators)"
    ),
    (
        "Parameters",
        "Required and Non-required Parameters of Decorators.",
        f"[Parameters]({decorators}#parameters)"
    ),
    (
        "Examples",
        "Example of Decorators.",
        f"[Example of Decorators]({decorators}#examples)"
    )
]

DEPLOYMENT = [
    (
        "Config Vars.",
        "About Config Vars and Explanation.",
        f"[Config Vars]({deployment}#config-vars--setting-up-vars)"
    ),
    (
        "Branches",
        "Check available Branches in UserGe repo.",
        f"[Branches]({deployment}#steps-to-deploy)"
    ),
    (
        "Deploy to Heroku",
        "Directly Deploy to Heroku.",
        f"[Deploy to Heroku]({deployment}#deploying-with-heroku)"
    ),
    (
        "Deploy with termux",
        "Deploy UserGe with Termux.",
        f"[Deploy with Termux](https://theuserge.github.io/termux.html)"
    ),
    (
        "Deploying with Docker",
        "Deploy UserGe using Docker.",
        f"[Deploy with Docker]({deployment}#deploying-with-docker-)"
    ),
    (
        "Deploying with Legacy Method",
        "Deploying UserGe with Legacy Method.",
        f"[Deploying with Legacy Method]({deployment}#deploying-with-legacy-method)"
    )
]

ERRORS = [
    (
        "description : Bad request : chat not found",
        "#1-description--bad-request--chat-not-found",
        "https://telegra.ph/file/1b707364fd2bb0e6a3805.jpg"
    ),
    (
        "ERROR :: Required Command : jq : could not be found !",
        "#2-error--required-command--jq--could-not-be-found-",
        "https://telegra.ph/file/28e9365af63d3b509f501.jpg"
    ),
    (
        "'fatal: bad revision 'HEAD...upstream/master'",
        "#3-fatal-bad-revision-headupstreammaster",
        "https://telegra.ph/file/aeda709f622f34ae3802d.jpg"
    ),
    (
        "Error R14 (memory quota exceeded)",
        "#4-error-r14-memory-quota-exceeded",
        "https://telegra.ph/file/d5f90faff504b334e541f.jpg"
    ),
    (
        "GitCommandError",
        "#5-gitcommanderror",
        "https://telegra.ph/file/1a286bbd6284f71abfed4.jpg"
    )
]

VARS = [
    (
        "Api Id and Api hash",
        "How to get Api Id and Api hash",
        f"[API_ID and API_HASH]({deployment}#1-api_id-and-api_hash)"
    ),
    (
        "Database Url",
        "How to get Database Url",
        f"[DATABASE_URL]({deployment}#2-database_url)"
    ),
    (
        "Log Channel Id",
        "How to get Log Channel Id",
        f"[LOG_CHANNEL_ID]({deployment}#3-log_channel_id)"
    ),
    (
        "Load Unofficial Plugins",
        "How to Load Unofficial Plugins.",
        f"[LOAD_UNOFFICIAL_PLUGINS]({deployment}#1-load_unofficial_plugins)"
    ),
    (
        "Custom Plugins Repo",
        "Add custom plugins repo",
        f"[CUSTOM_PLUGINS_REPO]({deployment}#2-custom_plugins_repo)"
    ),
    (
        "Assert single instance",
        "What is assert single instance",
        f"[ASSERT_SINGLE_INSTANCE]({deployment}#3-assert_single_instance)"
    ),
    (
        "Workers",
        "Explained Workers Var",
        f"[WORKERS]({deployment}#4-workers)"
    ),
    (
        "Rss chat id",
        "What is rss chat id",
        f"[RSS_CHAT_ID]({deployment}#5-rss_chat_id)"
    ),
    (
        "Gdrive Client Id and Client Secret",
        "How to get G_DRIVE_CLIENT_ID and G_DRIVE_CLIENT_SECRET",
        f"[G_DRIVE_CLIENT_ID and G_DRIVE_CLIENT_SECRET]({deployment}#6-g_drive_client_id--g_drive_client_secret)"
    ),
    (
        "G_DRIVE_ID_TD",
        "Explained G_DRIVE_IS_TD",
        f"[G_DRIVE_IS_TD]({deployment}#7-g_drive_is_td)"
    ),
    (
        "G_DRIVE_INDEX_LINK",
        "How to get Index Link",
        f"[G_DRIVE_INDEX_LINK]({deployment}#8-g_drive_index_link)"
    ),
    (
        "Down Path",
        "Explained about Download Path",
        f"[DOWN_PATH]({deployment}#9-down_path)"
    ),
    (
        "Preferred Language",
        "Explained Preferred Language",
        f"[PREFERRED_LANGUAGE]({deployment}#10-preferred_language)"
    ),
    (
        "Currency Api",
        "How to get Currency Api",
        f"[CURRENCY_API]({deployment}#11-currency_api)"
    ),
    (
        "Ocr Space Api Key",
        "How to get Ocr Space Pai Key.",
        f"[OCR_SPACE_API_KEY]({deployment}#12-next-var-is-ocr_space_api_key)"
    ),
    (
        "Weather Defcity",
        "Weather Default City.",
        f"[WEATHER_DEFCITY]({deployment}#13-weather_defcity)"
    ),
    (
        "Userge antispam api",
        "What is userge antispam api",
        f"[USERGE_ANTISPAM_API]({deployment}#14-userge_antispam_api)"
    ),
    (
        "Spamwatch Api",
        "How to get SpamWatch Api.",
        f"[SPAM_WATCH_API]({deployment}#15-spam_watch_api)"
    ),
    (
        "Open Weather Map",
        "How to get Open Weather Map.",
        f"[OEPN_WEATHER_MAP]({deployment}#16-open_weather_map)"
    ),
    (
        "Remove Background Api",
        "How to get Remove Background Api.",
        f"[REMOVE_BG_API_KEY]({deployment}#17-remove_bg_api_key)"
    ),
    (
        "Gdrive Parent folder Id",
        "How to get Gdrive Parent folder Id",
        f"[G_DRIVE_PARENT_ID]({deployment}#18-g_drive_parent_id)"
    ),
    (
        "Command Trigger",
        "What is Command Trigger.",
        f"[CMD_TRIGGER]({deployment}#19-cmd_trigger)"
    ),
    (
        "Sudo Trigger",
        "What is Sudo Trigger.",
        f"[SUDO_TRIGGER]({deployment}#20-sudo_trigger)"
    ),
    (
        "Upstream Repo",
        "What is Upstream Repo",
        f"[UPSTREAM_REPO]({deployment}#21-upstream_repo)"
    ),
    (
        "Finished Progress Bar",
        "What is Finished Progress Bar.",
        f"[FINISHED_PROGRESS_STR]({deployment}#22-finished_progress_str)"
    ),
    (
        "UnFinished Progress Bar",
        "What is UnFinished Progress Bar.",
        f"[UNFINISHED_PROGRESS_STR]({deployment}#23-unfinished_progress_str)"
    ),
    (
        "Custom Pack Name",
        "What is Custom Pack Name.",
        f"[CUSTOM_PACK_NAME]({deployment}#24-custom_pack_name)"
    ),
    (
        "Alive Media",
        "How to get Alive Media var.",
        f"[ALIVE_MEDIA]({deployment}#25-alive_media)"
    ),
    (
        "Heroku Api Key",
        "How to get Heroku Api Key",
        f"[HEROKU_API_KEY]({deployment}#26-heroku_api_key)"
    ),
    (
        "Heroku App Name",
        "How to get Heroku App Name",
        f"[HEROKU_APP_NAME]({deployment}#27-heroku_app_name)"
    ),
    (
        "Max duration",
        "What is max duration",
        f"[MAX_DURATION]({deployment}#28-max_duration)"
    ),
    (
        "Heroku Session String",
        "How to get Heroku Session String",
        f"[HU_STRING_SESSION]({deployment}#1-user-mode)"
    ),
    (
        "Plugin Channel ID.",
        "How to Add/Load Custom Plugins?",
        f"[PLUGINS_CHANNEL_ID]({faqs}#26-how-to-addload-custom-plugins)"
    ),
]

MODES = [
    (
        "User Mode",
        "Explained Docs for User Mode.",
        f"[What is User Mode?]({deployment}#1-user-mode)",
        f"{USER_THUMB}"
    ),
    (
        "Bot Mode",
        "Explained Docs for Bot Mode.",
        f"[What is Bot Mode?]({deployment}#2-bot-mode)",
        f"{BOT_THUMB}"
    ),
    (
        "Dual Mode",
        "Explained Docs for Dual Mode.",
        f"[What is Dual Mode?]({deployment}#3-dual-mode)",
        f"{DUAL_THUMB}"
    )
]

EXAMPLES = [
    (
        "Cmd Example",
        "Explained Docs for Cmd Example.",
        f"[Example Cmd]({deployment}#example-command)"
    ),
    (
        "Filter Example",
        "Explained Docs for Filter Example.",
        f"[Example Filters]({deployment}#example-filter)"
    )
]

FAQS = [
    ("How to Setup userge?", f"{faqs}#1-how-to-setup-userge"),
    ("How to Add unofficial plugins?",
    f"{faqs}#2-how-to-add-unofficial-plugins"),
    ("How to genrate String Session?", f"{faqs}#3-how-to-generate-string-session-"),
    ("How to get all cmd list?", f"{faqs}#4-how-to-get-all-commands-list"),
    ("How to use a cmd?", f"{faqs}#5-how-to-use-a-command"),
    ("What is sudo and how to enable it?", f"{faqs}#6-what-is-sudo-how-to-enable-it"),
    ("How to Setup Google Drive and GDrive Parent Id?",
    f"{faqs}#7-how-to-setup-google-drive-how-to-setup-gdrive-parent-id"),
    ("What is bot mode and how to enable bot mode?",
    f"{faqs}#8-what-is-bot-mode-how-to-enable-bot-mode"),
    ("How to get Help Menu as Inline Mode?",
    f"{faqs}#9-how-to-get-help-menu-as-inline-mode"),
    ("What is dyno saver and what is .die cmd?",
    f"{faqs}#10-what-is-dyno-saver-what-is-die-only-for-heroku-users"),
    ("How to add buttons in Notes/Filters?",
    f"{faqs}#11-how-to-add-buttons-in-text-notes-and-filters"),
    ("How to setup Lydia ?",
    f"{faqs}#12-how-to-setup-lydia-"),
    ("What is floodwait?", f"{faqs}#13-what-is-floodwait"),
    ("How to setup deezloader?", f"{faqs}#14-how-to-setup-deezloader"),
    ("What is spamwatch?", f"{faqs}#15-what-is-spamwatch"),
    ("How to set your own custom media for .alive?",
    f"{faqs}#16how-to-set-your-own-custom-media-for-alive"),
    ("How to send secret message in userge bot ?",
    f"{faqs}#17-how-to-send-secret-message-using-your-userge-bot"),
    ("How to clear download path?", f"{faqs}#18-how-to-clear-downloads-path"),
    ("How to stop autopic?", f"{faqs}#19-how-to-stop-autopic"),
    ("How to Unzip, Unrar and Unpacks files?", f"{faqs}#20-how-to-unzip-unrar-and-unpack-files-in-userge"),
    ("How to add media in pm permit?", f"{faqs}#21-how-to-add-media-in-custom-pm-permit"),
    ("How to use spam watch api?", f"{faqs}#22-how-to-use-spam-watch-api"),
    ("How to update userbot?", f"{faqs}#23-how-to-update-userge-userbot"),
    ("How to know dyno usage?", f"{faqs}#24-how-to-know-dyno-usage"),
    ("File type issue while downloading from direct link?",
    f"{faqs}#25-file-type-issue-while-downloading-from-link"),
    ("How to Add/Load Custom Plugins?", f"{faqs}#26-how-to-addload-custom-plugins")
]
