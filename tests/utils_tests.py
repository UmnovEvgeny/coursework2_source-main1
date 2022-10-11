import json


def get_posts_all():
    """Возвращает посты"""
    with open("posts.json", mode='r', encoding='utf-8') as posts:
        return json.load(posts)


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    try:
        pass

    except ValueError:

        return 'Такого пользователя нет или у пользователя нет постов'
    pass


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    try:
        pass

    except ValueError:

        return 'Такого поста нет ил у поста нет комментов'
    pass


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    pass


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    pass
