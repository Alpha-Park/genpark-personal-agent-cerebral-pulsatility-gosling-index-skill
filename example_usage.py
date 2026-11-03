"""
Example Usage: Transcranial Doppler Gosling Pulsatility Index (PI) Evaluation.
Demonstrates calculation of cerebral blood flow velocity indices and microvascular resistance.
"""

from client import CerebralPulsatilityIndexClient


def main():
    client = CerebralPulsatilityIndexClient()
    print("=== Transcranial Doppler Gosling Pulsatility Index Demo ===")

    # Test Case 1: Healthy young adult (Middle Cerebral Artery)
    res1 = client.evaluate_cerebral_pulsatility(
        peak_systolic_velocity_cm_s=98.0,
        end_diastolic_velocity_cm_s=45.0,
        mean_velocity_cm_s=63.0,
        target_vessel="MIDDLE_CEREBRAL_ARTERY"
    )
    print("\nTest Case 1: Healthy MCA Hemodynamics")
    print(f"  Vessel: {res1['target_vessel']} | Vs: {res1['peak_systolic_velocity_cm_s']} cm/s | Vd: {res1['end_diastolic_velocity_cm_s']} cm/s")
    print(f"  Gosling PI: {res1['gosling_pulsatility_index_pi']} | Pourcelot RI: {res1['pourcelot_resistance_index_ri']}")
    print(f"  Cerebral Compliance Score: {res1['cerebral_compliance_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Elevated downstream microvascular resistance
    res2 = client.evaluate_cerebral_pulsatility(
        peak_systolic_velocity_cm_s=115.0,
        end_diastolic_velocity_cm_s=32.0,
        target_vessel="MIDDLE_CEREBRAL_ARTERY"
    )
    print("\nTest Case 2: High Resistance & Pulsatility Strain")
    print(f"  Vs: {res2['peak_systolic_velocity_cm_s']} cm/s | Vd: {res2['end_diastolic_velocity_cm_s']} cm/s")
    print(f"  Gosling PI: {res2['gosling_pulsatility_index_pi']} | Pourcelot RI: {res2['pourcelot_resistance_index_ri']}")
    print(f"  Score: {res2['cerebral_compliance_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
