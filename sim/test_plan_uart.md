# UART Verification Test Plan

## Objective
Identify protocol-level bugs intentionally inserted into the UART peripheral.

---

## Tools Used
- **Cocotb (Python)** → Testbench development and stimulus generation  
- **Icarus Verilog** → Simulation and waveform generation  
- **GTKWave** → Waveform debugging

---

## Test Cases Executed

| Testcase ID | Description                              | Expected Result                          | Observed Result                        | Status |
|-------------|------------------------------------------|------------------------------------------|----------------------------------------|--------|
| TC1         | Basic TX output idle check               | TX remains high when idle                | TX remains high (No issue)             | PASS   |
| TC2         | TX edge-case pattern (0x00, 0x55, 0xAA)  | Correct UART frame with correct timing   | TX unstable during transitions         | **FAIL** |
| TC3         | RX→TX loopback simple                    | TX echoes received data properly         | Incorrect timing response on some bits | **FAIL** |
| TC4         | Random data transmission                 | No protocol violation                    | Protocol violation at bit boundary     | **FAIL** |

---

## Bugs Identified
- **UART protocol timing violation** during RX→TX transitions.
- Edge patterns (0x00, 0x55, 0xAA) produce unexpected TX line glitches.

---

## Coverage
- Edge patterns  
- Idle state validation  
- RX to TX loopback path  
- Random transmission stress test

---

## Summary
- **Bugs Found**: 3  
- **Tests Passed**: 1/4  
- **Coverage Goal**: Timing, protocol correctness, data integrity  
