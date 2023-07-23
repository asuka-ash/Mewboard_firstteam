class Config:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._addr = (host, port)

    @property
    def host(self):
        return self._host
    
    @property
    def addr(self):
        return self._addr

    @property
    def port(self):
        return self._port

    @host.setter
    def host(self, new_host):
        self._host = new_host

    @port.setter
    def port(self, new_port):
        self._port = new_port

