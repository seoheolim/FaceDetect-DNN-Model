import cv2
import numpy as np


def detectAndSave(frame):
    (height, width) = frame.shape[:2]
    model_name='res10_300x300_ssd_iter_140000.caffemodel'
    prototxt_name='deploy.prototxt.txt'
  
    model=cv2.dnn.readNetFromCaffe(prototxt_name,model_name);
    blob=cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),1.0,
                              (300,300),(104.0,177.0,123.0))
    model.setInput(blob)
    detections=model.forward()


    for i in range(0, detections.shape[2]):
        
            confidence = detections[0, 0, i, 2]
            min_confidence=0.4; # TODO: 최적의 임계값 찾기
           
            if confidence > min_confidence:
                  
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                    (startX, startY, endX, endY) = box.astype("int")
                    #print(confidence, startX, startY, endX, endY)
     
                    
                    text = "{:.2f}%".format(confidence * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 255, 0), 2)
                    cv2.putText(frame, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return frame
