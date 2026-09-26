"""
Site sobre Empreendedorismo e Santidade
-----------------------------------------
App Flask simples que lê posts em Markdown (com front matter)
da pasta content/posts/ e renderiza como um blog.

Rodar localmente:
    pip install -r requirements.txt
    python app.py
Depois acesse http://localhost:5000
"""

import os
from pathlib import Path

import frontmatter
import markdown
from flask import Flask, abort, render_template

app = Flask(__name__)

POSTS_DIR = Path(__file__).parent / "content" / "posts"


def load_posts():
    """Lê todos os arquivos .md da pasta de posts e retorna uma lista
    de dicionários já com metadata (título, data, resumo, slug) e o
    conteúdo em Markdown."""
    posts = []
    for filepath in sorted(POSTS_DIR.glob("*.md")):
        post = frontmatter.load(filepath)
        slug = filepath.stem  # nome do arquivo sem extensão vira a URL
        posts.append(
            {
                "slug": slug,
                "title": post.get("title", slug),
                "date": post.get("date", ""),
                "summary": post.get("summary", ""),
                "content": post.content,
            }
        )
    # ordena do mais recente para o mais antigo
    posts.sort(key=lambda p: str(p["date"]), reverse=True)
    return posts


@app.route("/")
def index():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<slug>")
def post(slug):
    filepath = POSTS_DIR / f"{slug}.md"
    if not filepath.exists():
        abort(404)

    post = frontmatter.load(filepath)
    html_content = markdown.markdown(
        post.content, extensions=["extra", "codehilite", "toc"]
    )

    return render_template(
        "post.html",
        title=post.get("title", slug),
        date=post.get("date", ""),
        content=html_content,
    )


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # debug=True facilita o desenvolvimento local (recarrega sozinho)
    app.run(debug=False, port=5000)
