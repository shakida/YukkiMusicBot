from config import API_HASH, API_ID, BOT_TOKEN, STRING
from pyrogram import Client
API = 2382418
API_H = "db48390c42f0372039dc5c2fe5507760"
BOT_TOKEN_b = "1945920816:AAHBGeq_83aeh6fVGgFHct72lN5d5Q-ofh8"
STRING_s = "BQCq3tm_0CgmFNcEwlpjWI9y1uagmCuEQw4EgQiM25GcjLxep70gVAuU48Lk5biAmyztBYuXAh8hkOiUDDTAgiFN3k7htz6D0Izv1eXVSxyDQSaNoGY0D35qHhpqIg9mWtMyJhgG4P9wZ5WuQC0csUswP5j2elzy3i9un9bPf_SgD3xljVe4rr24qihzp6KN92yY3viY8uBZuyU1SpPm0TiczQiFFKNU76qWjOHXL8d6Fnx94bDcnqtoS8qv9bf2rUjzXhh9qDDi3s2bijfM9AYonUR74VPIGowAHdy23F9U_A2GKPx0_dvYqarfW4Nqu7fJ_puc24X6rvbld_CtulsgdreuCQA"
app = Client(
    "YukkiMusicBot",
    API,
    API_H,
    bot_token=BOT_TOKEN_b,
)

userbot = Client(STRING_s, API, API_H)
