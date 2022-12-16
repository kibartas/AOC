const input = `Valve JC has flow rate=0; tunnels lead to valves XS, XK
Valve TK has flow rate=0; tunnels lead to valves AA, RA
Valve PY has flow rate=0; tunnels lead to valves UB, MW
Valve XK has flow rate=15; tunnels lead to valves CD, JC, TP, UE
Valve EI has flow rate=6; tunnels lead to valves UB, HD
Valve OV has flow rate=0; tunnels lead to valves QC, WK
Valve CX has flow rate=3; tunnels lead to valves ZN, AM, OE, YS, QE
Valve YS has flow rate=0; tunnels lead to valves QC, CX
Valve DC has flow rate=0; tunnels lead to valves UE, NM
Valve EA has flow rate=5; tunnels lead to valves QE, XO, GX
Valve VE has flow rate=0; tunnels lead to valves YH, NM
Valve RN has flow rate=0; tunnels lead to valves WK, NU
Valve VJ has flow rate=0; tunnels lead to valves QC, CS
Valve HD has flow rate=0; tunnels lead to valves JI, EI
Valve UB has flow rate=0; tunnels lead to valves EI, PY
Valve XS has flow rate=17; tunnels lead to valves JC, CE
Valve AM has flow rate=0; tunnels lead to valves NU, CX
Valve GX has flow rate=0; tunnels lead to valves EA, RA
Valve UI has flow rate=0; tunnels lead to valves NC, ZG
Valve NM has flow rate=22; tunnels lead to valves DC, VE, DX
Valve CE has flow rate=0; tunnels lead to valves XS, WD
Valve NC has flow rate=25; tunnels lead to valves UI, VQ
Valve TP has flow rate=0; tunnels lead to valves XK, RA
Valve ZN has flow rate=0; tunnels lead to valves CX, XI
Valve CS has flow rate=0; tunnels lead to valves AA, VJ
Valve MW has flow rate=23; tunnel leads to valve PY
Valve AA has flow rate=0; tunnels lead to valves TK, WC, CS, AL, MS
Valve RA has flow rate=4; tunnels lead to valves WD, TP, TK, GX, JI
Valve NU has flow rate=10; tunnels lead to valves DU, AM, RN, HS, AL
Valve QE has flow rate=0; tunnels lead to valves CX, EA
Valve AH has flow rate=0; tunnels lead to valves WK, MS
Valve YH has flow rate=20; tunnels lead to valves VE, CD
Valve SH has flow rate=0; tunnels lead to valves DU, ZG
Valve OE has flow rate=0; tunnels lead to valves WC, CX
Valve XO has flow rate=0; tunnels lead to valves EA, ZG
Valve JI has flow rate=0; tunnels lead to valves RA, HD
Valve XI has flow rate=0; tunnels lead to valves WK, ZN
Valve HS has flow rate=0; tunnels lead to valves QC, NU
Valve VQ has flow rate=0; tunnels lead to valves WK, NC
Valve UE has flow rate=0; tunnels lead to valves XK, DC
Valve YP has flow rate=19; tunnel leads to valve DX
Valve WD has flow rate=0; tunnels lead to valves CE, RA
Valve DX has flow rate=0; tunnels lead to valves NM, YP
Valve ZG has flow rate=11; tunnels lead to valves UI, SH, XO
Valve MS has flow rate=0; tunnels lead to valves AA, AH
Valve QC has flow rate=9; tunnels lead to valves HS, VJ, OV, YS
Valve DU has flow rate=0; tunnels lead to valves NU, SH
Valve WK has flow rate=12; tunnels lead to valves RN, XI, VQ, OV, AH
Valve CD has flow rate=0; tunnels lead to valves YH, XK
Valve AL has flow rate=0; tunnels lead to valves AA, NU
Valve WC has flow rate=0; tunnels lead to valves OE, AA`;

function parseInput() {
  const valves = [];
  const lines = input.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const key = line.split(" ")[1];
    const flowRate = parseInt(line.split("flow rate=")[1].split(";")[0]);
    let leadingTunnels = [];
    if (line.includes(",")) {
      leadingTunnels = line.split("tunnels lead to valves ")[1].split(", ");
    } else {
      leadingTunnels = [line.split("tunnel leads to valve ")[1]];
    }
    valves[key] = {
      flowRate,
      leadingTunnels,
      paths: {},
    };
  }

  return valves;
}

