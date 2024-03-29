from flask import Flask, request, jsonify, render_template
from mpd import MPDClient

app = Flask(__name__)
client = MPDClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mpd', methods=['POST'])
def control_mpd():
    if request.method == 'POST':
        command = request.json['command']
        if command == 'pause':
            client.pause()
        elif command == 'play':
            client.play()
        elif command == 'next':
            client.next()
        elif command == 'previous':
            client.previous()
        elif command == 'volume':
            volume = request.json['volume']
            client.setvol(volume)
        return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
