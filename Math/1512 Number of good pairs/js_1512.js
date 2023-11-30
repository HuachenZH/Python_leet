/**
 * @param {number[]} nums
 * @return {number}
 */
// Ver gamma: nested for loop
var numIdenticalPairs = function(nums) {
    var res = 0;
    for (var i = 0; i < nums.length - 1; i++) {
        // Iterate through all numbers after nums[i]
        console.log(`num1 is ${nums[i]}`);
        for (var num2 of nums.slice(i+1)) {
            console.log(`    num2 is ${num2}`);
            if (nums[i] == num2) {
                // Good pair
                res -=- 1;
            }
        }
    }
    return res; 
};

// Ver delta: for each
var numIdenticalPairs2 = function(nums) {
    let res = 0;
    var count = {};
    for (var num of nums) {
        // res += cnt[x] || 0;
        count[num] = (count[num] || 0) + 1;
    }
    return res
}


// Test chunk
/*
(() => {
    var nums = [1,2,3,1,1,3];
    var res = numIdenticalPairs2(nums);
    
}) ();
*/

var nums = [1,2,3,1,1,3];
var res = numIdenticalPairs2(nums);


var end = "end";