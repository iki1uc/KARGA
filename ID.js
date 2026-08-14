export function detectType(name) {
  if (name.startsWith("tmp")) return "tmp";
  if (name.startsWith("vec")) return "vec";
  if (name.startsWith("re"))  return "re";
  return "unknown";
}