function bfs(toGo, end, valves) {
  let depth = 1;
  while (true) {
    const nextToGo = [];
    for (let x in toGo) {
      const xValue = toGo[x];
      if (xValue === end) {
        console.log("depth", depth);
        return depth;
      }
      for (let y in valves[xValue].leadingTunnels) {
        nextToGo.push(valves[xValue].leadingTunnels[y]);
      }
    }
    toGo = nextToGo;
    depth++;
  }
}

function getValvesWithFlowKeys(valves) {
  const valvesWithFlow = [];
  for (let i in valves) {
    if (valves[i].flowRate > 0) valvesWithFlow.push(i);
  }
  return valvesWithFlow;
}

function checkDepths(valves, valvesWithFlowKeys) {
  const keysWithStart = [...valvesWithFlowKeys, "AA"];
  for (let i in keysWithStart) {
    for (let j in valvesWithFlowKeys) {
      if (i === j) continue;
      const k1 = keysWithStart[i];
      const k2 = valvesWithFlowKeys[j];
      valves[k1]["paths"][k2] = bfs(valves[k1]["leadingTunnels"], k2, valves);
    }
  }
}

let best = 0;

function searchForBest(opened, flowed, currentRoom, depthToGo, valves) {
  if (flowed > best) {
    console.log("current best", flowed);
    best = flowed;
  }
  if (depthToGo <= 0) {
    return;
  }
  if (!opened.includes(currentRoom)) {
    const newRooms = [...opened, currentRoom];
    const currentFlow = flowed + valves[currentRoom].flowRate * depthToGo;
    searchForBest(newRooms, currentFlow, currentRoom, depthToGo - 1, valves);
  } else {
    const keysOfPaths = Object.keys(valves[currentRoom].paths);
    const keysOfNotOpened = keysOfPaths.filter((x) => !opened.includes(x));
    for (let i in keysOfNotOpened) {
      const key = keysOfNotOpened[i];
      searchForBest(
        opened,
        flowed,
        key,
        depthToGo - valves[currentRoom].paths[key],
        valves
      );
    }
  }
}

function searchForBestWithElephant(
  opened,
  flowed,
  currentRoom,
  depthToGo,
  valves,
  isElephantTurn
) {
  if (flowed > best) {
    console.log("current best", flowed);
    best = flowed;
  }
  if (depthToGo <= 0) {
    return;
  }

  if (!opened.includes(currentRoom)) {
    const newRooms = [...opened, currentRoom];
    const currentFlow = flowed + valves[currentRoom].flowRate * depthToGo;
    searchForBestWithElephant(
      newRooms,
      currentFlow,
      currentRoom,
      depthToGo - 1,
      valves,
      isElephantTurn
    );
    if (!isElephantTurn) {
      searchForBestWithElephant(
        newRooms.reverse(),
        flowed + valves[currentRoom].flowRate * depthToGo,
        "AA",
        25,
        valves,
        true
      );
    }
  } else {
    const keysOfPaths = Object.keys(valves[currentRoom].paths);
    const keysOfNotOpened = keysOfPaths.filter((x) => !opened.includes(x));
    for (let i in keysOfNotOpened) {
      const key = keysOfNotOpened[i];
      searchForBestWithElephant(
        opened,
        flowed,
        key,
        depthToGo - valves[currentRoom].paths[key],
        valves,
        isElephantTurn
      );
    }
  }
}

function main() {
  const valves = parseInput();
  const valvesWithFlowKeys = getValvesWithFlowKeys(valves);
  checkDepths(valves, valvesWithFlowKeys);
  searchForBest(["AA"], 0, "AA", 29, valves);
  console.log(best);
}

function main2() {
  const valves = parseInput();
  const valvesWithFlowKeys = getValvesWithFlowKeys(valves);
  checkDepths(valves, valvesWithFlowKeys);
  searchForBestWithElephant(["AA"], 0, "AA", 25, valves, false);
  console.log(best);
}

// main();
main2();
