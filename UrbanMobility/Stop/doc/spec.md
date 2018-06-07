# gtfs:Stop

## Description

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It represents a GTFS `stop` which `location_type` shall be equal to `0`.

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:gtfs:Stop:<stop_identifier>` being `stop_identifier` a value that can derived from the GTFS `stop_id` field. 

+ `type`: Entity Type 
  + It shall be equal to `gtfs:Stop` 
 
+ `name`: Same as `stop_name`. 
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Mandatory
  
+ `code`: Same as `stop_code`. 
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional
  
+ `page`: Same as `stop_url`. 
  + Attribute type: Property. [URL](https://schema.org/URL)
  + Optional
  
+ `description`: Same as `stop_desc`. 
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Optional
 
+ `location`: Stop's location encoded as GeoJSON Point which coordinates shall be [`stop_long`,`stop_lat`].
  + Attribute type: GeoProperty. `geo:json`.
  + Normative References: [rfc7946](https://tools.ietf.org/html/rfc7946)
  + Mandatory if `address` is not present

+ `wheelChairAccessible`: Same as `wheelchair_boarding`. 
  + Attribute type: Property. [Text](https://schema.org/Text)
  + Allowed values: (`0`, `1`, `2`) as per the [GTFS](https://developers.google.com/transit/gtfs/reference/#stoptxt)

+ `address`: Stop's civic address. 
  + Attribute type: Property. [PostalAddress](https://schema.org/PostalAddress)
  + Mandatory if `location` is not present
  
`hasParentStation` : Same as `parent_station`.  
  + Attribute type: Relationship. It shall point to an Entity of Type [gtfs:Station](../../Station/doc/spec.md)
  + Optional

`operatedBy` : Agency that operates this stop.
  + Attribute type: Relationship. It shall point to an Entity of Type [gtfs:Agency](../../Agency/doc/spec.md)
  + Mandatory

`areaServed` : Same as `zone_id`. 
  + Attribute type: Relationship. It shall point to an Entity of Type [gtfs:Agency](../../Agency/doc/spec.md)
  + Optional
  
## Summary of GTFS mappings  

### Properties

| GTFS Field            | NGSI Attribute        | LinkedGTFS                  | Comment                                                |
|:--------------------- |:----------------------|:----------------------------|:-------------------------------------------------------|
| stop_name             | name                  | foaf:name                   |
| stop_code             | code                  | gtfs:code                   |
| stop_url              | page                  | foaf:page                   |
| stop_desc             | description           | dct:description             |
| stop_long,stop_lat    | location              | geo:long,geo:lat            | Encoded as a GeoJSON Point.
| wheelchair_boarding   | wheelChairAccessible  | gtfs:wheelChairAccessible   | `0`, `1`, `2` as per GTFS spec.   
|                       | address               |                             | Stop's [address](https://schema.org/address). Schema.org


### Relationships

| GTFS Field            | NGSI Attribute      | LinkedGTFS           | Comment                                                |
|:--------------------- |:--------------------|:-------------------- |:-------------------------------------------------------|
| parent_station        | hasParentStation    | gtfs:parentStation   | Shall point to another Entity of Type `gtfs:Station`
|                       | operatedBy          |                      | Shall point to another Entity of Type `gtfs:Agency`
| zone_id               | locatedInZone       |                      | Shall point to another Entity of Type `gtfs:Zone`.  

### Examples

```json
{
  "id": "urn:ngsi-ld:gtfs:Stop:Malaga_101",
  "type": "gtfs:Stop",
  "code": "101",
  "name": "Alameda Principal (Sur)",
  "location": {
    "type": "Point",
    "coordinates": [-4.424393,36.716872]
  },
  "operatedBy": "urn:ngsi-ld:gtfs:Agency:Malaga_EMT"
}
```

```json
{
  "id": "urn:ngsi-ld:gtfs:Stop:Madrid_par_4_1",
  "type": "gtfs:Stop",
  "code": "1",
  "name": "PLAZA DE CASTILLA",
  "location": {
    "type": "Point",
    "coordinates": [-3.68917,40.4669]
  },
  "page": "http://www.crtm.es",
  "operatedBy": "urn:ngsi-ld:gtfs:Agency:Metro_de_Madrid",
  "hasParentStation": "urn:ngsi-ld:Station:Madrid:est_90_21"
}
```
