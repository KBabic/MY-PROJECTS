/* **********1. Write a JavaScript program to display the current day and time in the following format.**********
Sample Output : Today is : Tuesday. 
Current time is : 10 PM : 30 : 38 */
/*
const days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'}

const makeHours = (h) => {
    return `${h - 12} PM`;
}   

const today = new Date();
const day = days[today.getDay()];
const min = today.getMinutes();
const sec = today.getSeconds();
let hour;
if (today.getHours() < 12) {
    hour = `${today.getHours()} AM`;
} else if(today.getHours() > 12) {
    hour = makeHours(today.getHours());
}

console.log(`Today is: ${day}.\nCurrent time is: ${hour} : ${min} : ${sec}.`);
*/

/* ********** 2. Write a JavaScript program to print the contents of the current window.********** */

//window.print();

/* ********** 3. Write a JavaScript program to get the current date. **********
Expected Output : 
mm-dd-yyyy, mm/dd/yyyy or dd-mm-yyyy, dd/mm/yyyy
*/
/*
const today = new Date();
const year = today.getFullYear();

const makeMonth = (m) => m < 10 ? `0${m + 1}` : `${m + 1}`; // months are zero-based!
const makeDay = (d) => d < 10 ? `0${d}` : `${d}`;

const month = makeMonth(today.getMonth());
const day = makeDay(today.getUTCDate());
//console.log(today);
console.log(`${month}/${day}/${year}`);
*/

/* ********** 4. Write a JavaScript program to find the area of a triangle **********
the lengths of the three of its sides are 5, 6, 7.
*/


// Area	= √p(p-a)(p-b)(p-c) where p=(a+b+c)/2
const a = 5;
const b = 6;
const c = 7;
const p = (a + b + c)/2;
const area = Math.sqrt(p*(p - a)*(p - b)*(p - c));
console.log(area);


