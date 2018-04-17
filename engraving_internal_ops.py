# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/Ozbend_Engraving_Internal

import bpy
from .engraving_internal import EngravingInternal
from .engraving_internal import EngravingInternalOptions
import os
import sys
import argparse

class EngravingInternalStart(bpy.types.Operator):
    bl_idname = 'engravinginternal.start'
    bl_label = 'Start EngravingInternal'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # load options
        if bpy.data.filepath:
            EngravingInternalOptions.readfromfile(os.path.dirname(bpy.data.filepath))
            # correct options with command line arguments
            if '--' in sys.argv:
                argv = sys.argv[sys.argv.index('--') + 1:]  # all args after '--'
                parser = argparse.ArgumentParser()
                parser.add_argument('-sx', '--size_x', dest='size_x', type=int, required=False, help='Image X resolution')
                parser.add_argument('-sy', '--size_y', dest='size_y', type=int, required=False, help='Image Y resolution')
                parser.add_argument('-s', '--scale', dest='scale', type=float, required=False, help='Mesh scale')
                parser.add_argument('-sa', '--samples', dest='samples', type=int, required=False, help='Render samples')
                parser.add_argument('-p', '--path', dest='path', metavar='FILE', required=False, help='Dest path')
                parser.add_argument('-n', '--name', dest='name', type=str, required=False, help='Dest name')
                parser.add_argument('-g', '--gravi', dest='gravi', metavar='FILE', required=False, help='Gravi path')
                args = parser.parse_known_args(argv)[0]
                if EngravingInternalOptions.options:
                    if args.size_x is not None:
                        EngravingInternalOptions.options['resolution_x'] = args.size_x
                    if args.size_y is not None:
                        EngravingInternalOptions.options['resolution_y'] = args.size_y
                    if args.scale is not None:
                        EngravingInternalOptions.options['correction']['scale']['X'] = args.scale
                        EngravingInternalOptions.options['correction']['scale']['Y'] = args.scale
                        EngravingInternalOptions.options['correction']['scale']['Z'] = args.scale
                    if args.samples is not None:
                        EngravingInternalOptions.options['samples'] = args.samples
                    if args.path is not None:
                        EngravingInternalOptions.options['dest_dir'] = args.path
                    if args.name is not None:
                        EngravingInternalOptions.const_dest_name = args.name
                    if args.gravi is not None:
                        EngravingInternalOptions.const_gravi_name = args.gravi
        else:
            print('Options file mast be in the same directory with blend-file')
            return {'CANCELLED'}
        if EngravingInternalOptions.options:
            context.screen.scene.render.resolution_x = EngravingInternalOptions.options['resolution_x']
            context.screen.scene.render.resolution_y = EngravingInternalOptions.options['resolution_y']
            context.screen.scene.cycles.samples = EngravingInternalOptions.options['samples']
            # search for *.obj
            if EngravingInternalOptions.options['source_obj_dir'] and os.path.exists(EngravingInternalOptions.options['source_obj_dir']):
                EngravingInternalOptions.objlist = [file for file in os.listdir(EngravingInternalOptions.options['source_obj_dir']) if file.endswith('.obj')]
            # serch for cameras
            EngravingInternalOptions.cameraslist = [object for object in context.screen.scene.objects if object.type=='CAMERA']
            # search for materials
            EngravingInternalOptions.materialslist = [material for material in bpy.data.materials if material.use_fake_user]
            EngravingInternalOptions.materialslist_gem = [material for material in EngravingInternalOptions.materialslist if material.name[:EngravingInternalOptions.materialidtextlength] == EngravingInternalOptions.materialgemid]
            EngravingInternalOptions.materialslist_met = [material for material in EngravingInternalOptions.materialslist if material.name[:EngravingInternalOptions.materialidtextlength] == EngravingInternalOptions.materialmetid]
            # start processing obj by list
            print('-- STARTED --')
            EngravingInternal.processobjlist(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(EngravingInternalStart)


def unregister():
    bpy.utils.unregister_class(EngravingInternalStart)
