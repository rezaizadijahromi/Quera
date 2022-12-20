#[derive(Clone)]
struct Plane {
    id: String,
    status: Option<u8>,
    band: Option<u8>,
}
impl Plane {
    /// Create new plane
    fn new(id: String, status: Option<u8>) -> Plane {
        Plane {
            id,
            status,
            band: None,
        }
    }
}
#[derive(PartialEq, Debug)]
enum BandStatus {
    FREE,
    BUSY,
}

struct Band {
    id: u8,
    status: BandStatus,
    airplane: Option<Plane>,
}

impl Band {
    fn new(id: u8) -> Band {
        Band {
            id,
            status: BandStatus::FREE,
            airplane: None,
        }
    }
}

fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let inputs: Vec<&str> = buffer.trim().split(' ').collect();

    let mut planes = Vec::new();
    let mut bands = Vec::new();

    for _ in 0..inputs[0].trim().parse().unwrap() {
        let mut buffer = String::new();
        std::io::stdin().read_line(&mut buffer).unwrap();

        planes.push(Plane::new(buffer.trim().to_string(), Some(1)));
    }
    for i in 0..inputs[1].trim().parse().unwrap() {
        bands.push(Band::new(i));
    }

    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();

    for _ in 0..buffer.trim().parse().unwrap() {
        let mut buffer = String::new();
        std::io::stdin().read_line(&mut buffer).unwrap();
        let command: Vec<&str> = buffer.trim().split(' ').collect();

        match command[0] {
            "TAKE-OFF" => {
                let target_plane = planes
                    .iter_mut()
                    .find(|plane| plane.id == command[1].trim());

                match target_plane {
                    Some(plane) => {
                        if plane.id == command[1].trim().to_string() {
                            if plane.status == Some(4) {
                                println!("YOU ARE NOT HERE");
                            } else if plane.status == Some(3) {
                                println!("YOU ARE LANDING NOW");
                            } else if plane.status == Some(2) {
                                println!("YOU ARE TAKING OFF")
                            } else if plane.status == Some(1) {
                                let target_band = bands
                                    .iter_mut()
                                    .find(|band| band.status == BandStatus::FREE);
                                match target_band {
                                    Some(band) => {
                                        if band.status == BandStatus::FREE {
                                            plane.status = Some(2);
                                            plane.band = Some(band.id);
                                            band.status = BandStatus::BUSY;
                                            band.airplane = Some(plane.clone());
                                        }
                                    }
                                    None => println!("NO FREE BOUND"),
                                }
                            }
                        }
                    }
                    None => planes.push(Plane::new(command[1].trim().to_string(), Some(4))),
                }
            }
            "LANDING" => {
                let target_plane = planes
                    .iter_mut()
                    .find(|plane| plane.id == command[1].trim());
                match target_plane {
                    Some(plane) => {
                        if plane.status == Some(1) {
                            println!("YOU ARE HERE");
                        } else if plane.status == Some(2) {
                            println!("YOU ARE TAKING");
                        } else if plane.status == Some(3) {
                            println!("YOU ARE LANDING NOW");
                        } else if plane.status == Some(4) {
                            let target_band = bands
                                .iter_mut()
                                .rev()
                                .find(|band| band.status == BandStatus::FREE);

                            match target_band {
                                Some(band) => {
                                    if band.status == BandStatus::FREE {
                                        plane.status = Some(3);
                                        plane.band = Some(band.id);
                                        band.status = BandStatus::BUSY;
                                        band.airplane = Some(plane.clone());
                                    }
                                }
                                None => println!("NO FREE BOUND"),
                            }
                        }
                    }
                    None => planes.push(Plane::new(command[1].trim().to_string(), Some(4))),
                }
            }
            "PLANE-STATUS" => {
                for plane in planes.iter() {
                    if plane.id == command[1].trim() {
                        println!("{:?}", plane.status.unwrap());
                    }
                }
            }
            "BAND-STATUS" => {
                let target_band = bands
                    .iter()
                    .find(|band| band.id == command[1].trim().parse().unwrap());

                match target_band {
                    Some(band) => println!("{:#?}", band.airplane.clone().unwrap().id),
                    None => println!("FREE"),
                }
            }
            _ => (),
        };
    }
}
