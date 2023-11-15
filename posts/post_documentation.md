# Bem-Vindo ao Nosso Wiki/ Blog!

## Estrutura do Projeto

O nosso projeto Wiki/ Blog foi estruturado de maneira organizada para facilitar o desenvolvimento, manutenção e documentação. Aqui está uma visão geral da estrutura atual:

- **/wiki-posts**
  - **/templates**
    - [index.html](templates/index.html)
    - [page_template.html](templates/page_template.html)
  - **/static**
    - **/css**
      - [style.css](static/css/style.css)
    - **/images**
      - [github-logo.jpeg](static/images/github-logo.jpeg)
      - [python-logo.png](static/images/python-logo.png)
  - **/posts**
    - [posts.json](posts/posts.json)
  - **/scripts**
    - [generate_pages.py](scripts/generate_pages.py)
  - **/output**
- [.gitignore](.gitignore)
- [README.md](README.md)

* **/templates:** Contém os modelos HTML utilizados para gerar as páginas.
* **/static:** Armazena arquivos estáticos como folhas de estilo CSS e imagens.
* **/posts:** Mantém o arquivo posts.json com as informações sobre as postagens.
* **/scripts:** Inclui o script Python generate_pages.py para criar páginas HTML a partir dos dados em posts.json.
* **/output:** Destinado a armazenar as páginas HTML geradas pelo script.

## Fluxo de Branches

O projeto utiliza o modelo de fluxo de branches do Gitflow para organizar o desenvolvimento colaborativo. As branches principais são:

- main: Contém o código estável e versões de lançamento.
- develop: Branch de desenvolvimento contínuo.
- feature: Utilizada para desenvolvimento de novas funcionalidades.
- release: Prepara a versão para lançamento, aplicando correções finais.
- hotfix: Corrige problemas críticos em produção.


## Passos Realizados

### Configuração do Repositório:

- Criada a branch main.
- Criado o arquivo .gitignore.
- Inicializado o arquivo README.md.


### Integração do Gitflow:

- Configurado o Gitflow com as branches develop, main, feature, release, e hotfix.


### Estrutura Básica do Projeto:

- Criada a estrutura básica do projeto com as pastas templates, static, posts, scripts, e output.
- Adicionados arquivos como index.html, post_template.html, style.css, github-logo.jpeg, python-logo.png, posts.json, e generate_pages.py.


### Geração de Páginas com Python:

- Desenvolvido o script Python generate_pages.py.
- Utilizado o Jinja2 para a geração dinâmica de páginas HTML.
- Adicionadas informações sobre postagens ao arquivo posts.json.


### Estilo CSS para Páginas:

- Adicionado estilo CSS global no arquivo style.css.
- Estilos específicos incluídos no page_template.html.


### Documentação:

- Criada branch documentation.
- Adicionado arquivo documentation.md explicando o fluxo de branches e o script Python.


### Executando o Projeto

Para executar o projeto:

- Certifique-se de estar na branch main.
- Clone o repositório localmente.
- Execute o script Python generate_pages.py para gerar as páginas HTML na pasta output.
- Abra o arquivo index.html no navegador para visualizar o site.
- Para adicionar novas postagens, edite o arquivo posts.json e execute o script novamente.

### Outras postagens do blog:
