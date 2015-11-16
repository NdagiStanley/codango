


def get_upload_file_name(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = instance.userid + instance.file_extension
    return 'user_{0}/{1}'.format(instance.user.id, filename)

