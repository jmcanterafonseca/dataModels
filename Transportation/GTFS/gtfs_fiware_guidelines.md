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
 
 Entity Attributes (Properties or Relationships) are subject to the restrictions defined by the
 [GTFS specification](https://developers.google.com/transit/gtfs/reference/#term-definitions)
 If an Attribute is an enumeration its value shall be provided as per the GTFS specification (not LinkedGTFS). 

## Agency

See [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)

### Entity id

It shall be `urn:ngsi-ld:gtfs:Agency:<agency_identifier>`

being `agency_identifier` a value that can be derived from `agency_id`. 

### Entity Type

It shall be equal to `gtfs:Agency` 

### Properties

| GTFS Field            | NGSI Attribute      | LinkedGTFS        | Comment                                                |
| --------------------- |:-------------------:| -----------------:| -------------------------------------------------------|
| agency_name           | name                | foaf:name         | 
| agency_url            | page                | foaf:page         |
| agency_timezone       | timezone            | gtfs:timezone     |
| agency_phone          | phone               | foaf:phone        |
| agency_lang           | language            | dct:language      |
|                       | address             |                   | Agency's [address](https://schema.org/address)
   


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

It represents a GTFS `stop` which `location_type` shall be equal to `0`. 

### Entity id

It shall be `urn:ngsi-ld:gtfs:Stop:<stop_identifier>`

being `stop_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Stop` 

### Properties

| GTFS Field            | NGSI Attribute        | LinkedGTFS                  | Comment                                                |
| --------------------- |:---------------------:| ---------------------------:| -------------------------------------------------------|
| stop_name             | name                  | foaf:name                   |
| stop_code             | code                  | gtfs:code                   |
| stop_url              | page                  | foaf:page                   |
| stop_desc             | description           | dct:description             |
| stop_long,stop_lat    | location              | geo:long,geo:lat            | Encoded as a GeoJSON Point.
| wheelchair_boarding   | wheelChairAccessible  | gtfs:wheelChairAccessible   | `0`, .1`, `2` as per GTFS spec.   
|                       | address               |                             | Stop's [address](https://schema.org/address)


### Relationships

| GTFS Field            | NGSI Attribute      | LinkedGTFS           | Comment                                                |
| --------------------- |:-------------------:| --------------------:| -------------------------------------------------------|
| parent_station        | parentStation       | gtfs:parentStation   | Shall point to another Entity of Type `gtfs:Station`
|                       | agency              |                      | Shall point's to stop's agency. 

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
  "agency": "urn:ngsi-ld:gtfs:Agency:Malaga_EMT"
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
  "agency": "urn:ngsi-ld:gtfs:Agency:Metro_de_Madrid",
  "parentStation": "urn:ngsi-ld:Station:Madrid:est_90_21"
}
```

## Station

See [https://developers.google.com/transit/gtfs/reference/#stoptxt](https://developers.google.com/transit/gtfs/reference/#stoptxt)

It is a GTFS `stop` which `location_type` is equal to `1`. 

### Entity id

It shall be `urn:ngsi-ld:gtfs:Station:<station_identifier>`

being `station_identifier` a value that can derived from the `stop_id` field. 

### Entity Type

It shall be equal to `gtfs:Station` 

### Properties

Same as `gtfs:Stop`. 

### Relationships

| GTFS Field            | NGSI Attribute      | LinkedGTFS           | Comment                                                |
| --------------------- |:-------------------:| --------------------:| -------------------------------------------------------|
|                       | hasStop             |                      | shall point to another Entity(ies) of type `gtfs:Stop`

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
  }
  "hasStop": ["urn:ngsi-ld:gtfs:Stop:Madrid_par_4_1"]
}
```


## Trip
