 # An application which tells future based upon the zodiac sign

next = True
while next == True:
    print(''' From all the mentioned Zodiac Signs
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer 
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    s = int(input("Pick your sign number and Press Enter to know your future\n"))


    if s==1:
        print("Ganesha predicts success if you're involved with the media. Here's a golden chance to showcase your talent, as all eyes are on you. Your skills and talent will be acknowledged, and short-term goals will see fulfillment.")
    elif s==2:
        print("Today may be the beginning of an exciting relationship, predicts Ganesha. You will feel oneness with words and actions, communicating with your colleagues with ease. The spot light at whichever party you go to will be following you as you will storm the place with your enthusiasm and charisma.")
    elif s==3:
        print("Your interest and performance in sports will go from strength to strength, says Ganesha. You are feeling a bit anxious and will not be able to concentrate on a single job. Instead, you will move from one project to another. You will spend more time at work and less time with the family.")
    elif s==4:
        print("Enough of waiting on the sidelines, watching others take credit for all your hard work. Today, you will stake your claim to what is rightfully yours, the due credit for your work. Surprisingly for you, your peers and superiors will not only appreciate your work without any fuss, but also share with you the big plans they have in store for you.")
    elif s==5:
        print("Ganesha foresees that today, you will be gripped by the desire to shop till you drop, even if it means having to spend a small fortune from your hard-earned savings! You have no problem with that, especially if all the money-spending is being undertaken to please your sweetheart. Those who try to warn you against carrying out your plans will be doing so in vain. It's not for nothing they say, “Love is blind.”")
    elif s==6:
        print("All you have to do is start what you intend to do, and its success will automatically fall in. Such is the day today for you, says Ganesha. Financial transactions will be rewarding. However, the day may not be as exciting as you expect. But then again, don't expect – just go with the flow, says Ganesha.")
    elif s==7:
        print("You are at your best when communicating with others, and your silver-tongued speech will charm many. Your day will be spent in negotiating, meetings, and in interacting with people to get things done. At work, you may be put in charge of some investigative task. Towards the evening, people around you will find you incredibly charming and irresistible.")
    elif s==8:
        print("Take the lonely road today in business ventures, advises Ganesha. Professionally, you are capable of managing massive missions. Be set to administer your department all by yourself. You shall stake a claim as a great team leader today, says Ganesha.")
    elif s==9:
        print("Belligerent – this word describes your state today. Good news, long since awaited, will come by at the workplace. Imagination is set to fly sky-high as you while the evening away in the pleasant company of someone from the opposite sex.")
    elif s==10:
        print("It is time again for that once-in-blue-moon mood swing. You will be easily irked by everyday activities and may let small, less important things bother you too much, foresees Ganesha. But the darkest hour is just before dawn. Things should start looking up later in the day. You enjoy doing things others won't dare, and for all you know, you may have already won millions of hearts with your impressive personality.")
    elif s==11:
        print("Worried about your future? Just approach your work more seriously. You may be overburdening yourself by helping others. While this is noble, Ganesha says it shouldn't be at the cost of your own health. By noon, your spirits will lift. You realise that it's okay to be a little selfish.")
    elif s==12:
        print("It is a good day for you, since all the projects you take up today will reach a satisfactory conclusion. However, this does not mean that you will not be strung out, a fact you would do well to keep hidden, lest your competitors try to take advantage of it, says Ganesha.")
    else:
        print("Hey You sure about the number?")

    next = True if input("\nShall we do it again? (Y/N) ")=="Y" else False
    


