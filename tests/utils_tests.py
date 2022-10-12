import app
import pytest


class TestAPI:
    def test_api_all_post_type_json(self):
        response = app.app.test_client().get("/api/posts", follw_redirects=True)
        keys ={"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        assert type(response.json) == list, "Получен не список"
        assert set(response.json[0].keys()) == keys, "Ключи не совпадают"

    def test_api_single_post_type_json(self):
        response = app.app.test_client().get("/api/posts/1", follw_redirects=True)
        keys ={"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        assert type(response.json) == dict, "Получен не список"
        assert set(response.json[0].keys()) == keys, "Ключи не совпадают"
