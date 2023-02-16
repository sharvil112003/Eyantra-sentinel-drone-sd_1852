<launch>

  <node name="usb_cam" pkg="usb_cam" type="usb_cam_node" output="screen" >
    
    <!-- You may need to change the value of the video_device field,, refer to the document for more details -->
    <param name="video_device" value="/dev/video0" />
    <param name="camera_frame_id" value="usb_cam" />
    <param name="io_method" value="mmap"/>

<!--     ################################################################################
    Recommended settings, this leads to more accuracy in marker detection
    swscaler gives warning with pixel format of mjpeg, this can be safely ignored
    mjpeg is chosen due to hardware limitations
    ################################################################################ -->
    <param name="image_width"   value="1280" />
    <param name="image_height"  value="720" />
    <param name="pixel_format"  value="mjpeg" />
    <param name="framerate"     value = "55"/> 

<!--     ################################################################################
    Backup settings below, only use if you face have enough height of ceiling and arena is visible completely in the frame
    Comment the above settings and uncomment the below ones in that case
    You should not face any problems if you are using at least the recommended configuration given by us
    ################################################################################ 
     <param name="image_width" value="1920" />
    <param name="image_height" value="1080" />
    <param name="pixel_format" value="mjpeg" />
    <param name="framerate" value="60" /> -->
  </node>


  <!-- Node to display the output -->
  <node ns="usb_cam_display" name="image_view" pkg="image_view" type="image_view" output="screen">
    <remap from="image" to="/usb_cam/image_raw"/>
  </node>
</launch>
