# B2 English Study Mode & Glossary Database
# This file sets up the custom hyperlink handling and vocabulary dictionary for B2 learners.

init -1 python:
    # Toggle to enable/disable study mode highlighting
    study_mode = True

    # Custom hyperlink handler for B2 vocabulary
    def b2_hyperlink_handler(value):
        # Check if the screen is already showing
        if renpy.get_screen("b2_glossary_popup"):
            renpy.hide_screen("b2_glossary_popup")
        
        # Show the glossary card popup
        renpy.show_screen("b2_glossary_popup", term_key=value)
        renpy.restart_interaction()
        
    config.hyperlink_handlers["b2"] = b2_hyperlink_handler

    # Glossary database mapping vocabulary keys to definition data
    b2_glossary = {
        # Phrasal Verbs
        "scroll_through": {
            "title": "scroll through",
            "category": "Phrasal Verb (B2)",
            "meaning": "To look at a series of pictures, posts, or texts on a screen by moving them up or down.",
            "structure": "scroll through + [noun phrase] (transitive)",
            "example": "I sat on my bed scrolling through my feed for two hours, which made me feel quite anxious."
        },
        "log_off": {
            "title": "log off / log out",
            "category": "Phrasal Verb (B2)",
            "meaning": "To stop using a computer, app, or website by closing your connection to it.",
            "structure": "log off (intransitive) or log off of [something]",
            "example": "If you are feeling overwhelmed by social media, you ought to log off and take a walk."
        },
        "fit_in": {
            "title": "fit in",
            "category": "Phrasal Verb (B2)",
            "meaning": "To feel that you belong to a particular group and are accepted by them.",
            "structure": "fit in (intransitive) or fit in with [someone]",
            "example": "She felt intense pressure to fit in with the popular crowd at school, so she edited her photos."
        },
        "call_out": {
            "title": "call out",
            "category": "Phrasal Verb (B2)",
            "meaning": "To challenge or publicly criticize someone about their behavior, especially when they have done something wrong.",
            "structure": "call [someone] out / call out [someone] (separable)",
            "example": "Rather than calling out the anonymous bullies publicly, she decided it was better to report them."
        },
        "check_out": {
            "title": "check out",
            "category": "Phrasal Verb (B2)",
            "meaning": "To look at or examine something interesting or attractive to see what it is like.",
            "structure": "check out + [noun phrase] (transitive)",
            "example": "You should check out that new social media app! Almost everyone in our class has joined it."
        },
        "compare_to": {
            "title": "compare to",
            "category": "Phrasal Verb (B2)",
            "meaning": "To evaluate or judge something in relation to another, often noticing similarities or differences.",
            "structure": "compare [someone/something] to [someone/something]",
            "example": "It is not healthy to compare your everyday life to the polished images that influencers post."
        },
        "deal_with": {
            "title": "deal with",
            "category": "Phrasal Verb (B2)",
            "meaning": "To take action in order to handle, manage, or solve a difficult situation or problem.",
            "structure": "deal with + [noun phrase] (transitive)",
            "example": "I really don't know how to deal with this mean comment. It's keeping me awake at night."
        },
        "check_in": {
            "title": "check in on",
            "category": "Phrasal Verb (B2)",
            "meaning": "To contact someone to see how they are doing or if they need any support.",
            "structure": "check in on + [someone] (transitive)",
            "example": "Liam noticed Mia looked upset at school and decided to check in on her later that evening."
        },
        "end_up": {
            "title": "end up",
            "category": "Phrasal Verb (B2)",
            "meaning": "To eventually reach a particular state, place, or situation, especially without having planned it.",
            "structure": "end up + [verb-ing] or end up + [preposition/noun]",
            "example": "If you stay awake all night scrolling, you will end up feeling exhausted during your exams."
        },
        "get_carried_away": {
            "title": "get carried away",
            "category": "Phrasal Verb / Idiom (B2)",
            "meaning": "To become so excited, angry, or interested in something that you lose control of your behavior.",
            "structure": "get carried away (intransitive, usually past/passive form)",
            "example": "I only planned to browse for five minutes, but I got carried away reading the drama."
        },
        "turn_to": {
            "title": "turn to",
            "category": "Phrasal Verb (B2)",
            "meaning": "To go to someone for help, advice, or support when you are facing a difficult situation.",
            "structure": "turn to + [someone] (transitive)",
            "example": "If you receive cyberbullying, you must turn to a trusted adult, like a teacher or parent."
        },
        "stand_out": {
            "title": "stand out",
            "category": "Phrasal Verb (B2)",
            "meaning": "To be highly noticeable, striking, or much better/different than other people or things.",
            "structure": "stand out (intransitive)",
            "example": "She wanted her profile picture to stand out, so she added a colorful filter and shiny border."
        },
        "shut_out": {
            "title": "shut out",
            "category": "Phrasal Verb (B2)",
            "meaning": "To deliberately prevent someone from sharing your thoughts, feelings, or life; to isolate yourself.",
            "structure": "shut [someone] out (separable)",
            "example": "Instead of talking about her anxiety, Mia shut her friends out and stopped replying to texts."
        },

        # Modal Verbs
        "should": {
            "title": "should / ought to",
            "category": "Modal Verbs (B2)",
            "meaning": "Used to give advice, make recommendations, or express what is the right/ethical thing to do.",
            "structure": "should + [base verb] / ought to + [base verb]",
            "example": "You should check your privacy settings. We ought to be more supportive of each other."
        },
        "must": {
            "title": "must / have to / need to",
            "category": "Modal Verbs (B2)",
            "meaning": "Used to express strong obligation, rules, or absolute necessity.",
            "structure": "must + [base verb] / have to + [base verb] / need to + [base verb]",
            "example": "Mia feels she must maintain her online popularity. You have to think twice before posting."
        },
        "might": {
            "title": "might / could / may",
            "category": "Modal Verbs (B2)",
            "meaning": "Used to express possibility, uncertainty, or potential outcomes in the present or future.",
            "structure": "might + [base verb] / could + [base verb] / may + [base verb]",
            "example": "He might block you if you comment that. Heavy filters could distort your self-image."
        },
        "cant": {
            "title": "can't / must not",
            "category": "Modal Verbs (B2)",
            "meaning": "Used to express prohibition ('must not') or a strong logical deduction of impossibility ('can't').",
            "structure": "can't + [base verb] / must not + [base verb]",
            "example": "That profile photo can't be real! You must not share your personal passwords with anyone."
        },
        "should_have": {
            "title": "should have + past participle",
            "category": "Modal Verbs (B2 - Past)",
            "meaning": "Used to express regret, criticism, or reflection on past events that did not happen as they should have.",
            "structure": "should have + [past participle] / shouldn't have + [past participle]",
            "example": "I shouldn't have posted that angry comment. I should have taken a deep breath first."
        },

        # Expressing Opinions
        "opinion_intro": {
            "title": "Introducing Opinions",
            "category": "Expressing Opinions (B2)",
            "meaning": "Phrases used to state your personal perspective in a structured, formal, and polite manner.",
            "structure": "From my perspective, ... / In my opinion, ... / As I see it, ... / To my mind, ... / It seems to me that...",
            "example": "From my perspective, social media has both high values and serious risks."
        },
        "strongly_believe": {
            "title": "strongly believe",
            "category": "Expressing Opinions (B2)",
            "meaning": "To have an extremely firm conviction or belief about a topic, showing strong confidence.",
            "structure": "I strongly believe that + [clause]",
            "example": "I strongly believe that popularity on an app shouldn't define your self-esteem at school."
        },

        # Pros and Cons
        "pros_cons_intro": {
            "title": "Weighing Arguments",
            "category": "Pros & Cons (B2)",
            "meaning": "Expressions used to transition between positive aspects (pros) and negative aspects (cons) of an issue.",
            "structure": "On the one hand, ... on the other hand, ... / While there are clear benefits, we must also consider the downsides...",
            "example": "On the one hand, social media helps us connect. On the other hand, it can lead to cyberbullying."
        },
        "advantage_drawback": {
            "title": "advantages & drawbacks",
            "category": "Pros & Cons (B2)",
            "meaning": "Formal nouns used to describe positive points (advantages/upsides/benefits) and negative points (drawbacks/downsides/disadvantages).",
            "structure": "A significant advantage/drawback is that... / The main upside/downside is...",
            "example": "A significant advantage is instant communication, but the main drawback is the risk of addiction."
        },
        "weigh_up": {
            "title": "weigh up",
            "category": "Pros & Cons (B2)",
            "meaning": "To carefully consider and balance the good and bad parts of a situation before making a choice.",
            "structure": "weigh up + [noun phrase] (transitive)",
            "example": "Before joining a new platform, you should weigh up the pros and cons of sharing your life."
        }
    }
