# DEPRECATED — Scheduled for Archive

This repository (`deepsight-agent`) is scheduled for deprecation as part of the
Influwealth sovereign architecture synthesis (Phase 6).

## Reason for Deprecation
The DeepSight agent pattern has been superseded by the Sovereign Agent Protocol (SAP)
architecture. Functionality has been absorbed into:

- **DeepFlex Supervisor** (`sovereign-stack/deepflex/`) — orchestration and routing
- **Argus Prime** (`argus-prime/`) — device-level agent execution (port 7700)
- **WealthBridge OS** (`sovereign-stack/wealthbridge-os/`) — business automation

## Status
No new features. Critical bug fixes only.

## Migration Path
If your code calls `deepsight-agent`:
1. Identify the capability you need (device ops, business logic, prediction)
2. Replace with the correct SAP-compliant service:
   - Device ops → POST http://localhost:7700/task (Argus Prime)
   - Business logic → POST http://localhost:8001/orchestrate (WealthBridge OS)
   - Prediction → ICP Caffeine Agent canister via qre-agent-platform

## Required SAP Headers
```
x-sap-node-id: <your-service-name>
x-sap-trace-id: <uuid>
x-sap-version: 1.0
```

## Archive Date
Pending final migration verification. Track progress on branch `claude/deepflex-argus-synthesis-jWjmO`.
