#creating CRUD APP
#create
# -first name
# -last name
# -email

# end point /create_contact

#imports
from flask import request, jsonify
from config import app, db
from models import Contact

#viewing the contacts

@app.route("/contacts", methods= ["GET"])
def get_contacts():
    contacts = Contact.query.all()
    # convert python objects into json 
    # map gives list so convert that datatype to list 
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

#creating contacts
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message" : "you must inculde firstname, lastname and email"}),
            400,
        )
    
    #if no error is caught that means we have firstname , lastname and email
    # make a new contact and add contact into database

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    # if we try to create , if u find a exception we retun jsonifyed message as exception as event turned into string , with error code 400
    except Exception as e:
        return jsonify({"message": str(e)}),400
    # if created then message user created with status code 200 
    return jsonify({"message": "USER created"}), 201

# route to update contact

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "USER not found"}), 404
    
    #if user was foundby the used_id

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "USER updated"}), 200


@app.route("/delete_contact/<int:user_id>" ,  methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    with app.app_context():
        # createing all the models that are in the models  if not already created 
        #spining up the database
        db.create_all()
    app.run(debug=True)
