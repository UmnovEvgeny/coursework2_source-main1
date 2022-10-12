import json


def get_posts_all():
    """Возвращает посты"""
    with open("data/posts.json", mode='r', encoding='utf-8') as comments:
        return json.load(comments)


def get_comments_all():
    """Возвращает комменты"""
    with open("data/comments.json", mode='r', encoding='utf-8') as posts:
        return json.load(posts)


# def get_post_by_user(user_name):
#     """Возвращает пост определенного пользователя"""
#     posts = get_posts_all()
#     for user in posts:
#         if user_name == user['poster_name']:
#             return user
#     raise ValueError


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if pk == post['pk']:
            return post
    raise ValueError


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    comments_list = {}
    comments = get_comments_all()
    for comment in comments:
        if post_id == comment['post_id']:
            comments_list[comment['commenter_name']] = comment['comment']
    return comments_list


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    for post in posts:
        if query in post['content']:
            return post


def get_posts_by_word(word):
    result = []
    for post in get_posts_all():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def get_posts_by_user(user_name):
    """Возвращает пост определенного пользователя"""
    result = []
    posts = get_posts_all()
    for user in posts:
        if user_name == user['poster_name'] or user_name == user['pk']:
            result.append(user)
    if not result:
        raise ValueError
    return result

