// const inputString = `Monkey 0:
//   Starting items: 79, 98
//   Operation: new = old * 19
//   Test: divisible by 23
//     If true: throw to monkey 2
//     If false: throw to monkey 3

// Monkey 1:
//   Starting items: 54, 65, 75, 74
//   Operation: new = old + 6
//   Test: divisible by 19
//     If true: throw to monkey 2
//     If false: throw to monkey 0

// Monkey 2:
//   Starting items: 79, 60, 97
//   Operation: new = old * old
//   Test: divisible by 13
//     If true: throw to monkey 1
//     If false: throw to monkey 3

// Monkey 3:
//   Starting items: 74
//   Operation: new = old + 3
//   Test: divisible by 17
//     If true: throw to monkey 0
//     If false: throw to monkey 1`;

// const monkeys = [
//   {
//     name: "Monkey 0",
//     startingItems: [79, 98],
//     operation: (old) => old * 19,
//     test: (newItem) => newItem % 23 === 0,
//     testNumber: 23,
//     ifTrue: 2,
//     ifFalse: 3,
//     timesInspected: 0,
//   },
//   {
//     name: "Monkey 1",
//     startingItems: [54, 65, 75, 74],
//     operation: (old) => old + 6,
//     test: (newItem) => newItem % 19 === 0,
//     testNumber: 19,
//     ifTrue: 2,
//     ifFalse: 0,
//     timesInspected: 0,
//   },
//   {
//     name: "Monkey 2",
//     startingItems: [79, 60, 97],
//     operation: (old) => old * old,
//     test: (newItem) => newItem % 13 === 0,
//     testNumber: 13,
//     ifTrue: 1,
//     ifFalse: 3,
//     timesInspected: 0,
//   },
//   {
//     name: "Monkey 3",
//     startingItems: [74],
//     operation: (old) => old + 3,
//     test: (newItem) => newItem % 17 === 0,
//     testNumber: 17,
//     ifTrue: 0,
//     ifFalse: 1,
//     timesInspected: 0,
//   },
// ];

const inputString = `Monkey 0:
  Starting items: 62, 92, 50, 63, 62, 93, 73, 50
  Operation: new = old * 7
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 1:
  Starting items: 51, 97, 74, 84, 99
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 2:
  Starting items: 98, 86, 62, 76, 51, 81, 95
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 3:
  Starting items: 53, 95, 50, 85, 83, 72
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 4:
  Starting items: 59, 60, 63, 71
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 5:
  Starting items: 92, 65
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 6:
  Starting items: 78
  Operation: new = old + 8
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 7:
  Starting items: 84, 93, 54
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 1`;

const monkeys = [
  {
    name: "Monkey 0",
    startingItems: [62, 92, 50, 63, 62, 93, 73, 50],
    operation: (old) => old * 7,
    test: (newItem) => newItem % 2 === 0,
    testNumber: 2,
    ifTrue: 7,
    ifFalse: 1,
    timesInspected: 0,
  },
  {
    name: "Monkey 1",
    startingItems: [51, 97, 74, 84, 99],
    operation: (old) => old + 3,
    test: (newItem) => newItem % 7 === 0,
    testNumber: 7,
    ifTrue: 2,
    ifFalse: 4,
    timesInspected: 0,
  },
  {
    name: "Monkey 2",
    startingItems: [98, 86, 62, 76, 51, 81, 95],
    operation: (old) => old + 4,
    test: (newItem) => newItem % 13 === 0,
    testNumber: 13,
    ifTrue: 5,
    ifFalse: 4,
    timesInspected: 0,
  },
  {
    name: "Monkey 3",
    startingItems: [53, 95, 50, 85, 83, 72],
    operation: (old) => old + 5,
    test: (newItem) => newItem % 19 === 0,
    testNumber: 19,
    ifTrue: 6,
    ifFalse: 0,
    timesInspected: 0,
  },
  {
    name: "Monkey 4",
    startingItems: [59, 60, 63, 71],
    operation: (old) => old * 5,
    test: (newItem) => newItem % 11 === 0,
    testNumber: 11,
    ifTrue: 5,
    ifFalse: 3,
    timesInspected: 0,
  },
  {
    name: "Monkey 5",
    startingItems: [92, 65],
    operation: (old) => old * old,
    test: (newItem) => newItem % 5 === 0,
    testNumber: 5,
    ifTrue: 6,
    ifFalse: 3,
    timesInspected: 0,
  },
  {
    name: "Monkey 6",
    startingItems: [78],
    operation: (old) => old + 8,
    test: (newItem) => newItem % 3 === 0,
    testNumber: 3,
    ifTrue: 0,
    ifFalse: 7,
    timesInspected: 0,
  },
  {
    name: "Monkey 7",
    startingItems: [84, 93, 54],
    operation: (old) => old + 1,
    test: (newItem) => newItem % 17 === 0,
    testNumber: 17,
    ifTrue: 2,
    ifFalse: 1,
    timesInspected: 0,
  },
];

