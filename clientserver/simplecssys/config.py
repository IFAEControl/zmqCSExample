#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '26/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import inspect
import json
import yaml


class ConfObject:
    def __init__(self):
        self._file_path = None

    def load_dict(self, conf):
        if not isinstance(conf, dict):
            raise Exception('Configuration must be a dictionary')

        for k in conf.keys():
            try:
                a = getattr(self, k)
                if not inspect.ismethod(a):
                    if isinstance(a, ConfObject):
                        a.load_dict(conf[k])
                    else:
                        setattr(self, k, conf[k])
            except AttributeError:
                pass

    def as_dict(self):
        t = {}
        for mem in inspect.getmembers(self):
            if not mem[0].startswith('_') and not inspect.ismethod(mem[1]):
                if isinstance(mem[1], ConfObject):
                    t[mem[0]] = mem[1].as_dict()
                else:
                    t[mem[0]] = mem[1]
        return t

    def load_json(self, json_path):
        if json_path is None:
            json_path = self._file_path
        elif self._file_path is None:
            self._file_path = json_path
        with open(json_path, 'r') as json_file:
            self.load_dict(json.load(json_file))

    def save_as_json(self, json_path):
        if json_path is None:
            json_path = self._file_path
        with open(json_path, 'w') as json_file:
            json.dumps(self.as_dict(), json_file)

    def load_yaml(self, yaml_path):
        if yaml_path is None:
            yaml_path = self._file_path
        elif self._file_path is None:
            self._file_path = yaml_path
        with open(yaml_path, 'r') as yaml_fp:
            self.load_dict(yaml.safe_load(yaml_fp))

    def save_as_yaml(self, yaml_path=None):
        if yaml_path is None:
            yaml_path = self._file_path
        with open(yaml_path, 'w') as yaml_fp:
            yaml.dump(self.as_dict(), yaml_fp)

    def set_file_path(self, full_path):
        self._file_path = full_path



