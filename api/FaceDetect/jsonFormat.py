from utils.Base64 import image_b64, feat_b64

def jsonFormat(bounding_boxes, points, scaled):

    rjson = {
        "bounding_boxes": [boxFormat(box) for box in bounding_boxes],
        "points": [feat_b64(points[:, i]) for i in range(scaled.shape[0])],
        "scaled": [image_b64(scaled[i]) for i in range(scaled.shape[0])]
    }

    return rjson

def boxFormat(box):
    rbox = {
        'x': box[0],
        'y': box[1],
        'w': box[2],
        'h': box[3],
        's': box[4]
    }
    return rbox