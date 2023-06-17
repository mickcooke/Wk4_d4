from flask import Blueprint, Flask, redirect, render_template, request

from models.biting import Biting
import repositories.biting_repository as biting_repository
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings = bitings)

# NEW
@bitings_blueprint.route("/bitings/new", methods=['GET'])
def new_biting():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans = humans, zombies = zombies)

# CREATE
@bitings_blueprint.route("/bitings", methods=['POST'])
def create_biting():
    human = human_repository.select(request.form['human_id'])
    zombie = zombie_repository.select(request.form['zombie_id'])
    biting = Biting(human, zombie)
    biting_repository.save(biting)
    return redirect('/bitings')




# EDIT
@bitings_blueprint.route("/bitings/edit/<id>", methods=['GET'])
def edit_biting(id):
    biting = biting_repository.select(id)
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/edit.html", biting = biting, humans = humans, zombies = zombies)


# UPDATE
@bitings_blueprint.route("/bitings/<id>", methods=['POST'])
def update_biting(id):
    human = human_repository.select(request.form['human_id'])
    zombie = zombie_repository.select(request.form['zombie_id'])
    
    biting = Biting(human, zombie, id)
    biting_repository.update(biting)
    return redirect('/bitings')




# DELETE
@bitings_blueprint.route("/bitings/delete/<id>", methods=['POST'])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect('/bitings')


