# How to represent GTFS feeds using FIWARE NGSI

## Introduction

 The General Transit Feed Specification (GTFS), also known as GTFS static or static transit,
 defines a common format for public transportation schedules and associated geographic information.
 GTFS "feeds" let public transit agencies publish their transit data and developers write applications that consume
 that data in an interoperable way.
 
 This document provides guidelines on how to map GTFS feeds into FIWARE NGSI content.
 This work leverages on [LinkedGTFS specification](https://github.com/OpenTransport/linked-gtfs/blob/master/spec.md).
 Whenever possible the NGSI attributes map directly to GTFS fields. Nonethless for some Entity Types extra attributes are suggested in order
 to better support the data model using the NGSI information model. 
 
 ## General rules
 
 Entity Attributes (Properties or Relationships) are subject to the restrictions defined by the [GTFS specification](https://developers.google.com/transit/gtfs/reference/#term-definitions)

## Agency

See [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)

### Entity id

It shall be `urn:ngsi-ld:gtfs:Agency:<agency_identifier>` being `agency_identifier` a value that can be derived from `agency_id`. 

### Entity Type

It shall be equal to `gtfs:Agency` 

### Properties

| GTFS Field            | NGSI Attribute      | LinkedGTFS        | Comment                                                 |
| --------------------- |:-------------------:| -----------------:| -------------------------------------------------------:|
| agency_name           | name                | foaf:name         | 
| agency_url            | page                | foaf:page         |
| agency_timezone       | timezone            | gtfs:timezone     |
| agency_phone          | phone               | foaf:phone        |
| agency_lang           | language            | dct:language      |
|                       | address             |                   | [https://schema.org/address](https://schema.org/address)
   


### Relationships

None

### Example

```json
{
  "id": "urn:ngsi-ld:gtfs:Agency:Malaga_EMT",
  "type": "gtfs:Agency",
  "name": "Empresa Malagueña de Transportes",
  "page": "http://www.emtmalaga.es/",
  "timezone": "Europe/Madrid",
  "language": "ES"
}
```

## Stop

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It represents a GTFS `stop` which `location_type` shall be 0. 

### Entity id

It shall be `urn:ngsi-ld:gtfs:Stop:<stop_identifier>` being `stop_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Stop` 

### Properties

Entity's properties are enumerated below:

`stop_name,stop_desc,stop_url`

`stop_lat` and `stop_long` shall be mapped to a `location` property, encoded as a GeoJSON point.

### Relationships

The field `parent_station` shall be mapped to a Relationship which shall point to another entity of type `gtfs:Station`
(GTFS stop with `location_type` attribute equal to `1`). 

### Example

```json
{
  "id": "urn:ngsi-ld:gtfs:Stop:Malaga_101",
  "type": "gtfs:Stop",
  "stop_code": "101",
  "stop_name": "Alameda Principal (Sur)",
  "location": {
    "type": "Point",
    "coordinates": [-4.424393,36.716872]
  }
}
```

## Station

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

`location_type` shall be `1`. 

### Entity id

It shall be `urn:ngsi-ld:gtfs:Station:<station_identifier>` being `station_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Station` 

### Properties

Entity's properties are enumerated below:

`stop_name,stop_desc,stop_url`

`stop_lat` and `stop_long` shall be mapped to a `location` property, encoded as a GeoJSON point.

### Relationships

`has_stops` is a Relationship which shall point to another entity of type `gtfs:Stop`
(GTFS stop with `location_type` attribute equal to `0`). 

### Example

```json
{
  "id": "urn:ngsi-ld:gtfs:Station:Malaga_101",
  "type": "gtfs:Station",
  "stop_code": "101",
  "stop_name": "Alameda Principal (Sur)",
  "location": {
    "type": "Point",
    "coordinates": [-4.424393,36.716872]
  }
}
```


## Trip
