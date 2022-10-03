use std::io;

fn main() {
    let mut n: String = String::new();
    io::stdin().read_line(&mut n).expect("Some thing went wrong in inputs");


    let mut inputs: String = String::new();
    io::stdin().read_line(&mut inputs).expect("Some thing went wrong in inputs");

    let numbers: Vec<&str> = inputs.trim().split(" ").collect();

    let mut results: Vec<&str> = Vec::new();
    for i in 0..numbers.len(){
        if numbers[i].parse::<i32>().unwrap() > 15 {
            results.push("cooler");
        }else{
            results.push("heater");
        }
    }

    for i in results{
        println!("{}", i);
    }
    
}
