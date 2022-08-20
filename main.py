import os
from panda_session import PandaSession
from settings import DOWNLOAD_DIR
import urllib.parse

if not DOWNLOAD_DIR:
    raise Exception(".env の DOWNLOAD_DIR が指定されていません")

url = input("please enter a url => ").strip()
if not url.startswith("https://panda.ecs.kyoto-u.ac.jp/"):
    raise Exception("please enter a url of PandA")

session = PandaSession()
session.login()
res = session.get(url)

file_name = urllib.parse.unquote(url.split("/")[-1])
file_path = os.path.join(DOWNLOAD_DIR, file_name)
with open(file_path, "wb") as f:
    f.write(res.content)
