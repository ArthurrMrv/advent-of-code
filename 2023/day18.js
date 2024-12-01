// read the file
const fs = require('fs');
const file = fs.readFileSync('Data/day18_example.txt', 'utf8');
const lines = file.split('\n');
const data = [];

// for (let i = 0; i < lines.length; i++) {
//     data.push([]);
//     for (let j = 0; j < lines[i].length; j++) {
//         data[data.length-1].push(lines[i][j]);
//     }
// }
// data = ['HASH']

for (let i = 0; i < lines.length; i++) {
    data.push(lines[i].split(' '));
}

function showGrid(grid) {
    for (let i = 0; i < grid.length; i++) {
        console.log(grid[i].join(''))
    }
}

function part1(data) {

    let dicDir = {
        'R' : [1, 0],
        'L' : [-1, 0],
        'U' : [0, -1],
        'D' : [0, 1]
    }

    const grid = [['#']];
    let currentPos = [0, 0]
    let currentDir = JSON.parse(JSON.stringify(dicDir['R']));

    for (let i = 1; i < data.length; i++) {
        for (let j = 0; j < data[i][1]; j++) {
            currentPos[0] += currentDir[0];
            currentPos[1] += currentDir[1];

            if (currentPos[0] > 0 && currentPos[1] > 0 && currentPos[0] < grid[0].length && currentPos[1] < grid.length) {
            } else if (currentPos[0] < 0) {
                currentPos[0] += 1;
                for (let k = 0; k < grid.length; k++) {
                    grid[k].unshift('.');
                }
            } else if (currentPos[1] < 0) {
                currentPos[1] += 1;
                grid.unshift([]);
                for (let k = 0; k < grid[1].length; k++) {
                    grid[0].push('.');
                }
            } else if (currentPos[0] >= grid[0].length) {
                for (let k = 0; k < grid.length; k++) {
                    grid[k].push('.');
                }
            } else if (currentPos[1] >= grid.length) {
                grid.push([]);
                for (let k = 0; k < grid[0].length; k++) {
                    grid[grid.length-1].push(' ');
                }
            }
            grid[currentPos[1]][currentPos[0]] = '#';
        }
        currentDir = JSON.parse(JSON.stringify(dicDir[data[i][0]]));
    }
    showGrid(grid);
    let ans = 0;
    console.log(grid.length, grid[0].length)

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            //console.log(j)
            console.log(`i: ${i}, j: ${j}, grid[i][j]: ${grid[i][j]}, ${grid[i].splice(0, j).filter(x => x === '#')}, ${ans}`)
            if (grid[i][j] === '#') {
                ans++;
            } else if (grid[i].splice(0, j).filter(x => x === '#').length%2 === 1) {
                ans++;
            } else {};
        }
    }
    return ans;
}
console.log(`Part 1: ${part1(data)}`);