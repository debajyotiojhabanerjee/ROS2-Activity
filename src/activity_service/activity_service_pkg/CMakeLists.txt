cmake_minimum_required(VERSION 3.8)
project(activity_service_pkg)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/ActivityCheck.srv"
)

install(
  PROGRAMS
    scripts/activity_server.py
    scripts/activity_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
