#!/usr/bin/python
# -*- coding: utf-8 -*-
import configparser


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)

        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
            return cls.instance


class ConfigReader(object):
    __metaclass__ = Singleton

    cfg = None

    @staticmethod
    def get_main_config():
        if ConfigReader.cfg is None:
            ConfigReader.cfg = configparser.ConfigParser()
            with open('main.cfg', 'r+') as cfg_file:
                ConfigReader.cfg.read_file(cfg_file)
                print(ConfigReader.cfg.get("param", "ext"))
        return ConfigReader.cfg


if __name__ == '__main__':
    pass
