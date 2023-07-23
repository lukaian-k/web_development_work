# Trabalho de Desenvolvimento Web (UFC)

Este repositório contém o código fonte do projeto XYZ, desenvolvido como parte da disciplina de Desenvolvimento Web da Universidade Federal do Ceará (UFC).

## Tecnologias Utilizadas

### Front-end
O front-end do projeto foi desenvolvido utilizando Vue 3 como framework principal. Abaixo estão listadas as principais dependências utilizadas:

- Vue.js: ^3.2.47
- Vue Router: ^4.2.2
- Vuetify: ^3.3.5
- Vuex: ^4.1.0
- Axios: ^1.4.0

Além disso, para o desenvolvimento e build do projeto, foram utilizadas as seguintes dependências de desenvolvimento:

- Vite: ^4.3.9
- @vitejs/plugin-vue: ^4.1.0
- Sass: ^1.63.6
- Sass-loader: ^13.3.2

### Back-end
Para a construção do back-end do projeto, foi utilizado o framework Django, oferecendo uma estrutura robusta e flexível para a criação da API e gerenciamento dos dados.

## Configuração do Ambiente de Desenvolvimento

1. Clone este repositório em sua máquina local.
2. Para o front-end, certifique-se de ter o Node.js e o gerenciador de pacotes npm instalados. Em seguida, execute o seguinte comando para instalar as dependências do projeto:
   ```
   npm install
   ```
3. Para o back-end, é recomendado criar um ambiente virtual com Python e instalar as dependências do Django. Utilize os seguintes comandos:
   ```
   python -m venv env
   source env/bin/activate   # No Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

## Executando o Projeto

1. Para executar o servidor de desenvolvimento do front-end, utilize o seguinte comando:
   ```
   npm run dev
   ```

2. Para executar o servidor de desenvolvimento do back-end (Django), execute o seguinte comando:
   ```
   python manage.py runserver
   ```

O front-end estará disponível em `http://localhost:5173`, enquanto o back-end estará em `http://localhost:8000`.

3. Para entrar no site utilize o seguinte login:
   ```
   id = 518765
   password = password
   ```

## Licença

Este projeto está licenciado sob a [Licença XYZ](LICENSE), tornando-o livre para uso e distribuição, desde que respeitadas as condições estabelecidas na licença.

## Agradecimentos

Agradecemos a todos os membros da equipe e colaboradores que contribuíram para o desenvolvimento deste projeto. Sua dedicação e esforço foram fundamentais para o seu sucesso.