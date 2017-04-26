# FlowerBed

## Description

 A garden plot in which flowers (or other plants) are grown.
 
## Data Model

A JSON Schema corresponding to this data model can be found {{add link to JSON Schema}}

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `FlowerBed. 

+ `dateModified` : Last update timestamp of this entity.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `dateCreated` : Entity's creation timestamp.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional    

+ `taxon` : Used to indicate the biological [taxon](http://en.wikipedia.org/wiki/en:taxon)
to which the trees, or plants in the flower bed belong.
    + Attribute type: List of [Text](https://schema.org/Text)
    + Optional
    
+ `category` : Category of this flower bed. 
    + Attribute type: List of [Text](https://schema.org/Text)
    + Allowed values: (`hedge`, `lawn`, `tree`) or any extended value needed by the application.

+ `location` : Location of the flower bed represented by a GeoJSON geometry. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    + Mandatory if `address` is not defined
    
+ `address` : Civic address of this flower bed.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not present.     

+ `dateLastWatering` : Timestamp which corresponds to the last watering of the flower bed.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `nextWateringDeadline` : Deadline for next watering operation.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `refGarden` : Flower bed's garden. 
    + Attribute type: Reference to an entity of type `Garden`
    + Optional
    
+ `refRecord` : List of records which contain measurements related to this flower bed.
    + Attribute type: List of references to entities of type `GardenRecord`
    + Optional

    
## Examples of use

``json
{
  "id": "FlowerBed-345",
  "type": "FlowerBed",
  "category": ["tree"],
  "dateLastWatering": "2017-03-31T08:00",
  "address": {
    "streetAddress": "Paseo Zorrilla, 122",
    "adressLocality": "Valladolid",
    "addressCountry": "Spain"
  },
  "refRecord": ["FlowerBed-345-Record-1"]
}
```
    
## Use it with a real service


## Open Issues

