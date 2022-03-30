module top;

  bit [7:0]q[$:7];

  initial begin

    //a= 8'd19;

    for(int i=0; i<7; i++) begin
      q[i] = i + 5;
      //$display("q[%0d]=%0d",i,q[i]);
    end

    for(int i=0; i<17; i++) begin
      $display("q[%0d]=%0d",i,a[i]);
    end
  
  end

endmodule : top
