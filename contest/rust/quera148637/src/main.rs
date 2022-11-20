use std::{io, collections::HashMap};



fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let airplanes_bounds: Vec<&str> = buffer.trim().split(' ').collect();

    // get number of air planes and bounds
    let number_of_airplanes: i32 = airplanes_bounds[0].trim().parse().unwrap();
    let number_of_air_bounds: i32 = airplanes_bounds[1].trim().parse().unwrap();

    // create hashmap for showing the status of bounds and airplans
    let mut plane_status: HashMap<String, i32> = HashMap::new();
    let mut bound_status: HashMap<i32, i32> = HashMap::new();

    // getting planes id and set status 1 for all of them
    for _ in 0..number_of_airplanes{
        let mut airplane: String = String::new();
        io::stdin().read_line(&mut airplane).unwrap();
        plane_status.insert(airplane, 1);
    }

    // set the bounds status to -1 means not taken
    for index in 0..number_of_air_bounds {
        bound_status.insert(index, -1);
    }

    // TODO should be in for loop for all the commands
    // get the command and split it 
    let mut commands: String = String::new();
    io::stdin().read_line(& mut commands.to_uppercase()).unwrap();
    let command: Vec<&str> = commands.split(" ").collect();

     
    let state = match command[0] {
        "TAKE-OFF" => {
            if plane_status.get(&command[1].to_owned()) == Some(&4) {
                Some("YOU ARE NOT HERE")
            }else if plane_status.get(&command[1].to_owned()) == Some(&3){
                Some("YOU ARE LANDING NOW")
            }
            else if plane_status.get(&command[1].to_owned()) == Some(&2){
                Some("YOU ARE TAKING OFF")
            }
            else if plane_status.get(&command[1].to_owned()) == Some(&1){
                for (k, v) in bound_status.iter(){
                    if v == &-1 {
                        Some(bound_status[k] = 1);
                    }else{
                        Some("NO FREE BOUND");
                    }
                }
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

