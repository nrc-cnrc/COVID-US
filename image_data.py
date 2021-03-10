import pandas as pd
from progressbar import ProgressBar
import cv2
import os


def extract_images(video_path, image_path, cropped=False, max_frames=None, target_class=['COVID', 'Pneumonia', 'Normal'], target_source=['Butterfly', 'GrepMed', 'LITFL', 'PocusAtlas'], target_probe=['convex', 'linear']):
    """
        Function to extract images from ultraasound video files.
        
        Parameters:
            - video_path: Path to the video folder to read video files from it (source folder)
            - image_path: Path to the image folder to store the extracted images in it (destination folder)
            - cropped: if True, frames will be extracted from cropped video files. Otherwise, from original video files.
            - max_frames: Maximum number of frames(images) to be extracted from a video file. Note: if a video file has fewer frames than the requested max_frames, all frames will be extracted
            - target_class: The target classes that user would like to extract images for
            - target_source: The target data sources to extract images
            - target_probe: Filter to identify type of the probe to extract images for
    """
    if cropped:
        # read cropped videos metadata file
        vid_prop_df = pd.read_csv('utils/video_cropping_metadata.csv', sep=',', encoding='latin1')
    else:
        # read videos metadata file
        metadata = pd.read_csv('utils/video_metadata.csv', sep=',', encoding='latin1')
        metadata = metadata[metadata.id !='22_butterfly_covid'] # 22_butterfly_covid.mp4 was removed in March release of butterfly


        # read videos' properties file
        vid_prop_df = pd.read_csv('utils/video_files_properties.csv')
        vid_prop_df = vid_prop_df[vid_prop_df.filename !='22_butterfly_covid.mp4'] # 22_butterfly_covid.mp4 was removed in March release of butterfly

        # merge with the video meta data file 
        vid_prop_df.filename = vid_prop_df.filename.astype(str)
        vid_prop_df.filename = vid_prop_df.filename.str.strip()

        metadata['filename2'] = metadata.id + '.' + metadata.filetype
        metadata.filename2 = metadata.filename2.astype(str)
        metadata.filename2 = metadata.filename2.str.strip()

        vid_prop_df = pd.merge(vid_prop_df, metadata[['filename2', 'source', 'probe', 'class']], left_on='filename', right_on='filename2', how='left').drop('filename2', axis=1)
        del metadata['filename2']

    # extract images based on the given parameters    
    progress = ProgressBar(max_value=vid_prop_df.shape[0])
    for idx, row in progress(vid_prop_df.iterrows()): # reselase the slicing condition on the dataframe after test is done
        if cropped:
            filename = row.filename.split('.')[0] + '_prc.avi'
            file_id = filename.split('.')[0]
            frame_count = row.org_framecount
        else:
            filename = row.filename
            file_id = row.filename.split('.')[0]
            #frame_rate = row.framerate
            frame_count = row.frame_count
        
        vid_probe = row.probe.lower()

        # read the video file and extracting frames
        cv2video = cv2.VideoCapture(video_path + str(filename))

        if max_frames:
            img_pos = int(frame_count / max_frames)
            n_frames = 1
        
        while cv2video.isOpened(): 
            frame_id = cv2video.get(1)  #current frame number
            ret, frame = cv2video.read()
            if (ret != True):
                break
            
            # storing frames
            if (max_frames) and (img_pos): # and (frame_count > max_frames):
                if (frame_id % img_pos == 0) and (n_frames <= max_frames):
                    img_filename = os.path.join(image_path, file_id + "_" + vid_probe + "_frame%d.jpg" % frame_id)
                    n_frames += 1
            else:
                img_filename = os.path.join(image_path, file_id + "_" + vid_probe + "_frame%d.jpg" % frame_id)

            cv2.imwrite(img_filename, frame)
        cv2video.release()    