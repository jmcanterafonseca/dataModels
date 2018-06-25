# gtfs:CalendarRule

## Description

See [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:gtfs:CalendarRule:<calendar_rule_identifier>`. 

+ `type`: Entity Type 
  + It shall be equal to `gtfs:CalendarRule`
  
+ `dateCreated` : Entity's creation timestamp.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated. 
 
+ `dateModified` : Last update timestamp of this Entity.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated.
  
+ `hasService` : Service to which this rule applies to. Derived from `service_id`.
  + Attribute type: Relationship. It shall point to an entity of Type [gtfs:Service](../../doc/Service/spec.md)
  + Mandatory
  
+ `name` : Name of this rule
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional

+ `description`: Description of this rule
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional
  
+ `monday`: Same as GTFS `monday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `tuesday`: Same as GTFS `tuesday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `wednesday`: Same as GTFS `wednesday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `thursday`: Same as GTFS `thursday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `friday`: Same as GTFS `friday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `saturday`: Same as GTFS `saturday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

+ `sunday`: Same as GTFS `sunday`
  + Attribute type: Property. [https://schema.org/Boolean](https://schema.org/Boolean)
  + Mandatory

### Examples

  `json
{
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",
  "type": "gtfs:CalendarRule",
  "name": "Rule Hospital Service 1",
  "hasService": "urn:ngsi-ld:Service:Hospital_1",
  "monday": true,
  "tuesday": true,
  "wednesday": true,
  "thursday": true,
  "friday": true,
  "saturday": false,
  "sunday": false
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
                              


### Relationships

| GTFS Field              | NGSI Attribute        | LinkedGTFS           | Comment                                                |
|:----------------------- |:----------------------|:-------------------- |:-------------------------------------------------------|
|                         | `hasService`          | `gtfs:service`        | Shall point to another Entity of Type `gtfs:Service`  |

## Open issues
