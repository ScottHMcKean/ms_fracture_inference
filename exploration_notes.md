- install porepy via github (dev version)
https://github.com/pmgbergen/porepy

- install paraview via ubuntu
sudo apt update
sudo apt install paraview

- install robust point in polyhedron for meshing
wget https://raw.githubusercontent.com/keileg/polyhedron/master/polyhedron.py
mkdir poly
mv polyhedron.py poly/robust_point_in_polyhedron.py
conda develop poly