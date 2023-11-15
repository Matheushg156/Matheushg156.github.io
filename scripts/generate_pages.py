import json
from jinja2 import Environment, FileSystemLoader
import markdown2

def remove_special_characters(text):
    return text.replace(' ', '_').replace('á', 'a').replace('ã', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ç', 'c').lower()

def generate_pages(posts_data):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('post_template.html')

    for post in posts_data:
        title = post['title']
        description = post['description']
        author = post['author']
        date = post['date']
        image = post.get('image', '')
        file_name = remove_special_characters(title)

        html_content = template.render(title=title, description=description, author=author, date=date, image=image)

        with open(f'docs/{file_name}.html', 'w') as file:
            file.write(html_content)

def generate_index_page(posts_data):
    index_template_path = 'templates/index_template.html'
    docs_output_path = 'docs/index.html'

    with open(index_template_path, 'r') as template_file:
        template_content = template_file.read()

    with open('posts/post_documentation.md', 'r') as documentation_file:
        documentation_content = markdown2.markdown(documentation_file.read())

    links = '\n'.join([
        f'<li><a href="{remove_special_characters(post["title"])}.html">{remove_special_characters(post["title"])}</a></li>' for post in posts_data
    ])

    context = {
        'content': documentation_content,
        'posts': posts_data,
        'links': links
    }

    updated_content = Environment(loader=FileSystemLoader('templates')).from_string(template_content).render(context)

    with open(docs_output_path, 'w') as output_file:
        output_file.write(updated_content)

if __name__ == "__main__":
    with open('posts/posts.json', 'r') as file:
        posts_data = json.load(file)

    generate_pages(posts_data)
    generate_index_page(posts_data)
