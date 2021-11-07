#! /usr/bin/env -S python3 -m unittest test_config.py
import unittest
import os
import config

class TestConfig(unittest.TestCase):
    def test_load(self):
        try:
            os.remove('config.json')
        except:
            pass
        conf = config.load_config()
        self.assertEqual(conf, {'ssid': '', 'password': '', 'server': ''})
        self.assertEqual(conf, config.get_config())

    def test_set_config(self):
        conf = config.get_config()
        conf['ssid']='test'
        config.set_config(conf)
        self.assertEqual(config.get_config()['ssid'], 'test')

    def test_save_config(self):
        try:
            os.remove('config.json')
        except:
            pass
        conf = config.get_config()
        conf['ssid']='test'
        config.set_config(conf)
        config.save_config()
        conf2 = config.load_config()
        self.assertEqual(conf2['ssid'], 'test')
        self.assertEqual(config.get_config()['ssid'], 'test')
        self.assertTrue(os.access('config.json', os.F_OK))

if __name__ == '__main__':
    unittest.main()