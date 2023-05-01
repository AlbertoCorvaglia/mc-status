from flask import Flask, render_template, jsonify
from mcstatus import JavaServer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server-data')
def server_data():
    # Create a server object that represents your Minecraft server
    server = JavaServer.lookup("167.86.94.50:25565")

    # Get the status of the server
    status = server.status()

    # Build a dictionary with the server information
    server_data = {}
    server_data["num_players"] = status.players.online
    server_data["ping"] = int(status.latency)
    if status.players.online:
        server_data["player_names"] = [player.name for player in status.players.sample]
    else:
        server_data["player_names"] = []

    # Return the server data as a JSON response
    return jsonify(server_data)

if __name__ == '__main__':
    app.run()