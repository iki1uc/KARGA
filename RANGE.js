export function inRange(type, num) {
  if (type === "tmp" && num <= 81) return true;
  if (type === "vec" && num >= 82 && num <= 162) return true;
  if (type === "re"  && num >= 163 && num <= 243) return true;
  return false;
}

