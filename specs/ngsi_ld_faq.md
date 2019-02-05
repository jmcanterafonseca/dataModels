# NGSI-LD FAQ

## Introduction

This FAQ compilation is intended to clarify NGSI-LD specification by providing answers to common questions.

* Q: What are the main (essential) differences between NGSI v2 and NGSI-LD?
  * R: The following:
    * The underlying Data Model is the Property Graph Data Model. [Here](https://github.com/Fiware/NGSI-LD_Wrapper/blob/master/doc/instantiation.png) you can see an example. 
    * Entity Ids shall be URIs (URLs or URNs)
    * The `metadata` dictionary disappears. Metadata are represented by nested Properties of Properties. 
    * There is some "metadata" standardised (`unitCode`, `observedAt`, ...)
    * There is a new type of Attribute `Relationship` intended to link one Entity to another Entity. That is done through the `object` member. 
    * Geospatial properties are represented using the Attribute type `GeoProperty`. 
    * The `type` of Attributes can only be  `Property`, `Relationship` or `GeoProperty`. 
    * A JSON-LD `@context` (a hash mapping names to URIs) can be added to Entities to provide Fully Qualified Names (URIs) associated to terms. That is somewhat "similar" to XML namespaces.  
    * Overall the REST API is quite similar (even simpler) than the NGSI v2, although subscription payloads change a bit (but they are the same in essence).
    
  * Q: Could you give me some examples of NGSI-LD payloads?
  
```json
{
  "id": "urn:ngsi-ld:AirQualityObserved:RZ:Obsv4567",
  "type": "AirQualityObserved",
  "dateObserved": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2018-08-07T12:00:00Z"
    }
  },
  "NO2": {
    "type": "Property",
    "value": 22,
    "unitCode": "GP",
    "accuracy": {
      "type": "Property",
      "value": 0.95
    }
  },
  "refPointOfInterest": {
    "type": "Relationship",
    "object": "urn:ngsi-ld:PointOfInterest:RZ:MainSquare"
  },
  "@context": [
    "http://schema.lab.fiware.org/ld/jsonldcontext.json",
    "http://uri.etsi.org/ngsi-ld/ngsi-ld-core-context.jsonld"
  ]
}
```

Additional examples can be found [here](https://github.com/Fiware/NGSI-LD_Tests/blob/master/contextProvision/create_entity_with_ldcontext_test.js#L16)

* Could you give me some examples of a JSON-LD @context?
  * R: Yes, [here](https://github.com/Fiware/NGSI-LD_Tests/blob/master/ldContext/testContext.jsonld) you can find one.
  
  
* Q: What is a Property of a Property / Relationship and all the combinations? 
  * R: It is similar to NGSI v2 metadata. In NGSIv2, in the example above, the Property `accuracy` would have been represented as a member of the `metadata` dictionary.

* Q: But, Property and Relationship can be arbitrarily nested? 
  * R: Yes, but only one or two nesting levels could make sense in a real world scenario.
  
  
* Q: What is `observedAt`?
  * R: It is a "timestamp" associated to a Property or Relationship. See the example below. 
  In NGSI v2 it is usually specified using the `timestamp` metadata member.
  
  ```json
  {
    "id": "urn:ngsi-ld:WasteContainer:RZ:Obsv4567",
    "type": "WasteContainer",
    "fillingLevel": {
      "type": "Property",
      "value": 0.85,
      "observedAt": "2017-02-07T16:00:00Z"
    },
    "location": {
      "type": "GeoProperty",
      "value": {
        "type": "Point",
        "coordinates": [-2,35]
      }
    },
    "@context": [
      "http://schema.lab.fiware.org/ld/jsonldcontext.json",
      "http://uri.etsi.org/ngsi-ld/ngsi-ld-core-context.jsonld"
    ]
} 
```
  
  
  * Q: How geo-location is represented? 
  * R: See the example above. In essence an Attribute of type `GeoProperty plus GeoJSON.  

* Q: How DateTime (timestamps, dates, time) is represented?
  * R: See the first example on this page
  