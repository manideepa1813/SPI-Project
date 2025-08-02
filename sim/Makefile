# Existing lines
VERILOG_SOURCES = $(shell find ../../verilog_core -name "*.v")
TOPLEVEL = mkSoc
MODULE   = test_uart

# Add these two lines
SIM_ARGS += --trace
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim

$(COCOTB_RESULTS_FILE): $(SIM_BUILD)/sim.vvp $(CUSTOM_SIM_DEPS)
	$(RM) $(COCOTB_RESULTS_FILE)
	MODULE=$(MODULE) TESTCASE=$(TESTCASE) TOPLEVEL=$(TOPLEVEL) TOPLEVEL_LANG=$(TOPLEVEL_LANG) \
	$(SIM_CMD_PREFIX) $(ICARUS_BIN_DIR)/vvp -M $(shell cocotb-config --lib-dir) -m libcocotbvpi_icarus sim_build/sim.vvp
	$(call check_for_results_file)
