# Parks and gardens datamodels

These data models are intended to model parks, gardens and related green areas in a city.
In the future low granularity entities such as trees or bushes might be modelled as well.

The main entity types identified are:

+ [Park](http://schema.org/Park). A park is an area of open space provided for recreational use, usually designed and in semi-natural state with grassy areas, trees and bushes.
Parks are often but not always municipal. Typically open to the public, but may be fenced off, and may be temporarily closed e.g. at night time.
[See OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dpark). Schema.org already provides an entity type for this purpose which can be reused. 

+ [Garden](../Garden/doc/spec.md). A garden is a distinguishable planned space, usually outdoors, set aside for the display, cultivation,
and enjoyment of plants and other forms of nature.
A garden can incorporate both natural and man-made materials. Western gardens are almost universally based on plants.
A garden can also be a part of a park and open to the public. [See OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dgarden).
A garden can be divided into several smaller parts, named flower beds (parterres). 

+ [FlowerBed](../FlowerBed/doc/spec.md). A garden plot in which flowers (or other plants) are grown.
Usually you will find flowerbeds in parks, gardens, pedestrian areas or at big highway interchanges.
[See OpenStreetMap](http://wiki.openstreetmap.org/wiki/Proposed_features/flowerbed)

+ [GardenRecord](../GardenRecord/doc/spec.md). This entity contains a harmonised description of the conditions recorded on a particular area or point inside a garden. Such record
can be associated to a garden or to an specific flowerbed inside a garden.

New entities pending to be defined:

+ `WateringPoint`
+ `GardenOperation`