// read the file
const fs = require('fs');
const file = fs.readFileSync('Data/day15.txt', 'utf8');
let data = file.split(',');
// data = ['HASH']

function part1(data) {
    let ans = 0;
    let temp = 0;

    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data[i].length;j++) {
            temp += data[i].charCodeAt(j);
            temp *= 17;
            temp %= 256;
            // console.log(`${data[i][j]} ${data[i].charCodeAt(j)} ${temp}`);
        }
        //console.log(`line: ${data[i]}, value: ${temp}`);
        ans += temp;
        temp = 0;
    }
    return ans;
}



console.log(data);
console.log(`Part1: ${part1(data)}`);