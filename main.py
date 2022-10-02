import os
from panda_session import PandaSession
from settings import DOWNLOAD_DIR, PASSWORD, USER_NAME
import urllib.parse

if not DOWNLOAD_DIR:
    raise Exception(".env の DOWNLOAD_DIR が指定されていません")

url = input("please enter a url => ").strip()
if not url.startswith("https://panda.ecs.kyoto-u.ac.jp/"):
    raise Exception("please enter a url of PandA")

if not USER_NAME or not PASSWORD:
    raise Exception(".env の USER_NAME または PASSWORD が指定されていません")

session = PandaSession(USER_NAME, PASSWORD)
session.login()
res = session.get(url)

file_name = urllib.parse.unquote(url.split("/")[-1])
file_path = os.path.join(DOWNLOAD_DIR, file_name)
with open(file_path, "wb") as f:
    f.write(res.content)
