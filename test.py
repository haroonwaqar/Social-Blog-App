from social_blog import app, db
from social_blog.models import User

with app.app_context():
    user = User.query.all()

print(user)
