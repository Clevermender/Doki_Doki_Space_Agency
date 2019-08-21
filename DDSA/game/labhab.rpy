
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
    "I once i arrive at the fountains, i see Yuri walking towards me."
    "She then notices me."
    mc "There you are."
    mc "I was looking for you."
    y "Why?"
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

label y_rt:
    scene bedroom
    "Well it's time to work on this project."
    "I'm going to help Yuri."
    "She is apparently working with communcations and control, and that is not really like her."
    "But said that she wanted to try it, because she wanted to interact with people more."
    scene kitchen
    "And we all now she don't like it too much."
    "I look at my watch, its...."
    mc "10:32!"
    "And the bus arrives in about 5 minutes."
    "I have still not had breackfast."
    "I will have to eat something at the facility when i arrive."
    pause 2.0
    scene house
    pause 5.0
    scene black
    #this is where the reception BG will be placed, if there even will be one, unless we will use a corridor BG.
    "After a 50 minute bus ride, i finally arrive."
    "I'm starving."
    "The first thing i do is to walk to the lunch room."
    "I arrive outside the lunchroom."
    "There are a a few doors leading to diffrent rooms."
    "I'm hearing people talk in the lunch room, it sounds like someone is doing a breafing."
    "I don't want to disrupt it so have to be a bit quiet."
    "Still, im starving..."
    "But they really leave me no choice."
    "I gently open the door..."
    "{cps=*1}Excuse m--{/cps}{nw}"
    scene black #This is where the lunchroom will be, or maybe this will be one of "those" scenes
    ""
    "The room became silent and everyone turned their heads towards me."#wut

    return


label launch_roll:
    mc "Let's roll the rocket."
    m "Sounds risky, but let's do it."
    m "Yuri, roll the rocket 90 degrees on."
    y "Okay... r-rolling."
    "Yuri moves the the mouse and clicks a few times before starting to type."
    "She then hits enter."
    "On one of the cameras we saw the RCS thrusters on the rocket light up as it began the 90 degree roll."
    "The rocket has now 25 degrees to go, and the reverse thrusters started to slow the rolling so that we don't roll to far."
    "Once we had rolled 90 degrees, the thrusters stoped."
    "But one of the thrusters started to burn with full thrust."
    $ lausu = False
    "The rocket started to shake as it rotated on both the pitch and roll axis."
    m "Yuri!"
    m "Engage the eme-!"
    call showpoem(poem_m5)
    "Just as she said that, all the moniters displaying the cameras on the rocket went black and and all of the monitors and screens recived the Loss of Signal message."
    return

label launch_auto:
    if nat_engi:
        mc "The rocket can fix this automatically."
        $ lausu = True
    else:
        n "It is doing good right now, so we should not change anything."
        n "Automatic is the best way."
        $ lausu = True
        m "Okay, let it be."
        m "Auto will take care of this."
    "And so it did."
    return

label launch_suc:
    m "That worked!"
    m "We are safe for the moment."
    m "Alright, seperation of the last stage in 20 seconds."
    s "Um~"
    s "I think the telescope is below our target altitude."
    s "Umm~"
    s "Can we have a celebration later?"
    s "Im hungry~"
    mc "..."
    m "Sayori, not on the main line!"
    s "Eh!{nw}"
    s "Sorry!"
    return
