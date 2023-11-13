/**
 * @param {number} n
 * @return {Function} counter
 */

// first try, test passed
var createCounter = function(n) {
    var counter = n
    // the line below printed only once, no matter how
    // many times i called the counter
    console.log("counter initialized")
    return function() {
        return counter++;
    };
}

// second try, test passed
var createCounter = function(n) {
    return function(){
        return n++;
    }
}



const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12