use pyo3::prelude::*;

mod dictionary;
mod parser;
mod bijoy;

use parser::parse_text;
use bijoy::{to_bijoy, to_unicode};

/// Parses English text to Bengali using Avro phonetic rules
#[pyfunction]
#[pyo3(signature = (text, bijoy=None, remap_words=None))]
fn parse(text: &str, bijoy: Option<bool>, remap_words: Option<bool>) -> PyResult<String> {
    let bijoy = bijoy.unwrap_or(false);
    let remap_words = remap_words.unwrap_or(true);
    
    let result = parse_text(text, remap_words);
    
    if bijoy {
        Ok(to_bijoy(&result))
    } else {
        Ok(result)
    }
}

/// Converts Bengali Unicode text to Bijoy format
#[pyfunction]
fn to_bijoy_rs(text: &str) -> PyResult<String> {
    Ok(to_bijoy(text))
}

/// Converts Bijoy format text to Bengali Unicode
#[pyfunction]
fn to_unicode_rs(text: &str) -> PyResult<String> {
    Ok(to_unicode(text))
}

/// A Python module implemented in Rust.
#[pymodule]
fn avro_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse, m)?)?;
    m.add_function(wrap_pyfunction!(to_bijoy_rs, m)?)?;
    m.add_function(wrap_pyfunction!(to_unicode_rs, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_parse() {
        let result = parse_text("ami banglay gan gai", true);
        assert!(result.contains("আমি"));
    }
}
