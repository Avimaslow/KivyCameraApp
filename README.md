DESCRIPTION
-----------
The camera screen, enabled by Kivy's Camera widget, allows users to start and stop the camera, and capture images. This functionality is facilitated through a 
straightforward and interactive GUI, with buttons to control camera actions. Once an image is captured, it's saved with a timestamp, enhancing file management.
Transitioning to the image screen, users can generate shareable links for their captured images. This is achieved using a custom Fileshare class, possibly integrating
file sharing services. The app also includes clipboard functionality to copy the generated link, and a web browser integration to open the link directly from the app.
The project, aimed at photographers, tech enthusiasts, or anyone interested in GUI development with Python, demonstrates the versatility of Kivy in creating cross-platform
applications. Its simplicity caters to beginners, while the integration of file sharing and web functionalities shows potential for expansion into more complex applications.

How to Use
----------
Starting the Camera:
First launch the app and navigate to the Camera Screen.
then click the 'Start Camera' button to start the camera.
Capturing an Image:
Once the camera is active, take your beautiful shot. Do this by -
Clicking the 'Capture' button to take a photo.
The image is automatically saved with a timestamp in the designated folder.
Generating and Using Shareable Links:
After capturing, switch to the Image Screen.
Click 'Create Shareable Link' to generate a URL for your image.
Use the 'Copy Link' button to copy the URL to your clipboard.
To view the image in your browser, click 'Open Link'.
Stopping the Camera:
Return to the Camera Screen and click 'Stop Camera' to turn it off.
