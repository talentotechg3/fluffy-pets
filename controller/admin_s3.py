import boto3
from credentials.keys import ACCESS_KEY, SECRET_KEY

bucket_name = "bucket-fluffy-pets"

def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')  #indicar como parámetro el servicio al que se desea conectar
        print("Connecting to S3")
        return s3_resource
    except Exception as err:
        print("Error en connection_s3", err)
        
def save_file(photo):
    try:
        photo_path_local = "/tmp/" + photo.filename
        #print(photo_path_local)
        photo.save(photo_path_local)
        print("photo saved")
        return photo_path_local
    except Exception as err:
        print("Error en save_file", err)
        
def upload_file(s3_resource, photo_path_local, photo, id):
    try:
        #photo_path_dest = "images/" + "photo.JPG"
        photo_name = photo.filename
        photo_ext = photo_name.split(".")[len(photo_name.split("."))-1]
        photo_path_dest = "images/" + id + "." + photo_ext
        #print(photo_path_dest)
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_path_dest)
        print("file uploaded")
        return True
    except Exception as err:
        print("Error en upload_file")
        return False
        
def consult_file(s3_resource, id):
    bucket_repo = s3_resource.Bucket(bucket_name)
    bucket_objects = bucket_repo.objects.all()
    path_name_list = []
    for obj in bucket_objects:
        print(obj.key)
        path_file_s3 = obj.key
        path_file_list = path_file_s3.split("/")
        name_photo = path_file_list[len(path_file_list)-1].split(".")[0]
        #print(name_photo)
        if name_photo == id:
            print(id+" found")
            return path_file_s3
    return None