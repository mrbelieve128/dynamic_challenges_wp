from CTFd.models import db,Challenges

class Writeup(db.Model):
    # __mapper_args__ = {"polymorphic_identity": "writeups"}
    wid = db.Column(db.Integer,primary_key=True)
    cid = db.Column(db.Integer,nullable=False)
    uid = db.Column(db.Integer,nullable=False)
    path = db.Column(db.String(200),nullable=False)

    def __init__(self,cid,uid,path):
        self.cid = int(cid)
        self.uid = int(uid)
        self.path = path

def insert_writeup(cid,uid,path):
    wp = Writeup(cid,uid,path)
    db.session.add(wp)
    db.session.commit()

def query_writeup(cid,uid):
    wp = db.session.query(Writeup).filter_by(cid=cid,uid=uid).first()
    return wp