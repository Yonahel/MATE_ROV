# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mate_rov: 2 messages, 0 services")

set(MSG_I_FLAGS "-Imate_rov:/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mate_rov_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg" NAME_WE)
add_custom_target(_mate_rov_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mate_rov" "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg" ""
)

get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg" NAME_WE)
add_custom_target(_mate_rov_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mate_rov" "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mate_rov
)
_generate_msg_cpp(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mate_rov
)

### Generating Services

### Generating Module File
_generate_module_cpp(mate_rov
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mate_rov
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mate_rov_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mate_rov_generate_messages mate_rov_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_cpp _mate_rov_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_cpp _mate_rov_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mate_rov_gencpp)
add_dependencies(mate_rov_gencpp mate_rov_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mate_rov_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mate_rov
)
_generate_msg_lisp(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mate_rov
)

### Generating Services

### Generating Module File
_generate_module_lisp(mate_rov
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mate_rov
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mate_rov_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mate_rov_generate_messages mate_rov_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_lisp _mate_rov_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_lisp _mate_rov_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mate_rov_genlisp)
add_dependencies(mate_rov_genlisp mate_rov_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mate_rov_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov
)
_generate_msg_py(mate_rov
  "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov
)

### Generating Services

### Generating Module File
_generate_module_py(mate_rov
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mate_rov_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mate_rov_generate_messages mate_rov_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/imu.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_py _mate_rov_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yonahel/MATE_ROV/mate_ws/src/mate_rov/msg/motor.msg" NAME_WE)
add_dependencies(mate_rov_generate_messages_py _mate_rov_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mate_rov_genpy)
add_dependencies(mate_rov_genpy mate_rov_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mate_rov_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mate_rov)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mate_rov
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(mate_rov_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mate_rov)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mate_rov
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(mate_rov_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov)
  install(CODE "execute_process(COMMAND \"/home/yonahel/miniconda3/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mate_rov
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(mate_rov_generate_messages_py std_msgs_generate_messages_py)
endif()
