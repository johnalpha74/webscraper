
parser = reqparse.RequestParser()  # initialize

parser.add_argument('userId', required=True)  # add arguments
parser.add_argument('name', required=True)
parser.add_argument('city', required=True)

args = parser.parse_args()  # parse arguments to dictionary
