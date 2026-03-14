\# Clone - Programa de Metas (Prefeitura de SP) 

O objetivo foi replicar a arquitetura e a interface do site oficial do Programa de Metas de São Paulo.



\##    Tecnologias Utilizadas

\*   \*\*Docker \& Docker Compose\*\*: Orquestração de containers.

\*   \*\*Django 5.0\*\*: Framework principal.

\*   \*\*Django Ninja\*\*: API de alta performance para os indicadores.

\*   \*\*PostgreSQL\*\*: Banco de dados relacional com persistência via Volumes.

\*   \*\*Tailwind CSS\*\*: Estilização baseada na identidade visual oficial.



\## Como rodar o projeto

1\. Clone o repositório.

2\. Certifique-se de que o Docker está instalado e aberto

3\. No terminal, execute:

&#x20;  docker compose up 

4\. entre em http://localhost:8000/ - Essa é a pagina do usuário

5\. entre em http://localhost:8000/admin/metas/metareal/?o=1 - Essa é a pagina do admin

6\. faça login na pagina de admin

usuário: admin

senha: admin123



Resumo de Comandos Rápidos

docker compose up: Liga o site e o banco de dados.

docker compose stop: Desliga o site, mas mantém tudo pronto para ligar rápido.

docker compose down: Desliga tudo e limpa a rede (bom para quando o site travar).

docker compose ps: Mostra se o site e o banco estão "Up" (ligados) ou "Exit" (desligados).

