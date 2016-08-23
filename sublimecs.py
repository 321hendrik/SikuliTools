import sublime
import sublime_plugin
import subprocess
import os
import time

sublime_version = 2

if not sublime.version() or int(sublime.version()) > 3000:
    sublime_version = 3

class CaptureSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        
        file_extension = 'png'
        timestamp = str(int(time.time()))
        curr_dir, curr_filename = os.path.split(self.view.file_name())
        image_path = os.path.join(curr_dir, timestamp + '.' + file_extension)
        
        subprocess.call('screencapture -s ' + image_path, shell=True)
        
        self.view.insert(edit, sel[0].begin(), "\"" + timestamp + ".png\"")


def plugin_loaded():
    pass


if sublime_version == 2:
    plugin_loaded()
