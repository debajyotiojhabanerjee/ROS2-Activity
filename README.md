# ROS 2 Activity Service

A ROS 2 (Humble) package demonstrating a custom service that counts how many times it has been called since the node started.

## Package: `activity_service_pkg`

### Custom Service: `ActivityCheck.srv`
- **Request:** empty  
- **Response:** `string message`

### Nodes
| Node | Role |
|------|------|
| `activity_server.py` | Advertises `/check_activity`, counts calls, responds with counter |
| `activity_client.py` | Sends one request and prints the server reply |

## Build & Run

```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_ws
colcon build --packages-select activity_service_pkg
source install/setup.bash
```

**Terminal 1:**
```bash
ros2 run activity_service_pkg activity_server.py
```

**Terminal 2:**
```bash
ros2 run activity_service_pkg activity_client.py
```



## 📁 Project Resources

A detailed project report, demo video, and presentation slides are available here:

🔗 [View Project Drive Folder]([https://drive.google.com/drive/folders/YOUR_FOLDER_ID_HERE](https://drive.google.com/file/d/1TsPNP0Fy6CXUZQLP5DzrkYrlOTOlJWj8/view?usp=sharing))
