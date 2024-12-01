// read the file
const fs = require('fs');
const file = fs.readFileSync('Data/day16.txt', 'utf8');
const lines = file.split('\n');
const data = [];

for (let i = 0; i < lines.length; i++) {
    data.push([]);
    for (let j = 0; j < lines[i].length; j++) {
        data[data.length-1].push(lines[i][j]);
    }
}
// data = ['HASH']

function showGrid(grid) {
    for (let i = 0; i < grid.length; i++) {
        console.log(grid[i].join(''))
    }
}

function countCharged(grid) {
    let ans = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length;j++) {
            if (grid[i][j] === 1) {
                ans++;
            }
        }
    }
    return ans;

}

function part1(board, begining) {

    let data = JSON.parse(JSON.stringify(board));
    let chargedMAp = JSON.parse(JSON.stringify(board));

    const toStudy = [begining];
    let direction;
    let position;
    const done = [];

    while (toStudy.length > 0) {
        current = toStudy.shift();
        direction = current[1];
        position = current[0];

        if (done.includes(JSON.stringify(current))) {
            continue;
        } else {}

        if (position[1] > 0 && position[0] > 0 && position[1] < data.length && position[0] < data[0].length) {
            chargedMAp[position[1]][position[0]] = 1;
        } else {}

        done.push(JSON.stringify(current));

        while (position[1]+direction[1] >= 0 && position[0]+direction[0] >= 0 && position[1]+direction[1] < data.length && position[0]+direction[0] < data[0].length) {
            position[1] += direction[1];
            position[0] += direction[0];

            chargedMAp[position[1]][position[0]] = 1;

            if (data[position[1]][position[0]] === '.') {
                // pass
            } else if (data[position[1]][position[0]] === '-') {
                if (direction[1] !== 0) {
                    toStudy.push([[position[0], position[1]], [1,0]]);
                    toStudy.push([[position[0], position[1]], [-1,0]]);
                    break;
                } else {
                    // pass
                }
            } else if (data[position[1]][position[0]] === '|') {
                if (direction[0] !== 0) {
                    toStudy.push([[position[0], position[1]], [0,1]]);
                    toStudy.push([[position[0], position[1]], [0,-1]]);
                    break;
                } else {
                    // pass
                }
            } else if (data[position[1]][position[0]] === '/') {
                toStudy.push([[position[0], position[1]], [-direction[1], -direction[0]]]);
                break;
            } else if (data[position[1]][position[0]] === '\\'){
                toStudy.push([[position[0], position[1]], [direction[1], direction[0]]]);
                break;
            }
        }
    }
    // showGrid(chargedMAp);
    return countCharged(chargedMAp);
}
// showGrid(data);
// console.log("_________");
function part2() {
    let directions = {
        up : {
            start : [0, -1],
            end : [data[0].length, -1],
            incr : [1, 0],
            dir : [0, 1]
        },
        left : {
            start : [-1, 0],
            end : [-1, data.length],
            incr : [0, 1],
            dir : [1, 0]
        },
        down : {
            start : [0, data.length],
            end : [data[0].length, data.length],
            incr : [1, 0],
            dir : [0, -1]
        },
        right : {
            start : [data[0].length, 0],
            end : [data[0].length, data.length],
            incr : [0, 1],
            dir : [-1, 0]
        }
    }
    let ans = 0;
    let tempAns;
    let keys = Object.keys(directions);
    let current;

    for (let i = 0; i < 4; i ++) {
        current = directions[keys[i]];
        // console.log(`Doing ${keys[i]}`);

        while (JSON.stringify(current.start) !== JSON.stringify(current.end)) {
            // console.log(`Current: ${current.start}`);
            tempAns = part1(data, [JSON.parse(JSON.stringify(current.start)), JSON.parse(JSON.stringify(current.dir))]);
            if (tempAns > ans) {
                ans = tempAns;
            } else {};

            current.start[0] += current.incr[0];
            current.start[1] += current.incr[1];

        }
    }
    return ans;
}
console.log(`Part1: ${part1(data, [[-1,0], [1,0]])}`);
console.log(`Part2: ${part2()}`);