"""Smartcard module exceptions.

This module defines the exceptions raised by the smartcard module.

__author__ = "http://www.gemalto.com"

Copyright 2001-2009 gemalto
Author: Jean-Daniel Aussel, mailto:jean-daniel.aussel@gemalto.com

This file is part of pyscard.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

class SmartcardException:
    """Base class for smartcard exceptions.

    smartcard exceptions are generated by the smartcard module and
    shield scard (i.e. PCSC) exceptions raised by the scard module.

    """
    def __init__( self, message="" ):
        self.message = message
    def __str__(self):
        return repr( 'Smartcard Exception: ' + self.message + '!' )

class CardConnectionException(SmartcardException):
    """Raised when a CardConnection class method fails."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, message )

class CardRequestException(SmartcardException):
    """Raised when a CardRequest wait fails."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, message )

class CardRequestTimeoutException(SmartcardException):
    """Raised when a CardRequest times out."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, "Time-out during card request" )

class CardServiceException(SmartcardException):
    """Raised when a CardService class method fails."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, message )

class InvalidATRMaskLengthException(SmartcardException):
    """Raised when an ATR mask does not match an ATR length."""
    def __init__( self, mask="" ):
        SmartcardException.__init__( self, 'Invalid ATR mask length: ' + mask )

class InvalidReaderException(SmartcardException):
    """Raised when trying to acces an invalid smartcard reader."""
    def __init__( self, readername="" ):
        SmartcardException.__init__( self, 'Invalid reader: ' + readername )

class ListReadersException(SmartcardException):
    """Raised when smartcard readers cannot be listed."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, 'failed to list readers' )

class NoCardException(SmartcardException):
    """Raised when no card in is present in reader."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, 'Unable to connect to card or no card in reader' )

class NoReadersException(SmartcardException):
    """Raised when the system has no smartcard reader."""
    def __init__( self, message="" ):
        SmartcardException.__init__( self, 'no readers found' )
