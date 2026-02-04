use std::collections::HashMap;
use anyhow::Result;
use reqwest::blocking::get;
use serde::Deserialize;

/*
 *
 * Make the API call to the weather website and store the response for the USD -> JPY conversion rates.
 *
 */
#[derive(Debug, Deserialize)]
struct ApiResponse {
    conversion_rates: HashMap<String, f64>,
}

fn make_request() -> Result<Option<f64>>
{
    let response = get("https://v6.exchangerate-api.com/v6/3420cb14e546955c837e27b5/latest/USD")?;
    
    println!("Status: {}", response.status());

    let api_response: ApiResponse = response.json()?;

    // Pull out JPY entry for later
    Ok(api_response.conversion_rates.get("JPY").copied())
}

/*
 *
 *  Time to make the GUI for the program now that we can make the request. make_request() will run
 *  on program start then GUI will run continuously.
 *
 * */

fn main() -> Result<()>
{

    // Call pull function to get rate for later use
    let jpy_rate = make_request()?;

    match jpy_rate {
        Some(rate) => println!("Fetched USD -> JPY rate = {}", rate),
        None => eprintln!("JPY rate not present in API response!"),
    }

    Ok(())



}
