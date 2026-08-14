import { lar } from "./EngineUnified.js";

export function symbiose(name) {
  const eco = lar(name, "ECONOMY");
  const spr = lar(name, "SPRINT");

  return {
    modul: name,
    economy: eco,
    sprint: spr,
    decision: spr.ok ? "SPRINT empfohlen" : "ECONOMY empfohlen"
  };
}
