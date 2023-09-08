
from flask import render_template

from app import app

from app.forms.transformation_form import TransformationForm
from ml.classification_utils import transformation_handle
from config import Configuration

config = Configuration()


@app.route('/transform', methods=['GET', 'POST'])
def transform():
    """API for selecting  an image and running a
    transformation job. Returns the image transformed"""
    form = TransformationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        # model_id = form.model.data
        img_path = f'/home/giuseppe/PycharmProjects/flask-classification-2022-F/app/static/imagenet_subset/{image_id}'
        transformation_img_path = f'/home/giuseppe/PycharmProjects/flask-classification-2022-F//app/static/img_transformation/transform_{image_id}'

        color_id = form.color.data
        brightness_id = form.brightness.data
        contrast_id = form.contrast.data
        sharpness_id = form.sharpness.data

        transformation_handle(img_path, transformation_img_path, color_factor=1.5, brightness_factor=1.8,
                             contrast_factor=1.9,
                             sharpness_factor=1.7)

        return render_template("trans_output.html", image_id=image_id)

    # otherwise, it is a get request and should return the
    # image and transformation selector
    return render_template('select_transf.html', form=form)