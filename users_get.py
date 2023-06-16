class Users(Resources):
        def get(self):
                    data = pd.read_csv('users.csv')  # read CSV
                            data = data.to_dict()  # convert dataframe to dictionary
                                    return {'data': data}, 200  # return data and 200 OK code
