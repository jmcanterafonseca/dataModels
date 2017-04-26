# Garden

## Description

A garden is a distinguishable planned space, usually outdoors, set aside for the display, cultivation,
and enjoyment of plants and other forms of nature.

## Data Model

A JSON Schema corresponding to this data model can be found {{add link to JSON Schema}}

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `Garden`.

+ `dateModified` : Last update timestamp of this entity.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `dateCreated` : Entity's creation timestamp.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional    

+ `source` : A sequence of characters giving the source of the entity data.
    + Attribute type: [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    + Optional

+ `location` : Location of garden represented by a GeoJSON geometry. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    + Mandatory if `address` is not defined. 
    
+ `address` : Civic address of garden
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not present. 

+ `name` : Garden's name. 
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Mandatory
    
+ `alternateName` : Garden's alternate name. 
    + Normative References: [https://schema.org/alternateName](https://schema.org/alternateName)
    + Optional

+ `category` : Garden's category. 
    + Attribute type: List of [Text](https://schema.org/Text)
    + Allowed Values: (`public`, `private`, `botanical`, `castle`, `community`, `monastery`,
    `residential`, `fenced`) or any other value needed by an application.
    + Optional
   
+  `style` : Garden's style.
    + Attribute type: [Text](https://schema.org/Text)
    + Allowed values: See [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Key:garden:style)
    + Optional

+  `openingHours :  Opening hours of the garden. 
    + Normative references: [https://schema.org/openingHours]
    + Optional
    
+ `areaServed` : Higher level area to which the garden belongs to. It can be used to group gardens per
responsible, district, neighbourhood, etc.
    + Attribute type: [Text](https://schema.org/Text)
    + Optional
    
## Examples of use

```json
    {
        "id": "Santander-Garden-Piquio",
        "type": "Garden",
        "name": "Jardines de Piquio",
        "description": "Los famosos Jardines de Piquio",
        "location": {
            "type": "Point",
            "coordinates": [-3.7836974, 43.4741091]
        },
        "address": {
            "streetAddress": "Avenida Castañeda",
            "addressLocality": "Santander",
            "postalCode": "39005"
        },
        "openingHours": "Mo-Su",
        "style": "french",
        "category": ["public"],
        "areaServed": "El Sardinero"
    }
```

## Use it with a real service

Soon to be available

## Open Issues
