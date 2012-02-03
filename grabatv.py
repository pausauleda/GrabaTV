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
		
    def on_buttonAnadirPrograma_clicked(self, widget):
		os.system("crontab -l > /tmp/grabatvcrontab.txt")
		fcrontab = open("/tmp/grabatvcrontab.txt","a")
		fcrontab.write(self.glade.get_widget("entryIniMin").get_text())
		fcrontab.write(" ")
		fcrontab.write(self.glade.get_widget("entryIniHora").get_text())
		fcrontab.write(" * * ")
		fcrontab.write(self.glade.get_widget("entryIniDia").get_text())
		fcrontab.write(" /usr/share/grabatv/sh/grabatv.grabar.sh\n")
		fcrontab.write(self.glade.get_widget("entryFinMin").get_text())
		fcrontab.write(" ")
		fcrontab.write(self.glade.get_widget("entryFinHora").get_text())
		fcrontab.write(" * * ")
		fcrontab.write(self.glade.get_widget("entryFinDia").get_text())
		if self.glade.get_widget("checkbuttonApagar").get_active():
			fcrontab.write(" /usr/share/grabatv/sh/grabatv.stopshut.sh\n")
		else:
			fcrontab.write(" /usr/share/grabatv/sh/grabatv.stop.sh\n")
		fcrontab.close()
		os.system("crontab /tmp/grabatvcrontab.txt")

    def on_buttonBorrarPrograma_clicked(self, widget):
		os.system("crontab -l > /tmp/grabatvcrontab.txt")
		os.system("sed -i '/'grabatv'/d' /tmp/grabatvcrontab.txt")
		os.system("crontab /tmp/grabatvcrontab.txt")
		
 
if __name__ == "__main__":
    try:
        aplic = AppGrabatv()
        gtk.main()
    except KeyboardInterrupt:
        pass

