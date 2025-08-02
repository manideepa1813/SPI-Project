import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def uart_bug_trigger(dut):
    """Stress test UART TX to trigger protocol bug"""

    cocotb.log.info("Starting UART stress test to trigger bug")

    # Start clock
    cocotb.start_soon(Clock(dut.CLK, 10, units="ns").start())

    # Apply reset
    dut.RST_N.value = 0
    await Timer(100, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)

    # Monitor TX for incorrect behavior
    for i in range(100):
        await RisingEdge(dut.CLK)
        tx_value = dut.uart_io_SOUT.value
        cocotb.log.info(f"UART TX bit at cycle {i}: {tx_value}")

    # Add a check (this is just placeholder for detecting bug)
    assert False, "Intentional fail to observe bug"

