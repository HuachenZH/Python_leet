kudo à https://www.unilim.fr/pages_perso/jean.debord/math/matrices/matrices.htm 
qui m'a aidé à réviser mon Calcul Matriciel Avancé que j'ai oublié juste après le partiel de S3.  
kudo à Mme Bhénabib.  


```shell
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
```

=>  

```shell
matrix:
94, 34
22, 67

and vector:
8400, 5400
```

=>  

```shell
matrix:
94, 22      This is matrix M
34, 67     ---> transpose

and vector:
8400, 5400   This is vector P
```

We are looking for vector x which fulfill:  
```shell
M x = P

<=>

M^-1 M x = M^-1 P

<=>

x = M^-1 P
```


Why transposing the matrix M?  
```shell
    x   y
A: 94  34
B: 22  67
G: 8400  5400
we can write as

    x   y
A: A1  A2
B: B1  B2
G: G1 G2

we are looking for vector x = (α, β),
                               ^       --> push how many times A button
                                  ^    --> push how many times B button
we have a system of linear equations:
A1 * α + B1 * β = G1
A2 * α + B2 * β = G2

Written in matrix form:
 A1  B1       α       G1 
(A2  B2)  ⋅  (β)  =  (G2)
```
Compare the two:  
```shell
 original   |  from the syst equa
 -----------|-------------------
  A1  A2    |     A1  B1
  B1  B2    |     A2  B2
see, it's transposed.
```
