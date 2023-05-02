import unittest
from unittest.mock import patch

from main import measure_temp, send_verb, find_secondary, connect_to_secondary


class TestMain(unittest.TestCase):
    # Test that the program exits when the Wi-Fi is not connected
    print('Test that the program exits when the Wi-Fi is not connected')
    @patch('builtins.print')
    @patch('network.WLAN')
    @patch('sys.exit')
#     def test_exit_program_not_connected(self, mock_exit, mock_wlan, mock_print):
#         mock_wlan.return_value.isconnected.return_value = False
#         mock_wlan.return_value.status.return_value = -1
#         unittest.main()
#         mock_exit.assert_called_with(1)
    def test_exit_program_not_connected(self, mock_exit, mock_wlan, mock_print):
        mock_wlan.return_value.isconnected.return_value = False
        mock_wlan.return_value.status.return_value = -1
        connect_to_secondary = patch('network.WLAN', mock_wlan)
        connect_to_secondary.start()
        unittest.main()
        mock_exit.assert_called_with(1) 
        connect_to_secondary.stop()

    # Test that the program prints "Wi-Fi Connected" when the Wi-Fi is connected
    @patch('builtins.print')
    @patch('network.WLAN')
    def test_print_wifi_connected(self, mock_wlan, mock_print):
        mock_wlan.return_value.isconnected.return_value = True
        unittest.main()
        mock_print.assert_any_call("Wi-Fi Connected")

    # Test that the measure_temp function returns a value between 0 and 100
    def test_measure_temp(self):
        temp = measure_temp()
        self.assertGreaterEqual(temp, 0)
        self.assertLessEqual(temp, 100)

    # Test that the send_verb function sends the expected verb and returns the expected response
    @patch('ussl.wrap_socket')
    @patch('usocket.socket')
    def test_send_verb(self, mock_socket, mock_wrap_socket):
        mock_socket.return_value.recv.side_effect = [b'@data:12345', b'OK']
        response, command = send_verb(mock_socket(), "test")
        self.assertEqual(response, "OK")
        self.assertEqual(command, "@")
        mock_socket.return_value.sendall.assert_called_with(b"test\r\n")

    # Test that the find_secondary function returns a valid IP address
    @patch('socket.getaddrinfo')
    def test_find_secondary(self, mock_getaddrinfo):
        mock_getaddrinfo.return_value = [(None, None, None, None, ('192.168.1.1', 0))]
        self.assertEqual(find_secondary("test"), "192.168.1.1")
        
    # Test that the connect_to_secondary function returns a valid socket
    @patch('ussl.wrap_socket')
    @patch('usocket.socket')
    def test_connect_to_secondary(self, mock_socket, mock_wrap_socket):
        mock_socket.return_value.recv.return_value = b'OK'
        s = connect_to_secondary("192.168.1.1")
        self.assertEqual(s.recv(1024), b'OK')
    
if __name__ == '__main__':
    unittest.main()

