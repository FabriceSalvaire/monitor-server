# -*- coding: utf-8 -*-

####################################################################################################

import json

####################################################################################################

import ovh

####################################################################################################

def to_url(*args, **kwargs):

    url = u'/' + u'/'.join([unicode(x) for x in args])
    # note: API supports kwargs
    if kwargs:
        url += u'/?' + u'&'.join([u'{}={}'.format(key, value)
                                  for key, value in kwargs.iteritems()])
    return url

####################################################################################################

def dump_json(obj):
    print json.dumps(obj, indent=2, sort_keys=True)

####################################################################################################

periods = ('today', 'lastday', 'lastweek', 'lastmonth', 'lastyear')
types = ('cpu:iowait', 'cpu:max', 'cpu:nice', 'cpu:sys', 'cpu:used', 'cpu:user',
         'mem:max', 'mem:used',
         'net:rx', 'net:tx')

####################################################################################################

class Client(ovh.Client):

    ##############################################

    def sget(self, *args, **kwargs):

        url = to_url(*args, **kwargs)
        print 'GET:', url
        return self.get(url) # super(Client, self)

    ##############################################

    def spost(self, *args, **kwargs):

        url = to_url(*args, **kwargs)
        print 'POST:', url
        return self.post(url) # super(Client, self)

    ##############################################

    def get_vps(self, *args, **kwargs):
        return self.sget('vps', *args, **kwargs)

    ##############################################

    def post_vps(self, *args, **kwargs):
        return self.spost('vps', *args, **kwargs)

####################################################################################################
# 
# End
# 
####################################################################################################
