#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2012 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys, traceback

import Ice
Ice.loadSlice('TestAMD.ice')
import Test

class InitialI(Test.Initial):

    def shutdown_async(self, cb, current=None):
        current.adapter.getCommunicator().shutdown()
        cb.ice_response()

    def pingPong_async(self, cb, o, current=None):
        cb.ice_response(o)

    def opOptionalException_async(self, cb, a, b, o, current=None):
        cb.ice_exception(Test.OptionalException(a, b, o))

    def opDerivedException_async(self, cb, a, b, o, current=None):
        cb.ice_exception(Test.DerivedException(a, b, o, b, o))

    def opRequiredException_async(self, cb, a, b, o, current=None):
        if b == Ice.Unset:
            ss = "none"
        else:
            ss = b
        if o == Ice.Unset:
            o2 = None
        else:
            o2 = o
        cb.ice_exception(Test.RequiredException(a, b, o, ss, o2))

    def opByte_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opBool_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opShort_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opInt_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opLong_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opFloat_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opDouble_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opString_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opMyEnum_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opSmallStruct_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opFixedStruct_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opVarStruct_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opOneOptional_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opOneOptionalProxy_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opByteSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opBoolSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opShortSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opIntSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opLongSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opFloatSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opDoubleSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opStringSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opSmallStructSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opSmallStructList_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opFixedStructSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opFixedStructList_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opVarStructSeq_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opIntIntDict_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opStringIntDict_async(self, cb, p1, current=None):
        cb.ice_response(p1, p1)

    def opClassAndUnknownOptional_async(self, cb, p, current=None):
        cb.ice_response()

def run(args, communicator):
    communicator.getProperties().setProperty("TestAdapter.Endpoints", "default -p 12010:udp")
    adapter = communicator.createObjectAdapter("TestAdapter")
    initial = InitialI()
    adapter.add(initial, communicator.stringToIdentity("initial"))
    adapter.activate()

    communicator.waitForShutdown()
    return True

try:
    communicator = Ice.initialize(sys.argv)
    status = run(sys.argv, communicator)
except:
    traceback.print_exc()
    status = False

if communicator:
    try:
        communicator.destroy()
    except:
        traceback.print_exc()
        status = False

sys.exit(not status)
