from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/train', methods=['GET'])
def train_model():
    try:
        # Calls train_model.py script
        subprocess.run(['python', 'train_model.py'], check=True)
        subprocess.run(['python', 'visualize_predictions.py'], check=True)
        return jsonify({'message': 'Visualization and training done successfully!'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
