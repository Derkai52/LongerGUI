import logging
import socket


class Communication(object):
    """
        Base class which provides interfaces.
    """

    def __init__(self, host_address=None):
        super().__init__()
        self._address = (host_address.split(':')[0], int(
            host_address.split(':')[1])) if host_address else None
        self._is_connected = False
        self.set_recv_size()

    # 判断当前连接是否断开
    def is_connected(self):
        return self._is_connected

    # 设置接收数据的长度，默认长度参见配置表
    def set_recv_size(self, size=1024):
        self.recv_size = size

    def send(self, msg, is_logging=True):
        """
            Interface.
        """

    def recv(self):
        """
            Interface.
        """

    def close(self):
        """
            Interface.
        """

    def before_recv(self):
        """
            Interface.
        """

    def after_recv(self):
        """
            Interface.
        """

    def after_handle(self):
        """
            Interface.
        """


class TcpServer(Communication):
    """
        A TCP server.
    """

    def __init__(self, host_address):
        super().__init__(host_address)
        self.bind_and_listen()

    # 绑定端口
    def bind_and_listen(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self._socket.bind(self._address)
        self._socket.listen(1)

    def local_socket(self):
        return self._socket

    def remote_socket(self):
        return (self._client_connect, self._remote_addr)

    def accept(self):
        logging.info("Wait for client...")
        self._is_connected = False
        try:
            self._client_connect, self._remote_addr = self._socket.accept()
        except Exception as e:
            logging.exception(e)
            return None
        self._is_connected = True
        logging.info("Client is connected!")

    def send(self, msg, is_logging=True):
        len_total = len(msg)
        while msg:
            len_sent = self._client_connect.send(msg)
            if len_sent == 0:
                logging.warning("Connection lost, close the client connection")
                self.close_client()
                return len_sent
            if is_logging:
                logging.info("Server send msg:{}".format(msg[:len_sent]))
            msg = msg[len_sent:]
        return len_total

    def recv(self):
        try:
            return self._client_connect.recv(self.recv_size)
        except Exception as e:
            logging.exception(e)
            return None

    def close(self):
        try:
            self._socket.close()
            self.close_client()
        except Exception as e:
            logging.exception(e)

    def close_client(self):
        self._client_connect.close()
        self._is_connected = False


class HttpServer(TcpServer):
    """
        A Http server.
    """

    def before_recv(self):
        self.accept()

    def after_handle(self):
        self.close_client()


class TcpClient(Communication):
    """
        A TCP client.

        @ivar is_bind_port: If server binds toRobot fixed port, clients need to set `True`.
    """
    is_bind_port = False

    def send(self, msg, is_logging=True):
        len_total = len(msg)
        while msg:
            len_sent = self._socket.send(msg)
            if len_sent == 0:
                logging.warning("Connection lost, try reconnect to server")
                return len_sent
            if is_logging:
                logging.info("Client send msg:{}".format(msg[:len_sent]))
            msg = msg[len_sent:]
        return len_total

    def recv(self):
        return self._socket.recv(self.recv_size)

    def close(self):
        self._socket.close()
        self._is_connected = False

    def set_timeout(self, seconds):
        self._socket.settimeout(seconds)

    def local_socket(self):
        return self._socket

    def reconnect_server(self, is_reconnect=True):
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.is_bind_port:
                self._socket.bind(("0.0.0.0", self._address[1]))
            self._socket.connect(self._address)
            self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self._is_connected = True
            logging.info("Adapter connected to server {}.".format(self._address))
            if is_reconnect:
                self.after_reconnect_server()
            else:
                self.after_connect_server()
        except socket.error:
            self._is_connected = False
            logging.warning("Connect server failed {}.".format(self._address))

    def after_connect_server(self):
        """
            Will be called after connecting to server.
        """

    def after_reconnect_server(self):
        """
            Will be called after reconnecting to server.
        """

    def after_timeout(self):
        """
            Will be called when timeout.
        """


