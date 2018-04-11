
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
    
label y_rt
    "Well it's time to work on this project."
    "I'm going to help Yuri."
    "She is apparently working with communcations and control, and that is not really like her."
    "But said that she wanted to try it, because she wanted to interact with people more."
    "And we all now she don't like it too much."
    "I look at my watch, its...."
    mc "10:32!"
    "And the bus arrives in about 5 minutes."
    "I have still not had breackfast."
    "I will have to eat something at the facility when i arrive."
    pause 5.0
    
    "After a 50 minute bus ride, i finally arrive."
    "I'm starving."
    "The first thing i do is to walk to the lunch room."
    "I arrive outside the lunchroom."
    "There are a a few doors leading to diffrent rooms."
    "I'm hearing people talk in the lunch room, it sounds like someone is telling others what to do."
    "I don't want to disrupt it so have to be a bit quiet."
    "But im starving so they leave me no choice."
    "I gently open the door..."
    "{cps=*1}Excuse m--{/cps}{nw}"
    ""#wut
    

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
    $ lausu = False
    "The rocket started to shake as it rotated on both the pitch and roll axis."
    m "Yuri!"
    m "Engage the eme-"
    call showpoem(poem_m5)
    "Just as she said that, all the moniters went black and and all of the monitors and screens recived the loss Of signal message."
    return

label launch_auto:
    if nat_engi:
        mc "The rocket can fix this automaticly."
        $ lausu = True
    else:
        n "It is doing good right now, so we should not change anything."
        n "Automatic is the best way."
        $ lausu = True
        m "Okay, let it be."
        m "Auto will take care of this."
    "And so it did."
    "The launch continiued as normal."
    return
