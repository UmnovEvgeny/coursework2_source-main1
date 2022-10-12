from flask import Flask, render_template, request, jsonify
import logging
import utils

app = Flask(__name__)

logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/")
def all_posts():
    """Главная страница"""
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:post_id>")
def post_by_id(post_id):
    """Подробный пост"""
    try:
        post = utils.get_post_by_pk(post_id)
    except ValueError:
        return "Такого поста нет или у пользователя нет постов"
    comment = utils.get_comments_by_post_id(post['pk'])
    comment_count = len(comment)
    return render_template('post.html', post=post, comment=comment, comment_count=comment_count)


@app.route('/search/')
def search_page():
    """Вывод постов по поиску"""
    search_query = request.args.get('s', ' ')
    posts = utils.get_posts_by_word(search_query)
    posts_count = len(posts)
    return render_template('search.html', posts=posts, search_query=search_query, posts_count=posts_count)


@app.route("/users/<user_name>")
def post_by_user_name(user_name):
    """Вывод постов конкретного пользователя"""
    try:
        posts = utils.get_posts_by_user(user_name)
    except ValueError:
        return "Такого пользователя нет или у пользователя нет постов"
    name = posts[0]['poster_name']
    return render_template('user-feed.html', posts=posts, name=name)


@app.route("/api/posts")
def all_posts_api():
    """Возвращает полный список постов в виде JSON-списка"""
    posts = utils.get_posts_all()
    logging.info("Запрос /api/posts")
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def post_api(post_id):
    """Возвращает один пост в виде JSON-словаря"""
    post = utils.get_post_by_pk(post_id)
    logging.info(f"Запрос /api/posts/{post_id}")
    print(post)
    return jsonify(post)


if __name__ == '__main__':
    app.run()
