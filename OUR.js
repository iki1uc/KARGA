export function ourMode(result) {
  return {
    ...result,
    shared: result.ok ? "team-ready" : "team-blocked"
  };
}
