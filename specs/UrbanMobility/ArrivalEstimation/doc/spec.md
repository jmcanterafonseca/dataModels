# ArrivalEstimation

## Description

This Entity Type captures the estimation of arrival of a public transport vehicle, performing service on a route, to a certain stop. 

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:gtfs:ArrivalEstimation:<identifier>`. 

+ `type`: Entity Type 
  + It shall be equal to `ArrivalEstimation`
  
+ `dateCreated` : Entity's creation timestamp.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated. 
 
+ `dateModified` : Last update timestamp of this Entity.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated.
  
+ `hasStop` : Stop to which this estimation applies to.
  + Attribute type: Relationship. It shall point to an Entity of Type [gtfs:Stop](../../doc/Stop/spec.md)
  + Mandatory
  
+ `hasTrip` : The trip to which this estimation applies to. 
  + Attribute type: Relationship. It shall point to an Entity of Type [gtfs:Trip](../../doc/Trip/spec.md)
  + Mandatory

+ `remainingTime`: It shall contain the remaining time of arrival for the trip heading to the concerned stop. 
  + Attribute type: Property. [Text](https://schema.org/Text). Remaining time shall be encoded as a ISO8601 duration. Ex. ."PT8M5S"`. 
  + Attribute Metadata:
    + `timestamp` (mapped to `observedAt` in NGSI-LD). Timestamp of the last attribute update
      + Type: `[DateTime](https://schema.org/DateTime)
      + Mandatory
  + Mandatory
  
+ `remainingDistance`: It shall contain  the remaining distance (in meters) of arrival for the trip heading to the concerned stop. 
  + Attribute type: Property. Positive Number. [https://schema.org/Number](https://schema.org/Number)
  + Attribute metadata:
    + `timestamp` (mapped to `observedAt` in NGSI-LD). Timestamp of the last attribute update
      + Type: `[DateTime](https://schema.org/DateTime)
      + Mandatory
  + Default Unit: Meters
  + Optional
  
+ `headSign`: It shall contain the text that appears on a sign that identifies the trip's destination to passengers.
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Mandatory


### Examples

```json
{
  "id": "urn:ngsi-ld:ArrivalEstimation:L67_Stop2",
  "type": "ArrivalEstimation",
  "hasStop": "urn:ngsi-ld:santander:transport:tus:busStop:74",
  "hasTrip": "urn:ngsi-ld:santander:transport:tus:busLine:5C1",
  "remainingTime": "PT8M5S",
  "remainingDistance": 1200,
  "headSign": "A destination"
}
```

## Open issues
