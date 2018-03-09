label script_main:
    scene dark
    stop music fadeout 2.0
    $ m_name = "???"
    m "W-What?"
    
    m "What is this?"

    m "Is this a m-mod?"

    m "Um, okay? I've heard about these before... They are pretty common now..."

    m "Ah, sorry, I'm just rambling! Haha..."

    m "Oh, I'm sorry, you're here to play the mod, correct?"

menu:
  "Yes":
      pass      

  "Yes":
      pass

  "Yes":
      pass

  "Yes":
      pass

  "Yes":
      pass

  "Yes":
      pass      

  "Yes":
      pass

  "Yes":
      pass

  "Yes":
      pass

  "Yes":
      pass

    stop music fadeout 2.0
    
    scene scene
    
    m "Alright, if you insist."
    
    m "[Player]..."
    
    m "I just looked over the mod files..."
    
    m "Looks like there's already a replacement script."
    
    m "Hmmm."
    
    
    m "..."
    
    m "..."
    
    m "..."
    
    m "Just a second..."
    
    m "..."
    
    m "..."
    
    m "..."
    
    m "Okay, that'll do. I think we're good now."
    
    m "I still don't understand. Why continue?"

    m "You're... doing it... for them... aren't you?"

    m "Well, I wish you the best of luck."
    
    $ m_name = "Monika"
    
    call screen dialog("Enjoy your trip!", ok_action=Return()) 

    scene bg residential_day
    with dissolve_scene_half
    play music t2

    "It's the day after the festival."
    "The festival really was something."
    "We had a lot of people that visited our club."
    "Most just walked in, looked around, and then they left."
    "But there was a few people that were intrested"
    "I don't really remember anything more then that."
    "But Monika said soemthing about the sky."
    "She had seen something special at the festival."
    "I was not with her when she did, but it sounds like she really liked it."
    "I will see what she has in mind at the club."

    scene bg club_day2
    with wipeleft
    play music t3

    "I walk into the classroom."
    "Monika is talking to a much older guy."
    "I have never seen him before."
    "He has some kind of emblem on his right arm."
    "He gives Monika some papers."
    "I cant see what they are doing."
    "They had a weird icon in the top left corner."
    "It looks like they are finished with whatever they did."
    "The man leaves and I walk up to Monika."

    show monika 1b at t11 zorder 2
    m "Hi, [player]."
    mc "Hello, Monika."
    mc "Who was that guy?"
    m 3l "That was..."
    m 4n "I will tell you later when everyone is here."
    mc "Okay?"
    hide monika
    "Monika went to the teacher's desk and put the papers on it."
    "I walked to the desk to have a look at the papers."
    pause 0.05
    "As i do, Monika jumps infront of me out of nowhere."
    show monika 1h at face
    m 2g "{cps=*1}What d-{/cps}{nw}"
    "I got scared and tried to evade."
    "But I was between two desks."
    "I was supposed to place my foot on the floor, but instead, I place it on one of the desk's supporting legs..."
    "And becouse my reaction time is very bad, I did not stop my fall."
    "I got some extra speed and instead of trying to stop, I rushed right into Monika."
    "We fall to the ground."
    m "{cps=*1}Whaa!?{/cps}{nw}"
    scene black
    hide monika
    pause 0.85
    scene bg club_day2
    "But becouse Monika is better and faster on movement then me, she was one her feet even before i knew what happend."
    show monika 2d at t11 zorder 2
    m "Do you need help with controlling yourself?"
    m 2i "Or you you think that its okay to force a girl against her own will?"
    "What?"
    mc "What are you talking about?"
    mc "I triped and fell!"
    m 1h "And flew into my..."
    m 2g "My..."
    m 4l "My posture..." #
    m 3n "Is that what you call them?" #
    mc "Wait what?" #
    mc "Why are you talking about your posture?" #
    show monika 2i
    "Monika looks at me with judgeing look."
    "I just remember my conversation with Yuri last week."
    mc "Ah, wait."
    mc "Never mind..."
    m "Your not as dense as a black hole, are you?"
    m 4k "Just kidding, [player]."
    m 4e "I know it was a accident."
    m 3n "And we can talk a little bit more open when its just you and me."
    m 4l "Right?"
    "I do not really understand what she is pointing at."
    "But i go along with her."
    mc "Off course!"
    m 4e "So you want to talk about stuff like that!?"
    "I thought of what she said."
    "Now i feel really stupid."
    mc "But anyway, whats about these papers?"
    "I tried to reach them, but Monika grabed my hand and directed it away from the papers."
    m 3e "As i said, i will talk about that later."
    "I looked at them again from a distance and saw that the icon is the same as the emblem on the arm of the man."
    "I sigh and walk to one of the desks."
    "Monika is constantly looking in my direction."
    "Probably to check that I'm not trying to look at the papers."

    "After about five minutes, the door opens."
    "Sayori walks in."
    "She was kinda down at the end of the last week."
    "I just rememberd."
    "I mumbled to myself."
    mc "Depression..."
    "But she was happy again at the festival, and seems to be in her normal mood today."
    show sayori 1c at t22 zorder 2
    show monika 1e at t21 zorder 2
    s "Hey Monika!"
    s 1c "And hi, [player]."
    mc "Hello there, Sayori."
    m 2a "Sayori, have you seen the others?"
    s 1n "Ehh..."
    s 1b "I met Yuri outside the classroom, she said that she was going to the toilet."
    s "But i have not seen Natsuki today."
    "I decided to go out and look for Yuri, and potentially Natsuki."
    mc "Well, i do not have anything better to, and we are not going to do anything before everyone is here..."
    mc "So i will search for Yuri and Natsuki."
    s 2c "But i sai-"
    "Monika interupts Sayori."
    m 4d "Bring our clubmembers home." #THE DOKIAN. BRING THEM HOME. 3.5.18
    m 3n "Umm...I meant bring them to the club.."
    hide monika
    hide sayori
    scene black
    pause 1.0
    "I walk out of the clubroom."
    scene bg corridor
    with wipeleft_scene

    "I start walking down the corrider."
    $ y_name = "Yuri"
    $ style.say_dialogue = style.normal
    "The first one to look for is Yuri."
    $ style.say_dialogue = style.edited
    "{cps=*2}Becouse Yuri is the best girl out of them all.{/cps}{nw}" #i demand a refund
    "{cps=*2}And I'm going to land on Dr. Edmunds planet to wait for the dokis to be real.{/cps}{nw}" #Dokistellar, Mc was friends with the dokis, but he was never meant to stop there.
    "{cps=*3}Even if that means waves big as mountians.{/cps}{nw}"
    "{cps=*3}And all of my friends and my other family will be dead by the time the dokis are real.{/cps}{nw}" #There will be more refrences to both movies, and possibly real events.
    $ style.say_dialogue = style.normal
    $ del _history_list[-4:]
    "Becouse Yuri is closer to the clubroom then Natsuki probably is." #yo what. Answer: I probably spelled answer wrong, and it did make sense in swedish.
    $ style.say_dialogue = style.edited
    "{cps=*2}I turned around the corner to the fountain Yuri cut herself at.{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ del _history_list[-1:]
    "I turned around the corner to the fountain from where Yuri goes to get water for her tea at."
    menu:
        "Do you really have time to walk?"
        "I do not have time.":
            call dont_have_time
            $ time_no = True
        "No need to hurry.": #this may be confusing, so the wording might have to be changed.
            $ time_no = False
            call do_have_time

    scene black
    "Skipping to when everyone is in the classroom." #This part is not connected to who to help, and fix the positions of where to show the girls.
    scene bg club_day2
    show monika 1b at f22 zorder 2
    m "Okay everyone!"
    m "I have some news."
    show sayori 1n at t21 zorder 2
    s "About what?"
    m 2j "We are starting a new project for the club."
    show yuri 2f at l33 zorder 2

    "Time to choose who to help."
    menu:
        "I should help..."

        "Natsuki.":
            $ nat_engi = True
        "Others.":
            $ nat_engi = False

            pass
    #I did not want to forget to write the launch, Monika will tell them soon.

    "Skipping to launch day."
    pause 5.0

    m "Let's begin with the launch checklist."
    m "T minus 85 secounds to launch."
    m "Electical Systems."
    n "Go."
    m "RCS control."
    n "Go."
    m "Guidence."
    y "..."
    y "G-Go."
    "The checklist is long and complicated."
    "Monika looks worried everytime she does not get a Go immedietly."
    m "Fuel pressure."
    n "Nominal."
    m "T minus 10 secounds."
    m "9."
    "I count with everyone else."
    "8"
    "7"
    "6"
    "5"
    "4"
    m "Main engine start."
    "There is a jet of smoke and fire bursting out of the engine as it starts,"
    "Even in the mission control room, the sound of the engines can be heard."
    m "2"
    m "1"
    "The engines scream and roar as the flame grows and get coverd by smoke and steam."
    m "And liftoff of the Markov telescope on a trip to earth orbit, in order to study further targets for other missions."
    m "We have cleared the tower."
    "I see Yuri looking at her bag for a secound."
    "She then tried to reach it with the arm, but stoped and then looked around her."
    "She then returned to monitor the rocket."
    y "W-we are at 500 meter per secound."
    "She sound excited and less worried."
    "Almost like last week, when she resited her poem in front of everyone."
    m "We have a altitude of 1.6 km."
    "20 secounds has now passed since the launch."
    m "Thats stage 1."
    m "Booster seperation comfired."
    "Natsuki was about to say something but stoped herself."
    "She looked at her monitor with a worried expression."
    n "One of the boosters did not seperate correctly."
    n "The decoupler malfunctioned and broke, so the seperation thruster instead ripped the booster away."
    n "Now part of the decoupler is still on the rocket."
    n "And possibly some wiring is exposed."
    m "But what about the center of mass?"
    n "I don't know..."
    n "Ask the one that can see the trajectory maybe!"
    m "Eh..."
    m "Yuri, by how much are we diverting away from our planned trajectory?"
    y "About z-zero point two degrees to the south..."
    y "Rotation speed is increasing by zero point zero eight dergrees per secound."
    if nat_engi:
        m "Alright, [player]!"
        m "You worked with the rocket's control systems the most."
        m "Should we roll the rocket 90 degrees so that the center of mass is pointing towards the east?"
        m "Or should we let the rocket automaticly adjust the course to componsate for the tilting?"
        mc "Well..."
        mc "Okay, lets do this."
        menu:
            mc "The best thing to do is."

            "Let's roll the rocket.":
                $ manual_ctrl = True
                call launch_roll
            "Let the computer take care of it.":
                $ manual_ctrl = False
                call launch_auto
        mc "Okay..."
    else:
        m "Alright, Natsuki."
        m "You worked with the rocket's controll systems the most."
        m "Should we roll the rocket 90 degrees so that the center of mass is pointing towards the east?"
        m "Or should we let the rocket automaticly adjust the course to componsate for the tilting?"
        n "It is doing good right now, so we should not change anything."
        n "Automatic is the best way."
        m "okay, let it be."
        m "Auto will take care of this."
        call launch_auto
    return

