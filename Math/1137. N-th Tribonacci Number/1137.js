var tribonacci = function(n) {
    var tribo = [0,1,1];
    if (n<3) {
        return tribo[n];
    }
    for (var i=0; i<n-2; i++){
        var last = parseInt(tribo.slice(-1));
        var secondLast = parseInt(tribo.slice(-2,-1));
        var thirdLast = parseInt(tribo.slice(-3,-2));
        var res = last + secondLast + thirdLast;
        tribo.push(res);
    }
    return tribo[n];
}

console.log(tribonacci(25))


/*
var test = function(n) {
    console.log(n)
    return
}
test(5)
*/