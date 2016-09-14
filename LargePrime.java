import java.util.*;
import java.math.*;

public class LargePrime {
	ArrayList<BigInteger> list = new ArrayList<BigInteger>();
	public LargePrime(){

	}
	
	public boolean isPrime(BigInteger test){
		int num = test.intValue();
		/*for(int i = 2; i < num; i++){
			if(num%i == 0){
				return false;
			}
		}*/

		for(
			BigInteger i = new BigInteger("2");
			i.compareTo(test) < 0;
			i = i.add(BigInteger.ONE)
			){

			if(test.mod(i).equals(BigInteger.ZERO)){
				return false;
			}
		}
		return true;
	}

	public ArrayList<BigInteger> findPrimes(BigInteger current){
		boolean debug = true; 

		ArrayList<BigInteger> list = new ArrayList<BigInteger>();
		while(!isPrime(current)){

			if(debug) System.out.println("Current is (not?) prime."); 
			for(BigInteger i = new BigInteger("2");
			i.compareTo(current) < 0;
			i = i.add(BigInteger.ONE)){

				if(current.mod(i) == BigInteger.ZERO){
					list.add(i);
					current = current.divide(i);
					continue;
				}
			}
		}
		list.add(current);
		return list;
	}

	public static void main(String[] args){
		System.out.println();
		LargePrime here = new LargePrime();
		BigInteger start = new BigInteger("600851475143") ;

		//BigInteger start = new BigInteger("69");

		/*System.out.println(start);
		for(int i = 0; i < 20; i++){
			BigInteger c = new BigInteger(Integer.toString(i));
			System.out.printf(i + ": ");
			System.out.println(here.isPrime(c));
		}*/

		ArrayList<BigInteger> print;
		print = here.findPrimes(start);
		for(BigInteger i: print){
			System.out.printf(i+", ");
		}
	}



}