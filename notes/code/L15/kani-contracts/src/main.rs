fn main() {
    println!("Hello, world!");
}

#[kani::requires(min != 0 && max != 0)]
#[kani::ensures(|result| *result != 0 && max % *result == 0 && min % *result == 0)]
#[kani::recursion]
fn gcd(mut max: u8, mut min: u8) -> u8 {
    if min > max {
        std::mem::swap(&mut max, &mut min);
    }

    let rest = max % min;
    if rest == 0 { min } else { gcd(min, rest) }
}

// cargo kani -Z function-contracts
#[kani::proof_for_contract(gcd)]
fn check_gcd() {
    let max: u8 = kani::any();
    let min: u8 = kani::any();
    gcd(max, min);
}
