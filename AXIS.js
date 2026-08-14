export function detectAxis(num) {
  if (num >= 1 && num <= 81) return "O";
  if (num >= 82 && num <= 162) return "Z";
  if (num >= 163 && num <= 243) return "T";
  return "X"; // Fehlerachse
}

