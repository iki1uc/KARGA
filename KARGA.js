import { core } from "./CORE.js";
import { diagnose } from "./DIAG.js";
import { save } from "./STORE.js";
import { ourMode } from "./OUR.js";

export function karga(name) {
  const result = core(name);
  const diag   = diagnose(result);
  const team   = ourMode(result);

  save(team);

  return { result, diag, team };
}

