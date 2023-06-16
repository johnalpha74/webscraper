
class Users(Resource):
        def post(self):
                    parser = reqparse.RequestParser()  # initialize
                            
                                    parser.add_argument('userId', required=True)  # add args
                                            parser.add_argument('name', required=True)
                                                    parser.add_argument('city', required=True)
                                                            
                                                                    args = parser.parse_args()  # parse arguments to dictionary
                                                                            
                                                                                    # create new dataframe containing new values
                                                                                            new_data = pd.DataFrame({
                                                                                                            'userId': args['userId'],
                                                                                                                        'name': args['name'],
                                                                                                                                    'city': args['city'],
                                                                                                                                                'locations': [[]]
                                                                                                                                                        })
                                                                                                    # read our CSV
                                                                                                            data = pd.read_csv('users.csv')
                                                                                                                    # add the newly provided values
                                                                                                                            data = data.append(new_data, ignore_index=True)
                                                                                                                                    # save back to CSV
                                                                                                                                            data.to_csv('users.csv', index=False)
                                                                                                                                                    return {'data': data.to_dict()}, 200  # return data with 200 OK

