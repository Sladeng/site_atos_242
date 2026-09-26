# Empreendedorismo & Santidade

Blog simples em Flask. Posts em Markdown, sem banco de dados, sem WordPress.

## Rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

Acesse http://localhost:5000

## Como publicar um novo post

Crie um arquivo `.md` dentro de `content/posts/`, por exemplo:

```
content/posts/meu-novo-post.md
```

Com este formato no topo (front matter):

```markdown
---
title: "Título do post"
date: 2026-08-10
summary: "Uma linha resumindo o post (aparece na lista)"
---

Conteúdo do post aqui, em Markdown normal.
```

O nome do arquivo vira a URL do post (`/post/meu-novo-post`). Não precisa
mexer em código — só adicionar o arquivo.

## Estrutura

```
app.py                  -> lógica da aplicação
requirements.txt        -> dependências Python
content/posts/*.md      -> seus posts
templates/              -> layout HTML (base, lista, post, 404)
static/css/style.css    -> estilo visual
```

## Próximos passos sugeridos

- Subir este projeto para um repositório no GitHub
- Fazer deploy em um serviço que roda Python nativamente (Render, Railway,
  Fly.io ou um VPS com gunicorn + nginx) — nada de hospedagem só-PHP
- Automatizar o deploy: a cada `git push`, o serviço publica sozinho
- Trocar `debug=True` por configuração de produção antes de publicar
