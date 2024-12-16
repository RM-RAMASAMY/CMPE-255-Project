from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/update_movies', methods=['GET'])
def update_movies():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        # Run the Python script with the user ID
        result = subprocess.run(['python', 'my_model.py', user_id], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({'error': result.stderr}), 500
        return jsonify({'message': 'Movies updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)