label dont_have_time:
    "I need to get this done quickly."
    "And I need to find Natsuki and Yuri."
    "I start running."
    "The floor is wet."
    $ y_name = "???"
    "I almost slip next to the water fountains."
    y "[player]?"
    "I hear someone behind me."
    "I almost slip again trying to stop."
    mc "Yuri?"
    $ y_name = "Yuri"
    show yuri 1e at t11 zorder 2
    y "I heard you shout my name."
    y 3f "Is something wrong?"
    mc "The club is about to start."
    mc "Monika has something important to announce."
    y "What is it abo-"
    mc "I dont know!"
    show yuri 4c
    y "I'm sorry..."
    mc "For what?"
    y "I..."
    mc "You did nothing wrong."
    mc "Im just a little bit stressed out."
    y 4a "Are you sure?"
    mc "Yes..."
    y 1l "Alright."
    y 1b "Lets go."
    mc "Wait, we need to find Natsuki first."
    y 1j "I saw her by the vending machines just a few minutes ago."
    mc "Can you go and get her?"
    mc "I will go and tell the others."
    y 1k "I will try."
    return

label do_have_time:
    "I dont need to hurry."
    return

label launch_roll:
    mc "Let's roll the rocket."
    m "Sounds risky, but let's do it."
    m "Yuri, roll the rocket 90 degrees on."
    y "Okay... r-rolling."
    "Yuri moves the the mouse and clicks a few times before starting to type."
    "She then hits enter."
    "On one of the cameras we saw the roll thrusters on the rocket light up as it began the 90 degree roll."
    "The rocket has now 25 degrees to go, and the reverse thrusters started to slow the rolling so that we don't roll to far."
    "Once we had rolled 90 degrees, the thrusters stoped."
    "But one of the thrusters started to burn with full thrust."
    "The rocket started to shake as it rotated on both the pitch and roll axis."
    m "Yuri!"
    m "Engage the eme-"
    call showpoem(poem_m5)
    "Just as she said that, all the cameras went black and and all of the monitors and screens recived the lose Of signal message."
    return

label launch_auto:
    if nat_engi:
        mc "The rocket can fix this automaticly."
    else:
        n "It is doing good right now, so we should not change anything."
        n "Automatic is the best way."
        m "okay, let it be."
        m "Auto will take care of this."
    "And so it did."
    "The launch continiued as normal."
    return
