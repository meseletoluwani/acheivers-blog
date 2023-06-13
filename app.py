# This is the entry point to our application. We run app.py to be able to use the application

from website import create_app
# app = create_app()
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

<<<<<<< HEAD

=======
app = create_app()
>>>>>>> 0e06106f55e7185599e0dd208965af1d4b9bb91c
