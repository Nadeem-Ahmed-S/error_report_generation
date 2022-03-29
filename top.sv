module top;

  bit [7:0]a;

  initial begin

    a= 8'd19

    for(int i=0; i<8; i++) begin
      $display("a[%0d]=%0d"i,a[i]);
    end
  
  end

endmodule : top
