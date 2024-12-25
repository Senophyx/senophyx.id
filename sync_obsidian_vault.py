import shutil
import os

obsidian_dir = r"D:\Personal\Obsidian Vault\Personal Blog"
content_dir = os.path.join(os.getcwd(), 'content')

if os.path.exists(content_dir):
    shutil.rmtree(content_dir)

shutil.copytree(obsidian_dir, content_dir, dirs_exist_ok=True)