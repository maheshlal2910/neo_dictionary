#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nltk import wordnet as wn

from neo_dictionary.word import *

class Creator(object):
    
    def create_meaning_graph(self):
        entity_syns= wn.wordnet.synsets('entity')
        self.create_word_graph(entity_syns)
    
    def create_word_graph(self, syns, hypernym= None):
        for syn in syns:
            word = self.create_word(syn)
            meaning = self.create_meaning(syn, word)
            if hypernym:
                hypernym.has_hyponym(meaning)
            self.create_ideas(syn, meaning)
            hyponyms = syn.hyponyms()
            self.create_word_graph(hyponyms, meaning)
    
    def create_word(self, syn):
        return Word.get_or_create(name = syn.name.split('.')[0])
    
    def create_meaning(self, syn, word):
        meaning = PossibleMeaning.get_or_create(complete_name = syn.name)
        meaning.update(name = syn.name.split('.')[0], part_of_speech = syn.pos, definition = syn.definition)
        word.can_mean(meaning)
        meaning.save()
        word.save()
        return meaning
    
    def create_ideas(self, syn, meaning):
        for lemma in syn.lemmas:
            idea = Idea.get_or_create(name = lemma.name)
            meaning.can_represent(idea)
            idea.save()


    def create_synonyms(self, syn, meaning):
        pass