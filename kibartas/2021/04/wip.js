const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

const arr = input.split("\n\n");

const drawnNumbers = arr[0].split(",");

arr.shift();

const bingoBoards = arr
  .map((el) => el.split("\n"))
  .map((board) => {
    return board.map((row) => {
      return row.split(/\s{1,2}/).filter((num) => {
        return num.indexOf(/\s+/) === -1 && num.length > 0;
      });
    });
  });

let won = 0;

let result = 0;

const checkRowsAndColumns = (bingoBoard) => {
  // Rows
  const rowWin = bingoBoard.some((row) => {
    return row.length === row.filter((num) => num === "-1").length;
  });
  if (rowWin) return true;
  //Columns
  for (let i = 0; i < bingoBoard[0].length; i++) {
    let columnWin = true;
    for (const row of bingoBoard) {
      if (row[i] !== "-1") {
        columnWin = false;
        break;
      }
    }
    if (columnWin) {
      return true;
    }
  }
  return false;
};

let lastWon = 0;
let lastNumberWon = 0;

const wonBoards = [];

drawnNumbers.some((drawnNumber) => {
  bingoBoards.forEach((board, i) => {
    if (wonBoards.indexOf(i) !== -1) return;
    bingoBoards[i] = board.map((row) => {
      return row.map((number) => (number === drawnNumber ? "-1" : number));
    });
    if (checkRowsAndColumns(bingoBoards[i])) {
      lastWon = i;
      lastNumberWon = drawnNumber;
      wonBoards.push(i);
    }
  });
  return false;
});

const sum = bingoBoards[lastWon]
  .flatMap((el) => el)
  .filter((el) => el !== "-1")
  .reduce((el, acc) => parseInt(acc) + parseInt(el), 0);
result = sum * lastNumberWon;

console.log({ result });
