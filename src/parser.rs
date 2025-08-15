use crate::dictionary::{DICTIONARY, Pattern};
use regex::Regex;
use std::collections::HashMap;

pub fn parse_text(text: &str, _remap_words: bool) -> String {
    let mut result = String::new();
    let mut chars: Vec<char> = text.chars().collect();
    let mut i = 0;

    while i < chars.len() {
        let mut found_match = false;
        
        // Try to match patterns starting from the longest possible
        for pattern_len in (1..=std::cmp::min(5, chars.len() - i)).rev() {
            if i + pattern_len <= chars.len() {
                let substr: String = chars[i..i + pattern_len].iter().collect();
                
                // Look for pattern match
                for pattern in &DICTIONARY.avro.patterns {
                    if pattern.find == substr {
                        result.push_str(&pattern.replace);
                        i += pattern_len;
                        found_match = true;
                        break;
                    }
                }
                
                if found_match {
                    break;
                }
            }
        }
        
        // If no pattern matched, keep the original character
        if !found_match {
            result.push(chars[i]);
            i += 1;
        }
    }
    
    result
}

pub fn fix_string_case(text: &str) -> String {
    // For now, just return as-is. We can implement case fixing later
    text.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_parsing() {
        let result = parse_text("ami", true);
        assert!(result.len() > 0);
    }
}