use std::io;

fn main() {
    let mut inputs: String = String::new();
    io::stdin().read_line(&mut inputs).expect("Some thing went wrong in inputs");

    let numbers: Vec<&str> = inputs.trim().split(" ").collect();

    let startTime: i32 = numbers[0].parse().unwrap();
    let endTime:i32 = numbers[1].parse().unwrap();
    let duration:i32 = numbers[2].parse().unwrap();
    let enterence:i32 = numbers[3].parse().unwrap();

    if enterence < startTime{
        println!("exam did not started!");
    }else if enterence >= endTime{
        println!("exam finished!");
    }else if enterence >= startTime && enterence < endTime{
        if (endTime - enterence) > duration{
            println!("{}", duration)
        }else{
            println!("{}", endTime - enterence)
        }
    }
}
