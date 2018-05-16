# gtfs:Agency

## Description

See [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)

## Data Model

### Entity id

It shall be `urn:ngsi-ld:gtfs:Agency:<agency_identifier>`

being `agency_identifier` a value that can be derived from `agency_id`. 

### Entity Type

It shall be equal to `gtfs:Agency` 

### Properties

| GTFS Field            | NGSI Attribute      | LinkedGTFS        | Comment                                                |
|:--------------------- |:--------------------|:----------------- |:-------------------------------------------------------|
| agency_name           | name                | foaf:name         | 
| agency_url            | page                | foaf:page         |
| agency_timezone       | timezone            | gtfs:timezone     |
| agency_phone          | phone               | foaf:phone        |
| agency_lang           | language            | dct:language      |
|                       | address             |                   | Agency's [address](https://schema.org/address). Schema.org
   

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
