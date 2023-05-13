############################################# VIRTUAL ENVIRONMENT CREATION ##############################################################
## Install virtualenv package using pip
python3 -m pip install --user virtualenv
## Create a virutal Environment
python3 -m virtualenv YOLOV8_VENV # Already done
## Activate Virtaul Environment
source YOLOV8_VENV/bin/activate
## Install neccesary python modules
# Install OpenCV
# Install Tensorflow
# Install pytorch

pip install ultralytics # YOLOv8

############################ Installing Dependencies (Not mentioned in the video lecture ) #######################################

mkdir -p ~/.gazebo/models
sudo apt install -y python3-colcon-common-extensions
sudo apt install -y ros-foxy-gazebo-ros-pkgs

############################################# BUILDING THE PROJECT ######################################################################
## You should create a workspace and bring the project
## Bring all models into your .gazebo/models
cp -r delivery_robot_pkg/models/* ~/.gazebo/models
## Notify Colcon to ignore YOLOV8_VENV while build
touch YOLOV8_VENV/COLCON_IGNORE
## Build repo
colcon build

############################################# RUNNING THE PROJECT #######################################################################

>>>>>>> Open A new Terminal <<<<<<<<

## Activate Environment
source YOLOV8_VENV/bin/activate
## Source *your Workspace* in any terminal you open to Run files from this workspace
source ~/ROS2/delivery_robot_ws/install/setup.bash # workspace sourcing
source /opt/ros/foxy/setup.bash

## once build you can run the simulation e.g [ ros2 launch (package_name) world(launch file) ] 
ros2 launch delivery_robot_pkg world_gazebo.launch.py
