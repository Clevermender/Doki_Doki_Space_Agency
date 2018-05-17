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
    y "[player]!"
    y "No time to explain!"
    y "Hold still or you will die!"
    "Something hits you in the back and you black out."
    scene black
    pause 5.0
    menu:
        "What do you choose?"
        "A boys chamaro.":
            $ black_bird = True
        "Something else." #Write something else in this choise, okay?
            $ black_bird = False

    scene corridor
    mc "W-what happend?"
    "Someone is behind you."
    "You turn around and see Monika."
    m "Come her, boy."
    m "You remember me, don't you?"
    m "Also, [player], i just want to let you know."
    m "I'm not a gigantic robot that wants something that you have on your mind."
    m "Also, this route have nothing to do with the orignal idea of the mod."
    m "And why they have time for this is because someone in the team is a bit slow."
    m "And that they are also doing this meme route."
    m "Intresting, no?"
    pause 2.0
    m "When i think of the word transform, then i think of a electric transformer."
    m "Not like jolt, from the secound Transformers movie."
    m "But the word transform are really common in series you know?"
    m "As well as in manga."
    m "Also, don't you think manga is for kids?"
    "A few meters away, something is distorting space."
    "The distorion grows larger and then a flashself."
    "The distorion disepears and Natski is standing at the spot, glaring at Monika."
    n "What did you say, bitch?"
    n "That manga is for kids?"
    n "WHAT ABOUT MANGA WITH AGE RESTRICTIONS?"
    n "LIKE I DONT KNOW...."
    n "LIKE KÄMPFER?!?!"
    m "What are you talking about?"
    m "I don't have time to look into manga and that stuff."
    m "So any names that you say will go over my head."
    m "Also, I doubt that the word Kämpfer is a english word."
    n "What are you talking about?"
    n "English?"
    n "But we are in japan... Talking japanese...."
    m "Wait i am getting Deja Vu..."
    n "Yeah, thats because you said something simular before the festival."
    n "When i joked about your name."
    m "Oh, yeah, i was going to explain that to you."
    m "The thing is..."
    m "Its not easy to say, but we are in a game."
    m "So to them, the players, we speak english."
    m "Or should i say the text is in english."
    n "What stupid game would be about a club with girls in highschool?"
    n "A literature club..."
    n "Most games are open world with a bunch of things to do."
    n "The only games that usally is about highschools are da...."
    n "Dati...."
    n "No way...."
    n "Wait, but who is the player..."
    n "If its a da-DATING GAME!"
    n "It cant be a girl right?"
    n "And there is only one guy in the club...."
    n "No... No it cant be."
    n "Im not giving myself to that guy!"
    

    return
