import numpy as np
import trimesh


def inverse_matrix(m):
    m_np = np.array(m)
    m_np_inv = np.linalg.inv(m_np)
    return m_np_inv


### IO
input_stl = '_stl/plate.stl'

# output_stl = input_stl[:-4] + '_result.stl'
# print(output_stl)

output_0_stl = input_stl[:-4] + '_result_0.stl'
output_1_stl = input_stl[:-4] + '_result_1.stl'


### load a file by name or from a buffer
mesh_src = trimesh.load_mesh(input_stl)
# mesh.show()


### Calc BoundingBox
mat, whd = trimesh.bounds.oriented_bounds(mesh_src)
mat_inv = inverse_matrix(mat)
w, h, d = whd


# print(mat)
# print(mat_inv)
print("whd : {}".format(whd))



sc = 0.98
sc_inv = 1.0/sc

sc_not = 0.8

if np.argmin(whd) == 0:
    # print("Pattern : X")
    whd = [
            w * sc,
            h * sc_not,
            d * sc_not
        ]

elif np.argmin(whd) == 1:
    # print("Pattern : Y")
    whd = [
            w * sc_not,
            h * sc,
            d * sc_not
        ]

elif np.argmin(whd) == 2:
    # print("Pattern : Z")
    whd = [
            w * sc_not,
            h * sc_not,
            d * sc
        ]



### Add New Box
bbox = trimesh.creation.box(whd, mat_inv)
bbox.export(output_0_stl)


### Mesh Boolean
trimed = trimesh.boolean.difference([bbox, mesh_src])
trimed.export(output_1_stl)


### Blender-Env Check
# print(trimesh.interfaces.blender.exists)
