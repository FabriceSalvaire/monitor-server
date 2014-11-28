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
from urllib2 import urlopen

from PyQt4 import QtCore

####################################################################################################

from MonitorServer.Tools.SleepThread import SleepThread

####################################################################################################

_module_logger = logging.getLogger(__name__)

####################################################################################################

class HttpMonitoring(SleepThread, QtCore.QObject):

    _logger = _module_logger.getChild('HttpMonitoring')

    service_down = QtCore.pyqtSignal(str)

    ##############################################

    def __init__(self, time_resolution):

        SleepThread.__init__(self, sleep_time=time_resolution)
        QtCore.QObject.__init__(self)

        self.daemon = True

    ##############################################

    def _network_is_up(self, probe_url='http://www.google.com'):

        try:
            probe_url = 'http://ovh-vps'
            data = urlopen(probe_url).read()
            return True
        except:
            self._logger.info('Network is down')
            return False

    ##############################################

    def work(self):

        if self._network_is_up():
            probe_url = 'http://ovh-vps'
            try:
                data = urlopen(probe_url).read()
                # Test for content
                self._logger.info('%s is up', probe_url)
            except:
                message = '{} is down'.format(probe_url)
                self._logger.warning(message)
                self.service_down.emit(message)
        else:
            pass   
            # self.service_down.emit('Network is down')

####################################################################################################
# 
# End
# 
####################################################################################################
