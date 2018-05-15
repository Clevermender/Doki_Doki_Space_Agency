
label ddsa_ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    "I stammer, embarrassed."
    "Did Sayori really tell her about it that quickly?"
    if sayori_confess:
        "That we're...a couple now?"
        "I didn't really plan on bringing it up with anyone yet..."
    else:
        "About how I basically turned down her confession?"
        "That makes me really seem like the bad guy here..."
        "But I'm the one who knows what's best for her, right?"
    mc "Jeez..."
    mc "You don't know the full story at all, so..."
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika at thide zorder 1
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem(poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "What's wrong?"
    mc "Ah, nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Try not to take too long, okay?"
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    pause 6.0


    "..."

    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "She is not in her house."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so useless?"
    "What did I do right?"
    if sayori_confess:
        "Confessing to her..."
        "I did the right thing and confessed to her."
        "That's what Sayori needed out of all."
        "She told me how painful it is for others to care about her."
        "Then why did she get better when i confessed?"
    else:
        "Turning down her confession..."
        "That has to have been what pushed her over the edge."
        "Her agonized scream still echoes in my ears."
        "Why did i not meet her at the school or on the way to her house?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I did to make this happen."
    "If I just spent more time not worrying about her."
    "What if i just went to her house..."
    if sayori_confess:
        "And remained friends with her, like it always has been..."
    else:
        "And gave her what I know she wanted out of our relationship..."
        #As you can see, im changing this scene to be more non deppresing. Please change the rest of the text to someting more fitting.
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Screw the Literature Club."
    "Screw the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    "This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    $ in_sayori_kill = False


    return
