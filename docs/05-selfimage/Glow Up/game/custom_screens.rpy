# Custom Screens for 'GlowUp: The Price of Likes'
# This file defines the mobile UI, stats dashboard, glossary popup, and quizzes.

# ==============================================================================
# 1. B2 Glossary Popup Screen
# ==============================================================================
screen b2_glossary_popup(term_key):
    modal True
    zorder 100

    # Retrieve term data from the database
    python:
        term = b2_glossary.get(term_key, {
            "title": term_key,
            "category": "B2 Vocabulary",
            "meaning": "Definition not found.",
            "structure": "N/A",
            "example": "N/A"
        })

    # Dark background overlay to focus on card
    dismiss action Hide("b2_glossary_popup")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 420
        background Frame(Solid("#18181bdf"), 15, 15) # Premium dark transparent card
        padding (25, 25, 25, 25)

        vbox:
            spacing 18
            xfill True

            # Header with category badge
            hbox:
                xfill True
                label term["title"].upper():
                    text_color "#38bdf8" # Cyan
                    text_size 24
                    text_bold True
                    yalign 0.5
                
                frame:
                    yalign 0.5
                    xalign 1.0
                    background Solid("#0369a1") # Dark cyan badge
                    padding (8, 4, 8, 4)
                    label term["category"]:
                        text_color "#ffffff"
                        text_size 12
                        text_bold True
            
            # Divider line
            frame:
                xfill True
                ysize 1
                background Solid("#3f3f46")

            # Meaning
            vbox:
                spacing 4
                label "Meaning:":
                    text_color "#a1a1aa"
                    text_size 14
                    text_bold True
                text term["meaning"]:
                    color "#f4f4f5"
                    size 16

            # Structure
            vbox:
                spacing 4
                label "Sentence Structure:":
                    text_color "#a1a1aa"
                    text_size 14
                    text_bold True
                text term["structure"]:
                    color "#e4e4e7"
                    size 15
                    italic True

            # Example Sentence
            vbox:
                spacing 4
                label "Example in Social Media Context:":
                    text_color "#a1a1aa"
                    text_size 14
                    text_bold True
                frame:
                    background Solid("#27272a")
                    padding (10, 10, 10, 10)
                    xfill True
                    text term["example"]:
                        color "#10b981" # Emerald green for clarity
                        size 15

            # Close Button
            textbutton "I understand!":
                xalign 0.5
                yalign 1.0
                action Hide("b2_glossary_popup")
                background Solid("#0284c7")
                hover_background Solid("#0369a1")
                padding (20, 8, 20, 8)
                text_color "#ffffff"
                text_size 16
                text_bold True
                text_xalign 0.5


# ==============================================================================
# 2. Stats Dashboard Overlay Screen
# ==============================================================================
screen dashboard_ui():
    zorder 90
    
    # Study Mode Indicator & Switch
    frame:
        xalign 0.98
        yalign 0.02
        background Solid("#18181bbf")
        padding (10, 8, 10, 8)
        
        vbox:
            spacing 4
            hbox:
                spacing 8
                label "B2 Study Mode":
                    text_color "#ffffff"
                    text_size 12
                    yalign 0.5
                
                if study_mode:
                    textbutton "ON":
                        action SetVariable("study_mode", False)
                        background Solid("#10b981")
                        padding (6, 2, 6, 2)
                        text_color "#ffffff"
                        text_size 10
                        text_bold True
                else:
                    textbutton "OFF":
                        action SetVariable("study_mode", True)
                        background Solid("#ef4444")
                        padding (6, 2, 6, 2)
                        text_color "#ffffff"
                        text_size 10
                        text_bold True
            
            if study_mode:
                text "Click highlighted words for definitions!":
                    color "#38bdf8"
                    size 9
                    xalign 0.5

    # Main Stats Panel (Top-Left)
    frame:
        xalign 0.02
        yalign 0.02
        background Solid("#18181bbf")
        padding (15, 12, 15, 12)
        xsize 280

        vbox:
            spacing 10
            
            label "[player_name]'s Stats":
                text_color "#f4f4f5"
                text_size 14
                text_bold True
                bottom_margin 2
            
            # Self-Esteem Bar
            vbox:
                spacing 2
                hbox:
                    xfill True
                    text "❤️ Self-Esteem":
                        color "#38bdf8"
                        size 12
                        bold True
                    text "[self_esteem]%":
                        color "#38bdf8"
                        size 12
                        xalign 1.0
                bar:
                    value self_esteem
                    range 100
                    xsize 250
                    ysize 8
                    left_bar Solid("#0ea5e9")
                    right_bar Solid("#3f3f46")
            
            # Online Popularity Bar
            vbox:
                spacing 2
                hbox:
                    xfill True
                    text "🔥 GlowUp Popularity":
                        color "#ec4899"
                        size 12
                        bold True
                    text "[popularity]%":
                        color "#ec4899"
                        size 12
                        xalign 1.0
                bar:
                    value popularity
                    range 100
                    xsize 250
                    ysize 8
                    left_bar Solid("#db2777")
                    right_bar Solid("#3f3f46")

            # Real-Life Connection Bar
            vbox:
                spacing 2
                hbox:
                    xfill True
                    text "👥 Real Connection":
                        color "#10b981"
                        size 12
                        bold True
                    text "[connection]%":
                        color "#10b981"
                        size 12
                        xalign 1.0
                bar:
                    value connection
                    range 100
                    xsize 250
                    ysize 8
                    left_bar Solid("#10b981")
                    right_bar Solid("#3f3f46")


