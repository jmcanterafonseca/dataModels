# How to represent GTFS feeds using FIWARE NGSI

## Introduction

The General Transit Feed Specification (GTFS), also known as GTFS static or
static transit, defines a common format for public transportation schedules and
associated geographic information. GTFS "feeds" let public transit agencies
publish their transit data and developers write applications that consume that
data in an interoperable way.

This document provides guidelines on how to map GTFS feeds into FIWARE NGSI
content. This work leverages on
[LinkedGTFS specification](https://github.com/OpenTransport/linked-gtfs/blob/master/spec.md).
Whenever possible the NGSI attributes map directly to GTFS fields. Nonethless
for some Entity Types extra attributes are suggested in order to better support
the data model using the NGSI information model.

## General rules

Entity Attributes (Properties or Relationships) are subject to the restrictions
defined by the
[GTFS specification](https://developers.google.com/transit/gtfs/reference/#term-definitions)
If an Attribute is an enumeration its value shall be provided as per the GTFS
specification (not LinkedGTFS).

## Summary of Entity mappings with GTFS

| GTFS Feed Member Name                                                                           | NGSI Entity Type                                                                                                         |
| :---------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| [agency.txt](https://developers.google.com/transit/gtfs/reference/#agencytxt)                   | [GtfsAgency](../GtfsAgency/)                                                                                             |
| [stops.txt](https://developers.google.com/transit/gtfs/reference/#stopstxt)                     | [GtfsStop](../GtfsStop/). [GtfsStation](../GtfsStation/). [GtfsAccessPoint](../GtfsAccessPoint/)                         |
| [routes.txt](https://developers.google.com/transit/gtfs/reference/#routestxt)                   | [GtfsRoute](../GtfsRoute/)                                                                                               |
| [trips.txt](https://developers.google.com/transit/gtfs/reference/#tripstxt)                     | [GtfsTrip](../GtfsTrip/). See also [GtfsService](../GtfsService/)                                                        |
| [stop_times.txt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt)           | [GtfsStopTime](../GtfsStopTime/)                                                                                         |
| [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)               | [GtfsCalendarRule](../GtfsCalendarRule/)                                                                                 |
| [calendar_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt)   | [GtfsCalendarDateRule](../GtfsCalendarDateRule/)                                                                         |
| [fare_attributes.txt](https://developers.google.com/transit/gtfs/reference/#fare_attributestxt) | N/A                                                                                                                      |
| [fare_rules.txt](https://developers.google.com/transit/gtfs/reference/#fare_rulestxt)           | N/A                                                                                                                      |
| [shapes.txt](https://developers.google.com/transit/gtfs/reference/#shapestxt)                   | See [GtfsRoute](../GtfsRoute/), [GtfsTrip](../GtfsTrip/)                                                                 |
| [frequencies.txt](https://developers.google.com/transit/gtfs/reference/#frequenciestxt)         | [GtfsFrequency](../GtfsFrequency/)                                                                                       |
| [transfers.txt](https://developers.google.com/transit/gtfs/reference/#transferstxt)             | [GtfsTransferRule](../GtfsTransferRule/)                                                                                 |
| [feedinfo.txt](https://developers.google.com/transit/gtfs/reference/#feed_infotxt)              | N/A                                                                                                                      |
