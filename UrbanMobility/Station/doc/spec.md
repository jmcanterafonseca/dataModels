# gtfs:Station

## Description

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It is a GTFS `stop` which `location_type` is equal to `1`.

## Data Model

### Entity id

It shall be `urn:ngsi-ld:gtfs:Station:<station_identifier>`

being `station_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Station` 

### Properties

Same as `gtfs:Stop`. 

### Relationships

| GTFS Field            | NGSI Attribute      | LinkedGTFS           | Comment                                                       |
|:--------------------- |:--------------------|:---------------------|:--------------------------------------------------------------|
|                       | hasStop             |                      | shall point to another Entity(ies) of type `gtfs:Stop`
|                       | hasAccessPoint      |                      | shall point to another Entity(ies) of type `gtfs:AccessPoint`

### Example

```json
{
  "id": "urn:ngsi-ld:Station:Madrid:est_90_21",
  "type": "gtfs:Station",
  "code": "21",
  "name": "Intercambiador de Plaza de Castilla",
  "location": {
    "type": "Point",
    "coordinates": [-3.6892,40.4669]
  },
  "address": {
    "type": "PostalAddress",
    "streetAddress": "Paseo de la Castellana 189",
    "addressLocality": "Madrid",
    "addressCountry": "ES"
  },
  "hasStop": ["urn:ngsi-ld:gtfs:Stop:Madrid_par_4_1"]
}
```
