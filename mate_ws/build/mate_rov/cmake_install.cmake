# Install script for directory: /home/yonahel/MATE_ROV/mate_ws/src/mate_rov

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/yonahel/MATE_ROV/mate_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mate_rov/msg" TYPE FILE FILES
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg"
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mate_rov/cmake" TYPE FILE FILES "/home/yonahel/MATE_ROV/mate_ws/build/mate_rov/catkin_generated/installspace/mate_rov-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/yonahel/MATE_ROV/mate_ws/devel/include/mate_rov")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/yonahel/MATE_ROV/mate_ws/devel/share/common-lisp/ros/mate_rov")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/home/yonahel/miniconda3/bin/python" -m compileall "/home/yonahel/MATE_ROV/mate_ws/devel/lib/python3/dist-packages/mate_rov")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/yonahel/MATE_ROV/mate_ws/devel/lib/python3/dist-packages/mate_rov")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/yonahel/MATE_ROV/mate_ws/build/mate_rov/catkin_generated/installspace/mate_rov.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mate_rov/cmake" TYPE FILE FILES "/home/yonahel/MATE_ROV/mate_ws/build/mate_rov/catkin_generated/installspace/mate_rov-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mate_rov/cmake" TYPE FILE FILES
    "/home/yonahel/MATE_ROV/mate_ws/build/mate_rov/catkin_generated/installspace/mate_rovConfig.cmake"
    "/home/yonahel/MATE_ROV/mate_ws/build/mate_rov/catkin_generated/installspace/mate_rovConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mate_rov" TYPE FILE FILES "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/mate_rov" TYPE PROGRAM FILES
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/scripts/motor/py"
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/scripts/pid.py"
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/scripts/sensor.py"
    "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/scripts/server.py"
    )
endif()

