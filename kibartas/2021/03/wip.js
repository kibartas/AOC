const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

// const binaryStrings = [
//   "00100",
//   "11110",
//   "10110",
//   "10111",
//   "10101",
//   "01111",
//   "00111",
//   "11100",
//   "10000",
//   "11001",
//   "00010",
//   "01010",
// ];

const binaryStrings = input.split("\n");
const length = binaryStrings.length;
const stringLength = binaryStrings[0].length;
const sums = new Array(stringLength).fill(0);
binaryStrings.forEach((string) => {
  for (let i = 0; i < stringLength; i++) {
    sums[i] += parseInt(string[i]);
  }
});

let oxygenBinaries = [];
sums.some((sum, index) => {
  let oxygenLength = binaryStrings.length;
  if (index !== 0) {
    sum = oxygenBinaries.reduce((acc, el) => {
      acc += parseInt(el[index]);
      return acc;
    }, 0);
    oxygenLength = oxygenBinaries.length;
  }
  let filterFor = "0";
  if (sum >= oxygenLength / 2) {
    filterFor = "1";
  }
  if (index === 0) {
    oxygenBinaries.push(
      ...binaryStrings.filter((bin) => bin[index] === filterFor)
    );
  } else {
    oxygenBinaries = oxygenBinaries.filter((bin) => bin[index] === filterFor);
  }
  console.log(oxygenBinaries);
  if (oxygenBinaries.length === 1) return true;
  return false;
});

console.log(oxygenBinaries);

let co2Binaries = [];
sums.some((sum, index) => {
  let co2Length = binaryStrings.length;
  if (index !== 0) {
    sum = co2Binaries.reduce((acc, el) => {
      acc += parseInt(el[index]);
      return acc;
    }, 0);
    co2Length = co2Binaries.length;
  }
  let filterFor = "0";
  if (sum < co2Length / 2) {
    filterFor = "1";
  }
  if (index === 0) {
    co2Binaries.push(
      ...binaryStrings.filter((bin) => bin[index] === filterFor)
    );
  } else {
    co2Binaries = co2Binaries.filter((bin) => bin[index] === filterFor);
  }
  if (co2Binaries.length === 1) return true;
  return false;
});

console.log(co2Binaries);

const convertToDecimal = (binaryString) => {
  let multiplier = 1;
  let decimal = 0;
  for (let i = binaryString.length - 1; i >= 0; i--) {
    decimal += parseInt(binaryString[i]) * multiplier;
    multiplier *= 2;
  }
  return decimal;
};

let result =
  convertToDecimal(co2Binaries[0]) * convertToDecimal(oxygenBinaries[0]);
console.log({ result });
