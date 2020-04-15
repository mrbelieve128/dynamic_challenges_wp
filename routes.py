import os
from flask import Blueprint,render_template,request
from CTFd.utils.decorators import authed_only
from CTFd.utils.user import get_current_user
from . import models,utils


writeup_blueprint = Blueprint("writeup", __name__)

@writeup_blueprint.route('/writeup', methods=['POST'])
@authed_only
def uplaod_writeup():
    try:
        file = request.files['writeup']
        challenge_id = request.form.get('challenge_id')
        challenge_name = request.form.get('challenge_name')
        challenge_folder = challenge_id+'_'+challenge_name
        uid = get_current_user().id
        username = get_current_user().name
        UPLOAD_FOLDER = os.path.join(os.getcwd(),'writeup',challenge_folder,username)
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        print(file.filename)
        filename = utils.secure_filename(file.filename)
        print(filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        models.insert_writeup(challenge_id,uid,path)
        return 'Success'
    except:
        return 'Error'

@writeup_blueprint.route('/writeup',methods=['GET'])
@authed_only
def writeup_status():
    challenge_id = request.args.get("cid")
    uid = get_current_user().id
    wp = models.query_writeup(challenge_id,uid)
    if wp:
        return 'Uploaded'
    else:
        return 'Not uploaded'