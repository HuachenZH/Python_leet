/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let num1 = 0;
    let num2 = 0;
    for (let i=1; i<n+1; i++){
       // not divisible
       if (i % m != 0){
           num1 += i; 
       }else{ // divisible
           num2 += i;
       }
    }
    return num1 - num2
};

console.log(differenceOfSums(10,3))