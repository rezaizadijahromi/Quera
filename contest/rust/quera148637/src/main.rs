use std::{io, collections::HashMap, cmp::Ordering};

#[allow(dead_code, non_camel_case_types)]
#[derive(Clone,Copy, PartialEq, PartialOrd)]
enum PlaneStatus {
    FREE(i32),
    LANDING(i32),
    TAKE_OFF(i32),
    NOT_IN_AIRPORT(i32)
}
#[allow(dead_code)]
#[derive(Clone,Copy, PartialEq,PartialOrd)]
enum BandStatus{
    FREE(i32),
    BUSY(i32)
}
#[allow(dead_code)]
#[derive(Clone, PartialEq, PartialOrd)]
struct Plane {
    id: String,
    status: PlaneStatus,
    band: i32
}

#[allow(dead_code)]
impl Plane {
    fn new(id: String, status: PlaneStatus, band: i32) -> Self {
        Self {
            id,
            status,
            band
        }
    }
    fn status(&self) -> PlaneStatus{
        self.status
    }

    fn assign_to_band(&mut self, band: i32) -> i32 {
        self.band = band;
        return  self.band;
    }
}
#[allow(dead_code)]
#[derive(Clone,PartialEq, PartialOrd)]
struct Band{
    id: i32,
    status: BandStatus,
    airplane: Plane
}

#[allow(dead_code)]
impl Band {
    fn new(id: i32, status: BandStatus, airplane: Plane) -> Self{
        Self{
            id,
            status,
            airplane
        }
    }
    fn status(&self) -> BandStatus{
        self.status
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
    // list of planes
    let mut planes: Vec<Plane> = vec![];
    let mut bands: Vec<Band> = vec![];

    // getting planes id and set status 1 for all of them
    for _ in 0..number_of_airplanes{
        let mut airplane: String = String::new();
        io::stdin().read_line(&mut airplane).unwrap();   
        let plane: Plane = Plane::new(airplane.strip_suffix("\r\n").unwrap().to_string(), PlaneStatus::FREE(0), -1);
        planes.push(plane);
        
    }
    // set the bounds status to -1 means not taken
    for index in 0..number_of_air_bounds {
        let band: Band = Band::new(
            index, BandStatus::FREE(0),
         Plane { id: String::from(""), status: PlaneStatus::FREE(1), band: -1 }
        );
        bands.push(band);
    }

    println!("airplanes: {:?}", plane_status);
    // get the number of command and create loop for it
    let mut commands_count = String::new();
    // TODO should be in for loop for all the commands
    io::stdin().read_line(&mut commands_count).unwrap();
    for _ in 0..commands_count.trim().parse().unwrap(){
        // get the command and split it 
        let mut commands: String = String::new();
        io::stdin().read_line(&mut commands).unwrap();
        let command: Vec<&str> = commands.split(" ").collect();
        
        // Branches
        let _state = match command[0] {
            "TAKE-OFF" => {
                for plane in planes{
                    if plane.id == command[1].trim(){
                        if plane.status == PlaneStatus::NOT_IN_AIRPORT(4){
                            Some("YOU ARE NOT HERE");
                        }else if plane.status == PlaneStatus::LANDING(3){
                            Some("YOU ARE LANDING NOW");
                        }else if plane.status == PlaneStatus::TAKE_OFF(2){
                            Some("YOU ARE TAKING OFF");
                        }else if plane.status == PlaneStatus::FREE(1) {
                            let min_band:i32 = 0;
                            for band in bands{
                                if band.id == 0 && band.status == BandStatus::FREE(0){
                                    plane.band = band.id;
                                    plane.status = PlaneStatus::TAKE_OFF(2);
                                    band.airplane = plane;
                                    band.status = BandStatus::BUSY(1);
                                }else{
                                    Some("NO FREE BOUND");
                                }
                            };
                            // update for assing min band id
                            min_band += 1;
                        }else{
                            None;
                        }
                    }
                }
                break;
            },
            "LANDING" => { 
                for plane in planes{
                    if plane.id == command[1].trim(){
                        if plane.status == PlaneStatus::FREE(1){
                            Some("YOU ARE HERE");
                        }else if plane.status == PlaneStatus::TAKE_OFF(2){
                            Some("YOU ARE TAKING OFF");
                        }else if plane.status == PlaneStatus::LANDING(3){
                            Some("YOU ARE LANDING NOW");
                        }else if plane.status == PlaneStatus::NOT_IN_AIRPORT(4) {
                            // change the airplane status
                            plane.status = PlaneStatus::LANDING(3);
                            // finding the max value 
                            // TODO it's not all correct
                            let index_of_max: Option<usize> = bands
                                        .iter()
                                        .enumerate()
                                        .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap_or(Ordering::Equal))
                                        .map(|(index, _)| index);
                            let max_bound = bands.get(index_of_max.unwrap()).unwrap();            
                            if max_bound.status == BandStatus::FREE(0){
                                plane.band = max_bound.id;
                                max_bound.status = BandStatus::BUSY(1);
                                max_bound.airplane = plane;
                            }else{
                                Some("NO FREE BOUND");
                            } 
                        }else{
                            None;
                        }
                    }
                }
                break;
            },
            "PLANE-STATUS" => {
                for plane in planes{
                    if plane.id == command[1].trim(){
                        Some(plane.status);
                    }else{
                        None;
                    }
                }
                break;
            },
            "BAND-STATUS" => {
                for band in bands{
                    if band.id == command[1].trim().parse::<i32>().unwrap(){
                        Some(band.status);
                    }else{
                        None;
                    }
                }
                break;
            }
            _ => None
        };
    }


    // the branches are broken now
    // TODO: New implementation needed here
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

