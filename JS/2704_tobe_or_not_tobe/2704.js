/**
 * @param {string} val
 * @return {Object}
 */
/*
var expect = function(val) {
    return {
        toBe: function(val2) {
            console.log(var2)
        }
    };
};
    

expect(5).toBe(5); // true
// expect(5).notToBe(5); // throws "Equal"
*/

function expect(actualValue) {
    return {
        toBe: function(expectedValue) {
            if (actualValue == expectedValue) {
                return {"value": true}
            }else {
                return {"error": "Not Equal"}
            }
        },
        notToBe: function(expectedValue) {
            
        }
    }
};

// Example usage:
expect(5).toBe(5); // This should pass
expect(10).toBe(5); // This should fail