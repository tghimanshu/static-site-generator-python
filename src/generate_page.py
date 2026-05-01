import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    with open(from_path, "r") as from_file:
        from_content = from_file.read()

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from_content_html = markdown_to_html_node(from_content).to_html()
    page_title = extract_title(from_content)

    final_content = template_content.replace("{{ Title }}", page_title)
    final_content = final_content.replace("{{ Content }}", from_content_html)

    final_content = final_content.replace('href="/', f'href="{basepath}')

    with open(dest_path, "w") as dest_file:
        dest_file.write(final_content)
        print(f"Page generated: {dest_path}.")
