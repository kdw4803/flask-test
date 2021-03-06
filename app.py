from app import create_app
import argparse

parser = argparse.ArgumentParser()  
parser.add_argument("-e", "--env", help="select app enviroment")
parser.add_argument("-db", "--db", help="select app enviroment")
args = parser.parse_args()

if __name__ == '__main__':
    app = create_app(args)
    app.run(debug=True, host='0.0.0.0', port=80)
