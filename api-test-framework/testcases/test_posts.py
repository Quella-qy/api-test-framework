import pytest
import yaml
import os

def load_yaml(file):
    path = os.path.join(os.path.dirname(__file__),"../data", file)
    with open(path,encoding="utf-8") as f:
        return yaml.safe_load(f)

data = load_yaml("posts_data.yaml")

class TestPosts:

    def test_get_posts(self,api):
        resp=api.get("/posts")
        assert resp.status_code == 200
        assert len(resp.json())==100

    @pytest.mark.parametrize("case",data["get_post"])
    def test_get_single_post(self,api,case):
        resp=api.get(f"/posts/{case['id']}")
        assert resp.status_code == 200
        assert resp.json()["title"] == case["expected_title"]

    def test_create_post(self, api):
        payload = data["create_post"]
        resp = api.post("/posts", json=payload)
        assert resp.status_code == 201
        assert resp.json()["title"] == payload["title"]

    def test_update_post(self, api):
        resp = api.put("/posts/1", json={"title": "updated"})
        assert resp.status_code == 200
        assert resp.json()["title"] == "updated"

    def test_delete_post(self, api):
        resp = api.delete("/posts/1")
        assert resp.status_code == 200