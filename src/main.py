from copy_files import copy_files
from generate_page import generate_page
import sys
import os

if len(sys.argv) > 1:
    basepath = sys.argv[1]
    if basepath[-1] != "/":
        basepath += "/"
    if len(sys.argv) > 2:
        output_location = sys.argv[2]
    else:
        output_location = "public"
else:
    basepath = "/"
    output_location = "public"

copy_files(target_dir=output_location)

# generate_page("content/index.md", "template.html", "public/index.html")


def generate_page_recursively(content_dir, template_path, output_dir):
    for file in os.listdir(content_dir):
        if os.path.isdir(f"{content_dir}/{file}"):
            generate_page_recursively(
                f"{content_dir}/{file}", template_path, f"{output_dir}/{file}"
            )

        if file.endswith(".md"):
            output_path = f"{output_dir}/{file[:-3]}.html"
            generate_page(
                f"{content_dir}/{file}",
                template_path,
                output_path,
                f"{basepath}",
            )


generate_page_recursively("content", "template.html", output_location)
