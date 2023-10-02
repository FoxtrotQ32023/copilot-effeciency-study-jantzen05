# __Airline Hub__

World Wide Flyer (WWF) has landing rights at several airports throughout the world.  
They wish to place their central hub at the airport that minimizes the maximum direct flying distance from the hub to any other airport in the world.

## __Input__
Input file (_airlinehub.in_) contains several sets of input.  
Each set consists of a line containing 1 <= _n_ <= 1000, the number of airports.  
_n_ lines follow, each giving the latitude (between -180 and +180 degrees) and longitude (between -90 and +90 degrees) of an airport.  
The input floating point numbers will not have more than two digits after the decimal point.  
Input is terminated by end of file.

## __Output__
For each set of input print the latitude and longitude of the airport that best serves as a hub in a single line.  
If there is more than one airport that best serves as a hub print the one that appears last in the input of the corresponding input set.  
Your output should always contain two digits after the decimal point.

## __Sample Input 1__

``` text
3
3.2 -15.0
20.1 -175
-30.2 10
3
52.31 4.76
51.96 4.44
51.45 5.37
```

## __Sample Output 1__
``` text
3.20 -15.00
52.31 4.76
```