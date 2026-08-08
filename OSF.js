export const OSF_VECTOR = {
    AXIS: { x: 7, y: 7, z: 7 },
    LEVEL: "4er‑Richtigkeit",
    PHI: OSF_PHI.VALUE,
    BEAM: OSF_BEAM.SIGNAL,
    STATION: OSF_STATION.NAME,

    // mathematische Richtung
    DIR() {
        return {
            dx: this.AXIS.x * this.PHI,
            dy: this.AXIS.y * this.PHI,
            dz: this.AXIS.z * this.PHI
        };
    },

    // Φ∞‑Stabilität
    STABIL() {
        return this.PHI / Math.PI;
    }
};
