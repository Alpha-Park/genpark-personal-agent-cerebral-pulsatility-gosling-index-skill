# Transcranial Doppler Gosling Pulsatility Index (PI) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Transcranial Doppler Gosling Pulsatility Index (PI), Pourcelot Resistance Index (RI), and cerebral microvascular health.

```mermaid
flowchart TD
    TCD_Probe["2 MHz Transcranial Doppler Ultrasound Probe"] --> VelocityWaveform["Cerebral Blood Flow Velocity Envelope (Vs, Vd, Vm)"]
    VelocityWaveform --> IndexEquations["Gosling PI = (Vs-Vd)/Vm & Pourcelot RI = (Vs-Vd)/Vs"]
    IndexEquations --> ResistanceScore["Cerebral Microvascular Compliance Engine"]
    ResistanceScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Neuro-Sonology Standards**: Implements validated Gosling and Pourcelot hemodynamic formulas.
- **Microvascular Aging & Compliance Biomarker**: Early detection of intracranial microvascular stiffening.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CerebralPulsatilityIndexClient

client = CerebralPulsatilityIndexClient()
result = client.evaluate_cerebral_pulsatility(
    peak_systolic_velocity_cm_s=98.0,
    end_diastolic_velocity_cm_s=45.0
)
print("Gosling PI:", result["gosling_pulsatility_index_pi"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
