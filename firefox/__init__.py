from datetime import datetime
from time import sleep
from json import loads

import click
import requests

from archivy import app
from archivy.data import create_dir, get_items
from archivy.models import DataObj
from werkzeug.utils import secure_filename

num_links = 0
num_seen = 0
saved_urls = set()
with app.app_context():
    for item in get_items(collections=["bookmark"], structured=False):
        saved_urls.add(item["url"])


def parse_folder(data, path):
    global num_links, num_seen
    create_dir(path)
    for item in data["children"]:
        if "uri" in item and item["uri"].startswith("http"):
            if item["uri"] in saved_urls:
                num_seen += 1
            else:
                date = datetime.utcfromtimestamp(
                    item["dateAdded"] // 10 ** 6
                )  # micro-seconds
                bookmark = DataObj(
                    type="bookmark", path=path, date=date, url=item["uri"]
                )
                bookmark.process_bookmark_url()
                if bookmark.insert():
                    num_links += 1
                    print(f"Saving {bookmark.title} into {path}")
                else:
                    print(f"Failed to save {bookmark.url}")
        elif "children" in item:
            sub_path = path
            if not item["title"] in ["unfiled", "toolbar", "root", "menu", ""]:
                sub_path += f"{secure_filename(item['title'])}/"
            parse_folder(item, sub_path)


@click.command(
    help=f"Pull your upvoted or favorited posts from Hacker News and "
    f"save their contents into your knowledge base"
)
@click.argument(
    "export_file",
)
def firefox(export_file):
    """Download Firefox bookmarks into Archivy. Pass the location of the JSON export file"""
    with app.app_context():
        ff_data = loads(open(export_file, "r").read())
        parse_folder(ff_data, "firefox/")
        print(f"Saved {num_links} new links. {num_seen} were already saved.")
