from flask import Flask, render_template
import get_data
app = Flask(__name__)


@app.route("/")
def hello():
    artists = get_data.get_all_artist()
    return render_template("index.html", artists=artists)


@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs = get_data.get_all_songs(aid)
    artist = get_data.singer(aid)
    return render_template("songlist.html", artist=artist[0], songs=songs)


@app.route("/lyrics/<int:sid>")
def lyrics(sid):
    lyrics = get_data.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyrics)


if __name__ == "__main__":
    app.run()
