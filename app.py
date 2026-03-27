from flask import Flask, jsonify

app = Flask(__name__)

# Telecom Node Status Data
nodes = {
    "HLR": {"status": "UP", "ip": "192.168.1.1", "alarm": "None"},
    "HSS": {"status": "UP", "ip": "192.168.1.2", "alarm": "None"},
    "EIR": {"status": "DOWN", "ip": "192.168.1.3", "alarm": "NODE_DOWN"},
    "MNP": {"status": "UP", "ip": "192.168.1.4", "alarm": "None"},
    "UDM": {"status": "UP", "ip": "192.168.1.5", "alarm": "None"}
}

# Health Check
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "Telecom Node Monitor"
    })

# Get All Nodes
@app.route('/nodes')
def get_nodes():
    return jsonify(nodes)

# Get Specific Node
@app.route('/nodes/<node_name>')
def get_node(node_name):
    node = nodes.get(node_name.upper())
    if node:
        return jsonify({node_name.upper(): node})
    return jsonify({"error": "Node not found"}), 404

# Get Active Alarms
@app.route('/alarms')
def get_alarms():
    active_alarms = {
        name: data 
        for name, data in nodes.items() 
        if data["alarm"] != "None"
    }
    return jsonify({
        "active_alarms": active_alarms,
        "total": len(active_alarms)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)