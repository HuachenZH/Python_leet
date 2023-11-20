/**
 * @param {string} val
 * @return {Object}
 */


function expect(actualValue) {
    return {
        toBe: function(expectedValue) {
            if (actualValue === expectedValue) {
                return true
            }else {
                throw new Error('Not Equal');
            }
        },
        notToBe: function(expectedValue) {
            if (actualValue !== expectedValue) {
                return true
            }else {
                throw new Error('Equal');
            }
        }
    }
};


var expect = function(actualValue) {
    return {
        toBe: function(expectedValue) {
            if (actualValue === expectedValue) {
                return true
            }else {
                throw new Error('Not Equal');
            }
        },
        notToBe: function(expectedValue) {
            if (actualValue !== expectedValue) {
                return true
            }else {
                throw new Error('Equal');
            }
        }
    };
};
    

console.log(expect(5).toBe(5)); // true
expect(5).notToBe(5); // throws "Equal"




// Example usage:
console.log(expect(5).toBe(5)); // This should pass
console.log(expect(10).toBe(5)); // This should fail
