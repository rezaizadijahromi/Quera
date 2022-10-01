use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();

    let airplanes_bounds: Vec<&str> = buffer.trim().split(' ').collect();

    let number_of_airplanes: i32 = airplanes_bounds[0].trim().parse().unwrap();
    let number_of_air_bounds: i32 = airplanes_bounds[1].trim().parse().unwrap();

    let mut airplanes: Vec<String> = Vec::new();
    for _ in 0..number_of_airplanes{
        let mut airplane: String = String::new();
        io::stdin().read_line(&mut airplane).unwrap();
        airplanes.push(airplane);
    }

    let mut commands: String = String::new();
    io::stdin().read_line(& mut commands).unwrap();

}
