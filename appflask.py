import api
from distutils.log import debug
from flask import Flask, render_template, jsonify
app = Flask(__name__)


app.register_blueprint(api.api, url_prefix="/api")


@app.route("/")
def hello():
    return render_template("base.html",)


if __name__ == "__main__":
    app.run(debug=True)


# from distutils.log import debug
# from flask import Flask, render_template, jsonify
# import get_data
# import api


# app = Flask(__name__)

# app.register_blueprint(api.api, url_prefix="/api")


# @app.route("/")
# def hello():
#     return render_template("base.html",)


# @app.route("/artists")
# def get_artists():
#     artists = get_data.get_all_artist()
#     artists_arr = [{'id': i[0], "name":i[1]} for i in artists]
#     return jsonify(artists_arr)


# @app.route("/songs/<int:aid>")
# def list_all_songs(aid):
#     songs = get_data.get_all_songs(aid)
#     songs_arr = [{'id': i[1], "name":i[0]} for i in songs]
#     # singer= get_data.singer(aid)
#     # artists = get_data.get_all_artist()
#     return jsonify(songs_arr)


# @app.route("/songs/<int:aid>/lyrics/<int:sid>")
# def lyrics(sid, aid):
#     lyrics = get_data.get_lyrics(sid)
#     songs = get_data.get_all_songs(aid)
#     singer = get_data.singer(aid)
#     artists = get_data.get_all_artist()
#     # print(lyrics)
#     return jsonify(lyrics)


# if __name__ == "__main__":
#     app.run(debug=True)
