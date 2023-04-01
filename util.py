import re
import words

# Returns True if the given phrase or a synonym of it is found in the target
# phrase, otherwise return None
def fuzzy_match(target_phrase, given_phrase):
    p = re.compile(given_phrase)
    if p.search(target_phrase) is not None:
        return True
    for synonym_group in words.synonyms:
        for synonym in synonym_group:
            if synonym in given_phrase:
                found_synonym = synonym
                for synonym in synonym_group:
                    p = re.compile(given_phrase.replace(found_synonym, synonym))
                    return p.search(target_phrase) is not None

# Returns the matched synonym if the given phrase or a synonym of it is found
# in the target phrases, otherwise return None
def fuzzy_in(target_phrases, given_phrase):
    p = re.compile(given_phrase)
    for target_phrase in target_phrases:
        if p.search(target_phrase) is not None:
            return target_phrase
    for synonym_group in words.synonyms:
        for synonym in synonym_group:
            if synonym in given_phrase:
                found_synonym = synonym
                for synonym in synonym_group:
                    p = re.compile(given_phrase.replace(found_synonym, synonym))
                    for target_phrase in target_phrases:
                        if p.search(target_phrase) is not None:
                            return target_phrase