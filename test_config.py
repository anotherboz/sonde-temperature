#! /usr/bin/env -S python3 test_config.py
import unittest
import os
import config

class TestConfig(unittest.TestCase):
    def test_load(self):
        try:
            os.remove('config.json')
        except:
            pass
        conf = config.load()
        self.assertEqual(conf, {'ssid': '', 'password': '', 'server': ''})
        self.assertEqual(conf, config.get())

    def test_set_config(self):
        conf = config.get()
        conf['ssid']='test'
        config.set(conf)
        self.assertEqual(config.get()['ssid'], 'test')

    def test_save_config(self):
        try:
            os.remove('config.json')
        except:
            pass
        conf = config.get()
        conf['ssid']='test'
        config.set(conf)
        config.save()
        conf2 = config.load()
        self.assertEqual(conf2['ssid'], 'test')
        self.assertEqual(config.get()['ssid'], 'test')
        self.assertTrue(os.access('config.json', os.F_OK))

if __name__ == '__main__':
    unittest.main()