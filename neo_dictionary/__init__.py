#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bulbs.neo4jserver import Graph, Config

from neo_dictionary.word import Word, PossibleMeaning, Idea, CanMean, IsMeantBy, CanRepresent, RepresentedBy, HasHyponym


GRAPH='http://localhost:7474/db/data'

def graph_db_path():
    config = Config(GRAPH)
    graph = Graph(config)
    return graph

def init_db():
    g = graph_db_path()
    PossibleMeaning.register(g)
    Word.register(g)
    Idea.register(g)
    CanMean.register(g)
    IsMeantBy.register(g)
    CanRepresent.register(g)
    RepresentedBy.register(g)
    HasHyponym.register(g)
