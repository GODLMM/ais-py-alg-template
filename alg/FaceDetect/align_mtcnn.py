from scipy import misc
import tensorflow as tf
import numpy as np

from alg.FaceDetect import detect_face

path = './weights/mtcnn'

gpu_options = tf.GPUOptions(allow_growth = True)
config = tf.ConfigProto(log_device_placement = False, gpu_options = gpu_options)

sess=tf.Session(config = config)
pnet, rnet, onet = detect_face.create_mtcnn(sess, path)

def align(img, image_size = 160, margin = 32):
    img_size=img.shape[0:2]
        
    minsize = 20 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor

    bounding_boxes, points = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    if bounding_boxes.shape[0] == 0:
        scaled=None
    else:
        scaled=[]
        for _, det in enumerate(bounding_boxes):
            det = np.squeeze(det[0:4])
            bb = np.zeros(4, dtype=np.int32)
            bb[0] = np.maximum(det[0]-margin/2, 0)
            bb[1] = np.maximum(det[1]-margin/2, 0)
            bb[2] = np.minimum(det[2]+margin/2, img_size[1])
            bb[3] = np.minimum(det[3]+margin/2, img_size[0])
            cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]
            cropped = misc.imresize(cropped, (image_size,image_size), interp='bilinear')
            scaled.append(cropped)
        scaled = np.asarray(scaled)
    return bounding_boxes, points, scaled
        
        