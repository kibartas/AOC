const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim()
  .split(",");

for (let i = 0; i < 80; i++) {
  const newFishes = [];
  input.forEach((fish, index) => {
    if (fish === 0) {
      input[index] = 6;
      newFishes.push(8);
    } else {
      input[index]--;
    }
  });
  input.push(...newFishes);
}

let result = input.length;
console.log({ result });