function printMonkeyIspectedTimes() {
  for (let i = 0; i < monkeys.length; i++) {
    const monkey = monkeys[i];
    console.log(`${monkey.name} inspected ${monkey.timesInspected} items`);
  }
}

function getMonkeyIspectedTimes() {
  const times = [];
  for (let i = 0; i < monkeys.length; i++) {
    const monkey = monkeys[i];
    times.push(monkey.timesInspected);
  }
  //order times descending
  times.sort((a, b) => b - a);
  return times;
}

function printMonkeyHoldings() {
  for (let i = 0; i < monkeys.length; i++) {
    const monkey = monkeys[i];
    console.log(`${monkey.name} holds ${monkey.startingItems}`);
  }
  console.log("=====================================");
}

function main() {
  const roundCount = 1;
  for (let i = 0; i < roundCount; i++) {
    for (let j = 0; j < monkeys.length; j++) {
      const monkey = monkeys[j];
      const items = monkey.startingItems;
      for (let k = 0; k < items.length; k++) {
        const item = items[k];
        const newItem = parseInt(monkey.operation(item) / 3);
        if (monkey.test(newItem)) {
          monkeys[monkey.ifTrue].startingItems.push(newItem);
        } else {
          monkeys[monkey.ifFalse].startingItems.push(newItem);
        }
        monkey.startingItems = monkey.startingItems.filter((x) => x !== item);
        monkey.timesInspected++;
      }
    }
    printMonkeyHoldings();
  }
  printMonkeyIspectedTimes();
  const orderedTimes = getMonkeyIspectedTimes();
  console.log(orderedTimes[0] * orderedTimes[1]);
}

function calculateCommonDivider() {
  let commonDivider = 1;
  for (let i = 0; i < monkeys.length; i++) {
    const monkey = monkeys[i];
    commonDivider = commonDivider * monkey.testNumber;
  }
  return commonDivider;
}

function main2() {
  const commonDivider = calculateCommonDivider();
  const roundCount = 10000;
  for (let i = 0; i < roundCount; i++) {
    for (let j = 0; j < monkeys.length; j++) {
      const monkey = monkeys[j];
      const items = monkey.startingItems;
      for (let k = 0; k < items.length; k++) {
        const item = items[k];
        const newItem = parseInt(monkey.operation(item) % commonDivider);
        if (monkey.test(newItem)) {
          monkeys[monkey.ifTrue].startingItems.push(newItem);
        } else {
          monkeys[monkey.ifFalse].startingItems.push(newItem);
        }
        monkey.startingItems = monkey.startingItems.filter((x) => x !== item);
        monkey.timesInspected++;
      }
    }
    // printMonkeyHoldings();
  }
  printMonkeyIspectedTimes();
  const orderedTimes = getMonkeyIspectedTimes();
  console.log(orderedTimes[0] * orderedTimes[1]);
}

// main();
main2();
