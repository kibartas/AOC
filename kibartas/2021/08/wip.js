const input = require("fs")
  .readFileSync(require("path").join(__dirname, "oneLine.txt"), "utf8")
  .trim()
  .split("\n")
  .map((el) => el.split(" | ").map((iel) => iel.split(" ")));

// 1, 4, 7, 8
const digits = {
  1: ["c", "f"],
  4: ["b", "c", "d", "f"],
  7: ["a", "c", "f"],
  8: ["a", "b", "c", "d", "e", "f", "g"],
};

const nonUniq = {
  2: ["a", "c", "d", "e", "g"],
  3: ["a", "c", "d", "f", "g"],
  5: ["a", "b", "d", "f", "g"],
  0: ["a", "b", "c", "e", "f", "g"],
  6: ["a", "b", "d", "e", "f", "g"],
  9: ["a", "b", "c", "d", "f", "g"],
};

const sortString = (string) => {
  return string.split("").sort().join("");
};

const findKey = (obj, string) => {
  return Object.keys(obj).find((k) => {
    return obj[k].length === string.length;
  });
};

const findKeys = (obj, string) => {
  return Object.keys(obj).filter((k) => {
    return obj[k].length === string.length;
  });
};

const answers = {};
let result = 0;
input.forEach((el) => {
  let number = "";
  const candidates = {};
  let found = 0;
  el[1].forEach((inEl) => {
    //uniq
    const key = findKey(digits, inEl);
    if (key !== undefined) {
      number += `${digits[key]}`;
      found++;
    }
  });
  if (found === el[1].length) return;

  // Do some heavy lifting with the first 10 to decipher
  el[0] = el[0].sort((a, b) => (a.length < b.length ? -1 : 1));
  el[0].forEach((inEl, i) => {
    inEl = sortString(inEl);
    const key = findKey(digits, inEl);
    if (key !== undefined) {
      if (!candidates[inEl]) {
        candidates[inEl] = [digits[key]];
      }
    } else {
      findKeys(nonUniq, inEl).forEach((k) => {
        if (!candidates[inEl]) {
          candidates[inEl] = [nonUniq[k]];
        } else {
          candidates[inEl].push(nonUniq[k]);
        }
      });
    }
  });
  console.log(candidates);
});

// 2: ["a", "c", "d", "e", "g"],
// 3: ["a", "c", "d", "f", "g"],
// 5: ["a", "b", "d", "f", "g"],
// 0: ["a", "b", "c", "e", "f", "g"],
// 6: ["a", "b", "d", "e", "f", "g"],
// 9: ["a", "b", "c", "d", "f", "g"],
/* 
ab in cf
(ab)d in a(cf)
(ab)ef in b(c)d(f)

(b)c(d)(ef) in (a)(c)(d)eg -> a is f
(b)c(d)(ef) in (a)(c)(d)(f)g -> c is g
(b)c(d)(ef) in (a)(c)(d)(f)g -> c is g

f in e -> b is f
acdfg in acdfg
acdfg in abdfg

abcdf in acdeg OR acdefg OR acdfg
abcdef in abcefg OR abdefg OR abcdfg
bcdefg in abcefg OR abdefg OR abcdfg
abcdeg in abcefg OR abdefg OR abcdfg
abcdefg in abcdefg
*/

console.log({ result });
