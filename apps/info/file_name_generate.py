import os
import uuid

from os.path import splitext


def file_name_generator(instance, filename):
    instance = filename
    base, ext = splitext(filename)
    new_name = "%s%s" % (uuid.uuid4(), ext)
    return os.path.join('photos', new_name)
