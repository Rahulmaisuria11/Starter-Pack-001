from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # don't forget to import the class Engineer here, so uncomment the line below:
    # from app.models.engineer import Engineer
    # from app.models.location import Location
    # from app.models.roles import Roles
    # from app.models.roles_secondary import RolesSecondary

    """
    Engineer Routes
    """

    @app.route('/engineers', methods=['GET'])
    def get_engineers():
        """
        1. create an empty list to store the formatted data
        2. create a variable that will store the query for all engineers
        3. create a loop that will iterate through all engineers
        4. in the for loop, append each engineer to the empty list
        :return: a JSON object with the response and status
        """
        data = []

        # TODO

        return jsonify({
            'response': data,
            'status': 200
        })

    @app.route('/new_engineer', methods=['POST'])
    def new_engineer():
        """
        1. get the request
        2. query the database and filter by the username, to check if it has any
        3. if there isn't any, create the engineer, otherwise, return a response stating that there is already one
        4. create a variable with the Engineer class and add your variables
        5. add the variable to the db and commit the changes.
        :return: a JSON object with the response and status
        """
        # TODO

        return jsonify({
            'response': '{} has been created...'.format('your engineer here'),
            'status': 200
        })

    @app.route('/update_engineer/<_id>', methods=['PATCH'])
    def update_engineer(_id):
        """
        1. get the request
        2. query the database and filter by the username, to check if it has any
        3. if there isn't any, create the engineer, otherwise, return a response stating that there is already one
        4. update the values on the engineer
        5. commit the changes
        :param _id: id of the engineer to be updated
        :return: a JSON object with the response and status
        """

        # TODO

        return jsonify({
            'response': '{} has been updated...'.format('your engineer here'),
            'status': 200,
        })

    @app.route('/delete_engineer/<_id>', methods=['DELETE'])
    def delete_engineer(_id):
        """
        1. get the request
        2. query the database and filter by the username, to check if it has any
        3. if there isn't any, create the engineer, otherwise, return a response stating that there is already one
        4. delete the engineer and commit the changes
        :param _id: id of the engineer to be deleted
        :return: a JSON object with the response and status
        """

        # TODO

        return jsonify({
            'response': '{} has been deleted...'.format('your engineer here'),
            'status': 200,
        })

    """
    Locations Routes
    """

    @app.route('/locations', methods=['GET'])
    def get_locations():
        pass

    @app.route('/location/<int:_id>', methods=['GET'])
    def get_location(_id):
        pass

    @app.route('/new_location', methods=['POST'])
    def new_location():
        pass

    @app.route('/update_location/<int:_id>', methods=['PATCH'])
    def update_location(_id):
        pass

    @app.route('/delete_location', methods=['DELETE'])
    def delete_location(_id):
        pass

    """
    Roles Routes
    """

    @app.route('/roles', methods=['GET'])
    def get_roles():
        pass

    @app.route('/role/<int:_id>', methods=['GET'])
    def get_role(_id):
        pass

    @app.route('/new_role', methods=['POST'])
    def new_role():
        pass

    @app.route('/update_role/<int:_id>', methods=['PATCH'])
    def update_role(_id):
        pass

    @app.route('/delete_role/<int:_id>', methods=['DELETE'])
    def delete_role(_id):
        pass

    # This will allow for us to create the database on app start:
    with app.app_context():
        print('Flask starting...')
        db.create_all()

        # Create predefined roles:
        # TODO

    return app
