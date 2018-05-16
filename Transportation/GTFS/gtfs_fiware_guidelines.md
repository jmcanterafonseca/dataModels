# How to map GTFS (General Transit Feed Specification) entities to NGSI(-LD) entities

## Agency

### GTFS definition

### Entity id

It shall be `urn:ngsi-ld:gtfs:Agency:<agency_id>` being `agency_id` the value of the correspoding field in the Agency feed. 

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
  "id": "urn:ngsi-ld:gtfs:Agency:EMT",
  "type": "gtfs:Agency",
  "agency_name": "Empresa Malagueña de Transportes",
  "agency_url": "http://www.emtmalaga.es/",
  "agency_timezone": "Europe/Madrid",
  "agency_lang": "ES"
}
```
