from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/music/albums', methods=['GET'])
def get_albums():
    artist = request.args.get('artist')
    if not artist:
        return jsonify({'error': 'Artist parameter is required.'}), 400

    access_token = 'frIadzjoDoRQyUgt3fM1X38Y1AM9SLMWXYi2RCB26EC3r729hKa'
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.deezer.com/search/album?q={artist}'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve albums.'}), response.status_code

    data = response.json()
    albums = [{'id': album['id'], 'title': album['title'], 'cover_medium': album['cover_medium']} for album in data['data']]
    return jsonify(albums)

@app.route('/api/music/songs', methods=['GET'])
def get_songs():
    album_id = request.args.get('albumId')
    if not album_id:
        return jsonify({'error': 'Album ID parameter is required.'}), 400

    access_token = 'frIadzjoDoRQyUgt3fM1X38Y1AM9SLMWXYi2RCB26EC3r729hKa'
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.deezer.com/album/{album_id}/tracks'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve songs.'}), response.status_code

    data = response.json()
    songs = [{'title': song['title'], 'artist': song['artist'], 'artist_feat': song['artist_feat'], 'nb_play': song['nb_play'], 'duration': song['duration']} for song in data['data']]
    return jsonify(songs)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8086)