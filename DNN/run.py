from main import convertVideo

root_vid_PATH = 'C:/Users/BRAIN/Documents/Workspace/ProjectHIDE/Videos' # 테스트 영상을 담고 있는 폴더 경로 지정
img_PATH = None # Face Recognition을 하는 경우 인식하고자 하는 사람의 사진 경로 지정 (Recognition은 아직 미구현)
out_PATH = "C:/Users/BRAIN/Documents/Workspace/ProjectHIDE/Output" # 출력 영상을 저장하고 싶은 경로 지정
test_names = ['angle', 'distance', 'many_people', 'nationality'] 
vid_PATHS = [root_vid_PATH + "/" + test_names[i] + ".mp4" for i in range(4)]

for vid_PATH, test_name in zip(vid_PATHS, test_names):

    print(f"Converting Video for {test_name} test")
    
    convertVideo(vid_PATH, img_PATH, out_PATH, test_name)
    
    print("Completed!\n")