# ==============================================================================
# 3. Simulated Phone Frame Container
# ==============================================================================
# Serves as the wrapper visual frame mimicking a modern phone screen.
screen phone_frame_container(title="GlowUp"):
    frame:
        xalign 0.5
        yalign 0.4
        xsize 380
        ysize 650
        background Frame(Solid("#18181b"), 20, 20) # Rounded dark phone body
        padding (10, 30, 10, 15) # Leave room for speaker/notch and home bar

        # Top Notch representation
        frame:
            xalign 0.5
            ypos -22
            xsize 110
            ysize 15
            background Solid("#09090b")
            
        # Active Screen Area
        frame:
            xfill True
            yfill True
            background Solid("#09090b") # AMOLED Black Screen
            padding (0, 0, 0, 0)
            
            vbox:
                xfill True
                yfill True
                
                # Header Bar
                frame:
                    xfill True
                    ysize 45
                    background Solid("#18181b")
                    padding (10, 5, 10, 5)
                    
                    hbox:
                        xfill True
                        yalign 0.5
                        # App Name
                        text title:
                            color ("#db2777" if title == "GlowUp" else "#38bdf8")
                            size 18
                            bold True
                            yalign 0.5
                        
                        # Top Info
                        text ("10:42 AM" if title != "Night scrolling..." else "2:14 AM"):
                            color "#71717a"
                            size 11
                            xalign 1.0
                            yalign 0.5
                
                # Screen Content Placeholder
                frame:
                    xfill True
                    yfill True
                    background Solid("#0c0c0e")
                    padding (0, 0, 0, 0)
                    
                    # Yields to children injected dynamically via transclude
                    transclude

        # Bottom Home Bar
        frame:
            xalign 0.5
            ypos 615
            xsize 120
            ysize 4
            background Solid("#71717a")


# ==============================================================================
# 4. GlowUp Feed Screen
# ==============================================================================
# Standard Instagram/TikTok style scrollable list
screen glowup_feed(feed_items):
    use phone_frame_container(title="GlowUp"):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xfill True
            yfill True
            xpadding 10
            ypadding 10
            
            vbox:
                spacing 15
                xfill True
                
                for item in feed_items:
                    frame:
                        xfill True
                        background Solid("#18181b")
                        padding (10, 10, 10, 10)
                        
                        vbox:
                            spacing 8
                            # User Header
                            hbox:
                                spacing 8
                                # Circular Avatar placeholder
                                frame:
                                    xsize 30
                                    ysize 30
                                    background Solid(item["avatar_color"])
                                    padding (0,0,0,0)
                                    label item["username"][0].upper():
                                        xalign 0.5 yalign 0.5
                                        text_size 12
                                        text_bold True
                                        text_color "#ffffff"
                                
                                text item["username"]:
                                    color "#ffffff"
                                    size 13
                                    bold True
                                    yalign 0.5
                            
                            # Post Image Representation (Solid Color background)
                            frame:
                                xfill True
                                ysize 180
                                background Solid(item["gradient"])
                                label item["image_desc"]:
                                    xalign 0.5 yalign 0.5
                                    text_color "#ffffff"
                                    text_size 12
                                    text_bold True
                                    text_align 0.5
                            
                            # Post Engagement Bar
                            hbox:
                                spacing 12
                                text "❤️ " + str(item["likes"]) + " likes":
                                    color "#ec4899"
                                    size 11
                                    bold True
                            
                            # Caption
                            text "{b}" + item["username"] + "{/b} " + item["caption"]:
                                color "#e4e4e7"
                                size 12
                            
                            # Top Comment (if any)
                            if item.get("comment_user"):
                                text "{b}" + item["comment_user"] + "{/b}: " + item["comment_text"]:
                                    color "#a1a1aa"
                                    size 11
                            
                            # Interactive Call-to-Action button if current feed prompt
                            if item.get("cta_label") and item.get("cta_action"):
                                textbutton item["cta_label"]:
                                    action item["cta_action"]
                                    background Solid("#db2777")
                                    hover_background Solid("#be185d")
                                    xfill True
                                    padding (8, 6, 8, 6)
                                    text_color "#ffffff"
                                    text_size 12
                                    text_bold True
                                    text_xalign 0.5


