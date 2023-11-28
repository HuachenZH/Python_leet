/**
 * @param {number} candies
 * @param {number} num_people
 * @return {number[]}
 */
var distributeCandies = function(candies, num_people) {
    var ans = Array(num_people).fill(0);
    let remain = candies;
    let candiesToGive = 1;
    let indexPeople = 0;
    while (remain > candiesToGive) {
        console.log(`indexPeople is ${indexPeople}`);
        console.log(`candiesToGive is ${candiesToGive}`);
        ans[indexPeople] += candiesToGive;
        remain -= candiesToGive;
        candiesToGive -=- 1;
        indexPeople -=- 1;
        if (indexPeople > num_people-1) {
            indexPeople = 0;
            console.log("indexPeople reset");
        }
        console.log(`remain is ${remain}`);
        console.log(`answer is ${ans}`);
        console.log('  --  ');
    }
    ans[indexPeople] += remain;
    return ans
};

// (function() =>{}) ()

// var test = "";

(function () {
  console.log(Array(5));  // [ <5 empty items> ]
  console.log(Array(5).keys()); // Object [Array Iterator] {}
  console.log([...Array(5).keys()]); // [ 0, 1, 2, 3, 4 ]
  console.log(Array(5).fill(0)); // [ 0, 0, 0, 0, 0 ]
  console.log("new results here");
})();

distributeCandies(7,4);