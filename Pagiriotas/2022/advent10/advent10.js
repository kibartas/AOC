const input = `noop
addx 7
addx -1
addx -1
addx 5
noop
noop
addx 1
addx 3
addx 2
noop
addx 2
addx 5
addx 2
addx 10
addx -9
addx 4
noop
noop
noop
addx 3
addx 5
addx -40
addx 26
addx -23
addx 2
addx 5
addx 26
addx -35
addx 12
addx 2
addx 17
addx -10
addx 3
noop
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx 2
addx -39
noop
addx 15
addx -12
addx 2
addx 10
noop
addx -1
addx -2
noop
addx 5
noop
addx 5
noop
noop
addx 1
addx 4
addx -25
addx 26
addx 2
addx 5
addx 2
noop
addx -3
addx -32
addx 1
addx 4
addx -2
addx 3
noop
noop
addx 3
noop
addx 6
addx -17
addx 27
addx -7
addx 5
addx 2
addx 3
addx -2
addx 4
noop
noop
addx 5
addx 2
addx -39
noop
noop
addx 2
addx 5
addx 3
addx -2
addx 2
addx 11
addx -4
addx -5
noop
addx 10
addx -18
addx 19
addx 2
addx 5
addx 2
addx 2
addx 3
addx -2
addx 2
addx -37
noop
addx 5
addx 4
addx -1
noop
addx 4
noop
noop
addx 1
addx 4
noop
addx 1
addx 2
noop
addx 3
addx 5
noop
addx -3
addx 5
addx 5
addx 2
addx 3
noop
addx -32
noop`;

function readInstructions() {
  const instructions = [];
  const lines = input.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const parts = line.split(" ");
    const instruction = {
      command: parts[0],
      value: parseInt(parts[1]),
    };
    instructions.push(instruction);
  }
  return instructions;
}

function sumResults(results) {
  let sum = 0;
  for (let i = 0; i < results.length; i++) {
    sum += results[i];
  }
  return sum;
}

function main() {
  const instructions = readInstructions();
  const breakpoints = [20, 60, 100, 140, 180, 220];
  let x = 1;
  let currentInstruction = instructions[0];
  let waitedFor = 0;
  const results = [];
  for (let i = 1; i < 1000000000; i++) {
    if (currentInstruction === undefined) break;
    if (currentInstruction.command === "noop") {
      currentInstruction =
        instructions[instructions.indexOf(currentInstruction) + 1];
    } else if (currentInstruction.command === "addx") {
      if (waitedFor === 0 || waitedFor === 1) {
        waitedFor++;
      }
    }
    if (breakpoints.includes(i)) {
      console.log(`x: ${x}, i: ${i}, signal: ${x * i}`);
      results.push(x * i);
    }
    if (waitedFor === 2) {
      waitedFor = 0;
      x = x + currentInstruction.value;
      currentInstruction =
        instructions[instructions.indexOf(currentInstruction) + 1];
    }
    if (breakpoints[breakpoints - 1] === i - 1) {
      break;
    }
  }

  console.log(results);
  //sum results
  console.log(sumResults(results));
}

function getCurrentSpritePositions(x) {
  return [x - 1, x, x + 1];
}

function paintSprite(x) {
  let sprite = "";
  const currentSpritePositions = getCurrentSpritePositions(x);
  console.log(currentSpritePositions);

  for (let i = 0; i < 40; i++) {
    if (currentSpritePositions.includes(i)) {
      sprite += "#";
    } else {
      sprite += ".";
    }
  }
  console.log(sprite);
}

function getValueOfCrt(x, currentStep) {
  const currentSpritePositions = getCurrentSpritePositions(x);
  console.log(currentStep);
  if (currentSpritePositions.includes(currentStep)) {
    return "#";
  } else {
    return ".";
  }
}

function main2() {
  const instructions = readInstructions();
  let x = 1;
  let currentInstruction = instructions[0];
  let waitedFor = 0;
  let crt = "";
  let currentStep = 0;
  for (let i = 1; i < 1000000000; i++) {
    if (currentInstruction === undefined) break;
    if (currentInstruction.command === "noop") {
      currentInstruction =
        instructions[instructions.indexOf(currentInstruction) + 1];
    } else if (currentInstruction.command === "addx") {
      if (waitedFor === 0 || waitedFor === 1) {
        waitedFor++;
      }
    }

    if (currentStep % 40 === 0) {
      currentStep = 0;
      crt += "\n";
    }

    crt += getValueOfCrt(x, currentStep, crt);

    if (waitedFor === 2) {
      waitedFor = 0;
      x = x + currentInstruction.value;
      currentInstruction =
        instructions[instructions.indexOf(currentInstruction) + 1];
    }

    currentStep++;
  }

  console.log(crt);
}

main2();
