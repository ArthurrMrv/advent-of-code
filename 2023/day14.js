// read a text file
// split the text file into an array of lines
// for each line, split it into an array of words
// for each word, split it into an array of characters

// read the file
const fs = require('fs');
const file = fs.readFileSync('Data/day14.txt', 'utf8');
const lines = file.split('\n');
const data = [];

for (let i = 0; i < lines.length; i++) {
    data.push([]);
    for (let j = 0; j < lines[i].length; j++) {
        data[data.length-1].push(lines[i][j]);
    }
}

function showGrid(grid) {
    for (let i = 0; i < grid.length; i++) {
        console.log(grid[i].toString())
    }
}

function calculateAnswer(grid) {
    let ans = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length;j++) {
            if (grid[i][j] === 'O') {
                ans += grid.length - i;
            }
        }
    }
    return ans;
}

function part1(board) {

    let data = JSON.parse(JSON.stringify(board));

    for (let i = 1; i < data.length; i++) {
        for (let j = 0; j < data[i].length; j++) {

            if (data[i][j] == 'O') {
                let idx = i;
                while (idx > 0 && data[idx-1][j] === '.') {
                    data[idx-1][j] = 'O';
                    data[idx][j] = '.';
                    idx--;
                }
            }
        }
    }

    return calculateAnswer(data);
}

function part2 (board, cycles) {
    let data = JSON.parse(JSON.stringify(board));
    let seen = [];
    let repeat_index;
    let temp;

    for (let c = 1; c < cycles+1; c++) {
        // north
        for (let i = 1; i < data.length; i++) {
            for (let j = 0; j < data[i].length; j++) {
                if (data[i][j] == 'O') {
                    let idx = i;
                    while (idx > 0 && data[idx-1][j] === '.') {
                        data[idx-1][j] = 'O';
                        data[idx][j] = '.';
                        idx--;
                    }
                }
            }
        }

        // west
        for (let j = 1; j< data[0].length;j++) {
            for (let i = 0; i < data.length; i++) {
                if (data[i][j] == 'O') {
                    let idx = j;
                    while (idx > 0 && data[i][idx-1] === '.') {
                        data[i][idx-1] = 'O';
                        data[i][idx] = '.';
                        idx--;
                    }
                }
            }
        }

        // south
        for (let i = data.length-1; i >= 0; i--) {
            for (let j = 0; j < data[i].length; j++) {
                if (data[i][j] == 'O') {
                    let idx = i;
                    while (idx < data.length-1 && data[idx+1][j] === '.') {
                        data[idx+1][j] = 'O';
                        data[idx][j] = '.';
                        idx++;
                    }
                }
            }
        }

        // east
        for (let j = data[0].length-1; j >= 0;j--) {
            for (let i = 0; i < data.length; i++) {
                if (data[i][j] == 'O') {
                    let idx = j;
                    while (idx < data[0].length-1 && data[i][idx+1] === '.') {
                        data[i][idx+1] = 'O';
                        data[i][idx] = '.';
                        idx++;
                    }
                }
            }
        }
        // console.log(`After ${c+1} cycles`);
        // showGrid(data);
        repeat_index = seen.indexOf(JSON.stringify(data));
        if (repeat_index > -1) {
            console.log(`Found repeat between ${c} cycle and ${repeat_index+1} cycle`);
            temp = c;
            while (temp + c-(repeat_index+1) < cycles) {
                temp += c-(repeat_index+1);
            }
            c = temp;
            console.log(`Jumping to ${c} cycle`);
            seen = [];
            
        }

        seen.push(JSON.stringify(data));
        
    }
    
    return calculateAnswer(data);

}
console.log(`Part 1: ${part1(data)}`);
console.log(`Part 2: ${part2(data, 1_000_000_000)}`);