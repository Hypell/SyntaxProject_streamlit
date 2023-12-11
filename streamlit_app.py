from pathlib import Path
import re
import gzip, json
from textblob import TextBlob
import pandas as pd
import pronouncing
import nltk
nltk.download('all')
from io import StringIO

#-------------------------------------------------------------------------------------

import streamlit as st

st.header("영시 분석 결과 보기")

text_contents = '''
   CAMDEN! most reverend head, to whom I owe
   All that I am in arts, all that I know—
   How nothing’s that! to whom my country owes
   The great renown, and name wherewith she goes!
   Than thee the age sees not that thing more grave,
   More high, more holy, that she more would crave.
   What name, what skill, what faith hast thou in things!
   What sight in searching the most antique springs!
   What weight, and what authority in thy speech!
   Men scarce can make that doubt, but thou canst teach.
   Pardon free truth, and let thy modesty,
   Which conquers all, be once o’ercome by thee.
   Many of thine, this better could, than I;
   But for their powers, accept my piety.

   HERE lies, to each her parents’ ruth,
   Mary, the daughter of their youth;
   Yet, all heaven’s gifts, being heaven’s due,
   It makes the father less to rue.
   At six months’ end, she parted hence,
   With safety of her innocence;
   Whose soul heaven’s queen, whose name she bears,
   In comfort of her mother’s tears,
   Hath placed amongst her virgin-train;
   Where, while that severed doth remain,
   This grave partakes the fleshly birth;
   Which cover lightly, gentle earth!

   FAREWELL, thou child of my right hand, and joy;
   My sin was too much hope of thee, loved boy;
   Seven years thou wert lent to me, and I thee pay,
   Exacted by thy fate, on the just day.
   Oh! could I lose all father, now! for why,
   Will man lament the state he should envy?
   To have so soon ’scaped world’s, and flesh’s rage,
   And, if no other misery, yet age!
   Rest in soft peace, and, asked, say here doth lie
   Ben Jonson his best piece of poetry;
   For whose sake, henceforth, all his vows be such,
   As what he loves may never like too much.

   HOW I do love thee, Beaumont, and thy muse,
   That unto me dost such religion use!
   How I do fear myself, that am not worth
   The least indulgent thought thy pen drops forth!
   At once thou mak’st me happy, and unmak’st;
   And giving largely to me, more thou takest!
   What fate is mine, that so itself bereaves?
   What art is thine, that so thy friend deceives?
   When even there, where most thou praisest me,
   For writing better, I must envy thee.

   THE ports of death are sins; of life, good deeds:
   Through which our merit leads us to our meeds.
   How wilful blind is he, then, that would stray,
   And hath it in his powers to make his way!
   This world death’s region is, the other life’s:
   And here it should be one of our first strifes,
   So to front death, as men might judge us past it:
   For good men but see death, the wicked taste it.

   TO-NIGHT, grave sir, both my poor house and I
   Do equally desire your company;
   Not that we think us worthy such a guest,
   But that your worth will dignify our feast,
   With those that come; whose grace may make that seem
   Something, which else could hope for no esteem.
   It is the fair acceptance, sir, creates
   The entertainment perfect, not the cates.
   Yet shall you have, to rectify your palate,
   An olive, capers, or some bitter salad
   Ushering the mutton; with a short-legged hen,
   If we can get her, full of eggs, and then,
   Lemons and wine for sauce: to these, a coney
   Is not to be despaired of for our money;
   And though fowl now be scarce, yet there are clerks,
   The sky not falling, think we may have larks.
   I’ll tell you of more, and lie, so you will come:
   Of partridge, pheasant, woodcock, of which some
   May yet be there; and godwit if we can;
   Knat, rail, and ruff, too.  Howsoe’er, my man
   Shall read a piece of Virgil, Tacitus,
   Livy, or of some better book to us,
   Of which we’ll speak our minds, amidst our meat;
   And I’ll profess no verses to repeat:
   To this if aught appear, which I not know of,
   That will the pastry, not my paper, show of.
   Digestive cheese, and fruit there sure will be;
   But that which most doth take my muse and me,
   Is a pure cup of rich canary wine,
   Which is the Mermaid’s now, but shall be mine:
   Of which had Horace, or Anacreon tasted,
   Their lives, as do their lines, till now had lasted.
   Tobacco, nectar, or the Thespian spring,
   Are all but Luther’s beer, to this I sing.
   Of this we will sup free, but moderately,
   And we will have no Pooly’ or Parrot by;
   Nor shall our cups make any guilty men;
   But at our parting we will be as when
   We innocently met.  No simple word
   That shall be uttered at our mirthful board,
   Shall make us sad next morning; or affright
   The liberty that we’ll enjoy to-night.

   WEEP with me all you that read
      This little story;
   And know for whom a tear you shed,
      Death’s self is sorry.
   ’Twas a child that so did thrive
      In grace and feature,
   As heaven and nature seemed to strive
      Which owned the creature.
   Years he numbered scarce thirteen
      When fates turned cruel;
   Yet three filled zodiacs had he been
      The stage’s jewel;
   And did act, what now we moan,
      Old men so duly;
   As, sooth, the Parcæ thought him one
      He played so truly.
   So, by error to his fate
      They all consented;
   But viewing him since, alas, too late!
      They have repented;
   And have sought to give new birth,
      In baths to steep him;
   But, being so much too good for earth,
      Heaven vows to keep him.

   WOULDST thou hear what man can say
   In a little?  Reader, stay.
   Underneath this stone doth lie
   As much beauty as could die
   Which in life did harbour give
   To more virtue than doth live.
   If, at all, she had a fault
   Leave it buried in this vault.
   One name was Elizabeth,
   The other let it sleep with death.
   Fitter, where it died, to tell,
   Than that it lived at all.  Farewell.

   UNDERNEATH this sable hearse
   Lies the subject of all verse,
   Sidney’s sister, Pembroke’s mother:
   Death! ere thou hast slain another,
   Learned, and fair, and good as she,
   Time shall throw a dart at thee.

   TO draw no envy, Shakspeare, on thy name,
   Am I thus ample to thy book and fame;
   While I confess thy writings to be such,
   As neither man, nor muse can praise too much.
   ’Tis true, and all men’s suffrage.  But these ways
   Were not the paths I meant unto thy praise;
   For silliest ignorance on these may light,
   Which, when it sounds at best, but echoes right;
   Or blind affection, which doth ne’er advance
   The truth, but gropes, and urgeth all by chance;
   Or crafty malice might pretend this praise,
   And think to ruin, where it seemed to raise.
   These are, as some infamous bawd, or whore,
   Should praise a matron; what would hurt her more?
   But thou art proof against them, and, indeed,
   Above the ill-fortune of them, or the need.
   I, therefore, will begin: Soul of the age!
   The applause! delight! and wonder of our stage!
   My Shakspeare rise!  I will not lodge thee by
   Chaucer, or Spenser, or bid Beaumont lie
   A little further off, to make thee room:
   Thou art a monument without a tomb,
   And art alive still, while thy book doth live
   And we have wits to read, and praise to give.
   That I not mix thee so, my brain excuses,
   I mean with great, but disproportioned Muses;
   For if I thought my judgment were of years,
   I should commit thee surely with thy peers,
   And tell how far thou didst our Lily outshine,
   Or sporting Kyd, or Marlow’s mighty line.
   And though thou hadst small Latin and less Greek,
   From thence to honour thee, I will not seek
   For names: but call forth thundering Eschylus,
   Euripides, and Sophocles to us,
   Pacuvius, Accius, him of Cordoua dead,
   To live again, to hear thy buskin tread,
   And shake a stage; or, when thy socks were on,
   Leave thee alone for the comparison
   Of all that insolent Greece, or haughty Rome
   Sent forth, or since did from their ashes come.
   Triumph, my Britain, thou hast one to show,
   To whom all scenes of Europe homage owe.
   He was not of an age, but for all time!
   And all the Muses still were in their prime,
   When, like Apollo, he came forth to warm
   Our ears, or like a Mercury to charm!
   Nature herself was proud of his designs,
   And joyed to wear the dressing of his lines!
   Which were so richly spun, and woven so fit,
   As, since, she will vouchsafe no other wit.
   The merry Greek, tart Aristophanes,
   Neat Terence, witty Plautus, now not please;
   But antiquated and deserted lie,
   As they were not of nature’s family.
   Yet must I not give nature all; thy art,
   My gentle Shakspeare, must enjoy a part.
   For though the poet’s matter nature be,
   His heart doth give the fashion: and, that he
   Who casts to write a living line, must sweat,
   (Such as thine are) and strike the second heat
   Upon the Muse’s anvil; turn the same,
   And himself with it, that he thinks to frame;
   Or for the laurel, he may gain a scorn;
   For a good poet’s made, as well as born.
   And such wert thou!  Look how the father’s face
   Lives in his issue, even so the race
   Of Shakspeare’s mind and manners brightly shines
   In his well-turnèd, and true filèd lines;
   In each of which he seems to shake a lance,
   As brandished at the eyes of ignorance.
   Sweet Swan of Avon! what a sight it were
   To see thee in our water yet appear,
   And make those flights upon the banks of Thames,
   That so did take Eliza, and our James!
   But stay, I see thee in the hemisphere
   Advanced, and made a constellation there!
   Shine forth, thou star of poets, and with rage,
   Or influence, chide, or cheer the drooping stage,
   Which, since thy flight from hence, hath mourned like night,
   And despairs day, but for thy volume’s light.

   DRINK to me only with thine eyes,
      And I will pledge with mine;
   Or leave a kiss but in the cup,
      And I’ll not look for wine.
   The thirst that from the soul doth rise
      Doth ask a drink divine:
   But might I of Jove’s nectar sup,
      I would not change for thine.

   I sent thee late a rosy wreath,
      Not so much honouring thee,
   As giving it a hope that there
      It could not withered be.
   But thou thereon didst only breathe,
      And sent’st it back to me:
   Since when it grows, and smells, I swear,
      Not of itself, but thee.

      SEE the chariot at hand here of Love,
         Wherein my lady rideth!
      Each that draws is a swan or a dove,
         And well the car Love guideth.
      As she goes, all hearts do duty
            Unto her beauty;
      And, enamoured, do wish, so they might
            But enjoy such a sight,
      That they still were to run by her side,
   Through swords, through seas, whither she would ride.

      Do but look on her eyes, they do light
         All that Love’s world compriseth!
      Do but look on her hair, it is bright
         As Love’s star when it riseth!
      Do but mark, her forehead’s smoother
            Than words that soothe her!
      And from her arched brows, such a grace
            Sheds itself through the face,
      As alone there triumphs to the life
   All the gain, all the good, of the elements’ strife.

      Have you seen but a bright lily grow
         Before rude hands have touched it?
      Have you marked but the fall o’ the snow
         Before the soil hath smutched it?
      Have you felt the wool of beaver?
            Or swan’s down ever?
      Or have smelt o’ the bud o’ the brier?
            Or the nard in the fire?
      Or have tasted the bag of the bee?
   O so white!  O so soft!  O so sweet is she!

   MEN, if you love us, play no more
      The fools or tyrants with your friends,
   To make us still sing o’er and o’er
      Our own false praises, for your ends:
         We have both wits and fancies too,
         And, if we must, let’s sing of you.

   Nor do we doubt but that we can,
      If we would search with care and pain,
   Find some one good in some one man;
      So going thorough all your strain,
         We shall, at last, of parcels make
         One good enough for a song’s sake.

   And as a cunning painter takes,
      In any curious piece you see,
   More pleasure while the thing he makes,
      Than when ’tis made—why so will we.
         And having pleased our art, we’ll try
         To make a new, and hang that by.

      BRAVE infant of Saguntum, clear
      Thy coming forth in that great year,
   When the prodigious Hannibal did crown
   His cage, with razing your immortal town.
         Thou, looking then about,
         Ere thou wert half got out,
      Wise child, didst hastily return,
      And mad’st thy mother’s womb thine urn.
   How summed a circle didst thou leave mankind
   Of deepest lore, could we the centre find!

      Did wiser nature draw thee back,
      From out the horror of that sack,
   Where shame, faith, honour, and regard of right,
   Lay trampled on? the deeds of death and night,
         Urged, hurried forth, and hurled
         Upon th’ affrighted world;
      Sword, fire, and famine, with fell fury met,
      And all on utmost ruin set;
   As, could they but life’s miseries foresee,
   No doubt all infants would return like thee.

   For what is life, if measured by the space
         Not by the act?
   Or maskèd man, if valued by his face,
         Above his fact?
      Here’s one outlived his peers,
      And told forth fourscore years;
      He vexèd time, and busied the whole state;
         Troubled both foes and friends;
         But ever to no ends:
      What did this stirrer but die late?
   How well at twenty had he fallen or stood!
   For three of his fourscore he did no good.

      He entered well, by virtuous parts,
      Got up, and thrived with honest arts;
   He purchased friends, and fame, and honours then,
   And had his noble name advanced with men:
         But weary of that flight,
         He stooped in all men’s sight
            To sordid flatteries, acts of strife,
            And sunk in that dead sea of life,
   So deep, as he did then death’s waters sup,
   But that the cork of title buoyed him up.

      Alas! but Morison fell young:
      He never fell,—thou fall’st, my tongue.
   He stood a soldier to the last right end,
   A perfect patriot, and a noble friend;
         But most, a virtuous son.
         All offices were done
      By him, so ample, full, and round,
      In weight, in measure, number, sound,
   As, though his age imperfect might appear,
   His life was of humanity the sphere.

   Go now, and tell out days summed up with fears,
         And make them years;
   Produce thy mass of miseries on the stage,
         To swell thine age;
      Repeat of things a throng,
      To show thou hast been long,
   Not lived: for life doth her great actions spell.
      By what was done and wrought
      In season, and so brought
   To light: her measures are, how well
   Each syllabe answered, and was formed, how fair;
   These make the lines of life, and that’s her air!

      It is not growing like a tree
      In bulk, doth make men better be;
   Or standing long an oak, three hundred year,
   To fall a log at last, dry, bald, and sear:
         A lily of a day,
         Is fairer far in May,
      Although it fall and die that night;
      It was the plant, and flower of light.
   In small proportions we just beauties see;
   And in short measures, life may perfect be.

      Call, noble Lucius, then for wine,
      And let thy looks with gladness shine:
   Accept this garland, plant it on thy head
   And think, nay know, thy Morison’s not dead
         He leaped the present age,
         Possessed with holy rage
      To see that bright eternal day;
      Of which we priests and poets say,
   Such truths, as we expect for happy men:
   And there he lives with memory and Ben.

   Jonson, who sung this of him, ere he went,
            Himself to rest,
   Or taste a part of that full joy he meant
            To have expressed,
         In this bright Asterism!
         Where it were friendship’s schism,
      Were not his Lucius long with us to tarry,
         To separate these twi-
         Lights, the Dioscouri;
      And keep the one half from his Harry,
   But fate doth so alternate the design
   Whilst that in heaven, this light on earth must shine.

      And shine as you exalted are;
      Two names of friendship, but one star:
   Of hearts the union, and those not by chance
   Made, or indenture, or leased out t’advance
         The profits for a time.
         No pleasures vain did chime,
      Of rhymes, or riots, at your feasts,
      Orgies of drink, or feigned protests:
   But simple love of greatness and of good,
   That knits brave minds and manners more than blood.

      This made you first to know the why
      You liked, then after, to apply
   That liking; and approach so one the t’other,
   Till either grew a portion of the other:
         Each styled by his end,
         The copy of his friend.
      You lived to be the great sir-names,
      And titles, by which all made claims
   Unto the virtue; nothing perfect done,
   But as a Cary, or a Morison.

   And such a force the fair example had,
            As they that saw
   The good, and durst not practise it, were glad
            That such a law
         Was left yet to mankind;
         Where they might read and find
      Friendship, indeed, was written not in words;
         And with the heart, not pen,
         Of two so early men,
      Whose lines her rolls were, and records;
   Who, ere the first down bloomed upon the chin,
   Had sowed these fruits, and got the harvest in.

   AND must I sing?  What subject shall I choose!
   Or whose great name in poets’ heaven use,
   For the more countenance to my active muse?

   Hercules? alas, his bones are yet sore
   With his old earthly labours t’ exact more
   Of his dull godhead were sin.  I’ll implore

   Phœbus.  No, tend thy cart still.  Envious day
   Shall not give out that I have made thee stay,
   And foundered thy hot team, to tune my lay.

   Nor will I beg of thee, lord of the vine,
   To raise my spirits with thy conjuring wine,
   In the green circle of thy ivy twine.

   Pallas, nor thee I call on, mankind maid,
   That at thy birth mad’st the poor smith afraid.
   Who with his axe thy father’s midwife played.

   Go, cramp dull Mars, light Venus, when he snorts,
   Or with thy tribade trine invent new sports;
   Thou, nor thy looseness with my making sorts.

   Let the old boy, your son, ply his old task,
   Turn the stale prologue to some painted mask;
   His absence in my verse is all I ask.

   Hermes, the cheater, shall not mix with us,
   Though he would steal his sisters’ Pegasus,
   And rifle him; or pawn his petasus.

   Nor all the ladies of the Thespian lake,
   Though they were crushed into one form, could make
   A beauty of that merit, that should take

   My muse up by commission; no, I bring
   My own true fire: now my thought takes wing,
   And now an epode to deep ears I sing.

   NOT to know vice at all, and keep true state,
      Is virtue and not fate:
   Next to that virtue, is to know vice well,
      And her black spite expel.
   Which to effect (since no breast is so sure,
      Or safe, but she’ll procure
   Some way of entrance) we must plant a guard
      Of thoughts to watch and ward
   At th’ eye and ear, the ports unto the mind,
      That no strange, or unkind
   Object arrive there, but the heart, our spy,
      Give knowledge instantly
   To wakeful reason, our affections’ king:
      Who, in th’ examining,
   Will quickly taste the treason, and commit
      Close, the close cause of it.
   ’Tis the securest policy we have,
      To make our sense our slave.
   But this true course is not embraced by many:
      By many! scarce by any.
   For either our affections do rebel,
      Or else the sentinel,
   That should ring ’larum to the heart, doth sleep:
      Or some great thought doth keep
   Back the intelligence, and falsely swears
      They’re base and idle fears
   Whereof the loyal conscience so complains.
      Thus, by these subtle trains,
   Do several passions invade the mind,
      And strike our reason blind:
   Of which usurping rank, some have thought love
      The first: as prone to move
   Most frequent tumults, horrors, and unrests,
      In our inflamèd breasts:
   But this doth from the cloud of error grow,
      Which thus we over-blow.
   The thing they here call love is blind desire,
      Armed with bow, shafts, and fire;
   Inconstant, like the sea, of whence ’tis born,
      Rough, swelling, like a storm;
   With whom who sails, rides on the surge of fear,
      And boils as if he were
   In a continual tempest.  Now, true love
      No such effects doth prove;
   That is an essence far more gentle, fine,
      Pure, perfect, nay, divine;
   It is a golden chain let down from heaven,
      Whose links are bright and even;
   That falls like sleep on lovers, and combines
      The soft and sweetest minds
   In equal knots: this bears no brands, nor darts,
      To murder different hearts,
   But, in a calm and god-like unity,
      Preserves community.
   O, who is he that, in this peace, enjoys
      Th’ elixir of all joys?
   A form more fresh than are the Eden bowers,
      And lasting as her flowers;
   Richer than Time and, as Times’s virtue, rare;
      Sober as saddest care;
   A fixèd thought, an eye untaught to glance;
      Who, blest with such high chance,
   Would, at suggestion of a steep desire,
      Cast himself from the spire
   Of all his happiness?  But soft: I hear
      Some vicious fool draw near,
   That cries, we dream, and swears there’s no such thing,
      As this chaste love we sing.
   Peace, Luxury! thou art like one of those
      Who, being at sea, suppose,
   Because they move, the continent doth so:
      No, Vice, we let thee know
   Though thy wild thoughts with sparrows’ wings do fly,
      Turtles can chastely die;
   And yet (in this t’ express ourselves more clear)
      We do not number here
   Such spirits as are only continent,
      Because lust’s means are spent;
   Or those who doubt the common mouth of fame,
      And for their place and name,
   Cannot so safely sin: their chastity
      Is mere necessity;
   Nor mean we those whom vows and conscience
      Have filled with abstinence:
   Though we acknowledge who can so abstain,
      Makes a most blessèd gain;
   He that for love of goodness hateth ill,
      Is more crown-worthy still
   Than he, which for sin’s penalty forbears:
      His heart sins, though he fears.
   But we propose a person like our Dove,
      Graced with a Phœnix’ love;
   A beauty of that clear and sparkling light,
      Would make a day of night,
   And turn the blackest sorrows to bright joys:
      Whose odorous breath destroys
   All taste of bitterness, and makes the air
      As sweet as she is fair.
   A body so harmoniously composed,
      As if natùre disclosed
   All her best symmetry in that one feature!
      O, so divine a creature
   Who could be false to? chiefly, when he knows
      How only she bestows
   The wealthy treasure of her love on him;
      Making his fortunes swim
   In the full flood of her admired perfection?
      What savage, brute affection,
   Would not be fearful to offend a dame
      Of this excelling frame?
   Much more a noble, and right generous mind,
      To virtuous moods inclined,
   That knows the weight of guilt: he will refrain
      From thoughts of such a strain,
   And to his sense object this sentence ever,
      “Man may securely sin, but safely never.”

   THOUGH beauty be the mark of praise,
      And yours, of whom I sing, be such
      As not the world can praise too much,
   Yet is ’t your virtue now I raise.

   A virtue, like allay, so gone
      Throughout your form, as though that move,
      And draw, and conquer all men’s love,
   This subjects you to love of one,

   Wherein you triumph yet: because
      ’Tis of yourself, and that you use
      The noblest freedom, not to choose
   Against or faith, or honour’s laws.

   But who could less expect from you,
      In whom alone Love lives again?
      By whom he is restored to men;
   And kept, and bred, and brought up true?

   His falling temples you have reared,
      The withered garlands ta’en away;
      His altars kept from the decay
   That envy wished, and nature feared;

   And on them burns so chaste a flame,
      With so much loyalty’s expense,
      As Love, t’ acquit such excellence,
   Is gone himself into your name.

   And you are he: the deity
      To whom all lovers are designed,
      That would their better objects find;
   Among which faithful troop am I;

   Who, as an offering at your shrine,
      Have sung this hymn, and here entreat
      One spark of your diviner heat
   To light upon a love of mine;

   Which, if it kindle not, but scant
      Appear, and that to shortest view,
      Yet give me leave t’ adore in you
   What I, in her, am grieved to want.'''
