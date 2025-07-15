from social_blog import create_app, db

app = create_app()

if __name__ == "__main__": 
    # this create the .db file
    with app.app_context():
        db.create_all() 

    # this runs it on local and local internet IP address
    app.run(host='0.0.0.0', port=5555, debug=True)
