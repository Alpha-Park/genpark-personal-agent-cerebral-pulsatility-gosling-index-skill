---
name: genpark-personal-agent-cerebral-pulsatility-gosling-index-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Transcranial Doppler Gosling Pulsatility Index (PI), Pourcelot Resistance Index (RI), and cerebral compliance.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Transcranial Doppler Gosling Pulsatility Index (PI) Skill

A sovereign personal agent capability for evaluating cerebral blood flow velocity waveforms, calculating the Gosling Pulsatility Index ($PI = \frac{V_s - V_d}{V_m}$), and monitoring downstream cerebrovascular resistance.

## Core Capabilities
- **Gosling Pulsatility Index**: Normalizes pulse amplitude to mean flow velocity across intracranial arteries.
- **Pourcelot Resistance Index**: Quantifies downstream vascular bed impedance and peripheral vasoconstriction.
- **Cerebrovascular Compliance Score**: 0-100 rating indicating elasticity of the cerebral microvasculature.
- **Vascular Health Guidance**: Actionable pacing on aerobic exercise, blood pressure regulation, and cognitive recovery.

## Fast Invocation
```python
from client import CerebralPulsatilityIndexClient

client = CerebralPulsatilityIndexClient()
res = client.evaluate_cerebral_pulsatility(
    peak_systolic_velocity_cm_s=98.0,
    end_diastolic_velocity_cm_s=45.0,
    target_vessel="MIDDLE_CEREBRAL_ARTERY"
)
print("Gosling PI:", res["gosling_pulsatility_index_pi"])
print("Compliance Score:", res["cerebral_compliance_score"])
```
