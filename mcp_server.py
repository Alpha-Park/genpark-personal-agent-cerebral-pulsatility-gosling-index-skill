"""
MCP Server for Transcranial Doppler Gosling Pulsatility Index (PI) Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing cerebral blood flow velocities and microvascular resistance.
"""

import sys
import json
from typing import Dict, Any
from client import CerebralPulsatilityIndexClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_cerebral_pulsatility",
                "description": "Calculates Gosling Pulsatility Index (PI), Pourcelot Resistance Index (RI), and cerebral microvascular compliance score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "peak_systolic_velocity_cm_s": {
                            "type": "number",
                            "description": "Peak systolic velocity in cm/s (e.g. 96.0 cm/s in MCA)."
                        },
                        "end_diastolic_velocity_cm_s": {
                            "type": "number",
                            "description": "End-diastolic velocity in cm/s (e.g. 44.0 cm/s in MCA)."
                        },
                        "mean_velocity_cm_s": {
                            "type": "number",
                            "description": "Optional time-averaged mean velocity in cm/s (e.g. 62.0 cm/s)."
                        },
                        "target_vessel": {
                            "type": "string",
                            "description": "Insonated cerebral artery (MIDDLE_CEREBRAL_ARTERY, ANTERIOR_CEREBRAL_ARTERY, BASILAR_ARTERY).",
                            "default": "MIDDLE_CEREBRAL_ARTERY"
                        }
                    },
                    "required": ["peak_systolic_velocity_cm_s", "end_diastolic_velocity_cm_s"]
                }
            }
        ]
    }


def handle_request(client: CerebralPulsatilityIndexClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_cerebral_pulsatility":
            vm = args.get("mean_velocity_cm_s")
            if vm is not None:
                vm = float(vm)

            res = client.evaluate_cerebral_pulsatility(
                peak_systolic_velocity_cm_s=float(args.get("peak_systolic_velocity_cm_s", 95.0)),
                end_diastolic_velocity_cm_s=float(args.get("end_diastolic_velocity_cm_s", 42.0)),
                mean_velocity_cm_s=vm,
                target_vessel=str(args.get("target_vessel", "MIDDLE_CEREBRAL_ARTERY"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = CerebralPulsatilityIndexClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
