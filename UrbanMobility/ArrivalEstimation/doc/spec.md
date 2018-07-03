# ArrivalEstimation

## Description

This Entity Type captures the estimation of arrivals of public transport vehicles to a certain stop. 

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
  
+ `hasTrip` : An ordered list of trips to which this estimation applies to. 
  + Attribute type: Relationship. An Array that shall contain a list of Entities of Type [gtfs:Trip](../../doc/Trip/spec.md)
  + Mandatory

+ `remainingTime`: An ordered list that contains the remaining time of arrival for each of the trips heading to the concerned stop. 
  + Attribute type: Property. List of [Text](https://schema.org/Text). Remaining times shall be encoded
  as a ISO8601 duration. Ex. ."PT8M5S"`. 
  + Metadata:
    + `timestamp` (mapped to `observedAt` in NGSI-LD). Timestamp of the last attribute update
      + Type: `[DateTime](https://schema.org/DateTime)
      + Mandatory
  + Mandatory
  
+ `remainingDistance: Same as GTFS `monday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Attribute metadata:
    + `timestamp`
  + Optional
  
+ `headSign`:    


### Examples

```json
{
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",
  "type": "gtfs:CalendarRule",
  "name": "Rule Hospital Service 1",
  "hasService": "urn:ngsi-ld:Service:Madrid:Hospital_1",
  "monday": true,
  "tuesday": true,
  "wednesday": true,
  "thursday": true,
  "friday": true,
  "saturday": false,
  "sunday": false,
  "startDate": "2018-01-01",
  "endDate": "2019-01-01"
}
```

## Summary of mappings to GTFS

| GTFS Field                | NGSI Attribute          | LinkedGTFS                  | Comment                                                    |
|:--------------------------|:------------------------|:--------------------------- |:-----------------------------------------------------------|
|                           | `name`                  | `schema:name`               |                                                            |
|                           | `description`           | `schema:description`        |                                                            |
| `monday`                  | `monday`                | `gtfs:monday`               |                                                            |
| `tuesday`                 | `tuesday`               | `gtfs:tuesday`              |                                                            |
| `wednesday`               | `wednesday`             | `gtfs:wednesday`            |                                                            |
| `thursday`                | `thursday`              | `gtfs:thursday`             |                                                            |
| `friday`                  | `friday`                | `gtfs:friday`               |                                                            |
| `saturday`                | `saturday`              | `gtfs:saturday`             |                                                            |
| `sunday`                  | `sunday`                | `gtfs:sunday`               |                                                            |
| `start_date`              | `startDate`             | `schema:startDate`          |                                                            |
| `end_date`                | `endDate`               | `schema:endDate`            |                                                            |
                              


### Relationships

| GTFS Field              | NGSI Attribute        | LinkedGTFS           | Comment                                                |
|:----------------------- |:----------------------|:-------------------- |:-------------------------------------------------------|
|                         | `hasService`          | `gtfs:service`        | Shall point to another Entity of Type `gtfs:Service`  |

## Open issues
