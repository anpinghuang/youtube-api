from flask import Flask, request, jsonify
import streamlink

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    url = request.args.get('url')
    streams = streamlink.streams(url)
    if not streams:
        return jsonify({'success': False, 'error': 'No streams found'})
    stream = streams['best']
    download_url = stream.url
    return jsonify({'success': True, 'download_link': download_url})

if __name__ == '__main__':
    app.run(debug=True)
