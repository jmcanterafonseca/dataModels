# gtfs:Agency

## Description

See [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)

## Data Model

+ `id`: It shall be `urn:ngsi-ld:gtfs:Agency:<agency_identifier>`
being `agency_identifier` a value that can be derived from `agency_id`. 

+ `type`: It shall be equal to `gtfs:Agency`

+ `name`: Same as `agency_name`.
    + Attribute type: Property. [Text](https://schema.org/Text).
    + Mandatory
+ `page`: Same as `agency_url`.
    + Attribute type: Property. [URL](https://schema.org/URL).
    + Optional
+ `timezone`: Same as `agency_timezone`.
    + Attribute type: Property. [Text](https://schema.org/Text).
    + Allowed values: See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)
    + Optional
+ `phone`: Same as `agency_phone`.
   + Attribute type: Property. [Text](https://schema.org/Text)
   + Optional
+ `language`: Same as `agency_language`. 
   + Attribute type: Property. [Text](https://schema.org/Text)
   + Allowed values: See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)
   + Optional
+ `address`: Agency's civic address. 
   + Attribute type: Property. [PostalAddress](https://schema.org/PostalAddress)
   + Optional


## Summary of mappings to GTFS

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
