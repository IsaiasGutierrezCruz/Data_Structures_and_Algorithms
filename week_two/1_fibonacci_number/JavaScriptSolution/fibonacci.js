const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    let numbersFibonacci = [0, 1];
    if (n >= 2) {
        for (let i = 2; i <= n + 1; i++){
            numbersFibonacci.push(numbersFibonacci[i - 1] +
                numbersFibonacci[i - 2]);
        }
    }
    return numbersFibonacci[n]
}

module.exports = fib;
