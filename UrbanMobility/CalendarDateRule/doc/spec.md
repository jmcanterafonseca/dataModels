# gtfs:CalendarDateRule

## Description

See [https://developers.google.com/transit/gtfs/reference/#calendar_datestxt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt)

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:gtfs:CalendarDateRule:<calendar_date_rule_identifier>`. 

+ `type`: Entity Type 
  + It shall be equal to `gtfs:CalendarDateRule`
  
+ `dateCreated` : Entity's creation timestamp.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated. 
 
+ `dateModified` : Last update timestamp of this Entity.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated.
  
+ `hasService` : Service to which this rule applies to. Derived from `service_id`.
  + Attribute type: Relationship. It shall point to an entity of Type [gtfs:Service](../../doc/Service/spec.md)
  + Mandatory
  
+ `name` : Name given to this rule.
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional

+ `description`: Description given to this rule.
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional
  
+ `appliesOn`: Date (in YYYY-MM-DD format) this rule applies to. It shall be obtained from the GTFS `date` field. 
  + Attribute type: Property. [Date](https://schema.org/Date). Note: Use `DateTime` when storing data in Orion Context Broker. 
  + Mandatory

+ `exceptionType`: Same as GTFS `exception_type` field. (Only `"1"` and `"2"` are allowed as values)
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Mandatory

### Examples

```json
{
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",
  "type": "gtfs:CalendarDateRule",
  "name": "Rule Fair Area",
  "hasService": "urn:ngsi-ld:Service:Malaga:FairArea_1",
  "appliesOn": "2018-03-19",
  "exceptionType": "1"
}
```

## Summary of mappings to GTFS

| GTFS Field                | NGSI Attribute          | LinkedGTFS                  | Comment                                                    |
|:--------------------------|:------------------------|:--------------------------- |:-----------------------------------------------------------|
|                           | `name`                  | `schema:name`               |                                                            |
|                           | `description`           | `schema:description`        |                                                            |
| `date`                    | `appliesOn`             | `dct:date`                  |                                                            |
| `exception_type`          | `exceptionType`         | `gtfs:dateAddition`         |                                                            |

                              


### Relationships

| GTFS Field              | NGSI Attribute        | LinkedGTFS           | Comment                                                |
|:----------------------- |:----------------------|:-------------------- |:-------------------------------------------------------|
|                         | `hasService`          | `gtfs:service`        | Shall point to another Entity of Type `gtfs:Service`  |

## Open issues