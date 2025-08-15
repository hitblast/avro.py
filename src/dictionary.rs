use std::collections::HashMap;
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Pattern {
    pub find: String,
    pub replace: String,
    pub reverse: Option<String>,
    pub rules: Option<Vec<Rule>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Rule {
    pub matches: Vec<MatchCondition>,
    pub replace: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MatchCondition {
    #[serde(rename = "type")]
    pub match_type: String,
    pub scope: String,
    pub value: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AvroData {
    pub patterns: Vec<Pattern>,
    pub vowel: String,
    pub consonant: String,
    pub casesensitive: String,
    pub number: String,
    pub shorborno: String,
    pub shongkha: String,
    pub kar: Vec<String>,
    pub ignore: Vec<String>,
    pub exceptions: HashMap<String, String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BijoyData {
    pub mappings: HashMap<String, String>,
    pub prekar: Vec<String>,
    pub postkar: Vec<String>,
    pub banjonborno: Vec<String>,
    pub exceptions: HashMap<String, String>,
}

pub struct Dictionary {
    pub avro: AvroData,
    pub bijoy: BijoyData,
}

// Simplified dictionary with essential patterns for basic functionality
pub static DICTIONARY: Lazy<Dictionary> = Lazy::new(|| {
    let basic_patterns = vec![
        // Basic vowels
        Pattern { find: "a".to_string(), replace: "আ".to_string(), reverse: Some("a".to_string()), rules: None },
        Pattern { find: "i".to_string(), replace: "ই".to_string(), reverse: Some("i".to_string()), rules: None },
        Pattern { find: "u".to_string(), replace: "উ".to_string(), reverse: Some("u".to_string()), rules: None },
        Pattern { find: "e".to_string(), replace: "এ".to_string(), reverse: Some("e".to_string()), rules: None },
        Pattern { find: "o".to_string(), replace: "ও".to_string(), reverse: Some("o".to_string()), rules: None },
        
        // Basic consonants
        Pattern { find: "k".to_string(), replace: "ক".to_string(), reverse: Some("k".to_string()), rules: None },
        Pattern { find: "g".to_string(), replace: "গ".to_string(), reverse: Some("g".to_string()), rules: None },
        Pattern { find: "c".to_string(), replace: "চ".to_string(), reverse: Some("ch".to_string()), rules: None },
        Pattern { find: "j".to_string(), replace: "জ".to_string(), reverse: Some("j".to_string()), rules: None },
        Pattern { find: "t".to_string(), replace: "ত".to_string(), reverse: Some("t".to_string()), rules: None },
        Pattern { find: "d".to_string(), replace: "দ".to_string(), reverse: Some("d".to_string()), rules: None },
        Pattern { find: "n".to_string(), replace: "ন".to_string(), reverse: Some("n".to_string()), rules: None },
        Pattern { find: "p".to_string(), replace: "প".to_string(), reverse: Some("p".to_string()), rules: None },
        Pattern { find: "b".to_string(), replace: "ব".to_string(), reverse: Some("b".to_string()), rules: None },
        Pattern { find: "v".to_string(), replace: "ভ".to_string(), reverse: Some("bh".to_string()), rules: None },
        Pattern { find: "m".to_string(), replace: "ম".to_string(), reverse: Some("m".to_string()), rules: None },
        Pattern { find: "r".to_string(), replace: "র".to_string(), reverse: Some("r".to_string()), rules: None },
        Pattern { find: "l".to_string(), replace: "ল".to_string(), reverse: Some("l".to_string()), rules: None },
        Pattern { find: "s".to_string(), replace: "স".to_string(), reverse: Some("s".to_string()), rules: None },
        Pattern { find: "h".to_string(), replace: "হ".to_string(), reverse: Some("h".to_string()), rules: None },
        Pattern { find: "y".to_string(), replace: "য".to_string(), reverse: Some("j".to_string()), rules: None },
        
        // Common combinations
        Pattern { find: "ng".to_string(), replace: "ং".to_string(), reverse: Some("ng".to_string()), rules: None },
        Pattern { find: "ch".to_string(), replace: "ছ".to_string(), reverse: Some("ch".to_string()), rules: None },
        Pattern { find: "th".to_string(), replace: "থ".to_string(), reverse: Some("th".to_string()), rules: None },
        Pattern { find: "dh".to_string(), replace: "ধ".to_string(), reverse: Some("dh".to_string()), rules: None },
        Pattern { find: "bh".to_string(), replace: "ভ".to_string(), reverse: Some("bh".to_string()), rules: None },
        Pattern { find: "sh".to_string(), replace: "শ".to_string(), reverse: Some("sh".to_string()), rules: None },
        
        // Special characters
        Pattern { find: ".".to_string(), replace: "।".to_string(), reverse: Some(".".to_string()), rules: None },
    ];

    let mut bijoy_mappings = HashMap::new();
    // Add basic Bijoy mappings
    bijoy_mappings.insert("।".to_string(), "|".to_string());
    bijoy_mappings.insert("আ".to_string(), "Av".to_string());
    bijoy_mappings.insert("ই".to_string(), "B".to_string());
    bijoy_mappings.insert("উ".to_string(), "D".to_string());
    bijoy_mappings.insert("এ".to_string(), "G".to_string());
    bijoy_mappings.insert("ও".to_string(), "I".to_string());

    let avro_data = AvroData {
        patterns: basic_patterns,
        vowel: "aeiou".to_string(),
        consonant: "bcdfghjklmnpqrstvwxyz".to_string(),
        casesensitive: "oiudgjnrstyz".to_string(),
        number: "0123456789".to_string(),
        shorborno: "অআইঈউঊএঐওঔ".to_string(),
        shongkha: "০১২৩৪৫৬৭৮৯".to_string(),
        kar: vec!["া".to_string(), "ি".to_string(), "ী".to_string()],
        ignore: vec!["ঁ".to_string(), "।".to_string()],
        exceptions: HashMap::new(),
    };

    let bijoy_data = BijoyData {
        mappings: bijoy_mappings,
        prekar: Vec::new(),
        postkar: Vec::new(),
        banjonborno: Vec::new(),
        exceptions: HashMap::new(),
    };

    Dictionary {
        avro: avro_data,
        bijoy: bijoy_data,
    }
});