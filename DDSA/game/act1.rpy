################################################################
#This commented block is the original act structure of the game#
################################################################
    # if persistent.playthrough == 0:
    #     # Intro
    #     $ chapter = 0
#---------------------------------#

label act1:
     call ch0_main

#---------------------------------#

     # Poem minigame 1
     call poem

#---------------------------------#

     # Day 1
#     $ chapter = 1 #not exactly sure what this does
     call ch1_main
     call poemresponse_start
     call ch1_end

#---------------------------------#

     # Day 2
     $ chapter = 2
     call ch2_main
     call poemresponse_start
     call ch2_end

#---------------------------------#

     # Poem minigame 3
     call poem

#---------------------------------#

     # Day 3
     $ chapter = 3
     call ch3_main
     call poemresponse_start
     call ch3_end

#---------------------------------#

     $ chapter = 4
     call ch4_main

#---------------------------------#
