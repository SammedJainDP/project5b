import unittest
from unittest.mock import MagicMock
import main

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.settings = {"ssid": "wifi_ssid", "password": "wifi_password", "atSign": "test_atsign", "privateKey": [1234, 5678, 9012, 3456, 7890]}
        self.key = {"aesEncryptPrivateKey": "aes_priv_key", "aesEncryptPublicKey": "aes_pub_key", "aesPkamPrivateKey": "aes_pkam_priv_key", "aesPkamPublicKey": "aes_pkam_pub_key", "selfEncryptionKey": "self_enc_key"}
        self.secondary = "secondary_address:1234"
        self.verb = "test_verb"
        self.response = "@response\r\n@command"
        
    def test_measure_temp(self):
        main.sensor_temp.read_u16 = MagicMock(return_value=32768) # simulate reading of temperature sensor
        result = main.measure_temp()
        self.assertAlmostEqual(result, 27.0, places=1)
        
    def test_read_settings(self):
        with open('settings.json', 'w') as f:
            f.write('{"ssid": "wifi_ssid", "password": "wifi_password", "atSign": "test_atsign", "privateKey": [1234, 5678, 9012, 3456, 7890]}')
        ssid, password, atSign, privateKey = main.read_settings()
        self.assertEqual(ssid, "wifi_ssid")
        self.assertEqual(password, "wifi_password")
        self.assertEqual(atSign, "test_atsign")
        self.assertEqual(privateKey, [1234, 5678, 9012, 3456, 7890])
        
    def test_read_key(self):
        with open('/keys/@test_atsign_key.atKeys', 'w') as f:
            f.write('{"aesEncryptPrivateKey": "aes_priv_key", "aesEncryptPublicKey": "aes_pub_key", "aesPkamPrivateKey": "aes_pkam_priv_key", "aesPkamPublicKey": "aes_pkam_pub_key", "selfEncryptionKey": "self_enc_key"}')
        aesEncryptPrivateKey, aesEncryptPublicKey, aesPkamPrivateKey, aesPkamPublicKey, selfEncryptionKey = main.read_key("test_atsign")
        self.assertEqual(aesEncryptPrivateKey, "aes_priv_key")
        self.assertEqual(aesEncryptPublicKey, "aes_pub_key")
        self.assertEqual(aesPkamPrivateKey, "aes_pkam_priv_key")
        self.assertEqual(aesPkamPublicKey, "aes_pkam_pub_key")
        self.assertEqual(selfEncryptionKey, "self_enc_key")
        
    def test_send_verb(self):
        skt_mock = MagicMock()
        skt_mock.write = MagicMock()
        skt_mock.read = MagicMock(return_value=self.response.encode())
        result, command = main.send_verb(skt_mock, self.verb)
        skt_mock.write.assert_called_once_with((self.verb + "\r\n").encode())
        skt_mock.read.assert_called_once()
        self.assertEqual(result, "@response")
        self.assertEqual(command, "@command")
        
    def test_find_secondary(self):
        ss_mock = MagicMock()
        ss_mock.close = MagicMock()
        ss_mock.write = MagicMock()
        ss_mock.read = MagicMock(return_value=b"secondary_address\r\n")
        socket_mock = MagicMock()
        socket_mock.getaddrinfo = MagicMock(return_value=[(0,0,0,0,('ip_address', 64))])
        socket_mock.socket = MagicMock(return_value=ss_mock)
        ssl_mock = MagicMock()
        ssl_mock.wrap_socket = MagicMock(return_value=ss_mock)
        main.socket.getaddrinfo = socket_mock.getaddrinfo
        main.socket.socket = socket_mock.socket
        main.ssl.wrap_socket = ssl_mock.wrap_socket
        result = main.find_secondary("test_atsign")
        socket_mock.getaddrinfo.assert_called_once_with("root.atsign.org", 64)
        ss_mock.connect.assert_called_once_with(('ip_address', 1234))
        ss_mock.setblocking.assert_called_once_with(False)
        ss_mock.write.assert_called_once_with(b"test_atsign\r\n")
        ss_mock.read.assert_called_once()
        ss_mock.close.assert_called_once()
        self.assertEqual(result, "secondary_address")
        
    def test_connect_to_secondary(self):
        ss_mock = MagicMock()
        ss_mock.close = MagicMock()
        ss_mock.write = MagicMock()
        ssl_mock = MagicMock()
        ssl_mock.wrap_socket = MagicMock(return_value=ss_mock)
        socket_mock = MagicMock()
        socket_mock.getaddrinfo = MagicMock(return_value=[(0,0,0,0,('ip_address', 1234))])
        socket_mock.socket = MagicMock(return_value=ss_mock)
        main.socket.getaddrinfo = socket_mock.getaddrinfo
        main.socket.socket = socket_mock.socket
        main.ssl.wrap_socket = ssl_mock.wrap_socket
        result = main.connect_to_secondary(self.secondary)
        socket_mock.getaddrinfo.assert_called_once_with("secondary_address", 1234)
        ss_mock.connect.assert_called_once_with(('ip_address', 1234))
        ss_mock.setblocking.assert_called_once_with(False)
        ssl_mock.wrap_socket.assert_called_once_with(ss_mock, do_handshake=True)
        self.assertEqual(result, ss_mock)
        
    def test_b42_urlsafe_encode(self):
        payload = b"\x9a\xbf\x04\x1e\x80\x04\x08\xdc"
        result = main.b42_urlsafe_encode(payload)
        self.assertEqual(result, "ms8EHoAIEd")
        
if __name__ == '__main__':
    unittest.main()
