"""
Transcranial Doppler Gosling Pulsatility Index (PI) & Cerebral Resistance Engine.
Provides deterministic, zero-dependency modeling of middle cerebral artery (MCA) flow velocities,
Gosling Pulsatility Index (PI = (Vs - Vd) / Vm), Pourcelot Resistance Index (RI), and downstream microvascular resistance.
"""

from typing import Dict, Any, List, Optional


class CerebralPulsatilityIndexClient:
    """
    Deterministic client for calculating Transcranial Doppler (TCD) Gosling Pulsatility Index (PI).
    Assesses cerebral microvascular resistance, intracranial compliance, and pulsatile shear stress
    transmitted to cerebral small vessels.
    """

    def __init__(self):
        pass

    def evaluate_cerebral_pulsatility(
        self,
        peak_systolic_velocity_cm_s: float,
        end_diastolic_velocity_cm_s: float,
        mean_velocity_cm_s: Optional[float] = None,
        target_vessel: str = "MIDDLE_CEREBRAL_ARTERY"
    ) -> Dict[str, Any]:
        """
        Calculates Gosling PI = (Vs - Vd) / Vm and Pourcelot RI = (Vs - Vd) / Vs.
        If Vm is omitted, estimated via standard formula: Vm = Vd + (Vs - Vd) / 3.
        Normative values for middle cerebral artery:
        - PI: 0.65 - 1.10
        - RI: 0.50 - 0.68
        - Vs: 80 - 120 cm/s
        - Vd: 35 - 60 cm/s
        """
        if peak_systolic_velocity_cm_s <= 0 or end_diastolic_velocity_cm_s < 0:
            return {"error": "Systolic velocity must be positive and diastolic velocity non-negative"}
        if peak_systolic_velocity_cm_s <= end_diastolic_velocity_cm_s:
            return {"error": "Peak systolic velocity must exceed end diastolic velocity"}

        if mean_velocity_cm_s is None or mean_velocity_cm_s <= 0:
            mean_velocity_cm_s = end_diastolic_velocity_cm_s + (peak_systolic_velocity_cm_s - end_diastolic_velocity_cm_s) / 3.0

        vessel = target_vessel.upper()

        pi = round((peak_systolic_velocity_cm_s - end_diastolic_velocity_cm_s) / mean_velocity_cm_s, 2)
        ri = round((peak_systolic_velocity_cm_s - end_diastolic_velocity_cm_s) / peak_systolic_velocity_cm_s, 2)

        # Cerebral Microvascular Compliance Score (0 - 100):
        # Target PI 0.70 - 1.05 -> 88 - 98.
        # PI > 1.30 -> < 45 (Elevated downstream cerebral resistance / microvascular strain).
        if 0.70 <= pi <= 1.05:
            score = 90.0 + (1.05 - pi) * 20.0
        elif 0.60 <= pi < 0.70:
            score = 75.0 + ((pi - 0.60) / 0.10) * 15.0
        elif 1.05 < pi <= 1.25:
            score = 70.0 + ((1.25 - pi) / 0.20) * 18.0
        elif pi < 0.60:
            score = max(10.0, 75.0 - (0.60 - pi) * 100.0)
        else:
            score = max(5.0, 70.0 - (pi - 1.25) * 60.0)

        compliance_score = round(min(100.0, max(5.0, score)), 1)

        if 0.68 <= pi <= 1.10:
            tier = "OPTIMAL_CEREBRAL_HEMODYNAMICS"
            interp = f"Normal Gosling pulsatility (PI {pi}, RI {ri}) in {vessel}; optimal downstream cerebrovascular resistance and intracranial compliance."
            guidance = "Cerebral blood flow kinetics are flexible and well-buffered. Excellent cerebrovascular health."
        elif 1.10 < pi <= 1.28:
            tier = "ELEVATED_MICROVASCULAR_PULSATILITY"
            interp = f"Borderline elevated pulsatility index (PI {pi}); increased downstream vascular resistance or elevated pulsatile pressure transmission."
            guidance = "Moderate microvascular stiffness. Ensure resting blood pressure is within normal range and engage in Zone 2 aerobic pacing."
        elif pi > 1.28:
            tier = "HIGH_RESISTANCE_MICROVASCULAR_STRAIN"
            interp = f"Significantly elevated Gosling PI ({pi} > 1.25, RI {ri}); indicates high intracranial arteriolar resistance or cerebral small vessel disease."
            guidance = "High cerebral pulsatility detected. Recommend comprehensive neurological vascular review and continuous ambulatory blood pressure monitoring."
        else:
            tier = "LOW_PULSATILITY_PROXIMAL_DAMPING"
            interp = f"Depressed pulsatility index (PI {pi} < 0.60); indicates low peripheral resistance or proximal hemodynamic damping."
            guidance = "Unusually low cerebrovascular pulsatility. Evaluate proximal carotid flow velocities and systemic vasodilation."

        return {
            "target_vessel": vessel,
            "peak_systolic_velocity_cm_s": peak_systolic_velocity_cm_s,
            "end_diastolic_velocity_cm_s": end_diastolic_velocity_cm_s,
            "mean_velocity_cm_s": round(mean_velocity_cm_s, 1),
            "gosling_pulsatility_index_pi": pi,
            "pourcelot_resistance_index_ri": ri,
            "cerebral_compliance_score": compliance_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
