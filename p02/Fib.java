// Fib Sequence
// Even Fib Sequence I think, trying to reorganize.

import java.math.*;
import java.util.*;

public class Fib implements Runnable {

    /* Instance Vars */
    BigInteger a = new BigInteger("0"); 
    BigInteger b = new BigInteger("0"); 
    BigInteger sum = new BigInteger("0");

    /* Constructor */
    public Fib(){
        a = new BigInteger("0"); 
        b = new BigInteger("0"); 
    }

    /* Methods */ 

    public BigInteger fibon(int rank){
        if(a.equals(b) && a.equals(BigInteger.ZERO)){
            b = new BigInteger("1");
        }

        for (int i = 0; i < rank; i++){
            // Set the lesser of the two to their sum.
            if (a.compareTo(b) < 0) {
                a = sum;
            }
            else {
                b = sum;
            }

        // set the new sum.
            sum = a.add(b);
        }
        if(sum.equals(BigInteger.ZERO)){
            return BigInteger.ONE;
        }
        return this.sum;

    }

    public void run(){

        
    }

    
    public static void main (String[] args) {
        /*if(args.length == 0){
            System.err.println("Need an argument for the number of fibs!");
            return;
        }

        int count = Integer.parseInt(args[0]);
        */
        int count = 4000000;
        //ArrayList<BigInteger> list = new ArrayList<BigInteger>();
        BigInteger sum = new BigInteger("0");

        for(int x = 0; x < count; x++){
            //System.out.println(x);
            Fib fib = new Fib();
            BigInteger toPrint = fib.fibon(x);
            //System.out.println(toPrint);
            if(toPrint.mod(new BigInteger("2")).intValue() == 0 ) {
                //System.out.println(toPrint);
                sum = sum.add(toPrint);
            }
            if(fib.a.compareTo(new BigInteger("4000000")) > 0
             || fib.b.compareTo(new BigInteger("4000000"))  >0){
                break;
            }
        }
        
        System.out.println(sum);
        

    }



}