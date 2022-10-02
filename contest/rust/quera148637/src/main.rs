use std::{io, collections::HashMap};



fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();

    let airplanes_bounds: Vec<&str> = buffer.trim().split(' ').collect();

    let number_of_airplanes: i32 = airplanes_bounds[0].trim().parse().unwrap();
    let number_of_air_bounds: i32 = airplanes_bounds[1].trim().parse().unwrap();

    let mut plane_status: HashMap<String, i32> = HashMap::new();

    for _ in 0..number_of_airplanes{
        let mut airplane: String = String::new();
        io::stdin().read_line(&mut airplane).unwrap();
        plane_status.insert(airplane, 1);
    }

    let mut commands: String = String::new();
    io::stdin().read_line(& mut commands.to_uppercase()).unwrap();

    let command: Vec<&str> = commands.split(" ").collect();

     
    let state = match command[0] {
        "TAKE-OFF" => {
            if plane_status.get(&command[1].to_owned()) == Some(&4) {
                Some("YOU ARE NOT HERE")
            }else{
                None
            }
        },
        "LANDING" => {
            if plane_status.get(&command[1].to_owned()) == Some(&4) {
                Some("YOU ARE NOT HERE")
            }else{
                None
            }
        },
        _ => None
    };

}

