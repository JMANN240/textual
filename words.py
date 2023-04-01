import actions

# Things that don't take an object (dance, cry, etc.)
intransitive_verbs = {
    "dance": actions.dance
}

# Things that do take objects (grab, use, etc.)
transitive_verbs = {
    "grab": actions.grab,
    "go": actions.go,
    "use": actions.use
}

verbs = list(transitive_verbs.keys()) + list(intransitive_verbs.keys())

# Words that mean the same thing (grab, get, etc.)
synonyms = (
    ('get', 'grab', 'take'),
    ('walk', 'go'),
    ('front', 'forward'),
    ('behind', 'back', 'backward')
)