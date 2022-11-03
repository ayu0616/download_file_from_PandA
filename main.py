import os
import urllib.parse

from panda_session import PandaSession
from settings import DOWNLOAD_DIR, PASSWORD, USER_NAME

if not DOWNLOAD_DIR:
    raise Exception(".env の DOWNLOAD_DIR が指定されていません")

if not USER_NAME or not PASSWORD:
    raise Exception(".env の USER_NAME または PASSWORD が指定されていません")

print("start login to PandA")
session = PandaSession(USER_NAME, PASSWORD)
session.login()
print("finish login to PandA")


def download(url: str):
    if not url.startswith("https://panda.ecs.kyoto-u.ac.jp/"):
        print("please enter a url of PandA")
        return

    print("start download")
    res = session.get(url)

    file_name = urllib.parse.unquote(url.split("/")[-1])
    file_path = os.path.join(DOWNLOAD_DIR, file_name)
    with open(file_path, "wb") as f:
        f.write(res.content)
    print(f"finished download : {file_path}")


def input_url():
    url = input("please enter a url => ").strip()
    return url


url = input_url()
while url:
    download(url)
    url = input_url()
