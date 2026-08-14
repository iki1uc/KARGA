import { detectType } from "./ID.js";
import { detectAxis } from "./AXIS.js";
import { inRange } from "./RANGE.js";

export function mapModule(name) {
  const type = detectType(name);
  const num  = parseInt(name.match(/\d+/));
  const axis = detectAxis(num);
  const ok   = inRange(type, num);

  return { name, type, num, axis, ok };
}

