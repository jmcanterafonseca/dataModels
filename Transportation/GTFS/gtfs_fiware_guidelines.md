# How to map GTFS feeds to FIWARE NGSI

## Introduction

 The General Transit Feed Specification (GTFS), also known as GTFS static or static transit,
 defines a common format for public transportation schedules and associated geographic information.
 GTFS "feeds" let public transit agencies publish their transit data and developers write applications that consume
 that data in an interoperable way.
 
 This document provides guidelines on how to map GTFS feeds into FIWARE NGSI content.

## Agency

### Entity id

It shall be `urn:ngsi-ld:gtfs:Agency:<agency_id>` being `agency_id` a value that can be derived from `agency_id`. 

### Entity Type

It shall be equal to `gtfs:Agency` 

### Properties

Entity's properties are those listed as fields at

[https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)

### Relationships

None

### Example

```json
{
  "id": "urn:ngsi-ld:gtfs:Agency:Malaga_EMT",
  "type": "gtfs:Agency",
  "agency_name": "Empresa Malagueña de Transportes",
  "agency_url": "http://www.emtmalaga.es/",
  "agency_timezone": "Europe/Madrid",
  "agency_lang": "ES"
}
```

## Stop

### Entity id

It shall be `urn:ngsi-ld:gtfs:Stop:<stop_id>` being `stop_id` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Stop` 

### Properties

Entity's properties are those listed as fields at

[https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

with the exception of `stop_lat` and `stop_long` which shall be mapped to `location`, encoded as a GeoJSON point.

### Relationships

The field `parent_station` shall be mapped to a Relationship which shall point to another entity of type `gtfs_Stop` which location_type is equal to `1`. 

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