st.download_button('Download sample text file', text_contents)

st.write('download corpus: http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz')

uploaded_file = st.file_uploader("Upload text files", accept_multiple_files=True)
uploaded_file_2 = st.file_uploader("Upload corpus")

#--------------------------------------------------------------------------------------

book_num = st.text_input("input book numbers from corpus divided by ':'", key = '1')
book_nums = book_num.split(':')

#--------------------------------------------------------------------------------------

all_text = []


def get():
    if uploaded_file is not None and uploaded_file_2 is not None:
        for i in range(0, len(uploaded_file)):
            stringio = StringIO(uploaded_file[i].getvalue().decode("utf-8"))
            string_data = stringio.read()
            trimmed_poems =  re.sub("[\n0-9]", "", string_data)
            text = trimmed_poems.split(',')
            all_text.extend([text])

        all_lines = []
        for line in gzip.open(uploaded_file_2):
            all_lines.append(json.loads(line.strip()))
        a = len(all_lines)
        text = []
        for i in range(0,a):
            each_line =  all_lines[i]
            dict_items = each_line.items()

            for b in range(0, len(book_nums)):
                if list(dict_items)[1] ==  ('gid', book_nums[b]):
                    text.append(each_line.get('s'))
        all_text.extend(text)
        return all_text

    elif uploaded_file is not None and uploaded_file_2 is None:
        for i in range(0, len(uploaded_file)):
            stringio = StringIO(uploaded_file[i].getvalue().decode("utf-8"))
            string_data = stringio.read()
            trimmed_poems =  re.sub("[\n0-9]", "", string_data)
            text = trimmed_poems.split(',')
            all_text.extend([text])
        return all_text

    elif uploaded_file_2 is not None and uploaded_file is None:
        all_lines = []
        for line in gzip.open(uploaded_file_2):
            all_lines.append(json.loads(line.strip()))
        a = len(all_lines)
        text = []
        for i in range(0,a):
            each_line =  all_lines[i]
            dict_items = each_line.items()

            for b in range(0, len(book_nums)):
                if list(dict_items)[1] ==  ('gid', book_nums[b]):
                    text.append(each_line.get('s'))
        all_text.extend(text)
        return all_text
    
    else:
        st.markdown("no files uploaded")


