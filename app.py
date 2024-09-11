from app import create_app, database

app = create_app()

with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2525, debug=True)