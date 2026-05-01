from copy_files import copy_files
from generate_page import generate_page
import os

copy_files()

# generate_page("content/index.md", "template.html", "public/index.html")


def generate_page_recursively(content_dir, template_path, output_dir):
    for file in os.listdir(content_dir):
        if os.path.isdir(f"{content_dir}/{file}"):
            generate_page_recursively(
                f"{content_dir}/{file}", template_path, f"{output_dir}/{file}"
            )

        if file.endswith(".md"):
            output_path = f"{output_dir}/{file[:-3]}.html"
            generate_page(f"{content_dir}/{file}", template_path, output_path)


generate_page_recursively("content", "template.html", "public")