# ==============================================================================
# 5. Direct Message / Chat Screen
# ==============================================================================
screen chat_screen(contact_name, messages):
    use phone_frame_container(title=contact_name):
        vbox:
            xfill True
            yfill True
            
            # Message history viewport
            viewport:
                yinitial 1.0 # Start scrolled to bottom
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True
                yfill True
                yoffset -50 # Save space for bottom prompt if needed
                xpadding 10
                ypadding 10
                
                vbox:
                    spacing 10
                    xfill True
                    
                    for msg in messages:
                        # Message Bubble
                        hbox:
                            xfill True
                            if msg["sender"] == "me":
                                # Outgoing message - Align Right (Green/Blue bubble)
                                align (1.0, 0.5)
                                frame:
                                    xsize 240
                                    background Solid("#0284c7") # Sky blue bubble
                                    padding (10, 8, 10, 8)
                                    xalign 1.0
                                    text msg["text"]:
                                        color "#ffffff"
                                        size 12
                            else:
                                # Incoming message - Align Left (Dark grey bubble)
                                align (0.0, 0.5)
                                hbox:
                                    spacing 6
                                    # Tiny Avatar
                                    frame:
                                        xsize 20
                                        ysize 20
                                        background Solid("#ec4899" if contact_name == "Chloe" else "#10b981")
                                        label contact_name[0].upper():
                                            xalign 0.5 yalign 0.5
                                            text_size 8
                                            text_color "#ffffff"
                                            text_bold True
                                    
                                    frame:
                                        xsize 220
                                        background Solid("#27272a") # Zinc dark grey bubble
                                        padding (10, 8, 10, 8)
                                        text msg["text"]:
                                            color "#e4e4e7"
                                            size 12
            
            # Bottom Textbox simulation
            frame:
                xfill True
                ysize 40
                background Solid("#18181b")
                padding (10, 5, 10, 5)
                hbox:
                    xfill True
                    text "Type a message..." color "#71717a" size 11 yalign 0.5
                    text "➡️" color "#0284c7" size 14 xalign 1.0 yalign 0.5


# ==============================================================================
# 6. Interactive End-of-Chapter Language Quiz Screen
# ==============================================================================
screen language_quiz(chapter_title, sentence_with_gap, options, correct_index, explanation):
    modal True
    zorder 105

    # Main Overlay background
    frame:
        xfill True
        yfill True
        background Solid("#09090bdf") # Deep dark overlay

    frame:
        xalign 0.5
        yalign 0.5
        xsize 650
        ysize 480
        background Frame(Solid("#18181bf0"), 15, 15)
        padding (30, 30, 30, 30)

        vbox:
            spacing 20
            xfill True
            
            # Header
            vbox:
                spacing 4
                text "B2 LANGUAGE REFLECTION":
                    color "#0ea5e9"
                    size 14
                    bold True
                    xalign 0.5
                text chapter_title.upper():
                    color "#f4f4f5"
                    size 20
                    bold True
                    xalign 0.5
            
            frame:
                xfill True
                ysize 1
                background Solid("#3f3f46")
            
            # Question Context
            text "Before finalizing the day, think about how you would express these thoughts. Fill in the blank using the correct B2 grammar structure:":
                color "#a1a1aa"
                size 14
                text_align 0.5
            
            # The Sentence Card
            frame:
                background Solid("#27272a")
                padding (15, 15, 15, 15)
                xfill True
                text sentence_with_gap:
                    color "#ffffff"
                    size 16
                    bold True
                    text_align 0.5
                    xalign 0.5
            
            # Options Grid
            vbox:
                spacing 10
                xfill True
                
                for idx, opt in enumerate(options):
                    if idx == correct_index:
                        textbutton opt:
                            action Jump("quiz_correct")
                            background Solid("#3f3f46")
                            hover_background Solid("#10b981") # Turns green on hover
                            xfill True
                            padding (12, 10, 12, 10)
                            text_color "#ffffff"
                            text_size 14
                            text_bold True
                            text_xalign 0.5
                    else:
                        textbutton opt:
                            action Show("quiz_feedback_popup", feedback=explanation)
                            background Solid("#3f3f46")
                            hover_background Solid("#ef4444") # Turns red on hover
                            xfill True
                            padding (12, 10, 12, 10)
                            text_color "#ffffff"
                            text_size 14
                            text_bold True
                            text_xalign 0.5


# ==============================================================================
# 7. Language Quiz Feedback Screen
# ==============================================================================
screen quiz_feedback_popup(feedback):
    modal True
    zorder 110
    
    dismiss action Hide("quiz_feedback_popup")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 250
        background Frame(Solid("#18181be0"), 12, 12)
        padding (20, 20, 20, 20)
        
        vbox:
            spacing 15
            xfill True
            
            label "Not quite right!":
                text_color "#ef4444"
                text_size 18
                text_bold True
                xalign 0.5
                
            text feedback:
                color "#e4e4e7"
                size 14
                text_align 0.5
                xalign 0.5
                
            textbutton "Try Again":
                action Hide("quiz_feedback_popup")
                background Solid("#ef4444")
                padding (15, 6, 15, 6)
                text_color "#ffffff"
                text_size 14
                text_bold True
                xalign 0.5
