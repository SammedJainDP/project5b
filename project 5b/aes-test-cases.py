import unittest
import binascii
from binascii import a2b_base64
import base64
from aes1 import aes_decrypt, aes_encrypt, hex_str_to_bytes, str_to_bytes, str_to_bytearray, bytearray_to_str, bytes_to_str

class TestAESFunctions(unittest.TestCase):

    def test_aes_encrypt_decrypt(self):
        plain_text = "This is a test message."
        aes256Base64Key = base64.b64encode(b"0123456789ABCDEF0123456789ABCDEF").decode('utf-8')
        
        encrypted_text = aes_encrypt(plain_text, aes256Base64Key)
        self.assertNotEqual(plain_text, encrypted_text)
        
        decrypted_text = aes_decrypt(encrypted_text, aes256Base64Key)
        self.assertEqual(plain_text, decrypted_text)

    def test_hex_str_to_bytes(self):
        hex_str = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        expected_result = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(hex_str_to_bytes(hex_str), expected_result)

    def test_str_to_bytes_and_bytes_to_str(self):
        base64_str = "VGhpcyBpcyBhIHRlc3QgbWVzc2FnZS4="
        bytes_value = base64.b64decode(base64_str)
        self.assertEqual(str_to_bytes(base64_str), bytes_value)
        self.assertEqual(bytes_to_str(bytes_value), base64_str)

    def test_str_to_bytearray_and_bytearray_to_str(self):
        base64_str = "VGhpcyBpcyBhIHRlc3QgbWVzc2FnZS4="
        bytes_value = base64.b64decode(base64_str)
        bytearray_value = bytearray(bytes_value)
        self.assertEqual(str_to_bytearray(base64_str), bytearray_value)
        self.assertEqual(bytearray_to_str(bytearray_value), str(bytes_value))

    def test_aes_encrypt_decrypt_with_different_keys(self):
        plain_text = "This is another test message."
        aes256Base64Key1 = base64.b64encode(b"0123456789ABCDEF0123456789ABCDEF").decode('utf-8')
        aes256Base64Key2 = base64.b64encode(b"FEDCBA9876543210FEDCBA9876543210").decode('utf-8')
        
        encrypted_text1 = aes_encrypt(plain_text, aes256Base64Key1)
        encrypted_text2 = aes_encrypt(plain_text, aes256Base64Key2)
        self.assertNotEqual(encrypted_text1, encrypted_text2)
        
        decrypted_text1 = aes_decrypt(encrypted_text1, aes256Base64Key1)
        decrypted_text2 = aes_decrypt(encrypted_text2, aes256Base64Key2)
        self.assertEqual(decrypted_text1, plain_text)
        self.assertEqual(decrypted_text2, plain_text)

    def test_hex_str_to_bytes_with_different_inputs(self):
        hex_str1 = "01 23 45 67 89 AB CD EF"
        expected_result1 = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF'
        self.assertEqual(hex_str_to_bytes(hex_str1), expected_result1)
        
        hex_str2 = "0123456789ABCDEF"
        expected_result2 = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF'
        with self.assertRaises(ValueError):
            hex_str_to_bytes(hex_str2)

    def test_str_to_bytes_and_bytes_to_str_with_empty_input(self):
        base64_str = ""
        bytes_value =b'\\n'
        self.assertEqual(str_to_bytes(base64_str), bytes_value)
        self.assertEqual(bytes_to_str(bytes_value), base64_str)

    def test_str_to_bytearray_and_bytearray_to_str_with_empty_input(self):
        base64_str = ""
        bytes_value = bytearray(b'')
        bytearray_value = bytearray(bytes_value)
        self.assertEqual(str_to_bytearray(base64_str), bytearray_value)
        self.assertEqual(bytearray_to_str(bytearray_value), str(bytes_value))

if __name__ == "__main__":
    unittest.main()
