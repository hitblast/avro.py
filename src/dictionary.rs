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
        Pattern { find: "bhl".to_string(), replace: "ভ্ল".to_string(), reverse: None, rules: None },
        Pattern { find: "psh".to_string(), replace: "পশ".to_string(), reverse: None, rules: None },
        Pattern { find: "bdh".to_string(), replace: "ব্ধ".to_string(), reverse: Some("bdh".to_string()), rules: None },
        Pattern { find: "bj".to_string(), replace: "ব্জ".to_string(), reverse: Some("bj".to_string()), rules: None },
        Pattern { find: "bd".to_string(), replace: "ব্দ".to_string(), reverse: Some("bd".to_string()), rules: None },
        Pattern { find: "bb".to_string(), replace: "ব্ব".to_string(), reverse: Some("bb".to_string()), rules: None },
        Pattern { find: "bl".to_string(), replace: "ব্ল".to_string(), reverse: Some("bl".to_string()), rules: None },
        Pattern { find: "bh".to_string(), replace: "ভ".to_string(), reverse: Some("bh".to_string()), rules: None },
        Pattern { find: "vl".to_string(), replace: "ভ্ল".to_string(), reverse: Some("vl".to_string()), rules: None },
        Pattern { find: "b".to_string(), replace: "ব".to_string(), reverse: Some("b".to_string()), rules: None },
        Pattern { find: "v".to_string(), replace: "ভ".to_string(), reverse: Some("bh".to_string()), rules: None },
        Pattern { find: "cNG".to_string(), replace: "চ্ঞ".to_string(), reverse: Some("cng".to_string()), rules: None },
        Pattern { find: "cch".to_string(), replace: "চ্ছ".to_string(), reverse: Some("cch".to_string()), rules: None },
        Pattern { find: "cc".to_string(), replace: "চ্চ".to_string(), reverse: Some("cc".to_string()), rules: None },
        Pattern { find: "ch".to_string(), replace: "ছ".to_string(), reverse: None, rules: None },
        Pattern { find: "c".to_string(), replace: "চ".to_string(), reverse: Some("ch".to_string()), rules: None },
        Pattern { find: "dhn".to_string(), replace: "ধ্ন".to_string(), reverse: Some("dhn".to_string()), rules: None },
        Pattern { find: "dhm".to_string(), replace: "ধ্ম".to_string(), reverse: Some("dhm".to_string()), rules: None },
        Pattern { find: "dgh".to_string(), replace: "দ্ঘ".to_string(), reverse: Some("dgh".to_string()), rules: None },
        Pattern { find: "ddh".to_string(), replace: "দ্ধ".to_string(), reverse: Some("ddh".to_string()), rules: None },
        Pattern { find: "dbh".to_string(), replace: "দ্ভ".to_string(), reverse: Some("dv".to_string()), rules: None },
        Pattern { find: "dv".to_string(), replace: "দ্ভ".to_string(), reverse: Some("dv".to_string()), rules: None },
        Pattern { find: "dm".to_string(), replace: "দ্ম".to_string(), reverse: Some("dd".to_string()), rules: None },
        Pattern { find: "DD".to_string(), replace: "ড্ড".to_string(), reverse: Some("dd".to_string()), rules: None },
        Pattern { find: "Dh".to_string(), replace: "ঢ".to_string(), reverse: Some("dh".to_string()), rules: None },
        Pattern { find: "dh".to_string(), replace: "ধ".to_string(), reverse: Some("dh".to_string()), rules: None },
        Pattern { find: "dg".to_string(), replace: "দ্গ".to_string(), reverse: None, rules: None },
        Pattern { find: "dd".to_string(), replace: "দ্দ".to_string(), reverse: Some("dd".to_string()), rules: None },
        Pattern { find: "D".to_string(), replace: "ড".to_string(), reverse: Some("d".to_string()), rules: None },
        Pattern { find: "d".to_string(), replace: "দ".to_string(), reverse: Some("d".to_string()), rules: None },
        Pattern { find: "...".to_string(), replace: "...".to_string(), reverse: None, rules: None },
        Pattern { find: ".`".to_string(), replace: ".".to_string(), reverse: Some(".".to_string()), rules: None },
        Pattern { find: "..".to_string(), replace: "।।".to_string(), reverse: None, rules: None },
        Pattern { find: ".".to_string(), replace: "।".to_string(), reverse: Some(".".to_string()), rules: None },
        Pattern { find: "ghn".to_string(), replace: "ঘ্ন".to_string(), reverse: Some("ghn".to_string()), rules: None },
        Pattern { find: "Ghn".to_string(), replace: "ঘ্ন".to_string(), reverse: Some("ghn".to_string()), rules: None },
        Pattern { find: "gdh".to_string(), replace: "গ্ধ".to_string(), reverse: Some("gdh".to_string()), rules: None },
        Pattern { find: "Gdh".to_string(), replace: "গ্ধ".to_string(), reverse: Some("gdh".to_string()), rules: None },
        Pattern { find: "gN".to_string(), replace: "গ্ণ".to_string(), reverse: Some("gn".to_string()), rules: None },
        Pattern { find: "GN".to_string(), replace: "গ্ণ".to_string(), reverse: Some("gn".to_string()), rules: None },
        Pattern { find: "gn".to_string(), replace: "গ্ন".to_string(), reverse: Some("gn".to_string()), rules: None },
        Pattern { find: "Gn".to_string(), replace: "গ্ন".to_string(), reverse: Some("gn".to_string()), rules: None },
        Pattern { find: "gm".to_string(), replace: "গ্ম".to_string(), reverse: None, rules: None },
        Pattern { find: "Gm".to_string(), replace: "গ্ম".to_string(), reverse: Some("gm".to_string()), rules: None },
        Pattern { find: "gl".to_string(), replace: "গ্ল".to_string(), reverse: Some("gl".to_string()), rules: None },
        Pattern { find: "Gl".to_string(), replace: "গ্ল".to_string(), reverse: Some("gl".to_string()), rules: None },
        Pattern { find: "gg".to_string(), replace: "জ্ঞ".to_string(), reverse: Some("gg".to_string()), rules: None },
        Pattern { find: "GG".to_string(), replace: "জ্ঞ".to_string(), reverse: Some("gg".to_string()), rules: None },
        Pattern { find: "Gg".to_string(), replace: "জ্ঞ".to_string(), reverse: Some("gg".to_string()), rules: None },
        Pattern { find: "gG".to_string(), replace: "জ্ঞ".to_string(), reverse: Some("gg".to_string()), rules: None },
        Pattern { find: "gh".to_string(), replace: "ঘ".to_string(), reverse: Some("gh".to_string()), rules: None },
        Pattern { find: "Gh".to_string(), replace: "ঘ".to_string(), reverse: Some("gh".to_string()), rules: None },
        Pattern { find: "g".to_string(), replace: "গ".to_string(), reverse: Some("g".to_string()), rules: None },
        Pattern { find: "G".to_string(), replace: "গ".to_string(), reverse: Some("g".to_string()), rules: None },
        
        // Basic vowels and consonants
        Pattern { find: "a".to_string(), replace: "আ".to_string(), reverse: Some("a".to_string()), rules: None },
        Pattern { find: "i".to_string(), replace: "ই".to_string(), reverse: Some("i".to_string()), rules: None },
        Pattern { find: "u".to_string(), replace: "উ".to_string(), reverse: Some("u".to_string()), rules: None },
        Pattern { find: "e".to_string(), replace: "এ".to_string(), reverse: Some("e".to_string()), rules: None },
        Pattern { find: "o".to_string(), replace: "ও".to_string(), reverse: Some("o".to_string()), rules: None },
        Pattern { find: "k".to_string(), replace: "ক".to_string(), reverse: Some("k".to_string()), rules: None },
        Pattern { find: "j".to_string(), replace: "জ".to_string(), reverse: Some("j".to_string()), rules: None },
        Pattern { find: "t".to_string(), replace: "ত".to_string(), reverse: Some("t".to_string()), rules: None },
        Pattern { find: "n".to_string(), replace: "ন".to_string(), reverse: Some("n".to_string()), rules: None },
        Pattern { find: "p".to_string(), replace: "প".to_string(), reverse: Some("p".to_string()), rules: None },
        Pattern { find: "m".to_string(), replace: "ম".to_string(), reverse: Some("m".to_string()), rules: None },
        Pattern { find: "r".to_string(), replace: "র".to_string(), reverse: Some("r".to_string()), rules: None },
        Pattern { find: "l".to_string(), replace: "ল".to_string(), reverse: Some("l".to_string()), rules: None },
        Pattern { find: "s".to_string(), replace: "স".to_string(), reverse: Some("s".to_string()), rules: None },
        Pattern { find: "h".to_string(), replace: "হ".to_string(), reverse: Some("h".to_string()), rules: None },
        Pattern { find: "y".to_string(), replace: "য".to_string(), reverse: Some("j".to_string()), rules: None },
        
        // Common combinations
        Pattern { find: "ng".to_string(), replace: "ং".to_string(), reverse: Some("ng".to_string()), rules: None },
        Pattern { find: "th".to_string(), replace: "থ".to_string(), reverse: Some("th".to_string()), rules: None },
        Pattern { find: "sh".to_string(), replace: "শ".to_string(), reverse: Some("sh".to_string()), rules: None },
    ];

    let mut bijoy_mappings = HashMap::new();
    bijoy_mappings.insert("।".to_string(), "|".to_string());
    bijoy_mappings.insert("'".to_string(), "Ô".to_string());
    bijoy_mappings.insert("'".to_string(), "Õ".to_string());
    // Note: Skipping problematic Unicode quotes for now
    bijoy_mappings.insert("্র্য".to_string(), "ª¨".to_string());
    bijoy_mappings.insert("র‌্য".to_string(), "i¨".to_string());
    bijoy_mappings.insert("ক্ক".to_string(), "°".to_string());
    bijoy_mappings.insert("ক্ট".to_string(), "±".to_string());
    bijoy_mappings.insert("ক্ত".to_string(), "³".to_string());
    bijoy_mappings.insert("ক্ব".to_string(), "K¡".to_string());
    bijoy_mappings.insert("স্ক্র".to_string(), "¯Œ".to_string());
    bijoy_mappings.insert("ক্র".to_string(), "µ".to_string());
    bijoy_mappings.insert("ক্ল".to_string(), "K¬".to_string());
    bijoy_mappings.insert("ক্ষ".to_string(), "¶".to_string());
    bijoy_mappings.insert("ক্স".to_string(), "·".to_string());
    bijoy_mappings.insert("গু".to_string(), "¸".to_string());
    bijoy_mappings.insert("গ্ধ".to_string(), "»".to_string());
    bijoy_mappings.insert("গ্ন".to_string(), "Mœ".to_string());
    bijoy_mappings.insert("গ্ম".to_string(), "M¥".to_string());

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