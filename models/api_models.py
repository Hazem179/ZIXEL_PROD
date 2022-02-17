from app import db,ma

class APIModel(db.Model):
    __tablename__ = 'API'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.Text,nullable=False)
    tags = db.Column(db.JSON)
    price = db.Column(db.Float)
    url_context = db.Column(db.String(32))
    end_points = db.Column(db.JSON)
    user_id=db.Column(db.Integer,db.ForeignKey('Users.id'),nullable=False)

    def __repr__(self):
        return self.name


class APIModelSchema(ma.Schema):
    class Meta:
        model = APIModel
        fields = ("id","name" ,"description", "tags", "price", "url_context","end_points","user_id")
        ordered = True


api_schema = APIModelSchema()
apis_schema = APIModelSchema(many=True)
