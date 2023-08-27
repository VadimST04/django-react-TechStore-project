from django.db.models.signals import pre_save
from django.contrib.auth.models import User


def update_user(sender, instance, **kwargs):
    """
    This function is intended to be used as a signal handler to automatically update a user's
    username when their email is provided.
    :param sender: The sender of the signal. Typically, this is the model class sending the signal.
    :param instance: The instance of the user being updated.
    :param kwargs: Additional keyword arguments. No specific arguments are expected.
    :return: None
    """

    user = instance
    if user.email:
        user.username = user.email


pre_save.connect(update_user, sender=User)
