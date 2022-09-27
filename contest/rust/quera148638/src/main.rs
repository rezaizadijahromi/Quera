use std::io;


struct Perspolis{
    away_scores: i32,
    total_scores: i32
}

struct Esteghlal{
    away_scores: i32,
    total_scores: i32
}

fn main() {
    let mut number_of_game = String::new(); 
    io::stdin().read_line(&mut number_of_game).unwrap();
    let number_of_game: i32 = number_of_game.trim().parse().unwrap();

    let mut results: Vec<&str> = Vec::new();

    for _ in 1..=number_of_game {

        let mut perspolis = Perspolis {
            away_scores: 0,
            total_scores: 0
        };
    
        let mut esteghlal = Esteghlal {
            away_scores: 0,
            total_scores: 0
        };

        let mut games: String = String::new(); 
        io::stdin().read_line(&mut games).unwrap();
        
        let game_score_process: Vec<&str> = games.trim().split(' ').collect();

            if game_score_process[0].parse::<i32>().unwrap() > game_score_process[1].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[0].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[1].parse::<i32>().unwrap();
                esteghlal.away_scores = game_score_process[1].parse::<i32>().unwrap();
            }else if game_score_process[0].parse::<i32>().unwrap() < game_score_process[1].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[0].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[1].parse::<i32>().unwrap();
                esteghlal.away_scores = game_score_process[1].parse::<i32>().unwrap();
            }else if game_score_process[0].parse::<i32>().unwrap() == game_score_process[1].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[0].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[1].parse::<i32>().unwrap();
                esteghlal.away_scores = game_score_process[1].parse::<i32>().unwrap();
            }


            if game_score_process[2].parse::<i32>().unwrap() > game_score_process[3].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[2].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[3].parse::<i32>().unwrap();
                perspolis.away_scores = game_score_process[2].parse::<i32>().unwrap();
            }else if game_score_process[2].parse::<i32>().unwrap() < game_score_process[3].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[2].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[3].parse::<i32>().unwrap();
                perspolis.away_scores = game_score_process[2].parse::<i32>().unwrap();
            }else if game_score_process[2].parse::<i32>().unwrap() == game_score_process[3].parse::<i32>().unwrap(){
                perspolis.total_scores += game_score_process[2].parse::<i32>().unwrap();
                esteghlal.total_scores += game_score_process[3].parse::<i32>().unwrap();
                perspolis.away_scores = game_score_process[2].parse::<i32>().unwrap();
            }

            if perspolis.total_scores == esteghlal.total_scores{
                if esteghlal.away_scores > perspolis.away_scores {
                    results.push("esteghlal");
                }else if perspolis.away_scores > esteghlal.away_scores{
                    results.push("perspolis");

                }else if perspolis.away_scores == esteghlal.away_scores{
                    results.push("penalty");
                }
            } else if perspolis.total_scores > esteghlal.total_scores{
                results.push("perspolis");
            }else if perspolis.total_scores < esteghlal.total_scores{
                results.push("esteghlal");
            }
    }

    for index in 0..results.len(){
        println!("{}", results[index]);
    }

}
