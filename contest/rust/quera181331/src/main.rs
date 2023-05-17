use std::{io, vec};

#[allow(dead_code)]
#[derive(Clone, Debug)]
struct Food {
    id: usize,
    name: String,
    price: usize,
}
impl Food {
    fn new(id: usize, name: String, price: usize) -> Self {
        Self { id, name, price }
    }

    fn initialize_food(quantity: usize) -> Vec<Self> {
        let mut food_array: Vec<Food> = Vec::new();
        // initiliza the food on menu
        for i in 0..quantity {
            let food = get_input();
            let food_input: Vec<_> = food.trim().split(' ').collect();
            food_array.push(Food::new(
                i,
                food_input[0].to_owned(),
                food_input[1].parse::<usize>().unwrap(),
            ));
        }

        return food_array;
    }
}

#[allow(dead_code)]
struct Table {
    id: usize,
    capacity: usize,
}

impl Table {
    fn new(id: usize, capacity: usize) -> Self {
        Self { id, capacity }
    }

    fn initialize_table() -> Vec<Self> {
        let mut tables_array: Vec<Table> = Vec::new();
        let table = get_input();
        let table_input: Vec<_> = table.trim().split(' ').collect();
        let mut counter = 0;
        for i in table_input.iter() {
            tables_array.push(Table::new(counter, i.parse::<usize>().unwrap()));
            counter += 1;
        }

        return tables_array;
    }
}

enum CommandType {}
struct Command {}

fn get_input() -> String {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input
}

fn main() {
    let binding = get_input();
    let initial_inputs: Vec<&str> = binding.trim().split(' ').collect();
    let n: usize = initial_inputs[0].parse::<usize>().unwrap();
    let m: usize = initial_inputs[1].parse::<usize>().unwrap();
    // let k: usize = initial_inputs[2].parse::<usize>().unwrap();

    let food_values: Vec<Food> = Food::initialize_food(m);
    let talbe_vales: Vec<Table> = Table::initialize_table();
}
