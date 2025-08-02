module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/mkSoc.fst");
    $dumpvars(0, mkSoc);
end
endmodule
