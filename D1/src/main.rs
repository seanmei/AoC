use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec::{Vec, self};
use std::fmt::Debug;
 
fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("input.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut cals= Vec::new();

        for line in lines {
            if let Ok(ip) = line {
                cals.push(ip);
                
                
               // println!("{}", ip);
            }
        }
        add_calories(cals);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn add_calories<VEC :Debug>(cals: VEC){
    for cal in cals.into_inter() {

    }


}