# NGSI-LD HowTo

## Introduction

The OMA NGSI information model has been evolved to better support linked data (entity relationships), property graphs and semantics
(exploiting the capabilities offered by JSON-LD). This work has been conducted under the ETSI ISG CIM initiative and has been branded as
[NGSI-LD](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.01.01_60/gs_CIM009v010101p.pdf).
The main constructs of NGSI-LD are: Entity, Property and Relationship. NGSI-LD Entities (instances) can be the subject of Properties or Relationships. 
In terms of the traditional NGSI data model, Properties can be seen as the combination of an attribute and its value.
Relationships allow to establish associations between instances using linked data.
In practice, they are conveyed by means of an NGSI attribute, but with a special value (relationship’s object) which happens to be a
URI which points to another entity. They are similar to the “ref” attributes recommended the Data Models guidelines.

Properties and Relationships can be the subject of other Properties or Relationships. Thus, in the NGSI-LD information model there are no attribute’s metadata,
but just “properties of properties” or “properties of relationships”. It is not expected to have infinite graphs, and in practice, only one or two levels of Property
or Relationship “chaining” will happen. Typically, there will be one, equivalent to the NGSI metadata abstraction. 
NGSI-LD Entities are represented using JSON-LD, a JSON-based serialization format for Linked Data.
The main advantage of JSON-LD is that it offers the capability of expanding JSON terms to URIs, so that vocabularies can define terms unambiguously.

## Steps to migrate to JSON-LD

First of all, each Data Model shall have a JSON-LD @context, providing an unambiguous definition by mapping terms to URIs.
For practicality reasons, it is recommended to have a unique @context resource, containing all terms, subject to be used in every FIWARE Data Model,
the same way as schema.org does. The following steps have to be followed in order to migrate existing NGSI instantiations of the FIWARE Data Models to NGSI-LD:

* Entity ids have to be converted to URIs, preferably using the NGSI-LD URN namespace. 
*	Regular entity attributes have to be converted to JSON-LD nodes of type `Property`.
*	ref attributes (pointing to other entities) have to be converted to JSON-LD nodes of type `Relationship`.
*	The `timestamp` metadata item has to be mapped to the `observedAt` member of a Property node.
*	The `unitCode` metadata item has to be mapped to the `unitCode` member of a Property node.
*	The NGSI `DateTime` type has to be properly encoded as per the JSON-LD rules.
* The NGSI `geo:json` type has to be renamed to `GeoProperty`.

The FIWARE Community has already provided a simple script to migrate FIWARE NGSI entity representations to NGSI-LD, see https://github.com/Fiware/dataModels/blob/master/tools/normalized2LD.py
