# State Server!
Simple server to tell you which state, if any, a point is in from a provided json cordinates.
Some simplified geometries are included in states.json (so greatly simplified,
that some of the smaller ones disappear).

## Behavior

  $ ./state-server &
  [1] 21507
  $ curl  -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/
  ["Pennsylvania"]
  $
