#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import os, time
 
class AppGrabatv:
 
    def __init__(self):
        self.glade = gtk.glade.XML("glade/grabatv.glade")
        self.glade.signal_autoconnect(self)
        self.glade.get_widget("windowGrabatv").show_all()
 
    def on_windowGrabatv_delete_event(self, widget, event):
        gtk.main_quit()
 
    def on_buttonVer_clicked(self, widget):
		os.system("./sh/grabatv.ver.sh")
        
    def on_buttonGrabar_clicked(self, widget):
		self.glade.get_widget("buttonVer").hide()
		self.glade.get_widget("buttonGrabar").hide()
		self.glade.get_widget("labelEstado").set_text("GRABANDO")
		os.system("./sh/grabatv.grabar.sh")
        
    def on_buttonStop_clicked(self, widget):
		self.glade.get_widget("labelEstado").set_text("---")
		self.glade.get_widget("buttonVer").show()
		self.glade.get_widget("buttonGrabar").show()
		os.system("./sh/grabatv.stop.sh")
		time.sleep(3)
 
if __name__ == "__main__":
    try:
        aplic = AppGrabatv()
        gtk.main()
    except KeyboardInterrupt:
        pass

