use std::{io, collections::HashMap};


enum PlaneStatus {
    FREE,
    LANDING,
    TAKE_OFF,
    NOT_IN_AIRPORT
}

enum BandStatus{
    FREE,
    BUSY(i32)
}
struct Plane {
    id: String,
    status: PlaneStatus,
    band: i32
}

impl Plane {
    fn new(self) -> Self {
        Self {
            id: self.id,
            status: PlaneStatus::FREE,
            band: -1
        }
    }
}
struct Band{
    id: i32,
    status: BandStatus 
}

impl Band {
    fn new(self) -> Self{
        Self{
            id: self.id,
            status: BandStatus::FREE
        }
    }
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let airplanes_bounds: Vec<&str> = buffer.trim().split(' ').collect();

    // get number of air planes and bounds
    let number_of_airplanes: i32 = airplanes_bounds[0].trim().parse().unwrap();
    let number_of_air_bounds: i32 = airplanes_bounds[1].trim().parse().unwrap();

    // create hashmap for showing the status of bounds and airplans
    // TODO: For better managing and design should create a plane struct
    let mut plane_status: HashMap<String, i32> = HashMap::new();
    let mut bound_status: HashMap<i32, i32> = HashMap::new();

    // getting planes id and set status 1 for all of them
    for _ in 0..number_of_airplanes{
        let mut airplane: String = String::new();
        io::stdin().read_line(&mut airplane).unwrap();

        plane_status.insert(airplane.strip_suffix("\r\n").unwrap().to_string(), 1);
    }
    // set the bounds status to -1 means not taken
    for index in 0..number_of_air_bounds {
        bound_status.insert(index, -1);
    }

    println!("airplanes: {:?}", plane_status);

    // TODO should be in for loop for all the commands
    // get the command and split it 
    let mut commands: String = String::new();
    io::stdin().read_line(&mut commands).unwrap();
    let command: Vec<&str> = commands.split(" ").collect();

    let _state = match command[0] {
        "TAKE-OFF" => {
            if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&4) {
                Some("YOU ARE NOT HERE")
            }else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&3){
                Some("YOU ARE LANDING NOW")
            }
            else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&2){
                Some("YOU ARE TAKING OFF")
            }
            else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&1){
                for (k, v) in bound_status.to_owned().iter_mut(){
                    if v == &-1{
                        // when the bound is empty assign the plane to take off
                        *bound_status.get_mut(&k).unwrap() = match command[1].strip_suffix("\r\n").unwrap().parse::<i32>(){
                            Ok(c) => c,
                            Err(e) => panic!("{}", e)
                        };
                        // update the plane status
                        *plane_status.get_mut(&command[1].strip_suffix("\r\n").unwrap().to_owned()).unwrap() = 2;
                        break;
                    }else{
                        Some("NO FREE BOUND");
                    }
                }
                Some("Something")
            }else{
                None
            }
        },
        "LANDING" => {
            if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&1) {
                Some("YOU ARE HERE")
            }else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&2){
                Some("YOU ARE TAKING OFF")
            }else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&3){
                Some("YOU ARE LANDING NOW")
            }else if plane_status.get(&command[1].strip_suffix("\r\n").unwrap().to_owned()) == Some(&4){ 
                for (k, v) in bound_status.to_owned().iter_mut(){
                    if v == &-1{
                        // TODO Have to assign to the biggest bound
                        *bound_status.get_mut(&k).unwrap() = match command[1].strip_suffix("\r\n").unwrap().parse::<i32>(){
                            Ok(c) => c,
                            Err(e) => panic!("{}", e)
                        };

                        *plane_status.get_mut(&command[1].strip_suffix("\r\n").unwrap().to_owned()).unwrap() = 3;
                        break;
                    }else{
                        Some("NO FREE BOUND");
                    }
                }
                Some("Something")
            }
            else{
                None
            }
        },
        "PLANE-STATUS" => {
            
            Some("")
        }
        _ => None
    };

}

