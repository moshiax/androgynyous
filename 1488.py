import os
import re
from tqdm import tqdm
from urllib.parse import unquote

def rename_files_with_hashtag(root_dir):
    files_with_hashtag = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if '#' in filename:
                files_with_hashtag.append(os.path.join(dirpath, filename))

    with tqdm(total=len(files_with_hashtag), desc='Renaming files') as pbar:
        for file_path in files_with_hashtag:
            new_file_path = unquote(file_path).replace('#', '')
            try:
                os.rename(file_path, new_file_path)
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            pbar.update(1)

def replace_hashtag_in_html_files(root_dir):
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    with tqdm(total=len(html_files), desc='Processing HTML files') as pbar:
        for html_file in html_files:
            file_path = os.path.join(root_dir, html_file)
            try:
                with open(file_path, 'r') as file:
                    html_content = file.read()
                modified_html_content = re.sub(r'#', '', html_content)
                with open(file_path, 'w') as file:
                    file.write(modified_html_content)
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            pbar.update(1)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Получить путь к текущей директории скрипта
    rename_files_with_hashtag(current_dir)
    replace_hashtag_in_html_files(current_dir)
