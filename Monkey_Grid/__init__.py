# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Monkey Grid",
    "author" : "Goodluck Focus",
    "description" : "Add Grids Of Monkeys",
    "blender" : (2, 82, 0),
    "version" : (1, 0, 0),
    "location" : "Operator Search",
    "warning" : "",
    "category" : "Mesh"
}

import bpy

class MESH_OT_monkey_grid(bpy.types.Operator):
    """Lets Spread Some Joy"""
    bl_idname = "mesh.monkey_grid"
    bl_label = "Monkey Grid"
    bl_options={'REGISTER', 'UNDO'}
    
    count_x: bpy.props.IntProperty(
        name="X",
        description="Number of Monkeys in the X-direction",
        default=2,
        min=1, soft_max=10)
    
    count_y: bpy.props.IntProperty(
        name="Y",
        description="Number of Monkeys in the Y-direction",
        default=2,
        min=1, soft_max=10)
   
    size: bpy.props.FloatProperty(
        name="Size",
        description="Size of Each Monkey",
        default=0.2,
        min=0, soft_max=1) 
    
    @classmethod
    def poll(cls,context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        for idx in range(self.count_x * self.count_y):
            x = idx % self.count_x
            y = idx // self.count_y
            bpy.ops.mesh.primitive_monkey_add(
                size = self.size,
                location = (x,y,1))
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(MESH_OT_monkey_grid)

def unregister():
    bpy.utils.unregister_class(MESH_OT_monkey_grid)