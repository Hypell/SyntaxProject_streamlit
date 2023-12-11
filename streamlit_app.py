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

st.divider()

text_contents_1 = '''On Hellespont, guilty of true love's blood,
In view and opposite two cities stood,
Sea-borderers, disjoin'd by Neptune's might;
The one Abydos, the other Sestos hight.
At Sestos Hero dwelt; Hero the fair,
Whom young Apollo courted for her hair,
And offer'd as a dower his burning throne,
Where she should sit, for men to gaze upon.
The outside of her garments were of lawn,
The lining purple silk, with gilt stars drawn;
Her wide sleeves green, and border'd with a grove,
Where Venus in her naked glory strove
To please the careless and disdainful eyes
Of proud Adonis, that before her lies;
Her kirtle blue, whereon was many a stain,
Made with the blood of wretched lovers slain.
Upon her head she ware a myrtle wreath,
From whence her veil reach'd to the ground beneath:
Her veil was artificial flowers and leaves,
Whose workmanship both man and beast deceives:
Many would praise the sweet smell as she past,
When 'twas the odour which her breath forth cast;
And there for honey bees have sought in vain,
And, beat from thence, have lighted there again.
About her neck hung chains of pebble-stone,
Which, lighten'd by her neck, like diamonds shone.
She ware no gloves; for neither sun nor wind
Would burn or parch her hands, but, to her mind,
Or warm or cool them, for they took delight
To play upon those hands, they were so white.
Buskins of shell, all silver'd, used she,
And branch'd with blushing coral to the knee;
Where sparrows perch'd, of hollow pearl and gold,
Such as the world would wonder to behold:
Those with sweet water oft her handmaid fills,
Which, as she went, would cherup through the bills.
Some say, for her the fairest Cupid pin'd,
And, looking in her face, was strooken blind.
But this is true; so like was one the other,
As he imagin'd Hero was his mother;
And oftentimes into her bosom flew,
About her naked neck his bare arms threw,
And laid his childish head upon her breast,
And, with still panting rock, there took his rest.
So lovely-fair was Hero, Venus' nun,
As Nature wept, thinking she was undone,
Because she took more from her than she left,
And of such wondrous beauty her bereft:
Therefore, in sign her treasure suffer'd wrack,
Since Hero's time hath half the world been black.
  Amorous Leander, beautiful and young,
(Whose tragedy divine Musæus sung,)
Dwelt at Abydos; since him dwelt there none
For whom succeeding times make greater moan.
His dangling tresses, that were never shorn,
Had they been cut, and unto Colchos borne,
Would have allur'd the venturous youth of Greece
To hazard more than for the golden fleece.
Fair Cynthia wish'd his arms might be her sphere;
Grief makes her pale, because she moves not there.
His body was as straight as Circe's wand;
Jove might have sipt out nectar from his hand.
Even as delicious meat is to the tast,
So was his neck in touching, and surpast
The white of Pelops' shoulder: I could tell ye,
How smooth his breast was, and how white his belly;
And whose immortal fingers did imprint
That heavenly path with many a curious dint
That runs along his back; but my rude pen
Can hardly blazon forth the loves of men,
Much less of powerful gods: let it suffice
That my slack Muse sings of Leander's eyes;
Those orient cheeks and lips, exceeding his
That leapt into the water for a kiss
Of his own shadow, and, despising many,
Died ere he could enjoy the love of any.
Had wild Hippolytus Leander seen,
Enamour'd of his beauty had he been:
His presence made the rudest peasant melt,
That in the vast uplandish country dwelt;
The barbarous Thracian soldier, mov'd with nought,
Was mov'd with him, and for his favour sought.
Some swore he was a maid in man's attire,
For in his looks were all that men desire,--
A pleasant-smiling cheek, a speaking eye,
A brow for love to banquet royally;
And such as knew he was a man, would say,
"Leander, thou art made for amorous play:
Why art thou not in love, and lov'd of all?
Though thou be fair, yet be not thine own thrall."
  The men of wealthy Sestos every year,
For his sake whom their goddess held so dear,
Rose-cheek'd Adonis, kept a solemn feast:
Thither resorted many a wandering guest
To meet their loves: such as had none at all,
Came lovers home from this great festival;
For every street, like to a firmament,
Glister'd with breathing stars, who, where they went,
Frighted the melancholy earth, which deem'd
Eternal heaven to burn, for so it seem'd,
As if another Phaëton had got
The guidance of the sun's rich chariot.
But, far above the loveliest, Hero shin'd,
And stole away th' enchanted gazer's mind;
For like sea nymphs' inveigling harmony,
So was her beauty to the standers by;
Nor that night-wandering, pale, and watery star
(When yawning dragons draw her thirling car
From Latmus' mount up to the gloomy sky,
Where, crown'd with blazing light and majesty,
She proudly sits) more over-rules the flood
Than she the hearts of those that near her stood.
Even as when gaudy nymphs pursue the chase,
Wretched Ixion's shaggy-footed race,
Incens'd with savage heat, gallop amain
From steep pine-bearing mountains to the plain,
So ran the people forth to gaze upon her,
And all that view'd her were enamour'd on her:
And as in fury of a dreadful fight,
Their fellows being slain or put to flight,
Poor soldiers stand with fear of death dead-strooken,
So at her presence all surpris'd and tooken,
Await the sentence of her scornful eyes;
He whom she favours lives; the other dies:
There might you see one sigh; another rage;
And some, their violent passions to assuage
Compile sharp satires; but, alas, too late!
For faithful love will never turn to hate;
And many, seeing great princes were denied,
Pin'd as they went, and thinking on her died.
On this feast-day,--O cursed day and hour!--
Went Hero thorough Sestos, from her tower
To Venus' temple, where unhappily,
As after chanc'd, they did each other spy.
So fair a church as this had Venus none:
The walls were of discolour'd jasper-stone,
Wherein was Proteus carv'd; and over-head
A lively vine of green sea-agate spread,
Where by one hand light-headed Bacchus hung,
And with the other wine from grapes out-wrung.
Of crystal shining fair the pavement was;
The town of Sestos call'd it Venus' glass:
There might you see the gods, in sundry shapes,
Committing heady riots, incest, rapes;
For know, that underneath this radiant flour
Was Danäe's statue in a brazen tower;
Jove slily stealing from his sister's bed,
To dally with Idalian Ganymed,
And for his love Europa bellowing loud,
And tumbling with the Rainbow in a cloud;
Blood-quaffing Mars heaving the iron net
Which limping Vulcan and his Cyclops set;
Love kindling fire, to burn such towns as Troy;
Silvanus weeping for the lovely boy
That now is turn'd into a cypress-tree,
Under whose shade the wood-gods love to be.
And in the midst a silver altar stood:
There Hero, sacrificing turtle's blood,
Vail'd to the ground, veiling her eyelids close;
And modestly they open'd as she rose:
Thence flew Love's arrow with the golden head;
And thus Leander was enamoured.
Stone-still he stood, and evermore he gaz'd,
Till with the fire, that from his countenance blaz'd,
Relenting Hero's gentle heart was strook:
Such force and virtue hath an amorous look.
  It lies not in our power to love or hate,
For will in us is over-rul'd by fate.
When two are stript long ere the course begin,
We wish that one should lose, the other win;
And one especially do we affect
Of two gold ingots, like in each respect:
The reason no man knows; let it suffice,
What we behold is censur'd by our eyes.
Where both deliberate, the love is slight:
Who ever lov'd, that lov'd not at first sight?
  He kneel'd; but unto her devoutly pray'd:
Chaste Hero to herself thus softly said,
"Were I the saint he worships, I would hear him;"
And, as she spake those words, came somewhat near him.
He started up; she blush'd as one asham'd;
Wherewith Leander much more was inflam'd.
He touch'd her hand; in touching it she trembled:
Love deeply grounded, hardly is dissembled.
These lovers parled by the touch of hands:
True love is mute, and oft amazed stands.
Thus while dumb signs their yielding hearts entangled,
The air with sparks of living fire was spangled;
And Night, deep-drench'd in misty Acheron,
Heav'd up her head, and half the world upon
Breath'd darkness forth (dark night is Cupid's day):
And now begins Leander to display
Love's holy fire, with words, with sighs, and tears;
Which, like sweet music, enter'd Hero's ears;
And yet at every word she turn'd aside,
And always cut him off, as he replied.
At last, like to a bold sharp sophister,
With cheerful hope thus he accosted her.
"Fair creature, let me speak without offence:
I would my rude words had the influence
To lead thy thoughts as thy fair looks do mine!
Then shouldst thou be his prisoner, who is thine.
Be not unkind and fair; mis-shapen stuff
Are of behaviour boisterous and rough.
O, shun me not, but hear me ere you go!
God knows, I cannot force love as you do:
My words shall be as spotless as my youth,
Full of simplicity and naked truth.
This sacrifice, whose sweet perfume descending
From Venus' altar, to your footsteps bending,
Doth testify that you exceed her far,
To whom you offer, and whose nun you are.
Why should you worship her? her you surpass
As much as sparkling diamons flaring glass.
A diamond set in lead his worth retains;
A heavenly nymph, belov'd of human swains,
Receives no blemish, but oftimes more grace;
Which makes me hope, although I am but base,
Base in respect of thee divine and pure,
Dutiful service may thy love procure;
And I in duty will excel all other,
As thou in beauty dost exceed Love's mother.
Nor heaven nor thou were made to gaze upon:
As heaven preserves all things, so save thou one.
A stately builded ship, well rigg'd and tall,
The ocean maketh more majestical:
Why vow'st thou, then, to live in Sestos here,
Who on Love's seas more glorious wouldst appear?
Like untun'd golden strings all women are,
Which long time lie untouch'd, will harshly jar.
Vessels of brass, oft handed, brightly shine:
What difference betwixt the richest mine
And basest mould, but use? for both, not us'd,
Are of like worth.  Then treasure is abus'd,
When misers keep it: being put to loan,
In time it will return us two for one.
Rich robes themselves and others do adorn;
Neither themselves nor others, if not worn.
Who builds a palace, and rams up the gate,
Shall see it ruinous and desolate:
Ah, simple Hero, learn thyself to cherish!
Lone women, like to empty houses, perish.
Less sins the poor rich man, that starves himself
In heaping up a mass of drossy pelf,
Than such as you: his golden earth remains,
Which, after his decease, some other gains;
But this fair gem, sweet in the loss alone,
When you fleet hence, can be bequeath'd to none;
Or, if it could, down from th' enamell'd sky
All heaven would come to claim this legacy,
And with intestine broils the world destroy,
And quite confound Nature's sweet harmony.
Well therefore by the gods decreed it is,
We human creatures should enjoy that bliss.
One is no number; maids are nothing, then,
Without the sweet society of men.
Wilt thou live single still? one shalt thou be,
Though never singling Hymen couple thee.
Wild savages, that drink of running springs,
Think water far excels all earthly things;
But they, that daily taste neat wine, despise it:
Virginity, albeit some highly prize it,
Compar'd with marriage, had you tried them both,
Differs as much as wine and water doth.
Base bullion for the stamp's sake we allow:
Even so for men's impression do we you;
By which alone, our reverend fathers say,
Women receive perfection every way.
This idol, which you term virginity,
Is neither essence subject to the eye,
No, nor to any one exterior sense,
Nor hath it any place of residence,
Nor is't of earth or mould celestial,
Or capable of any form at all.
Of that which hath no being, do not boast:
Things that are not at all, are never lost.
Men foolishly do call it virtuous:
What virtue is it, that is born with us?
Much less can honour be ascrib'd thereto:
Honour is purchas'd by the deeds we do
Believe me, Hero, honour is not won,
Until some honourable deed be done.
Seek you, for chastity, immortal fame,
And know that some have wrong'd Diana's name?
Whose name is it, if she be false or not,
So she be fair, but some vile tongues will blot?
But you are fair, ay me! so wondrous fair,
So young, so gentle, and so debonair,
As Greece will think, if thus you live alone,
Some one or other keeps you as his own.
Then, Hero, hate me not, nor from me fly,
To follow swiftly blasting imfamy.
Perhaps thy sacred priesthood makes thee loath:
Tell me, to whom mad'st thou that heedless oath?"
"To Venus," answer'd she; and, as she spake,
Forth from those two tralucent cisterns brake
A stream of liquid pearl, which down her face
Made milk-white paths, whereon the gods might trace
To Jove's high court.  He thus replied: "The rites
In which love's beauteous empress most delights,
Are banquets, Doric music, midnight revel,
Plays, masks, and all that stern age counteth evil.
Thee as a holy idiot doth she scorn;
For thou, in vowing chastity, hast sworn
To rob her name and honour, and thereby
Committ'st a sin far worse than perjury,
Even sacrilege against her deity,
Through regular and formal purity.
To expiate which sin, kiss and shake hands:
Such sacrifice as this Venus demands."
Thereat she smil'd, and did deny him so,
As put thereby, yet might he hope for mo;
Which makes him quickly reinforce his speech,
And her in humble manner thus beseech:
"Though neither gods nor men may thee deserve,
Yet for her sake, whom you have vow'd to serve,
Abandon fruitless cold virginity.
The gentle queen of love's sole enemy.
Then shall you most resemble Venus' nun,
When Venus' sweet rites are perform'd and done.
Flint breasted Pallas joys in single life;
But Pallas and your mistress are at strife.
Love, Hero, then, and be not tyrannous;
But heal the heart that thou hast wounded thus;
Nor stain thy youthful years with avarice:
Fair fools delight to be accounted nice.
The richest corn dies, if it be not reapt;
Beauty alone is lost, too warily kept."
These arguments he us'd, and many more;
Wherewith she yielded, that was won before.
Hero's looks yielded, but her words made war:
Women are won when they begin to jar.
Thus, having swallow'd Cupid's golden hook,
The more she striv'd, the deeper was she strook:
Yet, evilly feigning anger, strove she still,
And would be thought to grant against her will.
So having paus'd a while, at last she said,
"Who taught thee rhetoric to deceive a maid?
Ay me! such words as these should I abhor,
And yet I like them for the orator."
With that, Leander stoop'd to have embrac'd her,
But from his spreading arms away she cast her,
And thus bespake him:  "Gentle youth, forbear
To touch the sacred garments which I wear.
Upon a rock, and underneath a hill,
Far from the town, (where all is whist and still,
Save that the sea, playing on yellow sand,
Sends forth a rattling murmur to the land,
Whose sound allures the golden Morpheus
In silence of the night to visit us,)
My turret stands; and there, God knows, I play
With Venus' swans and sparrows all the day.
A dwarfish beldam bears me company,
That hops about the chamber where I lie,
And spends the night, that might be better spent,
In vain discourse and apish merriment:--
Come thither."  As she spake this, her tongue tripp'd,
For unawares, "Come thither," from her slipp'd;
And suddenly her former colour chang'd,
And here and there her eyes through anger rang'd;
And, like a planet moving several ways
At one self instant, she, poor soul, assays,
Loving, not to love at all, and every part
Strove to resist the motions of her heart:
And hands so pure, so innocent, nay, such
As might have made Heaven stoop to have a touch,
Did she uphold to Venus, and again
Vow'd spotless chastity; but all in vain;
Cupid beats down her prayers with his wings;
Her vows about the empty air he flings:
All deep enrag'd, his sinewy bow he bent,
And shot a shaft that burning from him went;
Wherewith she strooken, look'd so dolefully,
As made Love sigh to see his tyranny;
And, as she wept, her tears to pearl he turn'd,
And wound them on his arm, and for her mourn'd.
Then towards the palace of the Destinies,
Laden with languishment and grief, he flies,
And to those stern nymphs humbly made request,
Both might enjoy each other, and be blest.
But with a ghastly dreadful countenance,
Threatening a thousand deaths at every glance,
They answer'd Love, nor would vouchsafe so much
As one poor word, their hate to him was such:
Hearken a while, and I will tell you why.
  Heaven's winged herald, Jove-born Mercury,
The self-same day that he asleep had laid
Enchanted Argus, spied a country maid,
Whose careless hair, instead of pearl t'adorn it,
Glister'd with dew, as one that seem'd to scorn it;
Her breath as fragrant as the morning rose;
Her mind pure, and her tongue untaught to glose:
Yet proud she was (for lofty Pride that dwells
In towered courts, is oft in shepherds' cells),
And too-too well the fair vermilion knew
And silver tincture of her cheeks, that drew
The love of every swain.  On her this god
Enamour'd was, and with his snaky rod
Did charm her nimble feet, and made her stay,
The while upon a hillock down he lay,
And sweetly on his pipe began to play,
And with smooth speech her fancy to assay,
Till in his twining arms her lock'd her fast,
And then he woo'd with kisses; and at last,
As shepherds do, her on the ground he laid,
And, tumbling in the grass, he often stray'd
Beyond the bounds of shame, in being bold
To eye those parts which no eye should behold;
And, like an insolent commanding lover,
Boasting his parentage, would needs discover
The way to new Elysium.  But she,
Whose only dower was her chastity,
Having striven in vain, was now about to cry,
And crave the help of shepherds that were nigh.
Herewith he stay'd his fury, and began
To give her leave to rise: away she ran;
After went Mercury, who us'd such cunning,
As she, to hear his tale, left off her running;
(Maids are not won by brutish force and might
But speeches full of pleasure, and delight;)
And, knowing Hermes courted her, was glad
That she such loveliness and beauty had
As could provoke his liking; yet was mute,
And neither would deny nor grant his suit.
Still vow'd he love: she, wanting no excuse
To feed him with delays, as women use,
Or thirsting after immortality,
(All women are ambitious naturally,)
Impos'd upon her lover such a task,
As he ought not perform, nor yet she ask;
A draught of flowing nectar she requested,
Wherewith the king of gods and men is feasted.
He, ready to accomplish what she will'd,
Stole some from Hebe (Hebe Jove's cup fill'd),
And gave it to his simple rustic love:
Which being known,--as what is hid from Jove?--
He inly storm'd, and wax'd more furious
Than for the fire filch'd by Prometheus;
And thrusts him down from heaven.  He, wandering here,
In mournful terms, with sad and heavy cheer,
Complain'd to Cupid: Cupid, for his sake,
To be reveng'd on Jove did undertake;
And those on whom heaven, earth, and hell relies,
I mean the adamantine Destinies,
He wounds with love, and forc'd them equally
To dote upon deceitful Mercury.
They offer'd him the deadly fatal knife
That shears the slender threads of human life;
At his fair feather'd feet the engines laid,
Which th' earth from ugly Chaos' den upweigh'd.
These he regarded not; but did entreat
That Jove, usurper of his father's seat,
Might presently be banish'd into hell,
And aged Saturn in Olympus dwell.
They granted what he crav'd; and once again
Saturn and Ops began their golden reign:
Murder, rape, war, and lust, and treachery,
Were with Jove clos'd in Stygian empery.
But long this blessed time continu'd not:
As soon as he his wished purpose got,
He, reckless of his promise, did despise
The love of th' everlasting Destinies.
They, seeing it, both Love and him abhorr'd,
And Jupiter unto his place restor'd:
And, but that learning, in despite of Fate,
Will amount aloft, and enter heaven-gate,
And to the seat of Jove itself advance,
Hermes had slept in hell with Ignorance.
Yet, as a punishment, they added this,
That he and Poverty should always kiss
And to this day is every scholar poor:
Gross gold from them runs headlong to the boor.
Likewise the angry Sisters, thus deluded,
To venge themselves on Hermes, have concluded
That Midas' brood shall sit in Honour's chair,
To which the Muses' sons are only heir;
And fruitful wits, that inaspiring are,
Shall discontent run into regions far;
And few great lords in virtuous deeds shall joy
But be surpris'd with every garish toy,
And still enrich the lofty servile clown,
Who with encroaching guile keeps learning down.
Then muse not Cupid's suit no better sped,
Seeing in their loves the Fates were injured.

By this, sad Hero, with love unacquainted,
Viewing Leander's face, fell down and fainted.
He kiss'd her, and breath'd life into her lips;
Wherewith, as one displeas'd, away she trips;
Yet, as she went, full often look'd behind,
And many poor excuses did she find
To linger by the way, and once she stay'd,
And would have turn'd again, but was afraid,
In offering parley, to be counted light:
So on she goes, and, in her idle flight,
Her painted fan of curled plumes let fall,
Thinking to train Leander therewithal.
He, being a novice, knew not what she meant,
But stay'd, and after her a letter sent;
Which joyful Hero answer'd in such sort,
As he had hoped to scale the beauteous fort
Wherein the liberal Graces lock'd their wealth;
And therefore to her tower he got by stealth.
Wide-open stood the door; he need not climb;
And she herself, before the pointed time,
Had spread the board, with roses strew'd the room,
And oft look'd out, and mus'd he did not come.
At last he came: O, who can tell the greeting
These greedy lovers had at their first meeting?
He ask'd; she gave; and nothing was denied;
Both to each other quickly were affied:
Look how their hands, so were their hearts united,
And what he did, she willingly requited.
(Sweet are the kisses, the embracements sweet,
When like desires and like affections meet;
For from the earth to heaven is Cupid rais'd,
Where fancy is in equal balance pais'd.)
Yet she this rashness suddenly repented,
And turn'd aside, and to herself lamented,
As if her name and honour had been wrong'd,
By being possess'd of him for whom she long'd;
Ay, and she wish'd, albeit not from her heart,
That he would leave her turret and depart.
The mirthful god of amorous pleasure smil'd
To see how he this captive nymph beguil'd;
For hitherto he did but fan the fire,
And kept it down, that it might mount the higher.
Now wax'd she jealous lest his love abated,
Fearing her own thoughts made her to be hated.
Therefore unto him hastily she goes,
And, like light Salmacis, her body throws
Upon his bosom, where with yielding eyes
She offers up herself a sacrifice
To slake his anger, if he were displeas'd:
O, what god would not therewith be appeas'd?
Like Æsop's cock, this jewel he enjoy'd,
And as a brother with his sister toy'd,
Supposing nothing else was to be done,
Now he her favour and goodwill had won.
But know you not that creatures wanting sense,
By nature have a mutual appetence,
And, wanting organs to advance a step,
Mov'd by love's force, unto each other lep?
Much more in subjects having intellect
Some hidden influence breeds like effect.
Albeit Leander, rude in love and raw,
Long dallying with Hero, nothing saw
That might delight him more, yet he suspected
Some amorous rites or other were neglected.
Therefore unto his body hers he clung:
She, fearing on the rushes to be flung,
Striv'd with redoubled strength; the more she striv'd,
The more a gentle pleasing heat reviv'd,
Which taught him all that elder lovers know;
And now the same gan so to scorch and glow,
As in plain terms, yet cunningly, he crave it:
Love always makes those eloquent that have it.
She, with a kind of granting, put him by it,
And ever, as he thought himself most nigh it,
Like to the tree of Tantalus, she fled,
And, seeming lavish, sav'd her maidenhead.
Ne'er king more sought to keep his diadem,
Than Hero this inestimable gem:
Above our life we love a steadfast friend;
Yet when a token of great worth we send,
We often kiss it, often look thereon,
And stay the messenger that would be gone;
No marvel, then, though Hero would not yield
So soon to part from that she dearly held:
Jewels being lost are found again; this never;
'Tis lost but once, and once lost, lost for ever.
  Now had the Morn espied her lover's steeds;
Whereat she starts, puts on her purple weeds,
And, red for anger that he stay'd so long,
All headlong throws herself the clouds among.
And now Leander, fearing to be miss'd,
Embrac'd her suddenly, took leave, and kiss'd:
Long was he taking leave, and loathe to go,
And kiss'd again, as lovers use to do.
Sad Hero wrung him by the hand, and wept,
Saying, "Let your vows and promises be kept":
Then standing at the door, she turn'd about,
As loathe to see Leander going out.
And now the sun, that through th' horizon peeps,
As pitying these lovers, downward creeps;
So that in silence of the cloudy night,
Though it was morning, did he take his flight.
But what the secret trusty night conceal'd,
Leander's amorous habit soon reveal'd:
With Cupid's myrtle was his bonnet crown'd,
About his arms the purple riband wound,
Wherewith she wreath'd her largely-spreading hair;
Nor could the youth abstain, but he must wear
The sacred ring wherewith she was endow'd,
When first religious chastity she vow'd;
Which made his love through Sestos to be known,
And thence unto Abydos sooner blown
Than he could sail; for incorporeal Fame,
Whose weight consists in nothing but her name,
Is swifter than the wind, whose tardy plumes
Are reeking water and dull earthly fumes.
  Home when he came, he seem'd not to be there,
But, like exiled air thrust from his sphere,
Set in a foreign place; and straight from thence,
Alcides-like, by mighty violence,
He would have chas'd away the swelling main,
That him from her unjustly did detain.
Like as the sun in a diameter
Fires and inflames objects removed far,
And heateth kindly, shining laterally;
So beauty sweetly quickens when 'tis nigh,
But being separated and remov'd,
Burns where it cherish'd, murders where it lov'd.
Therefore even as an index to a book,
So to his mind was young Leander's look.
O, none but gods have power their love to hide!
Affection by the countenance is descried;
The light of hidden fire itself discovers,
And love that is conceal'd betrays poor lovers.
His secret flame apparently was seen:
Leander's father knew where he had been,
And for the same mildly rebuk'd his son,
Thinking to quench the sparkles new-begun.
But love resisted once, grows passionate,
And nothing more than counsel lovers hate;
For as a hot proud horse highly disdains
To have his head controll'd, but breaks the reins,
Spits forth the ringled bit, and with his hoves
Checks the submissive ground; so he that loves,
The more he is restrain'd, the worse he fares:
What is it now but mad Leander dares?
"O Hero, Hero!" thus he cried full oft;
And then he got him to a rock aloft,
Where having spied her tower, long star'd he on't,
And pray'd the narrow toiling Hellespont
To part in twain, that he might come and go;
But still the rising billows answer'd, "No."
With that, he stripp'd him to the ivory skin,
And, crying, "Love, I come," leap'd lively in:
Whereat the sapphire-visag'd god grew proud,
And made his capering Triton sound aloud,
Imagining that Ganymede, displeas'd,
Had left the heavens; therefore on him he seiz'd.
Leander striv'd; the waves about him wound,
And pull'd him to the bottom, where the ground
Was strew'd with pearl, and in low coral groves
Sweet-singing mermaids sported with their loves
On heaps of heavy gold, and took great pleasure
To spurn in careless sort the shipwreck treasure;
For here the stately azure palace stood,
Where kingly Neptune and his train abode.
The lusty god embrac'd him, call'd him "love,"
And swore he never should return to Jove:
But when he knew it was not Ganymed,
For under water he was almost dead,
He heav'd him up, and, looking on his face,
Beat down the bold waves with his triple mace,
Which mounted up, intending to have kiss'd him.
And fell in drops like tears because they miss'd him.
Leander, being up, began to swim,
And, looking back, saw Neptune follow him:
Whereat aghast, the poor soul gan to cry,
"O, let me visit Hero ere I die!"
The god put Helle's bracelet on his arm,
And swore the sea should never do him harm.
He clapp'd his plump cheeks, with his tresses play'd,
And, smiling wantonly, his love bewray'd;
He watch'd his arms, and, as they open'd wide
At every stroke, betwixt them would he slide,
And steal a kiss, and then run out and dance,
And, as he turn'd, cast many a lustful glance,
And throw him gaudy toys to please his eye,
And dive into the water, and there pry
Upon his breast, his thighs, and every limb,
And up again, and close beside him swim,
And talk of love.  Leander made reply,
"You are deceiv'd; I am no woman, I."
Thereat smil'd Neptune, and then told a tale,
How that a shepherd, sitting in a vale,
Play'd with a boy so lovely-fair and kind,
As for his love both earth and heaven pin'd;
That of the cooling river durst not drink,
Lest water-nymphs should pull him from the brink;
And when he sported in the fragrant lawns,
Goat-footed Satyrs and up-staring Fauns
Would steal him thence.  Ere half this tale was done,
"Ay me," Leander cried, "th' enamour'd sun,
That now should shine on Thetis' glassy bower,
Descends upon my radiant Hero's tower:
O, that these tardy arms of mine were wings!"
And, as he spake, upon the waves he springs.
Neptune was angry that he gave no ear,
And in his heart revenging malice bare:
He flung at him his mace; but, as it went,
He call'd it in, for love made him repent:
The mace, returning back, his own hand hit,
As meaning to be veng'd for darting it.
When this fresh-bleeding wound Leander view'd,
His colour went and came, as if he ru'd
The grief which Neptune felt: in gentle breasts
Relenting thoughts, remorse, and pity rests;
And who have hard hearts and obdurate minds,
But vicious, hare-brain'd, and illiterate hinds?
The god, seeing him with pity to be mov'd,
Thereon concluded that he was belov'd;
(Love is too full of faith, too credulous,
With folly and false hope deluding us;)
Wherefore, Leander's fancy to surprise,
To the rich ocean for gifts he flies;
'Tis wisdom to give much; a gilt prevails
When deep-persuading oratory fails.
  By this, Leander, being near the land,
Cast down his weary feet, and felt the sand.
Breathless albeit he were, he rested not
Till to the solitary tower he got;
And knock'd, and call'd: at which celestial noise
The longing heart of Hero much more joys,
Than nymphs and shepherds when the timbrel rings,
Or crooked dolphin when the sailor sings.
She stay'd not for her robes, but straight arose,
And, drunk with gladness, to the door she goes;
Where seeing a naked man, she screech'd for fear,
(Such sights as this to tender maids are rare,)
And ran into the dark herself to hide
(Rich jewels in the dark are soonest spied).
Unto her was he led, or rather drawn
By those white limbs which sparkled through the lawn.
The nearer that he came, the more she fled,
And, seeking refuge, slipt into her bed;
Whereon Leander sitting, thus began,
Through numbing cold, all feeble, faint, and wan.
"If not for love, yet, love, for pity-sake,
Me in thy bed and maiden bosom take;
At least vouchsafe these arms some little room,
Who, hoping to embrace thee, cheerly swoom:
This head was beat with many a churlish billow,
And therefore let it rest upon thy pillow."
Herewith affrighted, Hero shrunk away,
And in her lukewarm place Leander lay;
Whose lively heat, like fire from heaven fet,
Would animate gross clay, and higher set
The drooping thoughts of base-declining souls,
Than dreary-Mars-carousing nectar bowls.
His hands he cast upon her like a snare:
She, overcome with shame and sallow fear,
Like chaste Diana when Actæon spied her,
Being suddenly betray'd, div'd down to hide her;
And, as her silver body downward went,
With both her hands she made the bed a tent,
And in her own mind thought herself secure,
O'ercast with dim and darksome coverture.
And now she lets him whisper in her ear,
Flatter, entreat, promise, protest, and swear:
Yet ever, as he greedily assay'd
To touch those dainties, she the harpy play'd,
And every limb did, as a soldier stout,
Defend the fort, and keep the foeman out;
For though the rising ivory mount he scal'd,
Which is with azure circling lines empal'd.
Much like a globe (a globe may I term this,
By which Love sails to regions full of bliss,)
Yet there with Sisyphus he toil'd in vain,
Till gentle parley did the truce obtain.
Even as a bird, which in our hands we wring,
Forth plungeth, and oft flutters with her wing,
She trembling strove: this strife of hers, like that
Which made the world, another world begat
Of unknown joy.  Treason was in her thought,
And cunningly to yield herself she sought.
Seeming not won, yet won she was at length:
In such wars women use but half their strength.
Leander now, like Theban Hercules,
Enter'd the orchard of th' Hesperides;
Whose fruit none rightly can describe, but he
That pulls or shakes it from the golden tree.
Wherein Leander, on her quivering breast,
Breathless spoke something, and sigh'd out the rest;
Which so prevail'd, as he, with small ado,
Enclos'd her in his arms, and kiss'd her too:
And every kiss to her was as a charm,
And to Leander as a fresh alarm:
So that the truce was broke, and she, alas,
Poor silly maiden, at his mercy was.
Love is not full of pity, as men say,
But deaf and cruel where he means to prey.
  And now she wish'd this night were never done,
And sigh'd to think upon th' approaching sun;
For much it griev'd her that the bright day-light
Should know the pleasure of this blessed night,
And them, like Mars and Erycine, display
Both in each other's arms chain'd as they lay.
Again, she knew not how to frame her look,
Or speak to him, who in a moment took
That which so long, so charily she kept;
And fain by stealth away she would have crept,
And to some corner secretly have gone,
Leaving Leander in the bed alone.
But as her naked feet were whipping out,
He on the sudden cling'd her so about,
That, mermaid-like, unto the floor she slid;
One half appear'd the other half was hid.
Thus near the bed she blushing stood upright,
And from her countenance behold ye might
A kind of twilight break, which through the air,
As from an orient cloud, glimps'd here and there;
And round about the chamber this false morn
Brought forth the day before the day was born.
So Hero's ruddy cheek Hero betray'd,
And her all naked to his sight display'd:
Whence his admiring eyes more pleasure took
Than Dis, on heaps of gold fixing his look.
By this, Apollo's golden harp began
To sound forth music to the ocean;
Which watchful Hesperus no sooner heard,
But he the bright Day-bearing car prepar'd,
And ran before, as harbinger of light,
And with his flaring beams mock'd ugly Night
Till she, o'ercome with anguish, shame, and rage,
Dang'd down to hell her loathsome carriage.


COME live with me, and be my love;
And we will all the pleasures prove
That hills and valleys, dales and fields,
Woods or steepy mountain yields.

And we will sit upon the rocks,
Seeing the shepherds feed their flocks
By shallow rivers, to whose falls
Melodious birds sing madrigals.

And I will make thee beds of roses,
And a thousand fragrant posies;
A cap of flowers, and a kirtle
Embroider'd all with leaves of myrtle

A gown made of the finest wool
Which from our pretty lambs we pull;
Fair-lined slippers for the cold,
With buckles of the purest gold;

A belt of straw and ivy-buds,
With coral clasps and amber studs:
An if these pleasures may thee move,
Come live with me, and be my love.

The shepherd-swains shall dance and sing
For thy delight each May morning:
If these delights thy mind may move,
Then live with me, and be my love.


I WALK'D along a stream, for pureness rare,
  Brighter than sun-shine; for it did acquaint
The dullest sight with all the glorious prey
That in the pebble-paved channel lay.

No molten crystal, but a richer mine,
  Even Nature's rarest alchymy ran there,--
Diamonds resolv'd, and substance more divine,
  Through whose bright-gliding current might appear
A thousand naked nymphs, whose ivory shine,
  Enamelling the banks, made them more dear
Than ever was that glorious palace' gate
Where the day-shining Sun in triumph sate.

Upon this brim the eglantine and rose,
  The tamarisk, olive, and the almond tree,
As kind companions, in one union grows,
  Folding their twining arms, as oft we see
Turtle-taught lovers either other close,
  Lending to dulness feeling sympathy;
And as a costly valance o'er a bed,
So did their garland-tops the brook o'erspread.

Their leaves, that differ'd both in shape and show,
  Though all were green, yet difference such in green,
Like to the checker'd bent of Iris' bow,
  Prided the running main, as it had been--
   '''
text_contents_2 = '''
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



st.download_button('Download sample text file : Christopher Marlowe', text_contents_1)
st.download_button('Download sample text file : Ben Jonson', text_contents_2)

st.write('download corpus: http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz')

st.divider()

uploaded_file = st.file_uploader("Upload text files", accept_multiple_files=True)

st.divider()

uploaded_file_2 = st.file_uploader("Upload corpus")

book_num = st.text_input("input book numbers from corpus divided by ':'", key = '1')

book_nums = book_num.split(':')

st.divider()

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
