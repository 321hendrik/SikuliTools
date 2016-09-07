import sublime
import sublime_plugin
import subprocess
import os
import time

sublime_version = 2

if not sublime.version() or int(sublime.version()) > 3000:
    sublime_version = 3

class CaptureSelectionCommand(sublime_plugin.WindowCommand):
    """show an input panel to ask for filename, capture image, save it and insert at cursor"""
    def run(self):
        self.window.show_input_panel("file name for capture", "", self.save_file, None, None)
    
    def save_file(self, file_name):
        """capture image from screen and save to given filename"""
        file_extension = 'png'
        
        # use timestamp as filename if no is given
        if not file_name:
            file_name = str(int(time.time()))
        
        # add extension
        full_file_name = file_name + '.' + file_extension
        
        # get currently active view
        active_view = self.window.active_view()
        
        # extract current directory from file in active view
        curr_dir, curr_filename = os.path.split(active_view.file_name())
        
        # contruct image save path
        image_path = os.path.join(curr_dir, full_file_name)
        
        # screen capture and save file
        subprocess.check_call('screencapture -s ' + image_path, shell=True)
        
        # insert filename at cursor
        active_view.run_command("capture_selection_second", { "argument" : full_file_name});


class CaptureSelectionSecondCommand(sublime_plugin.TextCommand):
    """insert filename at current cursor position"""
    def run(self, edit, argument):
        sel = self.view.sel()
        self.view.insert(edit, sel[0].begin(), "\"" + argument + "\"")

def plugin_loaded():
    pass


if sublime_version == 2:
    plugin_loaded()
