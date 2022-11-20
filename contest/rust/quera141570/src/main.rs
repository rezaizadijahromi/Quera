
use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
   
    let score = buffer.trim().parse::<i32>().unwrap();

    if score >= 7 {
        println!("black");
    }else if score == 0{
        println!("out");
    }else{
        println!("white");
    }

}
