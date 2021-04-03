try:
    import secrets
except ImportError:
    pass

from api import app

if __name__ == "__main__":
    import pretty_errors
    app.run(debug=True)
