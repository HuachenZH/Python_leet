/**
 * @param {number} n
 * @return {number}
 */
 var numberOfMatches = function(n) {
    var res=0;
    while(n!=1){
        if(n%2==1){//when n is odd
            res+=(n-1)/2;
            n++;
            n/=2;
        }else{//when n is even
            res+=n/2;
            n/=2;
        }
    }
    return res;
};
