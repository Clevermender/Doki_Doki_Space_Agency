label meme_route:
    scene bg residential_day
    with dissolve_scene_full
    m "Why is there a meme route?"
    mc "Huh?"
    m "I'm sorry, that was a strange question to ask."
    mc "..."
    mc "..."
    m "omae wa mou shinderu" #This is how to take lemons and make a energy bar
    mc "nani!?!?!?!?!?"
    #Monika tries to delete MC but she can't
    $ consolehistory = []
    call updateconsole("os.remove(\"characters/mc.chr\")", "Failed. Reason: WTH Monika")
    m "darnit!"
    call updateconsole("os.remove(\"characters/monika.chr\")", "Failed. Reason: monika.chr does not exist")
    m "well..."
    m "this is dank..."
    m "I should work on the main project before this meme route shouldn't I..."
    m "Wait... Is that too much of a fourth wall break?"
    mc "..."
    mc "Mayoi is a better fourth wall breaker."
    m "*cries*"
    mc "Wait..."
    mc "How can you say an asterick"
    mc "how would you pronounce that"
    m "*looks up*"
    mc "..."
    mc "Don't just say /"*look up*/"..."
    'Y/'know what... This is bad comedy. Go read Konosuba if you want comedy.'
    "Yuri burst through the door with a knife in her hand, followed by Natsuki."

    return
