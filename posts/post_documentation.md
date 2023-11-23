# Bem-Vindo ao Nosso Wiki/ Blog!

## Colaboradores do Projeto

- Davi Oliveira
- João Paulo Pereira
- Marcos Henriques
- Matheus Henrique Gonzaga
- Rafael Delfino

## Estrutura do Projeto

O nosso projeto Wiki/ Blog foi estruturado de maneira organizada para facilitar o desenvolvimento, manutenção e documentação. Aqui está uma visão geral da estrutura atual:

- **/wiki-posts**
  - **/templates**
    - index.html
    - page_template.html
  - **/static**
    - **/css**
      - style.css
    - **/images**
      - github-logo.jpeg
      - python-logo.png
  - **/posts**
    - posts.json
  - **/scripts**
    - generate_pages.py
  - **/output**
- .gitignore
- README.md

* **/templates:** Contém os modelos HTML utilizados para gerar as páginas.
* **/static:** Armazena arquivos estáticos como folhas de estilo CSS e imagens.
* **/posts:** Mantém o arquivo posts.json com as informações sobre as postagens.
* **/scripts:** Inclui o script Python generate_pages.py para criar páginas HTML a partir dos dados em posts.json.
* **/output:** Destinado a armazenar as páginas HTML geradas pelo script.

## Fluxo de Branches

O projeto utiliza o modelo de fluxo de branches do Gitflow para organizar o desenvolvimento colaborativo. As branches principais são:

- **main:** Contém o código estável e versões de lançamento.
- **develop:** Branch de desenvolvimento contínuo.
- **feature:** Utilizada para desenvolvimento de novas funcionalidades.
- **release:** Prepara a versão para lançamento, aplicando correções finais.
- **hotfix:** Corrige problemas críticos em produção.

## Passos Realizados

### Configuração do Repositório:

1. Criada a branch main.
2. Criado o arquivo .gitignore.
3. Inicializado o arquivo README.md.

### Integração do Gitflow:

1. Configurado o Gitflow com as branches develop, main, feature, release, e hotfix.

### Estrutura Básica do Projeto:

1. Criada a estrutura básica do projeto com as pastas templates, static, posts, scripts, e output.
2. Adicionados arquivos como index.html, post_template.html, style.css, github-logo.jpeg, python-logo.png, posts.json, e generate_pages.py.

### Geração de Páginas com Python:

1. Desenvolvido o script Python generate_pages.py.
2. Utilizado o Jinja2 para a geração dinâmica de páginas HTML.
3. Adicionadas informações sobre postagens ao arquivo posts.json.

### Estilo CSS para Páginas:

1. Adicionado estilo CSS global no arquivo style.css.
2. Estilos específicos incluídos no page_template.html.

### Documentação:

1. Criada branch documentation.
2. Adicionado arquivo documentation.md explicando o fluxo de branches e o script Python.

### Executando o Projeto

Para executar o projeto:

1. Certifique-se de estar na branch main.
2. Clone o repositório localmente.
3. Execute o script Python generate_pages.py para gerar as páginas HTML na pasta output.
4. Abra o arquivo index.html no navegador para visualizar o site.
5. Para adicionar novas postagens, edite o arquivo posts.json e execute o script novamente.

### Outras postagens do blog:
