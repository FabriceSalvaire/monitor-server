# -*- coding: utf-8 -*-

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

import subprocess

from PyQt4 import QtCore, QtGui

####################################################################################################

from .MainWindowBase import MainWindowBase
# from .Pages.Page import PageMetaClass

from MonitorServer.Monitoring import OvhApi

####################################################################################################

class MainWindow(MainWindowBase):

    ##############################################

    def __init__(self):

        super(MainWindow, self).__init__(title='MonitorServer')

        self._init_action()
        self._init_ui()

    ##############################################

    def init_menu(self):

        super(MainWindow, self).init_menu()

    ##############################################

    def _init_action(self):

        pass

    ##############################################

    def _init_ui(self):

        central_widget = QtGui.QWidget(self)
        self.setCentralWidget(central_widget)

        self._form_layout = QtGui.QFormLayout(central_widget)
        server_label = QtGui.QLabel('Server', central_widget)
        self._form_layout.setWidget(0, QtGui.QFormLayout.LabelRole, server_label)
        self._server_label = QtGui.QLabel(central_widget)
        self._form_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self._server_label)
        ip_label = QtGui.QLabel('IP', central_widget)
        self._form_layout.setWidget(1, QtGui.QFormLayout.LabelRole, ip_label)
        self._ip_label = QtGui.QLabel(central_widget)
        self._form_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self._ip_label)

        vertical_layout = QtGui.QVBoxLayout()
        self._start_button = QtGui.QPushButton('Start', central_widget)
        vertical_layout.addWidget(self._start_button)
        self._reboot_button = QtGui.QPushButton('Reboot', central_widget)
        vertical_layout.addWidget(self._reboot_button)
        self._stop_button = QtGui.QPushButton('Stop', central_widget)
        vertical_layout.addWidget(self._stop_button)
        self._kvm_button = QtGui.QPushButton('KVM', central_widget)
        vertical_layout.addWidget(self._kvm_button)
        self._form_layout.setLayout(2, QtGui.QFormLayout.FieldRole, vertical_layout)

        self._load_information()
        self._start_button.clicked.connect(self._start_vps)
        self._reboot_button.clicked.connect(self._reboot_vps)
        self._stop_button.clicked.connect(self._stop_vps)
        self._kvm_button.clicked.connect(self._start_kvm)

        self._translate_ui()

    ##############################################

    def _translate_ui(self):

        pass
        # self.foo.setText(self.translate("..."))

    ##############################################

    def closeEvent(self, event=None):

        tray_icon = self._application.tray_icon
        if tray_icon is not None and tray_icon.isVisible():
            # Fixme: Config.Title
            # QtGui.QMessageBox.information(self, "Monitor Server",
            #                               "The program will keep running in the system tray. To "
            #                               "terminate the program, choose <b>Quit</b> in the "
            #                               "context menu of the system tray entry.")
            self.hide()
            if event is not None:
                event.ignore()
        else:
            self._application.exit()

    ##############################################

    def _load_information(self):

        self._client = OvhApi.Client()
        services = self._client.get_vps()
        self._server_name = services[0]
        self._server_label.setText(self._server_name)
        self._ip_label.setText('\n'.join(self._client.get_vps(self._server_name, 'ips')))

    ##############################################

    def _start_vps(self):
        return self._vps_action('start')

    ##############################################

    def _reboot_vps(self):
        return self._vps_action('reboot')

    ##############################################

    def _stop_vps(self):
        return self._vps_action('stop')

    ##############################################

    def _vps_action(self, action):

        choice = QtGui.QMessageBox.warning(self,
                                           '', 'Do you want to {} {}'.format(action, self._server_name),
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            self._client.post_vps(self._server_name, action)

    ##############################################

    def _start_kvm(self):

        data = self._client.post_vps(self._server_name, 'openConsoleAccess', protocol='VNC')
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(data['password'], QtGui.QClipboard.Selection)
        self._process = subprocess.Popen(('vncviewer', data['host']))

####################################################################################################
#
# End
#
####################################################################################################
