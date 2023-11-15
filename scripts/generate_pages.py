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

def generate_index_page(posts_data):
    """
    Gera o arquivo index.html na pasta docs.
    Inclui links para a documentação e as postagens geradas.
    """
    index_template_path = 'templates/index_template.html'
    docs_output_path = 'docs/index.html'

    with open(index_template_path, 'r') as template_file:
        template_content = template_file.read()

    # Adicione links para a documentação e postagens geradas
    # Use os caminhos relativos corretos para a documentação e postagens
    context = {
        'posts': posts_data
    }
    updated_content = Environment(loader=FileSystemLoader('templates')).from_string(template_content).render(context)

    with open(docs_output_path, 'w') as output_file:
        output_file.write(updated_content)

if __name__ == "__main__":
    with open('posts/posts.json', 'r') as file:
        posts_data = json.load(file)

    generate_pages(posts_data)
    generate_index_page(posts_data)
