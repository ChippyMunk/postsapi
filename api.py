from flask import Flask, request, jsonify, Response
import requests
import requests_cache
import time

app=Flask(__name__)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"success":True}), 200

requests_cache.install_cache('query_cache', expire_after=180)
@app.route('/api/posts', methods=['GET'])
def get_posts():
    tags=request.args.get("tags")
    sortBy=request.args.get("sortBy") or "id"
    direction=request.args.get("direction") or "asc"

    if not tags:
        return jsonify({"error":"Tags parameter is required"}), 400

    url="******************************"
    ids={}
    output=[]
    tags=tags.split(",")

    for tag in tags:
        params=dict(tag=tag)
        response=requests.get(url, params=params)
        now = time.ctime(int(time.time()))

        for post in response.json()["posts"]:
            id=post["id"]
            if id not in ids:
               ids[id]=True
               output.append(post)

    if sortBy not in ["id","reads","likes","popularity"] and direction not in ["asc","desc"]:
        return jsonify({"error":"sortBy and direction parameters are invalid"}), 400

    elif sortBy not in ["id","reads","likes","popularity"]:
        return jsonify({"error":"sortBy parameter is invalid"}), 400

    elif direction not in ["asc","desc"]:
        return jsonify({"error":"direction parameter is invalid"}), 400

    desc=False
    if direction=="desc":
        desc=True
    output.sort(key=lambda x: x[sortBy], reverse=desc)

    return jsonify({"posts":output}), 200



if __name__=="__main__":
    app.run(debug=False)
