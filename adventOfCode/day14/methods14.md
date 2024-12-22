

p=2,4 v=0,-3
```shell
p=2,4 v=0,-3
where 2: distance to the left wall
and 4: distance to the top wall
v=0,-3: here i put 0 for convenience and -3 means going up three tiles
leftwall
| _____________________topwall
| ........... -->0
| ..^........   -> after 1 sec
| ..|........
| ..|........
| ..1........  ->init pos 
| ...........
| ...........
  |
  |
  v
  0
```

The index seems weird to me, so in my script i will consider p=2,4 v=0,-3 as:  
```shell
In the first quadrant of a cartesian coordinate system,
p=2,4 means a point of coord (2,4)
v=0,-3 means a vector of (0,-3) (so instead of going up, it goes down)

y axis
  ^
  |
  | 
  ...........
  ...........
  ..1........  ->init pos
  ..|........
  ..|........
  ..v........
  ........... --> x axis
  ^ 
  this point is the origin.
```

After 6 secondes:
```shell
example           mine
..1........      ...........
...........      ...........
...........      ...........
...........      ...........
...........      ...........
...........      ...........
...........      ..1........

```
we can see that they are symmetric, <=> np.flip()  

and when i put them in np.zeroes, it flips again, returns to normal.  



