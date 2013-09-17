#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bulbs.property import String 
from bulbs_garnish.models import Node, Relationship
from bulbs_garnish.decorators import ActiveModel, IsMirrorRelationshipOf, HasRelationship

@IsMirrorRelationshipOf('is_meant_by')
@ActiveModel
class CanMean(Relationship):
    
    label = 'can_mean'


@IsMirrorRelationshipOf('can_mean')
@ActiveModel
class IsMeantBy(Relationship):
    
    label = 'is_meant_by'


@IsMirrorRelationshipOf('represented_by')
@ActiveModel
class CanRepresent(Relationship):
    
    label = 'can_represent'


@IsMirrorRelationshipOf('can_represent')
@ActiveModel
class RepresentedBy(Relationship):
    
    label = 'represented_by'


@HasRelationship({CanMean: 'possible_meaning'})
@ActiveModel
class Word(Node):
    
    element_type = 'word'
    keys = ['name']
    name = String()


@ActiveModel
class HasHyponym(Relationship):
    
    label = 'has_hyponym'


@HasRelationship({CanRepresent: 'idea'})
@HasRelationship({IsMeantBy: 'word'})
@HasRelationship({HasHyponym: 'possible_meaning'})
@ActiveModel
class PossibleMeaning(Node):
    
    element_type = 'possible_meaning'
    keys = ['complete_name']
    part_of_speech = String()
    complete_name = String()
    name = String()
    definition = String()


@HasRelationship({RepresentedBy: 'possible_meaning'})
@ActiveModel
class Idea(Node):
    
    element_type = 'idea'
    keys = ['name']
    name = String()
