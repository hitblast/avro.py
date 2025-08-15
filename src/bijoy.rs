use crate::dictionary::DICTIONARY;
use std::collections::HashMap;

pub fn to_bijoy(text: &str) -> String {
    let mut result = text.to_string();
    
    // Apply bijoy mappings
    for (unicode_char, bijoy_char) in &DICTIONARY.bijoy.mappings {
        result = result.replace(unicode_char, bijoy_char);
    }
    
    result
}

pub fn to_unicode(text: &str) -> String {
    let mut result = text.to_string();
    
    // Apply reverse bijoy mappings
    for (unicode_char, bijoy_char) in &DICTIONARY.bijoy.mappings {
        result = result.replace(bijoy_char, unicode_char);
    }
    
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bijoy_conversion() {
        let unicode_text = "।";
        let bijoy_result = to_bijoy(unicode_text);
        assert_eq!(bijoy_result, "|");
        
        let back_to_unicode = to_unicode(&bijoy_result);
        assert_eq!(back_to_unicode, unicode_text);
    }
}