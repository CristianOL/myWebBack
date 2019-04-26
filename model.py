
from flask import request, jsonify
import re
from sqlalchemy.exc import IntegrityError

from service import db, User



#db.session.query(User).delete()
#db.session.commit()



def form():
    data = request.json['linkedIn']
    try:
        pattern = re.search(r"^(https://es.linkedin.com/in/)", data)
        extract_name = pattern.string[pattern.regs[0][1] : pattern.endpos]
        
        new_row = User(linkedIn=extract_name)
        db.session.add(new_row)
        db.session.commit()

        print(User.query.all())

        return jsonify({'access': 'True'})

    except(AttributeError, IntegrityError):
        db.session.rollback()

        return jsonify({'access': 'False'})
        
    
 