#--------------------------------------------------------------------------------------

def result(C):
    lower_text = str(C).lower()
    no_punc_lower_text = re.sub('[\{\}\/?.,;:|\)*~`!^\-_+<>@\#$%&\\=\(\'\"]', ' ', lower_text)
    text_analysis = TextBlob(no_punc_lower_text)

    words_num = len(text_analysis.words)

    sent = text_analysis.sentiment

    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = text_analysis.words
    trimmed_text = []
    for w in word_tokens:
        if w not in stop_words:
            trimmed_text.append(w)
    trimmed_text_analysis = TextBlob(str(trimmed_text))
    # wordcount = trimmed_text_analysis.word_counts
    trimmed_word_tokens = trimmed_text_analysis.words

    c = dict(text_analysis.tags)
    d = c.values()
    text_pos = list(d)
    adjv = ((text_pos.count('JJ') + text_pos.count('JJR') + text_pos.count('JJS') + text_pos.count('RB') + text_pos.count('RBR') + text_pos.count('RBS'))/words_num)*100

    may_count = text_analysis.word_counts['may']
    might_count = text_analysis.word_counts['might']
    can_count = text_analysis.word_counts['can']
    could_count = text_analysis.word_counts['could']
    would_count = text_analysis.word_counts['would']
    should_count = text_analysis.word_counts['should']
    will_count = text_analysis.word_counts['will']
    must_count = text_analysis.word_counts['must']

    modal_1 = ((may_count + might_count)/words_num)*100
    modal_2 = ((can_count + could_count)/words_num)*100
    modal_3 = ((would_count + should_count)/words_num)*100
    modal_4 = (will_count/words_num)*100
    modal_5 = (must_count/words_num)*100

    wh_word = ((text_pos.count('WDT') + text_pos.count('WP') + text_pos.count('WP$') + text_pos.count('WRB'))/words_num)*100

    not_count = text_analysis.word_counts['not']
    nt_count = text_analysis.word_counts["n't"]
    none_count = text_analysis.word_counts['none']
    nothing_count = text_analysis.word_counts['nothing']
    nobody_count = text_analysis.word_counts['nobody']
    nowhere_count = text_analysis.word_counts['nowhere']
    nor_count = text_analysis.word_counts['nor']
    neither_count = text_analysis.word_counts['neither']

    neg_word = ((not_count + nt_count + none_count + nothing_count + nobody_count + nowhere_count + nor_count + neither_count)/words_num)*100


    from collections import defaultdict
    by_rhyming_part = defaultdict(lambda: defaultdict(list))

    for i in range(0, len(trimmed_word_tokens)):
        match = re.search(r'(\b\w+\b)\W*$', trimmed_word_tokens[i])
        if match:
            last_word = match.group()
            pronunciations = pronouncing.phones_for_word(last_word)
            if len(pronunciations) > 0:
                rhyming_part = pronouncing.rhyming_part(pronunciations[0])
                by_rhyming_part[rhyming_part][last_word.lower()].append(trimmed_word_tokens[i])

    rhyme_groups = [group for group in by_rhyming_part.values() if len(group) >= 4]

    rhyme = (len(rhyme_groups) / words_num)*100

    df = pd.DataFrame([
            {"분석요소": "감정(polarity)", "result" : sent[0]},
            {"분석요소": "감정(subjectivity)", "result" : sent[1]},
            {"분석요소": "형용사/부사", "result": adjv},
            {"분석요소": "조동사(약한)", "result": modal_1},
            {"분석요소": "조동사(조금 약한)", "result": modal_2},
            {"분석요소": "조동사(중간)", "result": modal_3},
            {"분석요소": "조동사(조금 강한)", "result": modal_4},
            {"분석요소": "조동사(강한)", "result": modal_5},
            {"분석요소": "WH-word", "result": wh_word},
            {"분석요소": "negative word", "result": neg_word},
            {"분석요소": "rhyme groups", "result": rhyme},
            ])
    st.data_editor(df)

#--------------------------------------------------------------------------------------

get_from = st.button('see results', key = 11)

if get_from == True:
    all_text = get()
    result(all_text)


reset_button = st.button('reset', key = 12)

if reset_button == True:
    all_text = []
