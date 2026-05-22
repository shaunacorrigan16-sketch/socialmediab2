# GlowUp: The Price of Likes - Interactive Ren'Py Story for B2 English Learners
# This is the main script that drives the story, variables, and branching logic.

# ==============================================================================
# Image Assets Definitions
# ==============================================================================
image bg bedroom = "images/bg_bedroom.png"

# Procedural Colored Backdrops for missing backgrounds
image bg school = Solid("#1e293b")   # Slate Blue hallway
image bg kitchen = Solid("#2d1f18")  # Cozy warm dark brown kitchen
image bg feed = Solid("#09090b")     # AMOLED Black for full-screen feed

# Character Sprites (copied to game/images)
image boy_player = "images/boy_player.png"
image girl_player = "images/girl_player.png"
image maya = "images/maya.png"
image mom = "images/mom.png"


# ==============================================================================
# Character Definitions
# ==============================================================================
define p = Character("[player_name]", color="#38bdf8")
define m = Character("Maya", color="#fbbf24")      # Blonde best friend (warm gold)
define mom = Character("Mom", color="#f97316")     # Concerned mother (orange)
define c = Character("Chloe", color="#ec4899")     # GlowUp Influencer classmate (pink)
define narrator = Character(None, kind=nvl)        # NVL-mode narrator for reflections
define sys = Character("System", color="#a1a1aa")  # System notifications


# ==============================================================================
# Game Initialization
# ==============================================================================
label start:
    # Initialize invisible stats (range 0 to 100)
    $ self_esteem = 50
    $ popularity = 20
    $ connection = 50

    # Default player information
    $ player_name = "Mia"
    $ player_gender = "girl"

    # Start with a fading scene
    scene black
    with dissolve

    # Title Introduction
    narrator "Welcome to 'GlowUp: The Price of Likes', an interactive visual novel designed for B2 English learners."
    narrator "In this game, you will explore the themes of social media pressure, self-image, and healthy boundaries."
    narrator "As you play, you will see key B2 grammar highlighted in different colors:\n
