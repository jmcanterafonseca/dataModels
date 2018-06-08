# gtfs:AccessPoint

## Description

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It is a GTFS `stop` which `location_type` is equal to `2`.

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:gtfs:AccessPoint:<access_point_identifier>` being `access_point_identifier` a value that can derived from the `stop_id` field. 

+ `type`: Entity Type 
  + It shall be equal to `gtfs:AccessPoint` 

Attributes shall be the same as [gtfs:Stop](../../Stop/doc/spec.md), i.e.
 
+ `name`  
+ `code`  
+ `page
+ `description`
+ `location`
+ `wheelChairAccessible`
+ `zoneCode`
+ `address`
+ `hasParentStation`


### Examples

```json
{
  "id": "urn:ngsi-ld:AccessPoint:Madrid:acc_4_1_3",
  "type": "gtfs:AccessPoint",
  "name": "Bravo Murillo",
  "location": {
    "type": "Point",
    "coordinates": [-3.69036,40.46629]
  },
  "address": {
    "type": "PostalAddress",
    "streetAddress": "Calle de Bravo Murillo 377",
    "addressLocality": "Madrid",
    "addressCountry": "ES"
  },
  "hasParentStation": "urn:ngsi-ld:Station:Madrid:est_90_21"
}
```

## Summary of GTFS Mappings

### Properties

Same as `gtfs:Stop`. 

### Relationships

| GTFS Field            | NGSI Attribute      | LinkedGTFS           | Comment                                                |
|:--------------------- |:--------------------|:---------------------|:-------------------------------------------------------|
|                       | hasParentStation    |                      | shall point to another Entity(ies) of type `gtfs:Station`

## Open issues
