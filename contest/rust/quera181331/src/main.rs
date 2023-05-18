use std::io;
use std::sync::atomic::{AtomicUsize, Ordering};

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

enum CommandType {
    ORDER,
}

struct FoodOrder {
    name: String,
    quantity: usize,
}

impl FoodOrder {
    fn new(food_name: String, quantity: usize) -> Self {
        Self {
            name: food_name,
            quantity,
        }
    }
}

struct Order {
    id: usize,
    foods: Vec<FoodOrder>,
    seat: usize,
    timestamp: String,
}
static COUNTER: AtomicUsize = AtomicUsize::new(0);

impl Order {
    fn get_index(&self) -> usize {
        COUNTER.load(Ordering::Relaxed) + 1
    }

    fn new(&self, foods: Vec<FoodOrder>, seat: usize, timestamp: String) -> Self {
        COUNTER.fetch_add(1, Ordering::Relaxed);
        let index: usize = Order::get_index(&self);
        Self {
            id: index,
            foods,
            seat,
            timestamp,
        }
    }

    fn register_food(&self) {
        let order: String = get_input();
        let mut order_input: Vec<_> = order.trim().split(' ').collect();
        let length = order_input.len();
        let seat_number: usize = order_input[length - 1].parse::<usize>().unwrap();
        let timestamp = order_input[length].to_string();
        // remove order, seat and timestamp from array
        order_input.remove(0);
        order_input.remove(length - 1);
        order_input.remove(length);
        let mut food_array: Vec<FoodOrder> = Vec::new();
        for food_element in order_input {
            let food: Vec<_> = food_element.trim().split('X').collect();
            // create a food order
            let foods = FoodOrder::new(food[0].to_string(), food[1].parse::<usize>().unwrap());
            food_array.push(foods);
        }

        Order::new(self, food_array, seat_number, timestamp);
    }
}

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
