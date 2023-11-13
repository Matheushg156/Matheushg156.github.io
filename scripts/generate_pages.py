import json
from jinja2 import Environment, FileSystemLoader

def generate_pages(posts_data):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('post_template.html')

    for post in posts_data:
        title = post['title']
        description = post['description']
        author = post['author']
        date = post['date']
        image = post.get('image', '')  # Pode não haver uma imagem em todos os posts

        html_content = template.render(title=title, description=description, author=author, date=date, image=image)

        with open(f'docs/{title.lower().replace(" ", "_")}.html', 'w') as file:
            file.write(html_content)

if __name__ == "__main__":
    with open('posts/posts.json', 'r') as file:
        posts_data = json.load(file)

    generate_pages(posts_data)
