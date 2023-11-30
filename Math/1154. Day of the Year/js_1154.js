/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    // Split to get day month and year
    var year = Number(date.split("-")[0]);
    var month = Number(date.split("-")[1]);
    var day = Number(date.split("-")[2]);

    // Check if it's a leap year or not.
    // Notice that 1900 is not a leap year.
    let mapp = [];
    if(year % 4 == 0 && year != 1900) {
        // Number of day of each month
        mapp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0];
    }else {
        mapp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0];
    }
    // Accumulate the number of day until month -1
    var initialValue = 0;
    let res = mapp.slice(0, month-1).reduce(
        ((accumulator, currentValue) => accumulator + currentValue), initialValue  );
    res += day;
    return res;
};


dayOfYear("2019-09-10")