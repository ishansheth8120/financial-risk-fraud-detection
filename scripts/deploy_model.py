


from flask import Flask
from app  import app 

from app.models import predict_fraud

if __name__ == '__main__':
    app.run(debug=True)
