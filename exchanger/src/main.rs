use std::collections::HashMap;
use anyhow::Result;
use reqwest::blocking::get;
use serde::Deserialize;

#[derive(Deserialize)]
struct ApiResponse {
    conversion_rates: HashMap<String, f64>,
}

fn make_request() -> Result<()>
{
    let result = get("https://v6.exchangerate-api.com/v6/3420cb14e546955c837e27b5/latest/USD")?;
    
    println!("Status: {}", result.status());

    // Parse out that string
    let api_response: ApiResponse = result.json()?;
    
    if let Some(conv_rate) = api_response.conversion_rates.get("JPY") {
        println!("USD to JPY: {}", conv_rate);
    } else {
        println!("Rate not found in response.");
    }

    Ok(())
}



fn main() -> Result<()>
{
    make_request()?;
    Ok(())
}