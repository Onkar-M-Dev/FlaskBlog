from flaskblog import create_app

app = create_app()

if __name__ == '__main__':  # in case you need to run applicatin without using environment variables
    app.run(debug = True)
