# gtfs:Stop

## Description

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It represents a GTFS `stop` which `location_type` shall be equal to `0`.

## Data Model

### Entity id

It shall be `urn:ngsi-ld:gtfs:Stop:<stop_identifier>`

being `stop_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Stop` 

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