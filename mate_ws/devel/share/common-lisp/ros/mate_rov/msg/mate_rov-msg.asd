
(cl:in-package :asdf)

(defsystem "mate_rov-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "motor" :depends-on ("_package_motor"))
    (:file "_package_motor" :depends-on ("_package"))
    (:file "imu" :depends-on ("_package_imu"))
    (:file "_package_imu" :depends-on ("_package"))
  ))