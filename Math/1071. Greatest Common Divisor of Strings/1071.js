/**
 * check if str1 % str2 == 0
 * @param {string} str1 
 * @param {string} str2 
 * @returns {boolean}
 */
var divisibleString = function(str1, str2){
    if (str1.length % str2.length != 0){
        return false;
    }
    var compare = "";
    var range = Math.floor(str1.length / str2.length);
    for (var i = 0; i < range; i++){
        compare += str2;
    }
    return (compare == str1);
}



/**
 * Returns the greatest common divisor of string
 * @param {string} str1 
 * @param {string} str2 
 * @returns {string}
 */
var gcdOfStrings = function(str1, str2){
    // if their lengths are equal, then only need to test if str1 % str2 == 0
    if (str1.length == str2.length){
        if (divisibleString(str1, str2)){
            return str1;
        }
        return "";
    }
    // convention: str1 is the larger, str2 is the smaller
    if (str1.length == str2.length){
        // Swap values using destructuring assignment
        [str1, str2] = [str2, str1];
    }

    for (var i = str2.length; i>-1; i--){
        // firstly it must be a factor of the smaller stirng
        if (divisibleString(str2, str2.slice(0, i+1))){
            // check for the larger string
            if (divisibleString(str1, str2.slice(0, i+1))){
                return str2.slice(0, i+1);
            }
        }
    }
    return "";
}

var str1 = "hellohello";
var str2 = "helloo";
console.log(gcdOfStrings(str1, str2));