- {color=#38bdf8}Phrasal Verbs{/color}\n
- {color=#fb923c}Modal Verbs{/color}\n
- {color=#f472b6}Expressing Opinions{/color}\n
- {color=#34d399}Expressing Pros & Cons{/color}"
    narrator "Make sure B2 Study Mode (top-right) is ON. You can click on any colored phrase to see its definition, structure, and usage examples!"
    
    nvl clear

    # Step 1: Customize Name
    $ player_name = renpy.input("To begin, please enter your character's name:", default="Mia", length=12).strip()
    if not player_name:
        $ player_name = "Mia"

    # Step 2: Choose Gender (updates default sprite and pronoun references)
    menu:
        "Select your gender:"
        "Boy (Play as [player_name])":
            $ player_gender = "boy"
            if player_name == "Mia":
                $ player_name = "Alex"
        "Girl (Play as [player_name])":
            $ player_gender = "girl"

    # Display Dashboard Overlay
    show screen dashboard_ui
    with dissolve

    jump chapter_1


# ==============================================================================
# Chapter 1: New App
# ==============================================================================
label chapter_1:
    scene bg school
    with dissolve

    "It's a sunny school morning. You are standing in the busy hallway of Oakwood High, holding your phone."
    
    # Introduce best friend Maya
    show maya at right
    with slideinright

    m "Hey! Did you hear about that new social media app, 'GlowUp'?"
    m "Almost everyone at school has signed up. People {a=b2:strongly_believe}{color=#f472b6}strongly believe{/color}{/a} that your popularity on the app determines your social status here."

    p "Wait, really? That seems a bit dramatic, doesn't it?"

    m "Maybe. {a=b2:opinion_intro}{color=#f472b6}From my perspective{/color}{/a}, it's just a distraction."
    m "But {a=b2:pros_cons_intro}{color=#34d399}on the one hand{/color}{/a}, you can share awesome creative photos, but {a=b2:pros_cons_intro}{color=#34d399}on the other hand{/color}{/a}, the pressure to look perfect {a=b2:might}{color=#fb923c}might{/color}{/a} be too high."
    m "Anyway, you should definitely {a=b2:check_out}{color=#38bdf8}check out{/color}{/a} the feed! Here, download it."

    # Player decides to sign up
    "You download GlowUp and set up your profile."
    
    if player_gender == "boy":
        show boy_player at left with slideinleft
    else:
        show girl_player at left with slideinleft

    p "Okay, I've got my profile ready! But I {a=b2:must}{color=#fb923c}need to{/color}{/a} choose what my very first post should be."
    p "I want to {a=b2:fit_in}{color=#38bdf8}fit in{/color}{/a} with the popular crowd, but I also want to be myself. What should I upload?"

    # First Branching Choice
    menu:
        "What kind of content do you post?"
        "An authentic photo of my lazy dog sleeping. (Authentic)":
            $ self_esteem += 10
            $ connection += 10
            $ popularity += 5
            p "I'll post this cute, unedited photo of Buster. It's funny and real!"
            m "Aww, he looks adorable! That's a super cute first post."
            $ first_post_type = "dog"
            
        "A heavily edited, filtered selfie showing off an outfit. (Trendy)":
            $ popularity += 15
            $ self_esteem -= 5
            p "I'll spend a few minutes editing this selfie. Smooth skin, brighter lighting... there! Perfect."
            m "Wow, you look completely different, like a model! You'll definitely get lots of likes."
            $ first_post_type = "edited"

        "A controversial 'Hot Take' post complaining about school lunches. (Drama/Opinion)":
            $ popularity += 20
            $ self_esteem -= 10
            $ connection -= 5
            p "Let's post an opinion! 'Oakwood High lunches are completely uneatable. We deserve better! #ChangeOurLunch'"
            m "Yikes! That's bold. People {a=b2:might}{color=#fb923c}could{/color}{/a} get offended, but it will definitely get attention."
            $ first_post_type = "drama"

    hide maya
    hide boy_player
    hide girl_player
    with dissolve

    # Show GlowUp Feed simulation
    "An hour later, you open GlowUp to see how your classmates are interacting."

    python:
        # Prepare content based on player choices
        my_caption = "Meet Buster, the sleepiest dog in the world! 🐶 #RealLife #DogsOfGlowUp" if first_post_type == "dog" else (
            "Loving this school outfit! ✨ feeling cute #SchoolStyle #Ootd" if first_post_type == "edited" else 
            "The cafeteria food is an absolute joke. Oakwood deserves better! 🍕❌ #SchoolDrama"
        )
        my_gradient = "#10b981" if first_post_type == "dog" else ("#ec4899" if first_post_type == "edited" else "#f59e0b")
        my_desc = "[Your Dog Buster]" if first_post_type == "dog" else ("[Highly Filtered Selfie]" if first_post_type == "edited" else "[Angry Text Rant]")
        my_likes = 12 if first_post_type == "dog" else (48 if first_post_type == "edited" else 67)

        feed_data = [
            {
                "username": player_name,
                "avatar_color": "#38bdf8",
                "gradient": my_gradient,
                "image_desc": my_desc,
                "likes": my_likes,
                "caption": my_caption,
                "comment_user": "Maya_Sun",
                "comment_text": "Love this! 🙌" if first_post_type == "dog" else ("Wow, stunning!" if first_post_type == "edited" else "Uh oh, principal might see this!")
            },
            {
                "username": "Chloe_Glows",
                "avatar_color": "#ec4899",
                "gradient": "#f43f5e",
                "image_desc": "[Chloe's Flawless Beach Sunset Selfie]",
                "likes": 521,
                "caption": "Chasing the sunset and living my absolute best life! 🌅✨ #Sunkissed #Blessed",
                "comment_user": "GlowUp_King",
                "comment_text": "Absolute queen! 👑"
            }
        ]

    # Show the feed screen!
    call screen glowup_feed(feed_items=feed_data)

    "You close the app, feeling a mixture of excitement and mild curiosity about what tomorrow will bring."

    # End of Chapter 1 Quiz
    $ quiz_next_label = "chapter_2"
    
    call screen language_quiz(
        chapter_title="Chapter 1: New App",
        sentence_with_gap="I really wanted to _______ with the popular crowd at my new school, so I signed up for GlowUp.",
        options=["stand out", "fit in", "log off"],
        correct_index=1,
        explanation="The correct phrasal verb is 'fit in', which means to belong to a group and be accepted by them. 'Stand out' means to be noticeably different, and 'log off' means to disconnect."
    )


# ==============================================================================
# Chapter 2: Comparison Trap
# ==============================================================================
label chapter_2:
    scene bg bedroom
    with dissolve

    "It is evening. You are sitting on your bed, {a=b2:scroll_through}{color=#38bdf8}scrolling through{/color}{/a} GlowUp."
    "Chloe's feed is a gallery of absolute perfection: pristine outfits, luxurious weekend parties, and flawless skin."

    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve

    p "I {a=b2:must}{color=#fb923c}can't{/color}{/a} understand how she always looks so perfect. My feed feels so boring in comparison."
    p "I {a=b2:compare_to}{color=#38bdf8}compare{/color}{/a} my ordinary room {a=b2:compare_to}{color=#38bdf8}to{/color}{/a} her fancy trips, and I {a=b2:end_up}{color=#38bder}end up{/color}{/a} feeling miserable."

    "You decide to take a bedroom selfie to upload, but looking at the photo on your screen, you immediately feel insecure."
    p "My eyes look tired, and my hair is a mess! I {a=b2:should}{color=#fb923c}should{/color}{/a} probably do something about this before anyone sees it."

    # Second Branching Choice
    menu:
        "What do you do with the selfie?"
        "Post it completely unedited, writing an honest caption about having a tired day. (Authentic)":
            $ self_esteem += 15
            $ connection += 10
            $ popularity += 0
            $ post_style = "unedited"
            p "I'll post it unedited. 'Tired eyes, messy hair, but keeping it real today!' Let's see how they react."
            
        "Apply a heavy 'GlowUp' filter to enlarge your eyes and smooth your skin completely. (Trendy)":
            $ popularity += 20
            $ self_esteem -= 15
            $ post_style = "filtered"
            p "This filter makes me look flawless. Bigger eyes, perfect skin. Nobody {a=b2:might}{color=#fb923c}might{/color}{/a} even notice it's edited!"

        "Delete the photo, log off of GlowUp, and text Maya to play video games. (Offline)":
            $ self_esteem += 5
            $ connection += 15
            $ popularity -= 5
            $ post_style = "deleted"
            p "You know what? I'm not going to post. I'm going to {a=b2:log_off}{color=#38bdf8}log off{/color}{/a} and text Maya instead."

    hide boy_player
    hide girl_player
    with dissolve

    # Text message simulation
    if post_style == "deleted":
        "You put the phone down, log off the app, and text Maya. Within a minute, your phone buzzes."
        
        python:
            chat_data = [
                {"sender": "me", "text": "Hey Maya! Free to play some online games? GlowUp is driving me crazy tonight."},
                {"sender": "Maya", "text": "Omg yes! I'm logging on right now. You {a=b2:should}{color=#fb923c}ought to{/color}{/a} take breaks from that app anyway. Let's smash some rounds!"}
            ]
        call screen chat_screen(contact_name="Maya", messages=chat_data)
        "You spend the evening laughing and playing games. Your real-life friendship feels stronger than ever."

    else:
        "You post the selfie and wait. Within twenty minutes, the notifications start piling up."
        
        if post_style == "filtered":
            "Chloe_Glows commented: 'OMG stunning! You look absolutely gorgeous bestie! 😍✨'"
            "You feel a quick rush of excitement, but a small voice inside says: {i}But that's not what I actually look like.{/i}"
        else:
            "Maya_Sun commented: 'I love this! So authentic and brave! 💖'"
            "A few classmates leave likes, but your follower count barely moves. Chloe doesn't engage."

    # End of Chapter 2 Quiz
    $ quiz_next_label = "chapter_3"
    
    call screen language_quiz(
        chapter_title="Chapter 2: Comparison Trap",
        sentence_with_gap="It's not healthy to _______ your daily life to the highly polished images that influencers post online.",
        options=["deal with", "compare to", "fit in with"],
        correct_index=1,
        explanation="The correct phrasal verb is 'compare [something] to [something]', which means to evaluate two things in relation to each other. 'Deal with' means to handle a problem, and 'fit in with' means to belong."
    )


# ==============================================================================
# Chapter 3: Cyberbullying
# ==============================================================================
label chapter_3:
    scene bg school
    with dissolve

    "The next day at school, the atmosphere feels strange. You see students whispering in the hallways, glancing at their phones, and then looking at you."
    "Maya runs up to you, looking deeply concerned."

    show maya at right
    with dissolve

    m "Hey... have you checked GlowUp this morning? You {a=b2:must}{color=#fb923c}have to{/color}{/a} see what's going on."
    
    p "No, why? What's wrong?"

    m "Someone created an anonymous account called 'GlowDown_[player_name]'."
    m "They posted a mean meme mocking you, and kids at school are sharing it in group chats."
    m "Chloe commented on it too, saying it was 'savage'."

    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve

    p "What?! That {a=b2:cant}{color=#fb923c}can't{/color}{/a} be true! Let me see."

    "You open the app. The post is a mockery of your profile. It's hurtful, aggressive, and public."
    p "This is humiliating! I feel so exposed. How am I supposed to {a=b2:deal_with}{color=#38bdf8}deal with{/color}{/a} this?"

    m "{a=b2:pros_cons_intro}{color=#34d399}While there are benefits{/color}{/a} to social media, this is the worst downside. You {a=b2:must}{color=#fb923c}must not{/color}{/a} let them get to you."
    m "What do you think we should do?"

    # Third Branching Choice
    menu:
        "How do you respond to the cyberbullying?"
        "Write an angry public comment calling out the bully and Chloe. (Call Out / Drama)":
            $ popularity += 15
            $ self_esteem -= 20
            $ connection -= 10
            $ response_type = "drama"
            p "I'm going to {a=b2:call_out}{color=#38bdf8}call{/color}{/a} them {a=b2:call_out}{color=#38bdf8}out{/color}{/a}! 'Whoever made this account is a pathetic coward. And Chloe, you are fake for supporting it!'"
            m "Oh no, replying publicly is exactly what they want! You're getting dragged into the drama."
            
        "Block the account, report it to the app administrators, and ignore it. (Block & Report)":
            $ self_esteem += 10
            $ popularity -= 5
            $ connection += 5
            $ response_type = "ignore"
            p "I'm just going to block them and report the account. They don't deserve my attention."
            m "Good call. It's best to starve the trolls of attention."

        "Turn to a trusted teacher or school counselor to report the bullying. (Adult Help)":
            $ connection += 20
            $ self_esteem += 15
            $ response_type = "support"
            p "I'm going to talk to Mrs. Vance, the school counselor. I need support to handle this."
            m "I'll go with you. You shouldn't have to carry this alone."

    hide maya
    hide boy_player
    hide girl_player
    with dissolve

    if response_type == "drama":
        "Your comment triggers a massive wave of replies. People are taking sides, and the notifications are buzzing every few seconds."
        "You feel a tight knot of anxiety in your stomach. The conflict is spreading rapidly."
    elif response_type == "ignore":
        "You block the account. The meme is still online, but you don't see it anymore. It's difficult to forget, but you feel a small sense of control."
    else:
        "Mrs. Vance listens carefully, comforts you, and contacts the school administration to track the incident."
        "You feel a huge weight lift from your shoulders. Knowing you have adults on your side makes you feel incredibly resilient."

    # End of Chapter 3 Quiz
    $ quiz_next_label = "chapter_4"
    
    call screen language_quiz(
        chapter_title="Chapter 3: Cyberbullying",
        sentence_with_gap="When you face severe cyberbullying at school, you must _______ a trusted friend, parent, or counselor.",
        options=["shut out", "get carried away by", "turn to"],
        correct_index=2,
        explanation="The correct phrasal verb is 'turn to', which means to ask someone for help or support. 'Shut out' means to isolate yourself, and 'get carried away' means to lose control."
    )


# ==============================================================================
# Chapter 4: Addiction Spiral
# ==============================================================================
label chapter_4:
    scene bg bedroom
    with dissolve

    "It is 2:15 AM. The bedroom is pitch black, illuminated only by the bright glow of your phone screen."
    "Notifications are constantly flashing. Your eyes are bloodshot and dry, but you feel a compulsive need to keep scrolling."

    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve

    p "Just five more minutes... I {a=b2:must}{color=#fb923c}have to{/color}{/a} check if they've replied. I {a=b2:cant}{color=#fb923c}can't{/color}{/a} close my eyes."
    p "I've totally {a=b2:get_carried_away}{color=#38bdf8}gotten carried away{/color}{/a} tonight."

    "A concerned direct message from Maya flashes on screen: 'Hey, I see you are online. Please log off! We have that B2 English exam tomorrow!'"
    "Suddenly, you hear soft footsteps. The bedroom door creaks open."

    show mom at right
    with dissolve

    mom "Sweetie? Are you still awake? The light from your phone is shining under the door."
    mom "{a=b2:opinion_intro}{color=#f472b6}To my mind{/color}{/a}, this constant scrolling is affecting your health. You look exhausted."
    mom "You {a=b2:should}{color=#fb923c}ought to{/color}{/a} put the phone away and sleep. It {a=b2:might}{color=#fb923c}might{/color}{/a} ruin your exam tomorrow if you don't."

    # Fourth Branching Choice
    menu:
        "What is your response to Mom?"
        "Tell her you'll log off, reply to Maya, and put the phone in the drawer. (Log Off)":
            $ connection += 15
            $ self_esteem += 10
            $ popularity -= 5
            $ scroll_choice = "sleep"
            p "You're right, Mom. I'm sorry. I'll send a quick text to Maya saying goodnight and then log off immediately."
            mom "Thank you, sweetheart. Sleep well."
            
        "Argue that you need to check one last thing, hide under the blanket, and keep scrolling. (Scroll)":
            $ popularity += 15
            $ self_esteem -= 15
            $ connection -= 15
            $ scroll_choice = "scroll"
            p "Just a second, Mom! I'm in the middle of something important!"
            "As soon as she closes the door, you pull the blanket over your head and continue scrolling through the drama until 4 AM."

    hide mom
    hide boy_player
    hide girl_player
    with dissolve

    if scroll_choice == "sleep":
        "You put your phone inside the desk drawer. It feels incredibly difficult to separate yourself, but you finally fall into a deep, peaceful sleep."
    else:
        "You wake up late the next morning. Your head is pounding, you feel dizzy, and you can barely concentrate during the English exam."

    # End of Chapter 4 Quiz
    $ quiz_next_label = "chapter_5"
    
    call screen language_quiz(
        chapter_title="Chapter 4: Addiction Spiral",
        sentence_with_gap="I feel completely exhausted today. I _______ stayed awake until 3 AM scrolling through GlowUp.",
        options=["should have", "shouldn't have", "must not"],
        correct_index=1,
        explanation="The correct grammatical structure for past regrets is 'shouldn't have + past participle'. 'Should have' would mean you wanted to stay awake, and 'must not' is for present prohibition."
    )


# ==============================================================================
# Chapter 5: Turning Point
# ==============================================================================
label chapter_5:
    scene bg kitchen
    with dissolve

    "It is afternoon. You are sitting at the kitchen table. Maya has come over to study, and Mom is brewing some tea."
    "The B2 English exam results are out. You are looking down at your paper."

    if scroll_choice == "scroll":
        "Your score is a C. You made simple mistakes because you couldn't focus."
    else:
        "Your score is an A. Despite the stress, you managed to concentrate perfectly."

    show maya at left
    show mom at right
    with dissolve

    m "Okay, we need to talk. {a=b2:weigh_up}{color=#34d399}Weighing up{/color}{/a} the events of this past week, we {a=b2:must}{color=#fb923c}need to{/color}{/a} decide what to do about GlowUp."
    m "{a=b2:opinion_intro}{color=#f472b6}As I see it{/color}{/a}, the app is taking over your life."

    mom "I agree. {a=b2:pros_cons_intro}{color=#34d399}A significant drawback{/color}{/a} is that it makes you feel anxious and insecure. But the {a=b2:advantage_drawback}{color=#34d399}main advantage{/color}{/a} of social media is that it can keep you connected, if used wisely."
    mom "What is your perspective on all this?"

    if player_gender == "boy":
        show boy_player at center with dissolve
    else:
        show girl_player at center with dissolve

    p "Well, I've been thinking about it a lot. I've realized that..."

    # Fifth Branching Choice (Determines Final Endings)
    menu:
        "What is your final decision regarding social media?"
        "I will establish strict screen limits, post authentically, and prioritize real connections. (Balance)":
            $ connection += 20
            $ self_esteem += 15
            $ popularity -= 10
            $ final_choice = "balance"
            p "I strongly believe that social media shouldn't control us. I will set healthy boundaries and spend more offline time with you guys."
            
        "I'm going to delete my account temporarily and take a long break to find myself. (Break)":
            $ self_esteem += 25
            $ connection += 15
            $ popularity -= 20
            $ final_choice = "break"
            p "I think the downsides outweigh the benefits. I'm going to log off permanently and focus on my real life."

        "I need to double down on my online brand. Popularity is too important to give up. (Popularity)":
            $ popularity += 25
            $ self_esteem -= 20
            $ connection -= 20
            $ final_choice = "popularity"
            p "I must stay popular. School is temporary, but having thousands of followers gives me real influence. I can handle the stress."

    hide maya
    hide mom
    hide boy_player
    hide girl_player
    with dissolve

    # Evaluate Ending based on Stats and Final Choice
    jump ending_determination


# ==============================================================================
# Ending Determination & Cutscenes
# ==============================================================================
label ending_determination:
    scene black
    with dissolve

    # Check stats for endings
    if final_choice == "popularity" and popularity >= 60 and connection < 40:
        jump ending_addiction
    elif self_esteem < 35 and connection < 40:
        jump ending_breakdown
    elif final_choice == "break" or (self_esteem >= 65 and popularity < 55):
        jump ending_authenticity
    else:
        jump ending_balance


# ------------------------------------------------------------------------------
# Ending 1: Healthy Balance
# ------------------------------------------------------------------------------
label ending_balance:
    scene bg bedroom
    with dissolve
    
    "🌱 THE HEALTHY BALANCE ENDING"
    
    "A few weeks have passed since the kitchen confrontation."
    "You still use GlowUp, but you've set a strict 30-minute daily screen limit."
    "You no longer edit your selfies to look like someone else, and you've blocked the anonymous rumor accounts."
    
    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve
        
    p "I've realized that social media can connect us, but it should never control us."
    p "On the one hand, I enjoy sharing my hobbies online, but on the other hand, my offline life is what truly keeps me grounded."
    
    show maya at right with slideinright
    m "I'm so proud of you! Let's put our phones away and go grab some ice cream."
    
    hide boy_player
    hide girl_player
    hide maya
    with dissolve
    
    sys "Congratulations! You achieved the 🌱 Healthy Balance Ending."
    sys "You managed to balance your online presence while maintaining deep, supportive, real-life relationships."
    sys "Take a moment to review the phrasal verbs and modals you've learned. They are incredibly useful for B2-level conversations!"
    
    return


# ------------------------------------------------------------------------------
# Ending 2: Authenticity Activist
# ------------------------------------------------------------------------------
label ending_authenticity:
    scene bg school
    with dissolve
    
    "✨ THE AUTHENTICITY ENDING"
    
    "Your decision to post unedited photos and write honest captions about your vulnerabilities has started a movement."
    "Classmates at school noticed your confidence and began doing the same."
    "You and Maya have formed the 'Unfiltered Club', encouraging students to support each other and drop unrealistic beauty standards."
    
    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve
        
    p "We must not hide our real selves behind filters. Authenticity is what makes us stand out!"
    
    show maya at right with slideinright
    m "Exactly! From my perspective, this is the most empowering thing we've ever done at school."
    
    hide boy_player
    hide girl_player
    hide maya
    with dissolve
    
    sys "Congratulations! You achieved the ✨ Authenticity Ending."
    sys "By showing high self-esteem, you inspired others to embrace who they really are."
    sys "In B2 speaking tests, expressing clear opinions and weighing pros and cons (as you did) will guarantee you high scores!"
    
    return


# ------------------------------------------------------------------------------
# Ending 3: Popular but Lonely
# ------------------------------------------------------------------------------
label ending_addiction:
    scene bg bedroom
    with dissolve
    
    "📱 THE ADDICTION ENDING"
    
    "It is midnight. You are scrolling through your GlowUp feed."
    "Your profile has reached over 2,000 followers. Your classmates see you as a school celebrity."
    "But Maya hasn't texted you in days. You shut her out to focus on replying to online comments."
    
    if player_gender == "boy":
        show boy_player at left with dissolve
    else:
        show girl_player at left with dissolve
        
    p "I've got all these followers, but why do I feel so lonely?"
    p "I shouldn't have prioritized these online likes over my real friends. I've ended up completely isolated."
    
    "You stare at the glowing screen in the dark, feeling hollow."
    
    hide boy_player
    hide girl_player
    with dissolve
    
    sys "Game Over: You achieved the 📱 Addiction Ending."
    sys "You chased popularity but lost your real-life connections. Online numbers cannot replace authentic human support."
    sys "Reflect on the B2 past modal: 'I shouldn't have prioritized...'. Reflect on how your choices led to this outcome."
    
    return


# ------------------------------------------------------------------------------
# Ending 4: Cyberbullying Breakdown
# ------------------------------------------------------------------------------
label ending_breakdown:
    scene bg bedroom
    with dissolve
    
    "💔 THE CYBERBULLYING BREAKDOWN ENDING"
    
    "The constant notifications, negative comments, and lack of real-life support have taken a massive toll."
    "You feel completely overwhelmed by anxiety. You've shut out Maya and your family, choosing to hide in your bedroom."
    "You stare at your phone screen, crying silently as anonymous comments keep coming."
    
    "If you ever feel this way in real life, please know that you must not deal with it alone."
    "There are always people who care. You should turn to your parents, a teacher, or professional support networks."
    
    sys "Game Over: You achieved the 💔 Cyberbullying Breakdown Ending."
    sys "This is a serious ending highlighting the severe consequences of online harassment and isolation."
    sys "If you or someone you know is struggling with mental health or cyberbullying, please reach out to trusted adults or local helplines."
    
    return
