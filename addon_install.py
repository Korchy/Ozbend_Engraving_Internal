# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/Ozbend_Engraving_Internal
#
# Add-on installation script
#
# console command to install: blender -b -P addon_install.py

import bpy
import sys
import argparse

__addon_name = 'Engraving_Internal'

if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]  # all args after '--'
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='source', metavar='FILE')
    args = parser.parse_known_args(argv)

    # remove
    if __addon_name in bpy.context.user_preferences.addons:
        bpy.ops.wm.addon_disable(module=__addon_name)
        bpy.ops.wm.addon_remove(module=__addon_name)
        # remove from memory
        for module in list(sys.modules.keys()):
            if hasattr(sys.modules[module], '__package__'):
                if sys.modules[module].__package__ == __addon_name:
                    del sys.modules[module]

    # install
    bpy.ops.wm.addon_install(filepath=args.source, overwrite=True)
    bpy.ops.wm.addon_enable(module=__addon_name)
    # save user settings
    bpy.ops.wm.save_userpref()
