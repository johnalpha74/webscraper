
        ...

                # read our CSV
                        data = pd.read_csv('users.csv')

                                if args['userId'] in list(data['userId']):
                                                return {
                                                                        'message': f"'{args['userId']}' already exists."
                                                                                    }, 401
                                                        else:
                                                                        # create new dataframe containing new values
                                                                                    new_data = pd.DataFrame({
                                                                                                        'userId': args['userId'],
                                                                                                                        'name': args['name'],
                                                                                                                                        'city': args['city'],
                                                                                                                                                        'locations': [[]]
                                                                                                                                                                    })
                                                                                                # add the newly provided values
                                                                                                            data = data.append(new_data, ignore_index=True)
                                                                                                                        data.to_csv('users.csv', index=False)  # save back to CSV
                                                                                                                                    return {'data': data.to_dict()}, 200  # return data with 200 OK

