const input = `move 5 from 4 to 5
move 2 from 5 to 8
move 2 from 9 to 1
move 2 from 9 to 1
move 1 from 5 to 3
move 10 from 5 to 8
move 1 from 4 to 7
move 1 from 1 to 2
move 5 from 3 to 7
move 1 from 2 to 8
move 21 from 8 to 5
move 13 from 5 to 7
move 2 from 9 to 4
move 1 from 7 to 4
move 5 from 1 to 4
move 1 from 5 to 7
move 2 from 2 to 7
move 1 from 3 to 2
move 1 from 1 to 6
move 7 from 5 to 9
move 16 from 7 to 4
move 7 from 9 to 3
move 1 from 7 to 5
move 1 from 3 to 8
move 3 from 2 to 7
move 1 from 8 to 9
move 3 from 3 to 6
move 21 from 4 to 9
move 1 from 5 to 7
move 4 from 4 to 9
move 8 from 6 to 3
move 6 from 7 to 1
move 12 from 9 to 8
move 6 from 7 to 2
move 3 from 6 to 5
move 1 from 6 to 9
move 4 from 8 to 6
move 3 from 8 to 5
move 4 from 1 to 8
move 4 from 6 to 1
move 2 from 1 to 3
move 1 from 5 to 8
move 2 from 2 to 8
move 5 from 8 to 3
move 4 from 2 to 7
move 5 from 8 to 1
move 2 from 1 to 7
move 1 from 8 to 2
move 2 from 1 to 7
move 11 from 9 to 2
move 1 from 8 to 5
move 2 from 9 to 4
move 3 from 9 to 5
move 2 from 5 to 1
move 6 from 5 to 8
move 2 from 4 to 2
move 1 from 5 to 6
move 7 from 1 to 8
move 2 from 2 to 7
move 13 from 8 to 1
move 16 from 3 to 1
move 3 from 2 to 1
move 12 from 7 to 6
move 15 from 1 to 8
move 2 from 3 to 8
move 16 from 1 to 2
move 24 from 2 to 8
move 1 from 1 to 5
move 1 from 5 to 8
move 3 from 6 to 7
move 26 from 8 to 3
move 20 from 3 to 9
move 1 from 2 to 9
move 16 from 9 to 3
move 14 from 3 to 1
move 13 from 1 to 6
move 3 from 3 to 4
move 3 from 9 to 4
move 1 from 7 to 8
move 5 from 8 to 2
move 8 from 8 to 5
move 18 from 6 to 1
move 4 from 8 to 5
move 6 from 4 to 1
move 2 from 2 to 5
move 5 from 3 to 8
move 5 from 8 to 7
move 2 from 5 to 8
move 5 from 5 to 4
move 3 from 2 to 8
move 22 from 1 to 2
move 1 from 1 to 2
move 5 from 8 to 2
move 2 from 5 to 2
move 1 from 1 to 6
move 5 from 5 to 2
move 1 from 9 to 8
move 5 from 4 to 1
move 6 from 6 to 9
move 3 from 1 to 9
move 1 from 1 to 7
move 8 from 9 to 6
move 6 from 7 to 1
move 5 from 6 to 5
move 27 from 2 to 1
move 4 from 5 to 7
move 9 from 1 to 5
move 1 from 9 to 1
move 3 from 6 to 2
move 9 from 2 to 1
move 2 from 7 to 2
move 1 from 8 to 7
move 10 from 5 to 9
move 1 from 9 to 7
move 25 from 1 to 8
move 6 from 7 to 4
move 11 from 1 to 7
move 3 from 8 to 1
move 3 from 2 to 6
move 3 from 8 to 9
move 11 from 8 to 6
move 1 from 2 to 6
move 12 from 6 to 4
move 13 from 4 to 5
move 1 from 6 to 1
move 3 from 7 to 5
move 5 from 8 to 7
move 1 from 7 to 1
move 5 from 1 to 6
move 3 from 6 to 4
move 3 from 8 to 6
move 2 from 5 to 2
move 12 from 5 to 9
move 5 from 6 to 2
move 2 from 5 to 9
move 6 from 4 to 9
move 11 from 7 to 3
move 1 from 2 to 5
move 1 from 7 to 8
move 1 from 5 to 7
move 1 from 7 to 1
move 1 from 8 to 1
move 2 from 4 to 7
move 2 from 6 to 8
move 5 from 3 to 6
move 2 from 7 to 2
move 2 from 2 to 9
move 1 from 2 to 9
move 1 from 1 to 6
move 35 from 9 to 7
move 2 from 8 to 7
move 3 from 3 to 8
move 5 from 2 to 4
move 3 from 3 to 7
move 2 from 4 to 7
move 4 from 6 to 5
move 4 from 5 to 9
move 3 from 4 to 5
move 1 from 8 to 3
move 4 from 9 to 8
move 1 from 9 to 6
move 38 from 7 to 2
move 1 from 3 to 5
move 1 from 1 to 7
move 4 from 7 to 3
move 3 from 6 to 1
move 22 from 2 to 7
move 1 from 5 to 8
move 7 from 8 to 4
move 8 from 2 to 8
move 3 from 5 to 1
move 4 from 3 to 9
move 1 from 8 to 3
move 1 from 3 to 7
move 2 from 2 to 3
move 5 from 8 to 9
move 3 from 9 to 1
move 2 from 1 to 7
move 6 from 2 to 3
move 6 from 3 to 1
move 2 from 3 to 6
move 1 from 6 to 1
move 14 from 7 to 2
move 4 from 1 to 6
move 8 from 1 to 3
move 4 from 3 to 6
move 3 from 9 to 5
move 1 from 8 to 6
move 1 from 8 to 4
move 9 from 7 to 1
move 8 from 2 to 4
move 4 from 2 to 9
move 2 from 2 to 1
move 3 from 5 to 8
move 1 from 8 to 6
move 1 from 7 to 8
move 1 from 6 to 5
move 3 from 9 to 5
move 2 from 9 to 5
move 4 from 3 to 9
move 3 from 6 to 3
move 3 from 6 to 9
move 9 from 4 to 1
move 1 from 9 to 8
move 3 from 3 to 6
move 2 from 7 to 4
move 4 from 8 to 5
move 7 from 5 to 6
move 19 from 1 to 9
move 5 from 9 to 3
move 2 from 1 to 6
move 1 from 4 to 6
move 4 from 3 to 2
move 21 from 9 to 7
move 1 from 1 to 2
move 1 from 9 to 1
move 1 from 1 to 8
move 16 from 7 to 6
move 24 from 6 to 5
move 7 from 4 to 5
move 1 from 8 to 3
move 2 from 2 to 8
move 31 from 5 to 8
move 1 from 4 to 6
move 2 from 6 to 9
move 1 from 7 to 4
move 3 from 7 to 9
move 1 from 4 to 8
move 2 from 3 to 5
move 1 from 2 to 3
move 1 from 3 to 7
move 1 from 7 to 9
move 24 from 8 to 6
move 1 from 8 to 1
move 30 from 6 to 1
move 2 from 5 to 2
move 1 from 6 to 9
move 6 from 9 to 7
move 1 from 6 to 4
move 1 from 4 to 6
move 23 from 1 to 3
move 21 from 3 to 4
move 4 from 2 to 6
move 3 from 6 to 1
move 1 from 5 to 1
move 4 from 1 to 9
move 3 from 9 to 6
move 8 from 1 to 6
move 4 from 8 to 5
move 2 from 7 to 5
move 7 from 4 to 3
move 3 from 4 to 9
move 9 from 3 to 9
move 1 from 7 to 6
move 6 from 5 to 8
move 14 from 6 to 2
move 4 from 8 to 4
move 7 from 4 to 5
move 1 from 7 to 9
move 6 from 4 to 3
move 13 from 2 to 6
move 5 from 3 to 7
move 1 from 3 to 8
move 1 from 8 to 2
move 4 from 8 to 3
move 6 from 6 to 4
move 2 from 2 to 8
move 5 from 4 to 7
move 3 from 7 to 5
move 1 from 7 to 9
move 2 from 3 to 9
move 3 from 7 to 3
move 1 from 7 to 9
move 1 from 7 to 9
move 3 from 4 to 1
move 6 from 6 to 1
move 2 from 7 to 5
move 1 from 3 to 5
move 11 from 9 to 4
move 9 from 4 to 5
move 3 from 3 to 4
move 1 from 3 to 9
move 2 from 8 to 1
move 9 from 1 to 8
move 22 from 5 to 8
move 2 from 1 to 3
move 3 from 4 to 6
move 14 from 8 to 9
move 1 from 3 to 9
move 19 from 9 to 3
move 3 from 9 to 4
move 2 from 7 to 2
move 1 from 4 to 6
move 1 from 3 to 8
move 8 from 3 to 1
move 2 from 9 to 6
move 1 from 2 to 5
move 3 from 4 to 9
move 1 from 2 to 3
move 20 from 8 to 3
move 4 from 9 to 5
move 1 from 4 to 2
move 26 from 3 to 5
move 1 from 8 to 3
move 8 from 1 to 4
move 1 from 3 to 7
move 1 from 2 to 1
move 1 from 1 to 6
move 1 from 6 to 7
move 4 from 5 to 3
move 3 from 4 to 2
move 5 from 5 to 3
move 2 from 2 to 6
move 3 from 3 to 5
move 2 from 4 to 8
move 5 from 3 to 9
move 5 from 9 to 8
move 19 from 5 to 9
move 1 from 5 to 2
move 2 from 7 to 1
move 1 from 1 to 7
move 1 from 7 to 4
move 13 from 9 to 3
move 8 from 6 to 2
move 10 from 3 to 5
move 14 from 5 to 4
move 7 from 8 to 4
move 1 from 6 to 2
move 6 from 3 to 8
move 4 from 9 to 7
move 2 from 9 to 8
move 1 from 7 to 1
move 3 from 2 to 7
move 1 from 5 to 3
move 7 from 8 to 6
move 5 from 6 to 2
move 8 from 4 to 5
move 3 from 5 to 8
move 3 from 8 to 6
move 5 from 7 to 9
move 5 from 3 to 6
move 1 from 9 to 4
move 17 from 4 to 7
move 1 from 8 to 1
move 12 from 7 to 8
move 3 from 1 to 4
move 2 from 4 to 6
move 8 from 6 to 1
move 4 from 6 to 3
move 1 from 7 to 8
move 5 from 5 to 8
move 4 from 7 to 1
move 3 from 2 to 6
move 2 from 5 to 1
move 6 from 1 to 6
move 4 from 3 to 5
move 4 from 5 to 3
move 1 from 4 to 8
move 3 from 3 to 2
move 17 from 8 to 4
move 6 from 6 to 3
move 14 from 4 to 9
move 1 from 3 to 8
move 1 from 7 to 4
move 3 from 8 to 3
move 5 from 2 to 5
move 6 from 1 to 7
move 2 from 6 to 4
move 4 from 5 to 7
move 1 from 1 to 5
move 1 from 6 to 3
move 10 from 7 to 4
move 1 from 5 to 4
move 1 from 2 to 3
move 15 from 4 to 5
move 3 from 3 to 1
move 6 from 2 to 6
move 1 from 2 to 3
move 2 from 4 to 7
move 2 from 7 to 8
move 1 from 4 to 2
move 2 from 1 to 7
move 1 from 7 to 2
move 12 from 9 to 1
move 4 from 9 to 5
move 4 from 6 to 2
move 1 from 7 to 3
move 6 from 2 to 4
move 1 from 8 to 5
move 2 from 4 to 2
move 11 from 1 to 7
move 3 from 1 to 4
move 17 from 5 to 6
move 15 from 6 to 4
move 1 from 8 to 9
move 10 from 4 to 1
move 1 from 3 to 9
move 2 from 6 to 5
move 1 from 2 to 6
move 4 from 5 to 6
move 4 from 1 to 2
move 6 from 6 to 7
move 2 from 2 to 6
move 9 from 4 to 9
move 6 from 1 to 2
move 3 from 4 to 1
move 10 from 9 to 8
move 4 from 2 to 1
move 1 from 1 to 2
move 5 from 8 to 6
move 1 from 2 to 7
move 1 from 9 to 4
move 2 from 6 to 9
move 13 from 7 to 2
move 5 from 7 to 5
move 2 from 5 to 2
move 1 from 4 to 5
move 4 from 8 to 4
move 17 from 2 to 6
move 3 from 4 to 6
move 2 from 9 to 1
move 7 from 6 to 8
move 1 from 5 to 2
move 1 from 4 to 1
move 2 from 9 to 4
move 1 from 3 to 9
move 4 from 3 to 7
move 2 from 8 to 5
move 3 from 7 to 5
move 10 from 5 to 8
move 2 from 2 to 4
move 6 from 1 to 2
move 4 from 6 to 3
move 8 from 2 to 6
move 1 from 7 to 4
move 5 from 4 to 5
move 7 from 6 to 7
move 5 from 3 to 5
move 5 from 5 to 2
move 4 from 8 to 1
move 6 from 1 to 6
move 3 from 3 to 2
move 22 from 6 to 2
move 1 from 9 to 7
move 8 from 8 to 6
move 1 from 7 to 6
move 2 from 5 to 7
move 4 from 8 to 5
move 7 from 6 to 7
move 2 from 6 to 4
move 14 from 2 to 1
move 7 from 1 to 3
move 12 from 7 to 3
move 1 from 4 to 3
move 2 from 5 to 8
move 2 from 8 to 1
move 1 from 4 to 3
move 6 from 2 to 9
move 6 from 9 to 2
move 2 from 2 to 7
move 6 from 7 to 5
move 13 from 3 to 5
move 5 from 2 to 6
move 5 from 6 to 1
move 2 from 3 to 6
move 1 from 6 to 5
move 1 from 6 to 1
move 3 from 1 to 9
move 6 from 2 to 7
move 1 from 2 to 3
move 24 from 5 to 2
move 7 from 3 to 7
move 13 from 7 to 9
move 4 from 1 to 9
move 4 from 1 to 6
move 1 from 5 to 6
move 16 from 9 to 5
move 1 from 6 to 4
move 1 from 5 to 2
move 5 from 1 to 3
move 11 from 2 to 1
move 4 from 9 to 6
move 1 from 4 to 7
move 2 from 3 to 4
move 6 from 6 to 9
move 1 from 1 to 3
move 2 from 9 to 4
move 1 from 7 to 9
move 4 from 2 to 9
move 8 from 9 to 2
move 3 from 3 to 2
move 1 from 9 to 4
move 5 from 1 to 7
move 1 from 4 to 8
move 2 from 1 to 9
move 1 from 8 to 7
move 6 from 5 to 3
move 1 from 5 to 1
move 5 from 2 to 3
move 4 from 1 to 5
move 4 from 7 to 1
move 8 from 5 to 8`;

