import requests

def api_test(params):
    url="http://127.0.0.1:5000/api/posts"
    response=requests.get(url, params=params)

    return response

test_cases=[{"tags":"tech,science"},{"tags":"politics,history", "sortBy":"popularity"},{"tags":"politics,history", "direction":"desc"},
{"tags":"tech,startups", "sortBy":"reads", "direction":"asc"},{"sortBy":"reads", "direction":"asc"},{"tags":"design,tech", "sortBy":"like"},{"tags":"culture,history", "direction":"dsc"},
{"tags":"tech,politics", "sortBy":"ids", "direction":"dsc"},{"tags":"music"}]

for case in test_cases:
    print case
    resp=api_test(case)
    sortBy, direction="id", "asc"
    if "sortBy" in case:
        sortBy=case["sortBy"]
    if "direction" in case:
        direction=case["direction"]


    if "tags" not in case:
        assert resp.json()["error"]=="Tags parameter is required"
        assert resp.status_code==400, "Status code incorrect."
        continue

    if sortBy not in ["id","reads","likes","popularity"] and direction not in ["asc","desc"]:
        assert resp.json()["error"]=="sortBy and direction parameters are invalid"
        assert resp.status_code==400, "Status code incorrect."
        continue

    elif sortBy not in ["id","reads","likes","popularity"]:
        assert resp.json()["error"]=="sortBy parameter is invalid"
        assert resp.status_code==400, "Status code incorrect."
        continue

    elif direction not in ["asc","desc"]:
        assert resp.json()["error"]=="direction parameter is invalid"
        assert resp.status_code==400, "Status code incorrect."
        continue

    assert resp.status_code==200, "Status code incorrect."
    posts=resp.json()["posts"]

    if direction=="asc":
        for i in range(1,len(posts)):
            for tag in posts[i]["tags"]:
                assert tag in posts[i]["tags"], "Tags do not match"
            assert posts[i]["id"]!=posts[i-1]["id"], "Duplicates in results."
            assert int(posts[i][sortBy])>=int(posts[i-1][sortBy]), "Results not in the right order."
    else:
        for i in range(1,len(posts)):
            for tag in posts[i]["tags"]:
                assert tag in posts[i]["tags"], "Tags do not match"
            assert posts[i]["id"]!=posts[i-1]["id"], "Duplicates in results."
            assert int(posts[i][sortBy])<=int(posts[i-1][sortBy]), "Results not in the right order."
