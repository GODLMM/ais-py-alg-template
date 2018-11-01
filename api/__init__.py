from api.eg.main import egHandler
from api.FaceDetect.main import detectHandler
handlers = [
    (r"/eg", egHandler),
    (r"/face-detect", detectHandler)
]