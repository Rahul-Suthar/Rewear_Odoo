from app import create_app, db
from sqlalchemy.exc import OperationalError
from sqlalchemy import text

app = create_app()

def check_db_connection():
    with app.app_context():
        try:
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database connection successful.")
        except OperationalError as e:
            print("Failed to connect to the database.")
            print(f"Error: {e}")
            exit(1)


if __name__ == "__main__":
    check_db_connection()
    print("Starting Flask server at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
