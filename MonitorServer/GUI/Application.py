####################################################################################################
# 
# MonitorServer - A Server Monitoring Application
# Copyright (C) 2014 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
####################################################################################################

####################################################################################################

import logging

from PyQt4 import QtCore, QtGui

####################################################################################################

from .GuiApplicationBase import GuiApplicationBase
from .Widgets.IconLoader import IconLoader
from MonitorServer.Application.ApplicationBase import ApplicationBase
from MonitorServer.Monitoring.HttpMonitoring import HttpMonitoring
import MonitorServer.Config.Config as Config

####################################################################################################

class Application(GuiApplicationBase, ApplicationBase):

    _logger = logging.getLogger(__name__)
    
    ###############################################
    
    def __init__(self, args):

        super(Application, self).__init__(args=args)
        self._logger.debug(str(args))

        self._icon_loader = IconLoader()
        
        from .MainWindow import MainWindow
        self._main_window = MainWindow()
        self._main_window.show()

        self._post_init_actions()
        self._init_tray_icon()
        self.post_init()
        self._init_monitoring()

    ##############################################

    def _init_actions(self):

        super(Application, self)._init_actions()

    ##############################################

    def _post_init_actions(self):

        self._restore_action = QtGui.QAction("&Restore",
                                             self._main_window,
                                             triggered=self._main_window.show,
                                             )

    ##############################################

    def _init_tray_icon(self):

        if QtGui.QSystemTrayIcon.isSystemTrayAvailable():
            menu = QtGui.QMenu(self._main_window)
            # menu.addAction(self.minimize_action)
            # menu.addAction(self.maximize_action)
            menu.addAction(self._restore_action)
            menu.addSeparator()
            menu.addAction(self.quit_action)
            
            icon = self._icon_loader.get_icon('applications-development-web', icon_size=32)
            
            self._tray_icon = QtGui.QSystemTrayIcon(icon, self._main_window)
            self._tray_icon.setContextMenu(menu)
            self._tray_icon.show()
        else:
            self._logger.info("System tray is not available")
            self._tray_icon = None
            # Fixme: exit

    ##############################################

    @property
    def tray_icon(self):
        return self._tray_icon

    ##############################################

    @property
    def icon_loader(self):
        return self._icon_loader

    ##############################################

    def _init_monitoring(self):

        self._monitoring = HttpMonitoring(Config.Monitoring.time_resolution)
        self._monitoring.service_down.connect(self.notify_for_event)
        self._monitoring.start()

    ##############################################

    def show_alert_message(self, title, message):

        self._tray_icon.showMessage(title, message, QtGui.QSystemTrayIcon.Critical)

    ##############################################

    def notify_for_event(self, message):

        self.show_alert_message('Warning', message)

####################################################################################################
#
# End
#
####################################################################################################
