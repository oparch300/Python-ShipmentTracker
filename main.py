# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:40:23 2020

@author: Ani
"""

from decimal import Decimal
from logging import getLogger
from re import compile
from suds import WebFault
from suds.bindings.document import Document
from suds.client import Client
from suds.plugin import MessagePlugin
from suds.sax.element import Element
from suds.sudsobject import asdict
from suds.xsd.sxbase import XBuiltin
from suds.xsd.sxbuiltin import Factory


PATTERN_HEX = r"[0-9a-fA-F]"
PATTERN_ID = r"{hex}{{8}}-{hex}{{4}}-{hex}{{4}}-{hex}{{4}}-{hex}{{12}}".format(
    hex=PATTERN_HEX)
RE_TRANSACTION_ID = compile(PATTERN_ID)


class BaseService(object):
    def call(self, method, **kwargs):
        """Call the given web service method.
        :param method: The name of the web service operation to call.
        :param kwargs: Method keyword-argument parameters.
        """
        self.logger.debug("%s(%s)", method, kwargs)
        instance = getattr(self.client.service, method)

        try:
            ret_val = instance(**kwargs)
        except WebFault as error:
            self.logger.warning("Retry %s", method, exc_info=True)
            self.plugin.authenticator = None

            try:  # retry with a re-authenticated user.
                ret_val = instance(**kwargs)
            except WebFault as error:
                self.logger.exception("%s retry failed", method)
                self.plugin.authenticator = None
                raise error     
        return ret_val
        
def get_tracking(self, transaction_id):
        """Get tracking events for a shipment.
        :param transaction_id: The transaction ID (or tracking number) returned
            by :meth:`get_label`.
        """
        if RE_TRANSACTION_ID.match(transaction_id):
            arguments = dict(StampsTxID=transaction_id)
        else:
            arguments = dict(TrackingNumber=transaction_id)

        return self.call("TrackShipment", **arguments)


import sys
sys.path.insert(1,'E:/ShipmentTracker')