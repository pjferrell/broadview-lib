# (C) Copyright Broadcom Corporation 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from agentapi import AgentAPI
from broadview_lib.config.broadviewconfig import BroadViewBSTSwitches
import unittest

class GetSwitchProperties(AgentAPI):
    def __init__(self, host, port):
        super(GetSwitchProperties, self).__init__()
        self.setFeature("")
        self.setHttpMethod("POST")
        self.setHost(host)
        self.setPort(port)
        self.__asic_id = "1"
        self.__json = None

    def setASIC(self, val):
        self.__asic_id = val

    def toDict(self):
        ret = {}
        params = {}
        ret["asic-id"] = self.__asic_id
        ret["params"] = params
        ret["method"] = "get-switch-properties"
        return ret

    def getJSON(self):
        return self.__json

    def send(self, timeout=30):
        status, json = self._send(self.toDict(), timeout)
        if status == 200:
            self.__version = json["version"]
            res = json["result"]
            self.__json = res
        return status

class GetSystemFeature(AgentAPI):
    def __init__(self, host, port):
        super(GetSystemFeature, self).__init__()
        self.setFeature("")
        self.setHttpMethod("POST")
        self.setHost(host)
        self.setPort(port)
        self.__asic_id = "1"
        self.__json = None

    def setASIC(self, val):
        self.__asic_id = val

    def toDict(self):
        ret = {}
        params = {}
        ret["asic-id"] = self.__asic_id
        ret["params"] = params
        ret["method"] = "get-system-feature"
        return ret

    def getJSON(self):
        return self.__json

    def send(self, timeout=30):
        status, json = self._send(self.toDict(), timeout)
        if status == 200:
            self.__version = json["version"]
            res = json["result"]
            self.__json = res
        return status

class ConfigureSystemFeature(AgentAPI):
    def __init__(self, host, port):
        super(ConfigureSystemFeature, self).__init__()
        self.setFeature("")
        self.setHttpMethod("POST")
        self.setHost(host)
        self.setPort(port)
        self.__asic_id = "1"
        self.__json = None
        self.__heartbeatEnable = False
        self.__msgInterval = 30

    def setASIC(self, val):
        self.__asic_id = val

    def setHeartbeatEnable(self, val):
        self.__heartbeatEnable = val

    def setMsgInterval(self, val):
        self.__msgInterval = val

    def toDict(self):
        ret = {}
        params = {}
        params["heartbeat-enable"] = 1 if self.__heartbeatEnable else 0  
        params["msg-interval"] = self.__msgInterval 
        ret["asic-id"] = self.__asic_id
        ret["params"] = params
        ret["method"] = "configure-system-feature"
        return ret

    def getJSON(self):
        return self.__json

    def send(self, timeout=30):
        status, json = self._send(self.toDict(), timeout)
        if status == 200:
            self.__version = json["version"]
            res = json["result"]
            self.__json = res
        return status

class CancelRequest(AgentAPI):
    def __init__(self, host, port):
        super(CancelRequest, self).__init__()
        self.setFeature("")
        self.setHttpMethod("POST")
        self.setHost(host)
        self.setPort(port)
        self.__asic_id = "1"
        self.__json = None
        self.__requestId = None

    def setASIC(self, val):
        self.__asic_id = val

    def setRequestId(self, val):
        self.__requestId = val

    def toDict(self):
        ret = {}
        params = {}
        params["request-id"] = self.__requestId
        ret["asic-id"] = self.__asic_id
        ret["params"] = params
        ret["method"] = "cancel-request"
        return ret

    def getJSON(self):
        return self.__json

    def send(self, timeout=30):
        status, json = self._send(self.toDict(), timeout)
        if status == 200:
            self.__version = json["version"]
            res = json["result"]
            self.__json = res
        return status

class TestTAPIParams(unittest.TestCase):

    def setUp(self):
        pass

    def test_GetSwitchProperties(self):

        sw = BroadViewBSTSwitches()
        if len(sw):
            for x in sw:
                host = x["ip"]
                port = x["port"]
                break
        else:
            host = "192.168.3.1"
            port = 8080

        x = GetSwitchProperties(host, port)
        d = x.toDict()
        self.assertTrue("asic-id" in d)
        self.assertTrue("params" in d)
        self.assertTrue("method" in d)
        self.assertTrue(x.getFeature() == "")
        self.assertTrue(x.getHttpMethod() == "POST")
        self.assertTrue(x.getHost() == host)
        self.assertTrue(x.getPort() == port)
        self.assertTrue(d["asic-id"] == "1")
        self.assertTrue(d["method"] == "get-switch-properties")

    def test_GetSystemFeature(self):

        sw = BroadViewBSTSwitches()
        if len(sw):
            for x in sw:
                host = x["ip"]
                port = x["port"]
                break
        else:
            host = "192.168.3.1"
            port = 8080

        x = GetSystemFeature(host, port)
        d = x.toDict()
        self.assertTrue("asic-id" in d)
        self.assertTrue("params" in d)
        self.assertTrue("method" in d)
        self.assertTrue(x.getFeature() == "")
        self.assertTrue(x.getHttpMethod() == "POST")
        self.assertTrue(x.getHost() == host)
        self.assertTrue(x.getPort() == port)
        self.assertTrue(d["asic-id"] == "1")
        self.assertTrue(d["method"] == "get-system-feature")

    def test_ConfigureSystemFeature(self):

        sw = BroadViewBSTSwitches()
        if len(sw):
            for x in sw:
                host = x["ip"]
                port = x["port"]
                break
        else:
            host = "192.168.3.1"
            port = 8080

        x = ConfigureSystemFeature(host, port)
        x.setHeartbeatEnable(False)
        x.setMsgInterval(10)
        d = x.toDict()
        self.assertTrue("asic-id" in d)
        self.assertTrue("params" in d)
        self.assertTrue(d["params"]["msg-interval"] == 10)
        self.assertTrue(d["params"]["heartbeat-enable"] == 0)
        self.assertTrue("method" in d)
        self.assertTrue(x.getFeature() == "")
        self.assertTrue(x.getHttpMethod() == "POST")
        self.assertTrue(x.getHost() == host)
        self.assertTrue(x.getPort() == port)
        self.assertTrue(d["asic-id"] == "1")
        self.assertTrue(d["method"] == "configure-system-feature")

    def test_CancelRequest(self):

        sw = BroadViewBSTSwitches()
        if len(sw):
            for x in sw:
                host = x["ip"]
                port = x["port"]
                break
        else:
            host = "192.168.3.1"
            port = 8080

        x = CancelRequest(host, port)
        x.setRequestId(2)
        d = x.toDict()
        self.assertTrue("asic-id" in d)
        self.assertTrue("params" in d)
        self.assertTrue(d["params"]["request-id"] == 2)
        self.assertTrue("method" in d)
        self.assertTrue(x.getFeature() == "")
        self.assertTrue(x.getHttpMethod() == "POST")
        self.assertTrue(x.getHost() == host)
        self.assertTrue(x.getPort() == port)
        self.assertTrue(d["asic-id"] == "1")
        self.assertTrue(d["method"] == "cancel-request")

if __name__ == "__main__":
    unittest.main()
