# 配置信息
@staticmethod
class Config:
    # 基本配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 图片上传配置
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

   # minio 配置
    MINIO_ACCESS_KEY = 'minioaccesskey'
    MINIO_SECRET_KEY = 'miniosecretkey'
    MINIO_ENDPOINT = 'http://localhost:9000'
    MINIO_BUCKET_NAME = 'minio-bucket'
    MINIO_BUCKET_DOMAIN = 'http://localhost:9000'
    MINIO_BUCKET_REGION = 'us-east-1'
    MINIO_BUCKET_ACL = 'public-read'
    MINIO_BUCKET_CANNED_ACL = 'public-read'
    MINIO_BUCKET_ENCRYPTION = 'AES256'
    MINIO_BUCKET_ENCRYPTION_KEY = 'minioencryptionkey'
