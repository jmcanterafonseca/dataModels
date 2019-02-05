# NGSI-LD HowTo

## Introduction

The OMA NGSI information model (currently adopted by SynchroniCity) has been evolved to better support linked data (entity relationships), property graphs and semantics (exploiting the capabilities offered by JSON-LD). This work has been conducted under the ETSI ISG CIM initiative and has been branded as NGSI-LD [21]. D2.2 provided an overview of NGSI-LD and its information model. This chapter is intended to show in practical terms how the SynchroniCity Data Models can be eventually migrated to NGSI-LD.
The main constructs of NGSI-LD are: Entity, Property and Relationship. NGSI-LD Entities (instances) can be the subject of Properties or Relationships. 
In terms of the traditional NGSI data model, Properties can be seen as the combination of an attribute and its value. Relationships allow to establish associations between instances using linked data. In practice, they are conveyed by means of an NGSI attribute, but with a special value (relationship’s object) which happens to be a URI which points to another entity. They are similar to the “ref” attributes recommended by the D2.2 guidelines.
