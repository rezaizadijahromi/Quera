use std::io;

fn main() {
    let mut inputs: String = String::new();
    io::stdin().read_line(&mut inputs).expect("Some thing went wrong in inputs");

    let numbers: Vec<&str> = inputs.trim().split(" ").collect();
    let n = numbers[0].parse::<i32>().unwrap();
    let k = numbers[1].parse::<i32>().unwrap();

    if n % k == 0{
        println!("YES");
    }else{
        println!("NO")
    }
}
