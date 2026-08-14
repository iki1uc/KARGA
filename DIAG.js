export function diagnose(result) {
  if (result.ok) return "OK";
  return `Fehler: ${result.type} verträgt Nummer ${result.num} nicht (Achse ${result.axis})`;
}

