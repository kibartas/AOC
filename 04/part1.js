const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

const arr = input.split("\n\n");

const drawnNumbers = arr[0].split(",");

arr.shift();

// const bingoBoards = arr.map((el) => el.split("\n"));

const bingoBoards = arr
  .map((el) => el.split("\n"))
  .map((board) => {
    return board.map((row) => {
      return row.split(/\s{1,2}/).filter((num) => {
        return num.indexOf(/\s+/) === -1 && num.length > 0;
      });
    });
  });

let won = false;

let result = 0;

drawnNumbers.some((drawnNumber) => {
  bingoBoards.some((board, i) => {
    bingoBoards[i] = board.map((row) => {
      const filtered = row.filter((number) => number !== drawnNumber);
      if (filtered.length === 0) {
        won = true;
      }
      return filtered;
    });
    if (won) {
      console.log(bingoBoards[i]);
      const sum = bingoBoards[i]
        .flatMap((el) => el)
        .reduce((el, acc) => parseInt(acc) + parseInt(el), 0);
      result = sum * drawnNumber;
      return true;
    }
    return false;
  });
  if (won) return true;
  return false;
});

console.log({ result });
