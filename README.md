# FaceDetect-DNN-Model
Face Detection을 위한 DNN Model 구현 repository입니다.  
<br/>
  

## 파일 설명
  
    - model.py  
      detectAndSave 함수를 포함하고 있다. 해당 함수는 프레임을 넘겨 받아서 얼굴을 인식하고 인식한  
      영역에 사각형을 그려준 뒤 프레임을 다시 반환한다  

    - main.py  
      영상과 사진을 넘겨 받아서 인식 작업을 진행하는 파일이다. (아직 face recognition을 구현하지  
      않아 사진은 사실상 필요 없다) 영상을 프레임 단위로 detectAndSave 함수에 넣어서 프레임을  
      변환하고, 변환한 프레임들을 다시 영상으로 조립해서 출력한다.  

    - run.py  
      테스트 영상이 여러 개 있기 때문에 이를 한번에 처리할 수 있도록 만든 파일이다.  

    - deploy.prototxt.txt  
      모델의 parameter 값들을 갖고 있는 파일로, model.py와 같은 경로에 있어야 한다.  

    - res10_300x300_ssd_iter_140000.caffemodel  
      모델 구조에 대한 정보를 담고 있는 파일로, 이 또한 model.py와 동일한 경로에 있어야 한다.  

    - openh264-1.8.0-win64.dll  
      openh264(cv2.VideoWriter)를 가동하기 위해 필요한 파일로, main.py와 동일한 경로에 있어야 한다.  
      해당 파일은 컴퓨터마다 버전이 다르기 때문에 https://github.com/cisco/openh264/releases에서  
      본인에게 맞는 버전의 파일을 다운로드 받아야 된다. 

## To-Do

    1. terminal에서 "pip install -r requirements.txt" 실행
    2. 위 링크에서 본인의 컴퓨터와 맞는 .dll 파일을 찾아서 다운로드 후, main.py와 동일한 경로에 저장
    3. run.py 파일에서 영상 및 사진 경로 지정 (사진은 None으로 해놔도 무방)
    4. run.py 파일 실행