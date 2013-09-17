#!/usr/bin/env python
#-*- coding:utf-8 -*-

from neo_dictionary import init_db
from neo_dictionary.creator import Creator

init_db()
creator = Creator()

creator.create_meaning_graph()