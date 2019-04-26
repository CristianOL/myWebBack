
from service import app
from model import form

# Endpoints:
@app.route("/", methods = ['POST'])
def formController():
    return form()















if __name__ == "__main__":
    app.run(debug = True)

