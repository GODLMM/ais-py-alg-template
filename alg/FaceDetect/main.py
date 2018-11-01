from utils.Base64 import b64_image
from alg.FaceDetect import align_mtcnn

def alg_process(img):
    img = b64_image(img)
    bounding_boxes , points, scaled = align_mtcnn.align(img)
    if scaled is not None:
        return bounding_boxes, points, scaled
    else:
        return [], [], []