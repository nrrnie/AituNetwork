from flask import request, render_template, session
from flask import redirect, url_for, flash
from aituNetwork.users import users
from aituNetwork.models import Users, ProfilePictures, Posts
from aituNetwork import db
from utils import picturesDB, auth_required


@users.route('/<slug>', methods=['GET'])
@auth_required
def profile(slug: str):
    profile_user = Users.query.filter_by(slug=slug).first()

    if profile_user is None:
        return 'user is not found'

    profile_picture = ProfilePictures.query.filter_by(user_id=profile_user.id).order_by(ProfilePictures.id.desc()).first()
    if profile_picture:
        profile_user.profile_picture = profile_picture.name

    user = session['user']

    # current page
    profile_status = None
    if user.id == profile_user.id:
        profile_status = 'own profile'
    elif user.id != profile_user.id:
        profile_status = "user's profile"

    return render_template('profile.html', user=user, profile_user=profile_user, profile_status=profile_status)


@users.route('/settings', methods=['GET', 'POST'])
@auth_required
def settings():
    if request.method == 'GET':
        return render_template('settings.html', user=session['user'])

    picture = request.files.get('profile-picture')
    if picture:
        picture_name = picturesDB.add_picture('profile-pictures', picture)
        profile_picture = ProfilePictures(user_id=session['user'].id,  name=picture_name)
        db.session.add(profile_picture)
        db.session.commit()

    flash('Info was updated', 'success')
    return redirect(url_for('users.settings'))


@users.route('/friends', methods=['GET'])
@auth_required
def friends():
    if request.method == 'GET':
        return render_template('friends.html', user=session['user'])


@users.route('/add/post', methods=['POST'])
@auth_required
def add_post():
    post_content = request.form.get('post-content')

    post = Posts(user_id=session['user'].id, content=post_content)
    db.session.add(post)
    db.session.commit()

    flash('Your post is added!', 'success')
    return redirect(url_for('users.profile', slug=session['user'].slug))
