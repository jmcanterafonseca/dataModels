# Urban Mobility Data Models

## Introduction

The Urban Mobility Data Models are largely based on GTFS. When an Entity Type is just a mirror of the corresponding GTFS table the Entity Type is
prefixed by .gtfs`. 

## GTFS Entities

 The General Transit Feed Specification (GTFS), also known as GTFS static or static transit,
 defines a common format for public transportation schedules and associated geographic information.
 GTFS "feeds" let public transit agencies publish their transit data and developers write applications that consume
 that data in an interoperable way.
 
 These data models are intended to map GTFS feeds into FIWARE NGSI content. Main entities are:
 
 + [gtfs:Agency](./Agency/doc/spec.md)
 + [gtfs:Stop](./Stop/doc/spec.md)
 + [gtfs:Station](./Station/doc/spec.md)
 + [gtfs:AccessPoint](./AccessPoint/doc/spec.md)
 + [gtfs:Route](./Route/doc/spec.md)
 + [gtfs:Trip](./Trip/doc/spec.md)
 + [gtfs:StopTime](./StopTime/doc/spec.md)
 + [gtfs:Service](./Service/doc/spec.md)
 + [gtfs:CalendarRule](./CalendarRule/doc/spec.md)
 + [gtfs:CalendarDateRule](./CalendarDateRule/doc/spec.md)
 
 
 ## Additional Entities
 
 + [ArrivalEstimation](./ArrivalEstimation/doc/spec.md)
 