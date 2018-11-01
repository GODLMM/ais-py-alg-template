import base64
import numpy as np
import cv2

def b64_image(image_b):
    img_b64decode = base64.b64decode(image_b) 
    nparr = np.fromstring(img_b64decode, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def image_b64(img):
    image_b = base64.b64encode(cv2.imencode('.jpg',img)[1]).decode()
    return image_b


def feat_b64(feat):
    feat=feat.astype(np.float32)
    b64 = base64.b64encode(feat).decode()
    return b64

def b64_feat(b64):
    r = base64.decodestring(b64.encode())
    feat = np.frombuffer(r, dtype=np.float32)
    return feat
