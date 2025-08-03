
from app import create_app
from app.utils import db
from sqlalchemy import text


app = create_app("Local")

if __name__ == '__main__':

        with app.app_context():
                try:
                        db.session.execute(text("select 1"))
                        print("database connected")

                        app.run(host="127.0.0.1", port=5001, debug=True)
                        print ("app running")
                except Exception as e:
                        print("database connection failed --> " + e)

       # 