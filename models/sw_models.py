from app import db, ma



class SoftwareModel(db.Model):
    __tablename__ = 'Software'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False,unique=True)
    description = db.Column(db.Text, nullable=False)
    tags = db.Column(db.JSON, nullable=True)
    price = db.Column(db.Float, nullable=True)
    platforms = db.Column(db.JSON, nullable=True)
    user_id=db.Column(db.Integer,db.ForeignKey('Users.id'),nullable=False)


    def __repr__(self):
        return self.name


class SoftwareModelSchema(ma.Schema):
    class Meta:
        model = SoftwareModel
        fields = ("id","name" ,"description", "tags", "price", "platforms","user_id")
        ordered = True



sw_schema = SoftwareModelSchema()
sws_schema = SoftwareModelSchema(many=True)

