import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form import ClassificationForm
from app.forms.histo_classification_form import ClassificationFormHistogram
from ml.classification_utils import classify_image, plot_histo_clr, plt_histo
from ml.classification_utils import classify_image
from config import Configuration
import matplotlib
matplotlib.use('Agg')

config = Configuration()


@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    """API for selecting a model and an image and running a 
    classification job. Returns the output scores from the 
    model."""
    form = ClassificationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        model_id = form.model.data

        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "model_id": model_id,
                "img_id": image_id
            })
            task = q.enqueue_job(job)

        # returns the image classification output from the specified model
        # return render_template('classification_output.html', image_id=image_id, results=result_dict)
        return render_template("classification_output_queue.html", image_id=image_id, jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('classification_select.html', form=form)

@app.route('/histogram_classifications', methods=['GET', 'POST'])
def histogram_classifications():
    """API for selecting an image and return the histogram of the image"""

    form = ClassificationFormHistogram()
    if form.validate_on_submit():
        image_id = form.image.data
        img_path = f'/home/giuseppe/PycharmProjects/flask-classification-2022-F/app/static/imagenet_subset/{image_id}'
        hist_img_path = f'/home/giuseppe/PycharmProjects/flask-classification-2022-F/app/static/img_histo/hist_{image_id}'
        hist_img_path_clr = f'/home/giuseppe/PycharmProjects/flask-classification-2022-F/app/static/img_histo_clr/hist_{image_id}'
        plt_histo(img_path, hist_img_path)
        plot_histo_clr(img_path, hist_img_path_clr)

        return render_template('histo_output.html', image_id=image_id)

    return render_template("histo_temp.html", form=form)


