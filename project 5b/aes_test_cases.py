import unittest
import aes1
from aes1 import aes_decrypt, aes_encrypt, hex_str_to_bytes, str_to_bytes, str_to_bytearray, bytearray_to_str, bytes_to_str
from ubinascii import b2a_base64

class TestEncryptionDecryption(unittest.TestCase):
    
     # initializing the variables and values to use for testing. Performs all the required setup for the test environment
    def setUp(self):
        self.plain_text = "Hello, world!"
        self.aes_key = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlz"
    
    #testing the AES encryption amd AES decryption with sample plain text as input
   # def test_encryption_decryption(self):
    #    encrypted_text = aes_encrypt(self.plain_text, self.aes_key)
     #   decrypted_text = aes_decrypt(encrypted_text, self.aes_key)
      #  self.assertEqual(decrypted_text, self.plain_text)
    
   # def test_aes_encrypt(self):
    #    plain_text = "Hello World!"
     #   aes256Base64Key = "2b7e151628aed2a6abf7158809cf4f3c"
      #  encoded_key = b2a_base64(bytes.fromhex(aes256Base64Key)).decode('utf-8').rstrip('\n')
       # expected_encrypted_text = "aTcqGDobT+Q/igqu6xeRow=="
        #from aes1 import aes_encrypt
        #encrypted_text = aes_encrypt(plain_text, encoded_key)
        #self.assertEqual(encrypted_text, expected_encrypted_text)
        
    #testing the convertion mechanism from hexadecimal value to byte values using a sample hex string argument
    def test_hex_str_to_bytes(self):
        hex_str = "48 65 6c 6c 6f 2c 20 77 6f 72 6c 64 21"
        expected_bytes = b'Hello, world!'
        bytes_result = hex_str_to_bytes(hex_str)
        self.assertEqual(bytes_result, expected_bytes)
        
    #testing the conversion of a sample base64 encoded string to bytes
    def test_str_to_bytes(self):
        base64_str = "SGVsbG8sIHdvcmxkIQ=="
        expected_bytes = b'Hello, world!'
        bytes_result = str_to_bytes(base64_str)
        self.assertEqual(bytes_result, expected_bytes)
        
      #testing the conversion of a sample base64 encoded string to bytesarray
    def test_str_to_bytearray(self):
        expected_bytearray = bytearray(b'Hello, world!')
        bytearray_result = str_to_bytearray("SGVsbG8sIHdvcmxkIQ==")
        self.assertEqual(bytearray_result, expected_bytearray)
        
    #testing the conversion of the byte array to string argument
    def test_bytearray_to_str(self):
        expected_string = "bytearray(b'Hello, world!')"
        bytearray_input = bytearray(b'Hello, world!')
        string_result = bytearray_to_str(bytearray_input)
        self.assertEqual(string_result, expected_string)

    #tests the converion of bytes input to expected string output   
    def test_bytes_to_str(self):
        expected_string = "b'SGVsbG8sIHdvcmxkIQ==\\n'"
        bytes_input = b'Hello, world!'
        string_result = bytes_to_str(bytes_input)
        self.assertEqual(string_result, expected_string)
        
if __name__ == '__main__':
    unittest.main()
