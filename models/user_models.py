from app import db, ma





class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    user_type = db.Column(db.Enum("D","B",name="usertype"), nullable=False)
    user_description = db.Column(db.Text,nullable=False)
    products_sw = db.relationship("SoftwareModel",backref="Users",lazy = 'dynamic')
    products_api = db.relationship("APIModel",backref="Users",lazy = 'dynamic')

    def __repr__(self):
        self.user_name


class UserModelSchema(ma.Schema):
    class Meta:
        model = UserModel
        fields = ("id", "user_name", "user_description","user_type")
        ordered = True

user_schema = UserModelSchema()
users_schema = UserModelSchema(many=True)



