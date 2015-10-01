import cloudinary

def upload_resource(file, **options):
    result = upload(file, **options)
    return cloudinary.CloudinaryResource(result["public_id"], version=str(result["version"]),
        format=result.get("format"), type=result["type"], resource_type=result["resource_type"], metadata=result)