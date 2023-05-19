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
#[derive(PartialEq, Debug, Clone, Copy)]
enum TableStatus {
    FREE,
    TAKEN,
}

#[allow(dead_code)]
#[derive(Debug, Clone)]
enum TimeStamp {
    FREE,
    TimeFormat(String),
}
#[allow(dead_code)]
#[derive(Debug, Clone)]
struct Table {
    id: usize,
    capacity: usize,
    status: TableStatus,
    timestamp: TimeStamp,
}

impl Table {
    fn new(id: usize, capacity: usize) -> Self {
        Self {
            id,
            capacity,
            status: TableStatus::FREE,
            timestamp: TimeStamp::FREE,
        }
    }

    fn initialize_table() -> Vec<Table> {
        let table = get_input();
        let table_input: Vec<&str> = table.trim().split(' ').collect();

        let mut counter = 0;
        let mut tables_array: Vec<Table> = Vec::new();
        for i in table_input.into_iter() {
            tables_array.push(Table::new(counter, i.parse::<usize>().unwrap()));
            counter += 1;
        }

        return tables_array;
    }
}
#[allow(dead_code)]
enum MessageStatus {
    NotEnogh,
    WaitList,
    Ready,
}

#[allow(dead_code)]
struct Message {
    message: Option<String>,
    status: MessageStatus,
}

impl Message {
    fn messaging(status: MessageStatus, table_number: Option<&usize>) -> Option<String> {
        let msg: Option<String> = match status {
            MessageStatus::NotEnogh => Some("not enough seat.".to_string()),
            MessageStatus::WaitList => Some("please wait for free table.".to_string()),
            MessageStatus::Ready => Some(format!("please seat at table number {:?}", table_number)),
        };

        return msg;
    }
}

#[derive(Debug)]
#[allow(dead_code)]
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

#[derive(Debug)]
#[allow(dead_code)]
struct Order {
    id: usize,
    foods: Vec<FoodOrder>,
    table: Table,
    timestamp: String,
}
static COUNTER: AtomicUsize = AtomicUsize::new(0);

impl Order {
    fn get_index() -> usize {
        COUNTER.load(Ordering::Relaxed) + 1
    }

    fn new(foods: Vec<FoodOrder>, table: Table, timestamp: String) -> Self {
        COUNTER.fetch_add(1, Ordering::Relaxed);
        let index: usize = Order::get_index();
        Self {
            id: index,
            foods,
            table,
            timestamp,
        }
    }

    fn check_table(seat: usize, tables: Vec<Table>) -> (bool, Option<Table>) {
        let filterd_table = tables
            .iter()
            .filter(|t| t.status == TableStatus::FREE && t.capacity <= seat)
            .min_by(|a, b| a.id.partial_cmp(&b.id).unwrap());

        if filterd_table.is_none() {
            return (false, None);
        } else {
            // println!("table: {:#?}", filterd_table);
            return (true, Some(filterd_table.unwrap().clone()));
        }
    }

    fn register_food(tables: &mut Vec<Table>) -> (String, Option<Order>) {
        let order: String = get_input();
        let mut order_input: Vec<_> = order.trim().split(' ').collect();
        // remove order command
        order_input.remove(0);
        // get timestamp
        let timestamp = order_input.pop().unwrap().to_string();
        // get number of seat needed for order
        let seat_number: usize = order_input.pop().unwrap().parse::<usize>().unwrap();
        // check if we have enoght seat on out tables or not
        let table_status: (bool, Option<Table>) = Order::check_table(seat_number, tables.clone());
        // if true we have available seats else weather our tables don't have enoght seats or our tables are taken
        if table_status.0 {
            // register given order
            let mut food_array: Vec<FoodOrder> = Vec::new();
            for food_element in order_input {
                // seperate the food name from the quantity
                let food: Vec<_> = food_element.trim().split('X').collect();
                // create a food order
                let foods = FoodOrder::new(food[0].to_string(), food[1].parse::<usize>().unwrap());
                food_array.push(foods);
            }
            // update table status to taken and change the timestamp
            let mut update_table = tables
                .iter_mut()
                .find(|t| t.id == table_status.1.clone().unwrap().id)
                .unwrap();

            update_table.status = TableStatus::TAKEN;
            update_table.timestamp = TimeStamp::TimeFormat(timestamp.clone());

            let registerd_order = Some(Order::new(
                food_array,
                table_status.1.as_ref().unwrap().clone(),
                timestamp,
            ));
            return (
                Message::messaging(MessageStatus::Ready, Some(&table_status.1.unwrap().id))
                    .unwrap(),
                registerd_order,
            );
        } else {
            // TODO proper message for not enoght seat and wait list
            return (
                Message::messaging(MessageStatus::NotEnogh, None).unwrap(),
                None,
            );
        }
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
    let _food_values: Vec<Food> = Food::initialize_food(m);
    let mut table_values: Vec<Table> = Table::initialize_table();

    // add command loop
    for _i in 0..n {
        let command = get_input();
        let command_input: Vec<_> = command.trim().split(' ').collect();
        match command_input[0] {
            "order" => {
                Order::register_food(&mut table_values);
                // order1.1.unwrap().table.status = TableStatus::TAKEN;
                //update_tables_status(&mut table_values, order1.1.unwrap());
                println!("{:?}", table_values);
            }
            _ => (),
        }
    }
}
