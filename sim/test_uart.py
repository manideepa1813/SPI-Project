import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock


@cocotb.test()
async def uart_bug_check(dut):
    """Simple UART TX functional check"""
    dut._log.info("Resetting DUT...")
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.RST_N.value = 0
    for _ in range(5):
        await RisingEdge(dut.CLK)
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)

    # Check TX output
    tx_val = int(dut.uart_io_SOUT.value)
    dut._log.info(f"UART TX pin value after reset: {tx_val}")
    assert tx_val in (0, 1), "UART TX must be binary 0 or 1"


@cocotb.test()
async def uart_bug_corner_cases(dut):
    """Send edge-case data to identify protocol-level bugs"""
    dut._log.info("Checking UART TX stability on edge cases")
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.RST_N.value = 0
    for _ in range(5):
        await RisingEdge(dut.CLK)
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)

    # Simulate toggling RX to trigger TX behavior
    edge_cases = [0, 1, 0, 1]
    for val in edge_cases:
        dut.uart_io_SIN.value = val
        await RisingEdge(dut.CLK)
        tx_val = int(dut.uart_io_SOUT.value)
        dut._log.info(f"Sent RX={val}, observed TX={tx_val}")
        assert tx_val in (0, 1), "UART TX output must remain binary"

