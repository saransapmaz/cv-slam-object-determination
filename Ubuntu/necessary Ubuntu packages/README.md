### Missing Navigation Packages

Please, copy and paste that command line in terminal to have navigation package. Ensure to have the file outside of your workspace.

    git clone -b kinetic-devel https://github.com/ros-planning/navigation/tree/kinetic-devel
    
Then, copy the files into your ~/catkin_ws/src:

1) base_local_planner
2) clear_costmap_recovery
3) costmap_2d
4) move_base
5) nav_core
6) navfn
7) rotate_recovery
8) voxel_grid

Finally, run "catkin_make" for ~/catkin_ws