const initialState = [
  ["S", "L", "W"], //1
  ["J", "T", "N", "Q"], //2
  ["S", "C", "H", "F", "J"], //3
  ["T", "R", "M", "W", "N", "G", "B"], //4
  ["T", "R", "L", "S", "D", "H", "Q", "B"], //5
  ["M", "J", "B", "V", "F", "H", "R", "L"], //6
  ["D", "W", "R", "N", "J", "M"], //7
  ["B", "Z", "T", "F", "H", "N", "D", "J"], //8
  ["H", "L", "Q", "N", "B", "F", "T"], //9
];

const movements = parseMovements();

function parseMovements() {
  const result = [];
  const splitInput = input.split("\n");
  for (let i = 0; i < splitInput.length; i++) {
    const move = splitInput[i].split(" ");
    const amount = parseInt(move[1]);
    const from = parseInt(move[3]);
    const to = parseInt(move[5]);
    result.push({ from, to, amount });
  }

  return result;
}

function move(from, to, amount) {
  const fromIndex = from - 1;
  const toIndex = to - 1;
  const fromArray = initialState[fromIndex];
  const toArray = initialState[toIndex];
  const moved = fromArray.splice(fromArray.length - amount, amount);
  //   moved.reverse(); Reversed for task 1 and not reversed for task 2
  toArray.push(...moved);
}

function solve() {
  for (let i = 0; i < movements.length; i++) {
    const { from, to, amount } = movements[i];
    move(from, to, amount);
  }
}

function getLastElementsToString() {
  const result = [];
  for (let i = 0; i < initialState.length; i++) {
    const array = initialState[i];
    result.push(array[array.length - 1]);
  }

  return result.join("");
}

solve();
console.log(getLastElementsToString());
// console.log(getLastElementsToString());
