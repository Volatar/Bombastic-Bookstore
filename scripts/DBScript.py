import re
import sqlite3

text = """Title: The Fault in Our Stars
Author: John Green
Categories: Young Adult Fiction
Genres: Young Adult Fiction
Publisher: Turtleback Books
Publish Date: 2012-01-01
ISBN: 9780804171083
Price: $7.27

Quantity: 4
---------------------------------------------

Title: Divergent
Author: Veronica Roth
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: RBA
Publish Date: 2011 
ISBN: 0008167907
Price: $23.78

Quantity: 5
---------------------------------------------

Title: Pride and Prejudice
Author: Jane Austen
Categories: British and irish fiction (fictional works by one author)
Genres: British and irish fiction (fictional works by one author)
Publisher: Createspace Independent Publishing Platform
Publish Date: March 31, 2004
ISBN: 9798404259933
Price: $10.69

Quantity: 13
---------------------------------------------

Title: 1984 (adaptation)
Author: Michael Dean, George Orwell
Categories: Totalitarianism
Genres: Totalitarianism
Publisher: Pearson Education ESL
Publish Date: 2011
ISBN: 9780582777316
Price: $23.81

Quantity: 18
---------------------------------------------

Title: The Kite Runner
Author: Khaled Hosseini
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: 10|18
Publish Date: 2008
ISBN: 9781594489600
Price: $16.93

Quantity: 16
---------------------------------------------

Title: The Fellowship of the Ring
Author: J.R.R. Tolkien
Categories: Elves
Genres: Elves
Publisher: "ĖKSMO-Press"
Publish Date: Mar 31, 2002
ISBN: 0008108293
Price: $22.99

Quantity: 14
---------------------------------------------

Title: The Lovely bones
Author: Alice Sebold
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: Recorded Books
Publish Date: 2003
ISBN: 160024842X
Price: $11.75

Quantity: 16
---------------------------------------------

Title: Gone Girl
Author: Gillian Flynn
Categories: FICTION / Mystery & Detective / General
Genres: FICTION / Mystery & Detective / General
Publisher: Orion Publishing Group, Limited
Publish Date: Jul 21, 2014
ISBN: 9788580572902
Price: $22.42

Quantity: 11
---------------------------------------------

Title: The Help
Author: Kathryn Stockett
Categories: novels
Genres: novels
Publisher: Maeva
Publish Date: 2011
ISBN: 1440697655
Price: $20.18

Quantity: 5
---------------------------------------------

Title: Of Mice and Men
Author: John Steinbeck
Categories: contemporary fiction
Genres: contemporary fiction
Publisher: Bantam Books
Publish Date: 2018-07-11
ISBN: 079281715X
Price: $24.52

Quantity: 15
---------------------------------------------

Title: The Alchemist
Author: Paulo Coelho
Categories: Translations into Indonesian
Genres: Translations into Indonesian
Publisher: Can Yayınları
Publish Date: November 1, 2005
ISBN: 9780062502537
Price: $13.97

Quantity: 14
---------------------------------------------

Title: Fifty Shades of Grey
Author: E. L. James
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: 
Publish Date:  2012.
ISBN: 8804632534
Price: $8.90

Quantity: 18
---------------------------------------------

Title: The Girl on the Train
Author: Paula Hawkins
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: Oberon Books, Limited
Publish Date: 2015
ISBN: 9781594634024
Price: $14.60

Quantity: 15
---------------------------------------------

Title: The Book Thief
Author: Markus Zusak
Categories: nyt:young-adult-paperback-monthly=2022-09-04
Genres: nyt:young-adult-paperback-monthly=2022-09-04
Publisher: Turtleback Books
Publish Date: 2007-09
ISBN: 9781407036908
Price: $13.58

Quantity: 15
---------------------------------------------

Title: Little Women
Author: Louisa May Alcott
Categories: Romans
Genres: Romans
Publisher: Simon & Schuster Children's Publishing
Publish Date: 2011
ISBN: 1490352171
Price: $22.63

Quantity: 13
---------------------------------------------

Title: Eat, Pray, Love
Author: Elizabeth Gilbert
Categories: Viajes
Genres: Viajes
Publisher: Aguilar
Publish Date: 2004
ISBN: 0747582882
Price: $15.20

Quantity: 15
---------------------------------------------

Title: Water for Elephants
Author: Sara Gruen, David LeDoux, John Randolph Jones
Categories: fiction
Genres: fiction
Publisher: Algonquin Paperbacks
Publish Date: May 9, 2007
ISBN: 1606860968
Price: $18.21

Quantity: 20
---------------------------------------------

Title: The Notebook
Author: Nicholas Sparks
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: December 2001
ISBN: 0553816713
Price: $14.35

Quantity: 20
---------------------------------------------

Title: Life of Pi
Author: Yann Martel
Categories: Teenage boys
Genres: Teenage boys
Publisher: Turtleback Books
Publish Date: May 01, 2003
ISBN: 3100478258
Price: $7.26

Quantity: 17
---------------------------------------------

Title: The hitchhiker's guide to the galaxy
Author: John Carnell
Categories: Science fiction comic books, strips
Genres: Science fiction comic books, strips
Publisher: iBooks
Publish Date: 1997
ISBN: 1596875860
Price: $7.22

Quantity: 16
---------------------------------------------

Title: Wuthering Heights
Author: Emily Brontë
Categories: British and irish fiction (fictional works by one author)
Genres: British and irish fiction (fictional works by one author)
Publisher: Createspace Independent Publishing Platform
Publish Date: 1910?
ISBN: 9798720739973
Price: $21.85

Quantity: 15
---------------------------------------------

Title: Where the Sidewalk Ends
Author: Shel Silverstein
Categories: Humorous poetry
Genres: Humorous poetry
Publisher: HarperCollins Publishers
Publish Date: 2004
ISBN: 0060586532
Price: $7.58

Quantity: 1
---------------------------------------------

Title: The Perks of Being a Wallflower
Author: Stephen Chbosky
Categories: Young adult fiction
Genres: Young adult fiction
Publisher: Turtleback Books
Publish Date: Sep 02, 2015
ISBN: 9781439122433
Price: $5.68

Quantity: 20
---------------------------------------------

Title: Insurgent
Author: Veronica Roth, Gemme
Categories: Future
Genres: Future
Publisher: RBA
Publish Date: 2016
ISBN: 8851121117
Price: $6.94

Quantity: 3
---------------------------------------------

Book The Curious Incident of the Dog in the Night-Time by Mark Haddon (2003) not found on Open Library.Title: Gone With the Wind
Author: Margaret Mitchell
Categories: survival
Genres: survival
Publisher: In the future,
Publish Date: 1947
ISBN: 9578477198
Price: $14.56

Quantity: 6
---------------------------------------------

Title: Frankenstein or The Modern Prometheus
Author: Mary Wollstonecraft Shelley
Categories: Frankenstein (Fictitious character)
Genres: Frankenstein (Fictitious character)
Publisher: Dell Publishing Company
Publish Date: February 1, 2008
ISBN: 1973472341
Price: $18.14

Quantity: 10
---------------------------------------------

Title: My Sister's Keeper
Author: Jodi Picoult
Categories: Jodi Picoult
Genres: Jodi Picoult
Publisher: Recorded Books
Publish Date: March 2019
ISBN: 9780340837740
Price: $22.42

Quantity: 15
---------------------------------------------

Title: A Thousand Splendid Suns
Author: Khaled Hosseini
Categories: desertion
Genres: desertion
Publisher: Hayakawa Shobō
Publish Date: Oct 01, 2008
ISBN: 8777149912
Price: $11.58

Quantity: 2
---------------------------------------------

Title: The Shining
Author: Stephen King
Categories: Fiction
Genres: Fiction
Publisher: Debolsillo
Publish Date: Sep 09, 2007
ISBN: 0451078721
Price: $6.31

Quantity: 20
---------------------------------------------

Title: The Maze Runner
Author: James Dashner
Categories: Fiction
Genres: Fiction
Publisher: Chicken House Ltd
Publish Date: Oct 02, 2014
ISBN: 9780385737944
Price: $10.03

Quantity: 19
---------------------------------------------

Title: Holes
Author: Louis Sachar
Categories: Newbery Medal
Genres: Newbery Medal
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: July 1, 2002
ISBN: 9780786261901
Price: $8.78

Quantity: 12
---------------------------------------------

Title: Sense and Sensibility
Author: Jane Austen
Categories: Fiction, Romance, Historical, Regency
Genres: Fiction, Romance, Historical, Regency
Publisher: State Street Press
Publish Date: June 16, 2005
ISBN: 1708343199
Price: $24.42

Quantity: 11
---------------------------------------------

Title: The Host
Author: Stephenie Meyer
Categories: Literature
Genres: Literature
Publisher: SPHERE
Publish Date: 2013
ISBN: 1600242707
Price: $14.64

Quantity: 5
---------------------------------------------

Title: Me Before You
Author: Jojo Moyes, Various
Categories: Young women
Genres: Young women
Publisher: DEBOLSILLO
Publish Date: Nov 02, 2014
ISBN: 0718184009
Price: $19.94

Quantity: 19
---------------------------------------------

Title: Bridget Jones's Diary
Author: Helen Fielding
Categories: single women
Genres: single women
Publisher: Huang guan wen hua chu ban you xian gong si
Publish Date: 2004
ISBN: 9780804193696
Price: $21.61

Quantity: 20
---------------------------------------------

Title: Miss Peregrine's Home for Peculiar Children
Author: Ransom Riggs, Jesse Bernstein
Categories: Orphanages
Genres: Orphanages
Publisher: Thorndike Press
Publish Date: 2011
ISBN: 9781594749025
Price: $6.82

Quantity: 14
---------------------------------------------

Title: The Picture of Dorian Gray
Author: Oscar Wilde
Categories: British and irish fiction (fictional works by one author)
Genres: British and irish fiction (fictional works by one author)
Publisher: Ibp Usa
Publish Date: Jan 08, 2017
ISBN: 9798553093693
Price: $20.52

Quantity: 7
---------------------------------------------

Title: The Secret Garden
Author: Frances Hodgson Burnett
Categories: Fiction, general
Genres: Fiction, general
Publisher: State Street Press
Publish Date: October 2002
ISBN: 1569874115
Price: $15.32

Quantity: 9
---------------------------------------------

Title: Into the Wild
Author: Erin Hunter
Categories: Cats
Genres: Cats
Publisher: 
Publish Date: 2016
ISBN: 9781538501436
Price: $12.92

Quantity: 12
---------------------------------------------

Title: The Glass Castle
Author: Jeannette Walls
Categories: Poor
Genres: Poor
Publisher: Hunan jiao yu chu ban she
Publish Date: 2006
ISBN: 9781417777891
Price: $18.10

Quantity: 2
---------------------------------------------

Title: The devil wears Prada
Author: Lauren Weisberger
Categories: Fashion editors
Genres: Fashion editors
Publisher: DeBolsillo
Publish Date: April 13, 2004
ISBN: 9780786255757
Price: $15.77

Quantity: 1
---------------------------------------------

Title: A Tale of Two Cities
Author: Charles Dickens
Categories: British
Genres: British
Publisher: State Street Press
Publish Date: February 1, 1948
ISBN: 9781590861523
Price: $21.11

Quantity: 20
---------------------------------------------

Title: Paper towns
Author: John Green
Categories: Fiction
Genres: Fiction
Publisher: AudioGO
Publish Date: 2016
ISBN: 846633534X
Price: $8.87

Quantity: 12
---------------------------------------------

Title: Allegiant
Author: Veronica Roth
Categories: dystopian
Genres: dystopian
Publisher: ADA
Publish Date: Apr 13, 2016
ISBN: 9780062024060
Price: $5.75

Quantity: 8
---------------------------------------------

Title: Steve Jobs
Author: Walter Isaacson
Categories: TECHNOLOGY & ENGINEERING / General
Genres: TECHNOLOGY & ENGINEERING / General
Publisher: LATTES
Publish Date: Sep 10, 2013
ISBN: 9783570101247
Price: $21.13

Quantity: 13
---------------------------------------------

Title: Bossypants
Author: Tina Fey
Categories: biography
Genres: biography
Publisher: Little, Brown & Company
Publish Date: 2013
ISBN: 9780316056892
Price: $17.11

Quantity: 6
---------------------------------------------

Title: City of Glass
Author: Cassandra Clare
Categories: Magic
Genres: Magic
Publisher: Margaret K. McElderry Books
Publish Date: 2009
ISBN: 1439158428
Price: $22.55

Quantity: 17
---------------------------------------------

Title: All the Light We Cannot See
Author: Anthony Doerr
Categories: Blind
Genres: Blind
Publisher: Suma
Publish Date: 2021
ISBN: 1476746583
Price: $9.04

Quantity: 12
---------------------------------------------

Title: The Princess Bride
Author: William Goldman
Categories: Castles
Genres: Castles
Publisher: Harcourt
Publish Date: October 20, 1999
ISBN: 9780747543220
Price: $6.81

Quantity: 4
---------------------------------------------

Title: Eleanor & Park
Author: Rainbow Rowell
Categories: Love & Romance
Genres: Love & Romance
Publisher: Jiangsu feng huang wen yi chu ban she
Publish Date: Jun 08, 2013
ISBN: 9780385368285
Price: $11.19

Quantity: 6
---------------------------------------------

Title: A Clash of Kings
Author: George R. R. Martin, George RR Martin
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Brand: Random House Audio
Publish Date: cop. 2012
ISBN: 0008322155
Price: $5.24

Quantity: 13
---------------------------------------------

Title: Fifty Shades Darker
Author: E. L. James
Categories: Sexual dominance and submission
Genres: Sexual dominance and submission
Publisher: 
Publish Date: Jan 03, 2017
ISBN: 9786050933406
Price: $8.10

Quantity: 5
---------------------------------------------

Title: Outlander
Author: Diana Gabaldon
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Random House Audio
Publish Date: october 2004
ISBN: 0440242940
Price: $9.44

Quantity: 15
---------------------------------------------

Title: The Count of Monte Cristo
Author: N/A
Categories: N/A
Genres: N/A
Publisher: Naxos AudioBooks
Publish Date: 2012
ISBN: 1986964337
Price: $22.13

Quantity: 16
---------------------------------------------

Title: The Adventures of Tom Sawyer
Author: Mark Twain
Categories: The Adventures of Tom Sawyer
Genres: The Adventures of Tom Sawyer
Publisher: nelson doubleday
Publish Date: May 1, 2001
ISBN: 9781690704119
Price: $19.85

Quantity: 14
---------------------------------------------

Title: Tuesdays with Morrie
Author: Mitch Albom
Categories: memoir
Genres: memoir
Publisher: Grupo Oceano
Publish Date: 2008
ISBN: 9785170602858
Price: $13.87

Quantity: 19
---------------------------------------------

Title: On the origin of species by means of natural selection
Author: Charles Darwin
Categories: Evolution
Genres: Evolution
Publisher: N. Zanichelli
Publish Date: September 25, 2003
ISBN: 0521867096
Price: $5.17

Quantity: 13
---------------------------------------------

Title: A Time to Kill
Author: John Grisham
Categories: african american girls
Genres: african american girls
Publisher: LA FACTORIA
Publish Date: 2004
ISBN: 0816155909
Price: $7.20

Quantity: 9
---------------------------------------------

Title: Thirteen reasons Why
Author: Jay Asher
Categories: Mystery
Genres: Mystery
Publisher: 
Publish Date: 2008
ISBN: 073935650X
Price: $9.41

Quantity: 2
---------------------------------------------

Title: Fifty Shades Freed
Author: E. L. James
Categories: Sexual dominance and submission
Genres: Sexual dominance and submission
Publisher: Windsor
Publish Date: Apr 14, 2013
ISBN: 9788804623250
Price: $18.20

Quantity: 17
---------------------------------------------

Title: One hundred years of solitude
Author: Regina Janes
Categories: N/A
Genres: N/A
Publisher: Twayne Publishers
Publish Date: 1991
ISBN: 9780805780383
Price: $6.44

Quantity: 2
---------------------------------------------

Title: A Room of One's Own
Author: Virginia Woolf
Categories: Authorship
Genres: Authorship
Publisher: Alianza
Publish Date: 1995
ISBN: 1095278886
Price: $10.57

Quantity: 13
---------------------------------------------

Title: Catch-22
Author: Joseph Heller
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Knopf
Publish Date: 1995
ISBN: 9785557018999
Price: $8.29

Quantity: 13
---------------------------------------------

Title: If I Stay
Author: Gayle Forman
Categories: Death
Genres: Death
Publisher: Speak
Publish Date: Mar 20, 2018
ISBN: 1984836501
Price: $22.37

Quantity: 11
---------------------------------------------

Title: The Grapes of Wrath
Author: John Steinbeck
Categories: Labor camps
Genres: Labor camps
Publisher: Ishi Press International
Publish Date: September 7, 2000
ISBN: 1440637121
Price: $8.19

Quantity: 6
---------------------------------------------

Title: On The Road
Author: Jack Kerouac
Categories: Beat generation
Genres: Beat generation
Publisher: Hunan literature and Art Publishing House
Publish Date: 1958
ISBN: 9780140182941
Price: $5.02

Quantity: 11
---------------------------------------------

Title: Les Misérables
Author: Victor Hugo
Categories: Poor
Genres: Poor
Publisher: T. Nelson and Sons
Publish Date: 1935
ISBN: 1117691306
Price: $23.50

Quantity: 10
---------------------------------------------

Title: Unbroken: A World War II Story of Survival, Resilience, and Redemption
Author: Laura Hillenbrand
Categories: Prisoners of war
Genres: Prisoners of war
Publisher: Random House Trade Paperbacks
Publish Date: Jul 29, 2014
ISBN: 0812974492
Price: $17.03

Quantity: 20
---------------------------------------------

Title: The Sea of Monsters
Author: Rick Riordan
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: Mar 27, 2013
ISBN: 9788364297007
Price: $17.58

Quantity: 12
---------------------------------------------

Title: American Gods
Author: Neil Gaiman, Mónica Faerna
Categories: science fiction
Genres: science fiction
Publisher: Roca Bolsillo
Publish Date: 2008
ISBN: 0062059882
Price: $7.98

Quantity: 1
---------------------------------------------

Title: The Martian Chronicles
Author: Ray Bradbury
Categories: American Science fiction
Genres: American Science fiction
Publisher: Booket
Publish Date: 1990
ISBN: 0380973839
Price: $14.40

Quantity: 1
---------------------------------------------

Title: Five Children and It
Author: Edith Nesbit
Categories: Fiction
Genres: Fiction
Publisher: Lulu.com
Publish Date: October 2002
ISBN: 9781513269726
Price: $14.01

Quantity: 7
---------------------------------------------

Title: Freakonomics
Author: Steven D. Levitt, Stephen J. Dubner, Andrea Montero Cusset
Categories: Economics
Genres: Economics
Publisher: Zeta Editores
Publish Date: Aug 29, 2007
ISBN: 8901065223
Price: $16.90

Quantity: 3
---------------------------------------------

Title: The Battle of the Labyrinth
Author: Rick Riordan
Categories: Greek mythology in fiction
Genres: Greek mythology in fiction
Publisher: Hyperion Books for Children 
Publish Date: Jun 27, 2010
ISBN: 1439578796
Price: $9.06

Quantity: 14
---------------------------------------------

Title: Anne of Green Gables
Author: Lucy Maud Montgomery
Categories: Country life
Genres: Country life
Publisher: Lulu.com
Publish Date: May 1, 2001
ISBN: 9788308045336
Price: $17.65

Quantity: 10
---------------------------------------------

Title: Confessions of a Shopaholic, Shopaholic Takes Manhattan, and Shopaholic Ties the Knot (Shopaholic Series, Books 1, 2, & 3)
Author: Sophie Kinsella
Categories: Humorous stories
Genres: Humorous stories
Publisher: Dial Press Trade Paperbacks
Publish Date: 2001
ISBN: 9780385335485
Price: $7.42

Quantity: 17
---------------------------------------------

Title: A walk to remember
Author: Nicholas Sparks
Categories: Fiction
Genres: Fiction
Publisher: Warner Books
Publish Date: September 1, 2004
ISBN: 0552209066
Price: $14.90

Quantity: 4
---------------------------------------------

Title: Matched (Matched Trilogy, Book 1)
Author: Ally Condie
Categories: Young adult fiction
Genres: Young adult fiction
Publisher: penguin audio
Publish Date: November 30, 2010
ISBN: 9780142419779
Price: $22.74

Quantity: 20
---------------------------------------------

Title: The Two Towers
Author: J.R.R. Tolkien
Categories: Ents
Genres: Ents
Publisher: Harper Collins Publishers
Publish Date: 2002 October 21
ISBN: 9788385100089
Price: $17.21

Quantity: 10
---------------------------------------------

Title: Dune
Author: Frank Herbert
Categories: Dune (Imaginary place)
Genres: Dune (Imaginary place)
Publisher: Debolsillo
Publish Date: April 1, 1982
ISBN: 9780425064344
Price: $12.03

Quantity: 19
---------------------------------------------

Title: A Storm of Swords
Author: George R. R. Martin
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Lao Động
Publish Date: July 31, 2006
ISBN: 8496208982
Price: $6.03

Quantity: 13
---------------------------------------------

Title: The Sisterhood of the Traveling Pants (Sisterhood of the Traveling Pants Series, Book 1)
Author: Ann Brashares
Categories: Best friends
Genres: Best friends
Publisher: Delacorte Press
Publish Date: April 2005
ISBN: 9780385729338
Price: $15.40

Quantity: 2
---------------------------------------------

Title: Before I Fall
Author: Lauren Oliver
Categories: Fiction
Genres: Fiction
Publisher: Carlsen
Publish Date: 2010
ISBN: 9780061987496
Price: $8.13

Quantity: 17
---------------------------------------------

Title: The Tipping Point
Author: Malcolm Gladwell
Categories: Contagion (Social psychology)
Genres: Contagion (Social psychology)
Publisher: Wheeler Pub.
Publish Date: February 1, 2007
ISBN: 9780316316965
Price: $10.09

Quantity: 7
---------------------------------------------

Title: Lolita
Author: Vladimir Nabokov
Categories: erotic fiction
Genres: erotic fiction
Publisher: Vintage International
Publish Date: Mar 20, 1989
ISBN: 9780241953242
Price: $23.96

Quantity: 12
---------------------------------------------

Title: The Return of the King
Author: J.R.R. Tolkien
Categories: Elves
Genres: Elves
Publisher: Martins Fontes
Publish Date: Aug 11, 2008
ISBN: 9505471165
Price: $22.30

Quantity: 3
---------------------------------------------

Title: The Titan's Curse
Author: Rick Riordan
Categories: nyt:series_books=2007-07-21
Genres: nyt:series_books=2007-07-21
Publisher: Miramax Books and Hyperion Books for Children
Publish Date: Jul 01, 2015
ISBN: 9782019109974
Price: $24.38

Quantity: 1
---------------------------------------------

Title: Me Talk Pretty One Day
Author: David Sedaris
Categories: David Sedaris
Genres: David Sedaris
Publisher: G.K. Hall
Publish Date: October 18, 2000
ISBN: 8497934903
Price: $6.43

Quantity: 7
---------------------------------------------

Title: Charlie and the Chocolate Factory
Author: Roald Dahl
Categories: Childrens Media Tie-In Books
Genres: Childrens Media Tie-In Books
Publisher: The piffin book
Publish Date: February 1, 2007
ISBN: 9780141319643
Price: $20.88

Quantity: 8
---------------------------------------------

Title: The last Olympian
Author: Robert Venditti, Orpheus Collar
Categories: Children's fiction
Genres: Children's fiction
Publisher: Disney-Hyperion
Publish Date: 2019
ISBN: 153645768X
Price: $17.25

Quantity: 15
---------------------------------------------

Title: The Pillars of the Earth
Author: Ken Follett
Categories: White Ship
Genres: White Ship
Publisher: Plaza & Janes Editores, S.A.
Publish Date: 1998-12
ISBN: 9783896045591
Price: $24.76

Quantity: 15
---------------------------------------------

Title: Girl with a Pearl Earring
Author: Tracy Chevalier
Categories: Artists' models
Genres: Artists' models
Publisher: HarperCollins
Publish Date: October 2003
ISBN: 0452287022
Price: $7.90

Quantity: 6
---------------------------------------------

Title: One Flew Over the Cuckoo's Nest
Author: Ken Kesey
Categories: Allegories
Genres: Allegories
Publisher: Wydawnictwo Albatros Andrzej Kuryłowicz
Publish Date: March 6, 2002
ISBN: 9780451137098
Price: $17.45

Quantity: 1
---------------------------------------------

Title: Something Wicked This Way Comes
Author: Ray Bradbury
Categories: Boys
Genres: Boys
Publisher: Knopf
Publish Date: Mar 12, 1969
ISBN: 9780246637628
Price: $11.50

Quantity: 11
---------------------------------------------

Title: Emma
Author: Jane Austen
Categories: Social life and customs
Genres: Social life and customs
Publisher: Hyde Park Editions Limited
Publish Date: 1981-03
ISBN: 1556850050
Price: $14.81

Quantity: 4
---------------------------------------------

Title: Middlesex
Author: Jeffrey Eugenides
Categories: Intersexuality
Genres: Intersexuality
Publisher: Audio Renaissance
Publish Date: 2015
ISBN: 2823617965
Price: $17.64

Quantity: 16
---------------------------------------------

Title: Cinder
Author: Marissa Meyer
Categories: Wealth
Genres: Wealth
Publisher: Perfection Learning
Publish Date: 2017
ISBN: 9781466800113
Price: $23.15

Quantity: 10
---------------------------------------------

Title: The Goldfinch
Author: Donna Tartt
Categories: goldfinch
Genres: goldfinch
Publisher: Little, Brown and Company
Publish Date: Jun 28, 2016
ISBN: 8817072389
Price: $23.97

Quantity: 3
---------------------------------------------

Title: The Name of the Wind
Author: Patrick Rothfuss
Categories: orphans
Genres: orphans
Publisher: Debolsillo
Publish Date: 2009
ISBN: 2352942837
Price: $10.26

Quantity: 8
---------------------------------------------

Title: The Lost Hero
Author: Rick Riordan
Categories: nyt:chapter_books=2010-11-06
Genres: nyt:chapter_books=2010-11-06
Publisher: Hyperion Books for Children
Publish Date: 2016
ISBN: 9785699503315
Price: $19.35

Quantity: 11
---------------------------------------------

Title: The Night Circus
Author: Erin Morgenstern
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Random House, Incorporated
Publish Date: Feb 21, 2012
ISBN: 1616577886
Price: $8.46

Quantity: 17
---------------------------------------------

Title: The Memory Keeper's Daughter
Author: Kim Edwards
Categories: women
Genres: women
Publisher: LGF
Publish Date: 2015
ISBN: 9780143037149
Price: $7.60

Quantity: 17
---------------------------------------------

Title: Ready Player One
Author: Ernest Cline, Arnaud Regnauld
Categories: Regression (Civilization)
Genres: Regression (Civilization)
Publisher: Broadway
Publish Date: Jun 05, 2012
ISBN: 8466663061
Price: $22.35

Quantity: 2
---------------------------------------------

Title: A Game of Thrones / A Clash of Kings / A Storm of Swords / A Feast of Crows / A Dance with Dragons
Author: George R. R. Martin
Categories: Comics & graphic novels, fantasy
Genres: Comics & graphic novels, fantasy
Publisher: Bantam
Publish Date: Oct 29, 2013
ISBN: 9780345535528
Price: $11.84

Quantity: 11
---------------------------------------------

Title: Anna Karenina
Author: Lev Nikolaevič Tolstoy
Categories: Fiction
Genres: Fiction
Publisher: Pravda
Publish Date: February 1, 2007
ISBN: 9780736639866
Price: $11.81

Quantity: 11
---------------------------------------------

Title: Deception Point
Author: Dan Brown
Categories: mystery fiction
Genres: mystery fiction
Publisher: ACT
Publish Date: 2011
ISBN: 3404770579
Price: $21.94

Quantity: 2
---------------------------------------------

Title: The Firm
Author: John Grisham
Categories: Certified Public Accountants
Genres: Certified Public Accountants
Publisher: Izd-vo AST
Publish Date: 2011
ISBN: 0375433465
Price: $13.62

Quantity: 16
---------------------------------------------

Title: The Stand
Author: Stephen King
Categories: suspense & thriller
Genres: suspense & thriller
Publisher: LATTES
Publish Date: 2002?
ISBN: 9783404134113
Price: $15.02

Quantity: 12
---------------------------------------------

Title: The Wonderful Wizard of Oz
Author: L. Frank Baum
Categories: Witches
Genres: Witches
Publisher: Bungāh-i Nashr-i Andīshah
Publish Date: November 2006
ISBN: 9781091421547
Price: $9.02

Quantity: 17
---------------------------------------------

Title: Big Little Lies
Author: Liane Moriarty
Categories: Suburbs
Genres: Suburbs
Publisher: PENGUIN
Publish Date: 2015
ISBN: 9781405916363
Price: $24.85

Quantity: 11
---------------------------------------------

Title: A Clockwork Orange
Author: Anthony Burgess
Categories: bible
Genres: bible
Publisher: Tandem Library
Publish Date: Jan 06, 2011
ISBN: 9783453130791
Price: $23.05

Quantity: 3
---------------------------------------------

Title: Hush, hush
Author: Becca Fitzpatrick
Categories: Fiction
Genres: Fiction
Publisher: Simon & Schuster
Publish Date: 2010
ISBN: 1416989412
Price: $12.34

Quantity: 17
---------------------------------------------

Title: The Ugly Duckling
Author: Hans Christian Andersen
Categories: Ducklings
Genres: Ducklings
Publisher: Childs World
Publish Date: 1982
ISBN: 9997745795
Price: $5.84

Quantity: 14
---------------------------------------------

Title: L'Éducation sentimentale
Author: Gustave Flaubert
Categories: Fiction
Genres: Fiction
Publisher: Alianza
Publish Date: July 1998
ISBN: 9781613824443
Price: $10.96

Quantity: 18
---------------------------------------------

Title: Crime and Punishment
Author: Фёдор Михайлович Достоевский
Categories: N/A
Genres: N/A
Publisher: CreateSpace Independent Publishing Platform
Publish Date: Mar 24, 2016
ISBN: 9798671990980
Price: $18.01

Quantity: 8
---------------------------------------------

Title: Matilda
Author: Roald Dahl
Categories: juvenile fiction
Genres: juvenile fiction
Publisher: imusti
Publish Date: 1990
ISBN: 9780141311364
Price: $8.09

Quantity: 1
---------------------------------------------

Title: Beautiful Creatures (Beautiful Creatures Series, Book 1)
Author: Kami Garcia, Margaret Stohl
Categories: Dreams
Genres: Dreams
Publisher: Little, Brown and Co.
Publish Date: 2009
ISBN: 9780316071284
Price: $23.09

Quantity: 17
---------------------------------------------

Title: Divine Secrets of the Ya-Ya Sisterhood
Author: Rebecca Wells
Categories: Fiction
Genres: Fiction
Publisher: Perennial
Publish Date: Mar 16, 1998
ISBN: 9780060759957
Price: $9.10

Quantity: 19
---------------------------------------------

Title: Digital Fortress
Author: Dan Brown
Categories: techno-thriller
Genres: techno-thriller
Publisher: Corgi Books
Publish Date: June 15, 2006
ISBN: 9788467219142
Price: $13.53

Quantity: 10
---------------------------------------------

Title: Dear John
Author: Nicholas Sparks
Categories: Long-distance relationships
Genres: Long-distance relationships
Publisher: Warner Books Large Print
Publish Date: 2007
ISBN: 9781594837920
Price: $7.67

Quantity: 8
---------------------------------------------

Title: Vampire Academy
Author: Richelle Mead
Categories: Kings, queens, rulers, etc. in fiction
Genres: Kings, queens, rulers, etc. in fiction
Publisher: Penguin USA, Inc.
Publish Date: August 16, 2007
ISBN: 1440675953
Price: $17.44

Quantity: 3
---------------------------------------------

Title: The Bell Jar
Author: Sylvia Plath
Categories: women college students
Genres: women college students
Publisher: Can Yayınları
Publish Date: 2009 November 3
ISBN: 9798354315864
Price: $21.88

Quantity: 14
---------------------------------------------

Title: Wild: A Journey from Lost to Found
Author: CHERYL STRAYED
Categories: Travel
Genres: Travel
Publisher: Atlantic Books
Publish Date: Apr 08, 2013
ISBN: 0857897756
Price: $21.65

Quantity: 16
---------------------------------------------

Title: The Shack
Author: William P. Young
Categories: Life change events
Genres: Life change events
Publisher: Euromedia Group
Publish Date: 2008
ISBN: 1935170031
Price: $22.61

Quantity: 17
---------------------------------------------

Title: Beautiful Disaster
Author: Jamie McGuire
Categories: collectionID:CDarkromance
Genres: collectionID:CDarkromance
Publisher: Simon & Schuster UK
Publish Date: Nov 27, 2012
ISBN: 9781471115042
Price: $15.63

Quantity: 14
---------------------------------------------

Title: The Red Tent
Author: Anita Diamant
Categories: Fiction
Genres: Fiction
Publisher: Large Print Press
Publish Date: December 2001
ISBN: 9781405005777
Price: $8.77

Quantity: 5
---------------------------------------------

Title: The last song
Author: Nicholas Sparks
Categories: Literature
Genres: Literature
Publisher: Grand Central Publishing
Publish Date: 2009
ISBN: 044655815X
Price: $15.70

Quantity: 7
---------------------------------------------

Title: Dead Until Dark (Sookie Stackhouse, #1)
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: Berkley Pub. Group
Publish Date: 2023
ISBN: 9781101146316
Price: $7.17

Quantity: 2
---------------------------------------------

Title: A Dance With Dragons
Author: George R. R. Martin
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Harper Collins
Publish Date: Apr 26, 2011
ISBN: 055338595X
Price: $7.22

Quantity: 3
---------------------------------------------

Title: The Immortal Life of Henrietta Lacks
Author: Rebecca Skloot
Categories: Cancer
Genres: Cancer
Publisher: PAN
Publish Date: Mar 08, 2011
ISBN: 9780230748699
Price: $5.21

Quantity: 8
---------------------------------------------

Title: Siddhartha
Author: Hermann Hesse
Categories: Alegorías
Genres: Alegorías
Publisher: Media Rodzina
Publish Date: 2011
ISBN: 1421805529
Price: $5.14

Quantity: 9
---------------------------------------------

Title: The Guernsey Literary and Potato Peel Pie Society
Author: Mary Ann Shaffe
Categories: Fiction
Genres: Fiction
Publisher: Bloomsbury Publishing
Publish Date: 2009
ISBN: 9781408803318
Price: $14.73

Quantity: 15
---------------------------------------------

Title: Something borrowed
Author: Emily Giffin
Categories: Single women
Genres: Single women
Publisher: Wheeler Publishing
Publish Date: 2011
ISBN: 9781597226028
Price: $21.63

Quantity: 2
---------------------------------------------

Title: Angela's Ashes
Author: Frank McCourt
Categories: Irish Americans
Genres: Irish Americans
Publisher: HarperCollins
Publish Date: November 30, 1999
ISBN: 0007117213
Price: $10.06

Quantity: 3
---------------------------------------------

Title: Persuasion
Author: Jane Austen
Categories: Fiction, Romance, Historical, Regency
Genres: Fiction, Romance, Historical, Regency
Publisher: Createspace Independent Publishing Platform
Publish Date: June 30, 2004
ISBN: 1674409257
Price: $5.33

Quantity: 19
---------------------------------------------

Title: Dark Places
Author: Gillian Flynn
Categories: Literature
Genres: Literature
Publisher: Turtleback Books
Publish Date: 2016-01-14
ISBN: 0307459926
Price: $21.52

Quantity: 8
---------------------------------------------

Title: Watchmen
Author: Alan Moore, Dave Gibbons, John Higgins
Categories: Watchmen (Comic strip)
Genres: Watchmen (Comic strip)
Publisher: Paw Prints 2008-04-18
Publish Date: 18/02/2009
ISBN: 0606357424
Price: $6.03

Quantity: 16
---------------------------------------------

Title: Fangirl
Author: Rainbow Rowell
Categories: Authorship
Genres: Authorship
Publisher: Alfaguara
Publish Date: 2015
ISBN: 153644961X
Price: $14.26

Quantity: 13
---------------------------------------------

Title: The Color Purple
Author: Alice Walker
Categories: Fiction & Literature
Genres: Fiction & Literature
Publisher: Washington Square Press published by Pocket Books
Publish Date: Jan 01, 2004
ISBN: 408760117X
Price: $6.06

Quantity: 15
---------------------------------------------

Title: One for the Money
Author: Janet Evanovich, Janet Evanovich
Categories: Women detectives
Genres: Women detectives
Publisher: H. Hamilton
Publish Date: 2049
ISBN: 9780061009051
Price: $17.25

Quantity: 17
---------------------------------------------

Title: Fallen Hearts
Author: V. C. Andrews
Categories: romance fiction
Genres: romance fiction
Publisher: Plaza & Janes Editores, S.A.
Publish Date: 2016
ISBN: 0002235404
Price: $14.54

Quantity: 13
---------------------------------------------

Title: The Gunslinger
Author: King, Stephen
Categories: succubus
Genres: succubus
Publisher: Berkley
Publish Date: Oct 05, 2003
ISBN: 1501143514
Price: $9.38

Quantity: 12
---------------------------------------------

Title: Interview with a Jewish Vampire
Author: Erica Manfred
Categories: N/A
Genres: N/A
Publisher: Fredonia Communications
Publish Date: Dec 18, 2011
ISBN: 9780971096813
Price: $18.44

Quantity: 7
---------------------------------------------

Title: The Nightingale
Author: Kristin Hannah
Categories: Civilians in war
Genres: Civilians in war
Publisher: St. Martin's Griffin
Publish Date: 2016-01-01
ISBN: 1509848622
Price: $19.78

Quantity: 4
---------------------------------------------

Title: Fight Club
Author: Chuck Palahniuk
Categories: Fiction
Genres: Fiction
Publisher: Owl Books
Publish Date: May 4, 2006
ISBN: 9780613918824
Price: $14.72

Quantity: 18
---------------------------------------------

Title: The Other Boleyn Girl
Author: Philippa Gregory
Categories: Mistresses
Genres: Mistresses
Publisher: Simon & Schuster
Publish Date: September 25, 2007
ISBN: 9781419329975
Price: $22.02

Quantity: 13
---------------------------------------------

Title: Sharp Objects
Author: Gillian Flynn
Categories: Fiction
Genres: Fiction
Publisher: Cengage Gale
Publish Date: 2008
ISBN: 0297851535
Price: $10.33

Quantity: 4
---------------------------------------------

Title: The Husband's Secret
Author: Liane Moriarty
Categories: Letters
Genres: Letters
Publisher: Penguin Books, Limited
Publish Date: 2014
ISBN: 0399159347
Price: $19.16

Quantity: 20
---------------------------------------------

Title: Bared to You
Author: Sylvia Day, Sylvia Day, Jill Redfield
Categories: Romance
Genres: Romance
Publisher: 
Publish Date: Dec 17, 2012
ISBN: 9780425276761
Price: $16.32

Quantity: 7
---------------------------------------------

Title: Marley and me
Author: Taylor, Don
Categories: Biography
Genres: Biography
Publisher: Barricade Books
Publish Date: 1995
ISBN: 1569800448
Price: $10.20

Quantity: 17
---------------------------------------------

Title: Throne of Glass
Author: Sarah J. Maas
Categories: Assassins
Genres: Assassins
Publisher: Bloomsbury usa
Publish Date: May 07, 2013
ISBN: 9789669824158
Price: $11.51

Quantity: 6
---------------------------------------------

Title: City of Fallen Angels
Author: Cassandra Clare
Categories: Magic
Genres: Magic
Publisher: Margraet K. McElderly Books
Publish Date: 2011
ISBN: 144240356X
Price: $8.22

Quantity: 14
---------------------------------------------

Title: Outliers
Author: Malcolm Gladwell
Categories: Psychology
Genres: Psychology
Publisher: Back Bay Books
Publish Date: 2011
ISBN: 014190349X
Price: $7.01

Quantity: 8
---------------------------------------------

Title: Blink
Author: Malcolm Gladwell
Categories: Intuition
Genres: Intuition
Publisher: Allen Lane
Publish Date: April 3, 2007
ISBN: 9780141014593
Price: $6.22

Quantity: 12
---------------------------------------------

Title: The Devil in the White City
Author: Erik Larson
Categories: Social life and customs
Genres: Social life and customs
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: February 2004
ISBN: 3502153957
Price: $18.85

Quantity: 7
---------------------------------------------

Title: Misery
Author: Stephen King, Stephen King
Categories: dope
Genres: dope
Publisher: Plaza & Janes Editores, S.A.
Publish Date: 2011 March
ISBN: 8466345256
Price: $7.29

Quantity: 6
---------------------------------------------

Title: The Red Thumb Mark
Author: R. Austin Freeman
Categories: Doctor Thorndyke (Fictitious character)
Genres: Doctor Thorndyke (Fictitious character)
Publisher: Aegypan
Publish Date: 1970
ISBN: 9798759415633
Price: $20.62

Quantity: 11
---------------------------------------------

Title: Shiver
Author: Maggie Stiefvater
Categories: Human-animal relationships
Genres: Human-animal relationships
Publisher: Scholastic
Publish Date: 2009
ISBN: 0545123267
Price: $7.34

Quantity: 8
---------------------------------------------

Title: The Silence of the Lambs
Author: Thomas Harris
Categories: lambs
Genres: lambs
Publisher: Ullstein Hörverlag
Publish Date: 1990 04
ISBN: 1585471100
Price: $8.33

Quantity: 7
---------------------------------------------

Title: The art of racing in the rain
Author: Garth Stein
Categories: Fiction
Genres: Fiction
Publisher: Harper
Publish Date: Sep 16, 2014
ISBN: 9780007281190
Price: $23.57

Quantity: 10
---------------------------------------------

Title: Atonement
Author: Ian McEwan
Categories: historical romance
Genres: historical romance
Publisher: Jonathan Cape
Publish Date: 2003-09
ISBN: 9780786239214
Price: $7.23

Quantity: 12
---------------------------------------------

Title: The Cuckoo's Calling
Author: J. K. Rowling
Categories: private investigators
Genres: private investigators
Publisher: Turtleback Books
Publish Date: Sep 22, 2014
ISBN: 0606361677
Price: $16.36

Quantity: 15
---------------------------------------------

Title: Inferno
Author: Dante Alighieri, Marcus Sanders, Doug Harvey
Categories: Poetry
Genres: Poetry
Publisher: NYRB Classics
Publish Date: Apr 02, 2014
ISBN: 9780007902095
Price: $7.96

Quantity: 3
---------------------------------------------

Title: An Abundance of Katherines
Author: John Green
Categories: Interpersonal relations, fiction
Genres: Interpersonal relations, fiction
Publisher: Nathan
Publish Date: 2019
ISBN: 9780525476887
Price: $21.97

Quantity: 13
---------------------------------------------

Title: The Ocean at the End of the Lane
Author: Neil Gaiman
Categories: Good and evil
Genres: Good and evil
Publisher: Buku Fixi (Fixi Verso)
Publish Date: 2016
ISBN: 0606385320
Price: $17.24

Quantity: 9
---------------------------------------------

Title: Bridge to Terabithia
Author: Katherine Paterson, Katherine Paterson
Categories: Amistad
Genres: Amistad
Publisher: Noguer
Publish Date: 1977
ISBN: 0786296208
Price: $8.17

Quantity: 5
---------------------------------------------

Title: Flowers for Algernon
Author: Daniel Keyes
Categories: institutionalization
Genres: institutionalization
Publisher: [publisher not identified]
Publish Date: 1966?
ISBN: 4151101012
Price: $24.97

Quantity: 11
---------------------------------------------

Title: Delirium
Author: Lauren Oliver
Categories: Science fiction
Genres: Science fiction
Publisher: HarperCollins
Publish Date: 2011
ISBN: 9780340980927
Price: $9.74

Quantity: 1
---------------------------------------------

Title: Red Queen
Author: Victoria Aveyard
Categories: Large type books
Genres: Large type books
Publisher: Orion Publishing Group, Limited
Publish Date: 2016
ISBN: 9781409176657
Price: $14.19

Quantity: 14
---------------------------------------------

Title: How to win friends and influence people
Author: Dale Carnegie
Categories: Succès
Genres: Succès
Publisher: Sovremennyĭ Literator
Publish Date: 1932
ISBN: 7547702430
Price: $15.88

Quantity: 17
---------------------------------------------

Title: The Scorch Trials
Author: James Dashner
Categories: Science fiction
Genres: Science fiction
Publisher: KaBOOM!
Publish Date: Jun 23, 2015
ISBN: 9780385907453
Price: $6.54

Quantity: 2
---------------------------------------------

Title: A Teacher's Guide to The Boy in the Striped Pajamas
Author: Greg Slingerland
Categories: N/A
Genres: N/A
Publisher: Lulu.com
Publish Date: Dec 05, 2015
ISBN: 1329739361
Price: $8.10

Quantity: 2
---------------------------------------------

Title: The 7 Habits of Highly Effective People
Author: Stephen R. Covey, Sean Covey
Categories: Success- Psychological aspects
Genres: Success- Psychological aspects
Publisher: Tian xia yuan jian chu ban
Publish Date: 2016
ISBN: 0684858398
Price: $22.16

Quantity: 2
---------------------------------------------

Title: Good Omens
Author: Neil Gaiman, Terry Pratchett
Categories: End of the world
Genres: End of the world
Publisher: Turtleback Books
Publish Date: February 28, 2006
ISBN: 9780061991127
Price: $18.12

Quantity: 17
---------------------------------------------

Title: Sarah's Key
Author: Tatiana de Rosnay
Categories: Vel' d'Hiv Roundup
Genres: Vel' d'Hiv Roundup
Publisher: Audiolib
Publish Date: 2006
ISBN: 9782350870458
Price: $13.40

Quantity: 18
---------------------------------------------

Title: Never Let Me Go
Author: Kazuo Ishiguro, Geoff Barton, Margaret Mulheran, Susan Elkin, Sue Bennett, Dave Stockwin, Anne Rabinovitch, Anne Rabinovitch, Anne Rabinovitch, Collins UK Staff, Collins GCSE Staff, David Sexton
Categories: Fiction
Genres: Fiction
Publisher: Retailer-exclusive titles
Publish Date: Apr 29, 2010
ISBN: 9781471853647
Price: $5.18

Quantity: 10
---------------------------------------------

Title: World War Z
Author: Max Brooks
Categories: Humor
Genres: Humor
Publisher: Turtleback Books
Publish Date: May 28, 2013
ISBN: 0307351939
Price: $19.21

Quantity: 6
---------------------------------------------

Title: East of Eden
Author: John Steinbeck
Categories: migrant labor
Genres: migrant labor
Publisher: Círculo de Lectores, S.A.
Publish Date: Feb 26, 1970
ISBN: 0749317744
Price: $21.62

Quantity: 14
---------------------------------------------

Title: The Mark of Athena
Author: Rick Riordan
Categories: Greek Gods
Genres: Greek Gods
Publisher: Vintage Espanol
Publish Date: 10/02/2012
ISBN: 9780141335766
Price: $14.94

Quantity: 10
---------------------------------------------

Title: The Graveyard Book
Author: Neil Gaiman
Categories: Fiction
Genres: Fiction
Publisher: Albin Michel Jeunesse
Publish Date: 2021
ISBN: 0061709123
Price: $16.25

Quantity: 3
---------------------------------------------

Title: Rebecca
Author: Daphne du Maurier
Categories: Married women
Genres: Married women
Publisher: Edicions 62
Publish Date: Nov 23, 2016
ISBN: 9789650303273
Price: $24.44

Quantity: 18
---------------------------------------------

Title: City of Lost Souls The Mortal Instruments Book 5
Author: Cassandra Clare
Categories: Magic
Genres: Magic
Publisher: Margaret K. McElderry Books
Publish Date: 2012
ISBN: 1442416866
Price: $20.01

Quantity: 20
---------------------------------------------

Title: The Bourne Identity
Author: Robert Ludlum
Categories: Jason Bourne (Fictitious character)
Genres: Jason Bourne (Fictitious character)
Publisher: Huang guan wen hua chu ban you xian gong si
Publish Date: May 1, 1983
ISBN: 0553242962
Price: $17.50

Quantity: 3
---------------------------------------------

Title: Shadow of the Wind
Author: Rachel Lawson
Categories: N/A
Genres: N/A
Publisher: Independently Published
Publish Date: 2018
ISBN: 1980296707
Price: $11.49

Quantity: 16
---------------------------------------------

Title: Legend
Author: Marie Lu
Categories: Criminals
Genres: Criminals
Publisher: Razorbill
Publish Date: Feb 01, 2012
ISBN: 9781101545959
Price: $22.06

Quantity: 14
---------------------------------------------

Title: We Were Liars
Author: E. Lockhart
Categories: Love
Genres: Love
Publisher: ReadHowYouWant.com, Limited
Publish Date: 2014
ISBN: 0385390092
Price: $17.73

Quantity: 9
---------------------------------------------

Title: A Man Called Ove
Author: N/A
Categories: N/A
Genres: N/A
Publisher: simon and Shuster
Publish Date: 2014
ISBN: N/A
Price: $20.22

Quantity: 6
---------------------------------------------

Book Is Everything Hanging Out Without Me? not found on Open Library.Title: Along Came a Spider
Author: James Patterson
Categories: Fiction
Genres: Fiction
Publisher: Little Brown & Company
Publish Date: August 1, 2003
ISBN: 9780759541528
Price: $23.76

Quantity: 6
---------------------------------------------

Title: The Rosie Project
Author: Graeme C. Simsion, Annette Hahn
Categories: Australia
Genres: Australia
Publisher: HarperCollins Publishers Ltd
Publish Date: May 21, 2013
ISBN: 8415630468
Price: $23.49

Quantity: 9
---------------------------------------------

Title: The Client
Author: John Grisham
Categories: suicide
Genres: suicide
Publisher: Island
Publish Date: Feb 01, 1993
ISBN: 9781407059013
Price: $9.57

Quantity: 2
---------------------------------------------

Title: The Son of Neptune
Author: Rick Riordan
Categories: Hera (Greek deity)
Genres: Hera (Greek deity)
Publisher: Turtleback Books
Publish Date: 2012
ISBN: 9780141370507
Price: $11.67

Quantity: 1
---------------------------------------------

Title: The Tales of Beedle the Bard
Author: J. K. Rowling
Categories: Magicians
Genres: Magicians
Publisher: Bloomsbury Publishing Plc
Publish Date: 2019
ISBN: 9789639884168
Price: $17.82

Quantity: 5
---------------------------------------------

Title: Love in the Time of Cholera
Author: Gabriel García Márquez
Categories: Fiction (fictional works by one author)
Genres: Fiction (fictional works by one author)
Publisher: N
Publish Date: N/A
ISBN: N/A
Price: $17.96

Quantity: 17
---------------------------------------------

Title: Extremely Loud and Incredibly Close
Author: Jonathan Safran Foer
Categories: Literature
Genres: Literature
Publisher: Houghton Mifflin Company
Publish Date: 2006
ISBN: 9785699538768
Price: $24.71

Quantity: 18
---------------------------------------------

Title: Neverwhere
Author: Neil Gaiman, Anthony Head, Benedict Cumberbatch, Christopher Lee, David Harewood, David Schofield, Full Cast, James McAvoy, Natalie Dormer, Sophie Okonedo
Categories: Fiction
Genres: Fiction
Publisher: Avon Books
Publish Date: Sep 26, 2017
ISBN: 9780062476371
Price: $21.69

Quantity: 6
---------------------------------------------

Title: The Nanny Diaries (Nanny #1)
Author: Emma McLaughlin, Emma Mclaughlin, Nicola Kraus
Categories: Rich people
Genres: Rich people
Publisher: Chivers Press
Publish Date: 2004
ISBN: 9780312278588
Price: $18.53

Quantity: 14
---------------------------------------------

Title: Treasure Island
Author: Robert Louis Stevenson
Categories: Fiction
Genres: Fiction
Publisher: Ferguson Publishing Company
Publish Date: December 28, 2004
ISBN: 9780786180417
Price: $20.63

Quantity: 12
---------------------------------------------

Title: 11/22/63
Author: Stephen King
Categories: Assassination
Genres: Assassination
Publisher: Luitingh
Publish Date: 2012
ISBN: 059331154X
Price: $24.27

Quantity: 10
---------------------------------------------

Title: A child called "it"
Author: David J. Pelzer
Categories: Biography
Genres: Biography
Publisher: Windsor
Publish Date: 2010
ISBN: 1841883093
Price: $17.59

Quantity: 10
---------------------------------------------

Title: A tree grows in Brooklyn
Author: Betty Smith
Categories: Teenage girls
Genres: Teenage girls
Publisher: Popular Library
Publish Date: Jan 18, 2005
ISBN: 0060736267
Price: $10.75

Quantity: 2
---------------------------------------------

Title: The light between oceans
Author: M. L. Stedman
Categories: Foundlings
Genres: Foundlings
Publisher: Black Swan
Publish Date: 2015
ISBN: 1594136327
Price: $8.87

Quantity: 2
---------------------------------------------

Title: Foundation
Author: Isaac Asimov
Categories: Psychohistory
Genres: Psychohistory
Publisher: Debolsillo
Publish Date: 2008
ISBN: 0553803719
Price: $13.72

Quantity: 17
---------------------------------------------

Title: Watership Down
Author: Richard Adams, James Sturm, Joe Sutphin
Categories: Rabbits
Genres: Rabbits
Publisher: Turtleback Books
Publish Date: November 1, 2005
ISBN: 072265197X
Price: $10.57

Quantity: 8
---------------------------------------------

Title: The Magician's Nephew
Author: C.S. Lewis
Categories: Fantasy
Genres: Fantasy
Publisher: Bonniers juniorförl.
Publish Date: October 2, 2001
ISBN: 9780871293688
Price: $14.92

Quantity: 13
---------------------------------------------

Title: Yes Please
Author: Amy Poehler
Categories: Women comedians
Genres: Women comedians
Publisher: HarperAudio
Publish Date: Nov 24, 2015
ISBN: 9781443440882
Price: $5.89

Quantity: 20
---------------------------------------------

Title: The 5th Wave
Author: Rick Yancey, Richard Yancey
Categories: Children's fiction
Genres: Children's fiction
Publisher: Penguin Young Readers Group
Publish Date: 2016-02-24
ISBN: 0606366407
Price: $10.32

Quantity: 3
---------------------------------------------

Title: Graceling
Author: Kristin Cashore
Categories: Women warriors
Genres: Women warriors
Publisher: HMH Books for Young Readers
Publish Date: 20 September 2018
ISBN: 9780547351278
Price: $20.27

Quantity: 11
---------------------------------------------

Title: The Sun Also Rises
Author: Ernest Hemingway
Categories: Expatriation
Genres: Expatriation
Publisher: 
Publish Date: 1947
ISBN: 0224034995
Price: $13.31

Quantity: 2
---------------------------------------------

Title: Can You Keep A Secret?
Author: Sophie Kinsella
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Wheeler
Publish Date: 2009
ISBN: 9780385338080
Price: $17.37

Quantity: 10
---------------------------------------------

Title: The Wise Man’s Fear
Author: Patrick Rothfuss
Categories: The Kingkiller Chronicle
Genres: The Kingkiller Chronicle
Publisher: Vintage Espanol
Publish Date: 2018
ISBN: 9780756404734
Price: $8.62

Quantity: 20
---------------------------------------------

Title: Running with Scissors
Author: Augusten Burroughs
Categories: Social life and customs
Genres: Social life and customs
Publisher: Jilin wen shi chu ban she
Publish Date: 2006
ISBN: 9781843541509
Price: $10.45

Quantity: 10
---------------------------------------------

Title: I Know Why the Caged Bird Sings
Author: Maya Angelou
Categories: Social life and customs
Genres: Social life and customs
Publisher: Random House, Incorporated
Publish Date: 2008
ISBN: 0435124277
Price: $14.52

Quantity: 11
---------------------------------------------

Title: Into the air
Author: Glenn Mack
Categories: Aeronautics
Genres: Aeronautics
Publisher: Nelson [(Australia)
Publish Date: 1968
ISBN: N/A
Price: $14.54

Quantity: 13
---------------------------------------------

Title: Atlas Shrugged
Author: Ayn Rand
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: February 25, 1993
ISBN: 0613627199
Price: $5.75

Quantity: 17
---------------------------------------------

Title: The Pelican Brief
Author: John Grisham
Categories: White House Chief of Staff
Genres: White House Chief of Staff
Publisher: Century
Publish Date: 2004
ISBN: 0385470487
Price: $6.65

Quantity: 7
---------------------------------------------

Book Inheart not found on Open Library.Title: James and the Giant Peach
Author: Roald Dahl
Categories: Christian Books
Genres: Christian Books
Publisher: Distributed by Random House
Publish Date: Sep 06, 2016
ISBN: 0141378530
Price: $20.31

Quantity: 5
---------------------------------------------

Title: Anna and the French Kiss
Author: Stephanie Perkins
Categories: Fiction
Genres: Fiction
Publisher: Penguin Young Readers Group
Publish Date: Oct 11, 2011
ISBN: 9780525423270
Price: $11.81

Quantity: 2
---------------------------------------------

Title: Pet Sematary
Author: Stephen King
Categories: fiction
Genres: fiction
Publisher: Doubleday & Company
Publish Date: Mar 27, 2018
ISBN: 9788497930994
Price: $7.86

Quantity: 7
---------------------------------------------

Title: Snow Flower and the Secret Fan
Author: Lisa See
Categories: Childbirth in fiction
Genres: Childbirth in fiction
Publisher: Gao bao shu ban ji tuan
Publish Date: 2006
ISBN: 9780739334676
Price: $20.79

Quantity: 2
---------------------------------------------

Title: The Elite (The Selection #2)
Author: Kiera Cass
Categories: Contests
Genres: Contests
Publisher: FISCHER Sauerländer
Publish Date: Apr 23, 2013
ISBN: 9788416240616
Price: $22.27

Quantity: 7
---------------------------------------------

Title: Where'd You Go, Bernadette
Author: Maria Semple
Categories: Women architects--Washington (State)--Seattle--Fiction.
Genres: Women architects--Washington (State)--Seattle--Fiction.
Publisher: Hachette Book Group
Publish Date: 2013
ISBN: 9780316415859
Price: $11.23

Quantity: 6
---------------------------------------------

Title: Cutting for Stone
Author: Abraham Verghese
Categories: literary fiction
Genres: literary fiction
Publisher: Alfred A. Knopf
Publish Date: 2011
ISBN: 0307357783
Price: $19.71

Quantity: 12
---------------------------------------------

Title: Orphan train
Author: Christina Baker Kline
Categories: Fiction
Genres: Fiction
Publisher: Turtleback
Publish Date: 2013
ISBN: 006195070X
Price: $12.21

Quantity: 12
---------------------------------------------

Title: The Eye of the World
Author: Robert Jordan
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Turtleback Books
Publish Date: November 15, 1990
ISBN: 0356501523
Price: $22.01

Quantity: 14
---------------------------------------------

Title: The Wonderful Wizard of Oz
Author: L. Frank Baum
Categories: Witches
Genres: Witches
Publisher: Bungāh-i Nashr-i Andīshah
Publish Date: November 2006
ISBN: 9781091421547
Price: $9.93

Quantity: 3
---------------------------------------------

Title: Three cups of tea
Author: Greg Mortenson, David Oliver Relin
Categories: nyt:paperback_nonfiction=2007-01-28
Genres: nyt:paperback_nonfiction=2007-01-28
Publisher: Puffin USA
Publish Date: 2006
ISBN: 1101015217
Price: $14.92

Quantity: 19
---------------------------------------------

Title: P.S. I Love You
Author: Barbara Conklin
Categories: N/A
Genres: N/A
Publisher: Bantam Juvenile
Publish Date: 1985
ISBN: 0553203231
Price: $23.57

Quantity: 18
---------------------------------------------

Title: Diary of a Wimpy Kid
Author: Jeff Kinney
Categories: School stories
Genres: School stories
Publisher: Baumhaus Verlag
Publish Date: February 4, 2008
ISBN: 9788993055023
Price: $13.75

Quantity: 2
---------------------------------------------

Title: Where the Red Fern Grows
Author: Wilson Rawls
Categories: Social Issues - Friendship
Genres: Social Issues - Friendship
Publisher: Turtleback Books
Publish Date: July 1977
ISBN: 0153003693
Price: $11.63

Quantity: 12
---------------------------------------------

Title: The Lucky One
Author: Nicholas Sparks
Categories: Fiction
Genres: Fiction
Publisher: Grand Central Publishing
Publish Date: 2008
ISBN: 9780446579933
Price: $9.67

Quantity: 9
---------------------------------------------

Title: Shadow Kiss
Author: Richelle Mead
Categories: Young Adult Fiction
Genres: Young Adult Fiction
Publisher: Penguin USA, Inc.
Publish Date: 2009
ISBN: 0141932082
Price: $6.62

Quantity: 15
---------------------------------------------

Title: Like Water For Chocolate
Author: Marco Leonardi, Lumi Cavazos, Regina Torné, Mario Iván Martínez
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: 2011-10-05
ISBN: N/A
Price: $10.32

Quantity: 2
---------------------------------------------

Title: Safe Haven
Author: Nicholas Sparks
Categories: Neighbors
Genres: Neighbors
Publisher: Grand Central Publishing
Publish Date: 2010
ISBN: 1607886197
Price: $19.53

Quantity: 19
---------------------------------------------

Title: The Strange Case of Dr. Jekyll and Mr. Hyde
Author: Robert Louis Stevenson
Categories: Fiction
Genres: Fiction
Publisher: Goldencraft
Publish Date: Sep 26, 2016
ISBN: 0804900426
Price: $19.41

Quantity: 11
---------------------------------------------

Title: The BFG
Author: Roald Dahl
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Rily
Publish Date: Jun 02, 2016
ISBN: 0224020404
Price: $12.03

Quantity: 8
---------------------------------------------

Title: Cat's Cradle
Author: Kurt Vonnegut
Categories: End of the world
Genres: End of the world
Publisher: Turtleback Books
Publish Date: 2004
ISBN: 9780805013191
Price: $7.22

Quantity: 19
---------------------------------------------

Title: The Hunt for Red October
Author: Tom Clancy
Categories: Fiction
Genres: Fiction
Publisher: Emece Editores
Publish Date: June 1986
ISBN: 9780425269367
Price: $6.42

Quantity: 14
---------------------------------------------

Title: The Subtle Knife
Author: Philip Pullman
Categories: Fantasy
Genres: Fantasy
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: August 28, 2007
ISBN: 0807210471
Price: $16.57

Quantity: 14
---------------------------------------------

Title: Under the Tuscan Sun
Author: Frances Mayes
Categories: Description and travel
Genres: Description and travel
Publisher: Broadway Books
Publish Date: 1997
ISBN: 055381611X
Price: $17.61

Quantity: 10
---------------------------------------------

Title: Kiss the Girls
Author: David Baldacci
Categories: Fiction
Genres: Fiction
Publisher: Books on Tape
Publish Date: November 1, 2005
ISBN: 9781570420290
Price: $11.39

Quantity: 10
---------------------------------------------

Title: Stardust
Author: Neil Gaiman
Categories: Young men
Genres: Young men
Publisher: HarperEntertainment
Publish Date: June 26, 2007
ISBN: 8416859698
Price: $24.26

Quantity: 11
---------------------------------------------

Title: I am Malala
Author: Malala Yousafzai, Christina Lamb, Malala Yousafzai, Malala Yousafazi
Categories: Young women
Genres: Young women
Publisher: Little, Brown Books for Young Readers
Publish Date: 2015
ISBN: 9785389084476
Price: $20.22

Quantity: 19
---------------------------------------------

Title: Who Moved My Cheese?
Author: Spencer Johnson
Categories: Change (psychology)
Genres: Change (psychology)
Publisher: G. P. Putnam's Sons
Publish Date: 2002-01-01
ISBN: 0399147241
Price: $12.71

Quantity: 5
---------------------------------------------

Title: I Am Number Four
Author: Pittacus Lore
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Harper
Publish Date: 2011
ISBN: 9780061969553
Price: $12.24

Quantity: 6
---------------------------------------------

Title: Will Grayson, Will Grayson
Author: John Green, David Levithan
Categories: Theater
Genres: Theater
Publisher: Turtleback Books
Publish Date: 2019
ISBN: 1921656239
Price: $13.83

Quantity: 3
---------------------------------------------

Title: The Godfather
Author: Mario Puzo
Categories: Detective and mystery stories
Genres: Detective and mystery stories
Publisher: B & B Audio
Publish Date: 1985
ISBN: 9780593542590
Price: $22.24

Quantity: 19
---------------------------------------------

Title: Reflected In You
Author: Sylvia Day
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Capa comum: 256 páginas Editora: Paralela
Publish Date: 2012
ISBN: 1405910259
Price: $20.87

Quantity: 9
---------------------------------------------

Title: The Death Cure
Author: James Dashner, James Dashner
Categories: Science fiction
Genres: Science fiction
Publisher: Nocturna ediciones
Publish Date: 2015
ISBN: 9780385907460
Price: $18.47

Quantity: 3
---------------------------------------------

Title: The Thorn Birds
Author: Colleen McCullough, Colleen McCullough
Categories: Fiction
Genres: Fiction
Publisher: Futura
Publish Date: 2002?
ISBN: 9780380637355
Price: $16.58

Quantity: 10
---------------------------------------------

Title: She's come undone
Author: Wally Lamb
Categories: Overweight women
Genres: Overweight women
Publisher: Scribner
Publish Date: 1992
ISBN: 9780671014735
Price: $19.93

Quantity: 13
---------------------------------------------

Title: Frostbite
Author: Richelle Mead
Categories: Magic
Genres: Magic
Publisher: Penguin Group UK
Publish Date: 2009
ISBN: 1436202515
Price: $24.07

Quantity: 18
---------------------------------------------

Title: A Walk in the Woods
Author: Bill Bryson
Categories: Description and travel
Genres: Description and travel
Publisher: Doubleday Canada
Publish Date: March 2001
ISBN: 0767902513
Price: $10.87

Quantity: 9
---------------------------------------------

Title: The Secret Agent
Author: Joseph Conrad
Categories: Fiction
Genres: Fiction
Publisher: Distributed by Random House
Publish Date: 1947
ISBN: 9780192834775
Price: $19.85

Quantity: 20
---------------------------------------------

Title: The Final Empire
Author: Brandon Sanderson
Categories: Courts and courtiers
Genres: Courts and courtiers
Publisher: Tor Books
Publish Date: July 25, 2006
ISBN: 076531178X 9780765311788 9780765350381 0765350386
Price: $21.18

Quantity: 14
---------------------------------------------

Title: Oliver Twist
Author: Charles Dickens
Categories: Bildungsromans
Genres: Bildungsromans
Publisher: Createspace Independent Publishing Platform
Publish Date: 1968
ISBN: 9781973338574
Price: $11.83

Quantity: 19
---------------------------------------------

Title: On The Road
Author: Jack Kerouac
Categories: Beat generation
Genres: Beat generation
Publisher: Hunan literature and Art Publishing House
Publish Date: 1958
ISBN: 9780140182941
Price: $11.73

Quantity: 16
---------------------------------------------

Title: The Crucible
Author: Arthur Miller
Categories: fiction classics
Genres: fiction classics
Publisher: Turtleback (Penguin Books)
Publish Date: 1953
ISBN: 9781580812191
Price: $11.57

Quantity: 13
---------------------------------------------

Title: The Unbearable Lightness Of Being In Aberystwyth
Author: Malcolm Pryce
Categories: Wales, fiction
Genres: Wales, fiction
Publisher: Bloomsbury Publishing PLC
Publish Date: 2006
ISBN: 9781408809020
Price: $19.14

Quantity: 8
---------------------------------------------

Title: Do Androids Dream of Electric Sheep?
Author: Philip K. Dick
Categories: Androids
Genres: Androids
Publisher: Minotauro
Publish Date: July 12, 1987
ISBN: 8435034771
Price: $10.58

Quantity: 14
---------------------------------------------

Title: A Discovery of Witches
Author: Deborah E. Harkness
Categories: Vampires--Fiction.
Genres: Vampires--Fiction.
Publisher: Penguin Random House Grupo Editorial
Publish Date: Dec 27, 2011
ISBN: 1410436330
Price: $5.55

Quantity: 19
---------------------------------------------

Title: Othello
Author: William Shakespeare
Categories: Drama
Genres: Drama
Publisher: Printed for J. Barker
Publish Date: 1956-03
ISBN: 0553213024
Price: $10.88

Quantity: 13
---------------------------------------------

Title: The Casual Vacancy
Author: J. K. Rowling, Tom Hollander
Categories: fiction
Genres: fiction
Publisher: Little, Brown and Co.
Publish Date: 2015
ISBN: 0316228591
Price: $20.30

Quantity: 1
---------------------------------------------

Title: The Fountainhead
Author: Ayn Rand
Categories: Fiction
Genres: Fiction
Publisher: Bobbs-Merril
Publish Date: 2009
ISBN: 0453009115
Price: $12.48

Quantity: 6
---------------------------------------------

Title: I Know This Much Is True
Author: Wally Lamb
Categories: Fiction
Genres: Fiction
Publisher: HarperCollins Publishers
Publish Date: October 1998
ISBN: 9780965605915
Price: $13.62

Quantity: 19
---------------------------------------------

Title: Nineteen Minutes
Author: Jodi Picoult
Categories: Literature
Genres: Literature
Publisher: 
Publish Date: March 2007
ISBN: 9781585479917
Price: $24.51

Quantity: 10
---------------------------------------------

Title: Salem’s Lot
Author: Stephen King
Categories: Catholic Church
Genres: Catholic Church
Publisher: Suma
Publish Date: 2008
ISBN: 9780816156863
Price: $13.69

Quantity: 12
---------------------------------------------

Title: The Screwtape Letters
Author: C.S. Lewis
Categories: Fiction
Genres: Fiction
Publisher: Audio Literature
Publish Date: February 28, 2006
ISBN: 1557488118
Price: $15.56

Quantity: 11
---------------------------------------------

Title: A Court of Thorns and Roses Box Set
Author: Sarah J. Maas
Categories: Children's fiction
Genres: Children's fiction
Publisher: Bloomsbury Publishing
Publish Date: 2022
ISBN: 9781681197746
Price: $24.36

Quantity: 4
---------------------------------------------

Title: The Red Pyramid
Author: Rick Riordan
Categories: Fiction
Genres: Fiction
Publisher: 
Publish Date: 2015
ISBN: 9780545398268
Price: $21.30

Quantity: 10
---------------------------------------------

Title: The last lecture
Author: Randy Pausch
Categories: Death
Genres: Death
Publisher: Hyperion
Publish Date: 2008
ISBN: 9781401309657
Price: $23.99

Quantity: 7
---------------------------------------------

Title: White oleander
Author: Fitch, Janet
Categories: Fiction
Genres: Fiction
Publisher: Books on Tape
Publish Date: August 2000
ISBN: 9784444407342
Price: $8.17

Quantity: 8
---------------------------------------------

Title: Beloved
Author: Toni Morrison
Categories: African American History
Genres: African American History
Publisher: Knopf
Publish Date: 1987-10
ISBN: 9780375704147
Price: $8.36

Quantity: 4
---------------------------------------------

Title: Good in bed
Author: Jodi Picocell
Categories: Humorous stories
Genres: Humorous stories
Publisher: Pocket Books
Publish Date: 2001
ISBN: 9780743544993
Price: $22.66

Quantity: 10
---------------------------------------------

Title: Ancestors and descendants of Albro Dexter Shepard and his wife Alice Zeviah Sill
Author: Winfred C. Shepard
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: 1949
ISBN: N/A
Price: $14.35

Quantity: 11
---------------------------------------------

Title: Stargirl (Stargirl #1)
Author: Jerry Spinelli, Maria Lara, Sandra Diaz-Aguado, Chiba Shigeki, Albert E. Knopf
Categories: Individuality
Genres: Individuality
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: July 1, 2002
ISBN: 9780439488402
Price: $11.48

Quantity: 11
---------------------------------------------

Title: Fear and Loathing in Las Vegas
Author: Hunter S. Thompson
Categories: comedy
Genres: comedy
Publisher: Flamingo
Publish Date: 1998
ISBN: 0679785892
Price: $11.38

Quantity: 16
---------------------------------------------

Title: 1st to Die
Author: James Patterson
Categories: Fiction
Genres: Fiction
Publisher: Warner Vision Books
Publish Date: May 22, 2008
ISBN: 9781472243454
Price: $10.08

Quantity: 4
---------------------------------------------

Book A Prayer to Owen Meany not found on Open Library.Title: The Importance of Being Earnest
Author: Oscar Wilde
Categories: British and irish drama (dramatic works by one author)
Genres: British and irish drama (dramatic works by one author)
Publisher: Prestwick House
Publish Date: 2011
ISBN: 9781494381189
Price: $15.25

Quantity: 19
---------------------------------------------

Title: For One More Day
Author: Mitch Albom
Categories: Future life
Genres: Future life
Publisher: Da kuai wen hua chu ban gu fen you xian gong si
Publish Date: 2008
ISBN: 9787532742387
Price: $16.59

Quantity: 8
---------------------------------------------

Title: The Witches
Author: Roald Dahl, Quentin Blake, Simon Callow
Categories: Fiction
Genres: Fiction
Publisher: Puffin Audiobooks
Publish Date: March 1985
ISBN: 9780141322643
Price: $6.15

Quantity: 9
---------------------------------------------

Title: Daughter of Smoke and Bone
Author: Laini Taylor
Categories: Chimera (Greek mythology)
Genres: Chimera (Greek mythology)
Publisher: Hodder Paperback
Publish Date: 2011
ISBN: 8925545926
Price: $9.75

Quantity: 2
---------------------------------------------

Title: Murder on the Orient Express
Author: Agatha Christie
Categories: Agatha Christie
Genres: Agatha Christie
Publisher: Pub. for the Crime Club, ltd., by Collins
Publish Date: 1959
ISBN: 0062693662
Price: $13.60

Quantity: 3
---------------------------------------------

Title: Blood Promise
Author: Richelle Mead
Categories: Vampires
Genres: Vampires
Publisher: Razorbill an imprint of Penguin Group (USA) Inc.
Publish Date: 2009
ISBN: 9781101138427
Price: $23.35

Quantity: 3
---------------------------------------------

Title: Hatchet
Author: Gary Paulsen
Categories: Divorce
Genres: Divorce
Publisher: Demco Media
Publish Date: Dec 26, 2006
ISBN: 9781534407862
Price: $6.41

Quantity: 16
---------------------------------------------

Title: Northanger Abbey
Author: Jane Austen
Categories: Mate selection
Genres: Mate selection
Publisher: Wildside Press, LLC
Publish Date: 1959
ISBN: 9781434117168
Price: $9.78

Quantity: 7
---------------------------------------------

Title: Dark Lover
Author: J. R. Ward
Categories: Fiction
Genres: Fiction
Publisher: New American Library
Publish Date: 2008
ISBN: 1429522348
Price: $5.05

Quantity: 8
---------------------------------------------

Title: The Color of Magic
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: N/A
ISBN: 143527458X
Price: $23.76

Quantity: 3
---------------------------------------------

Title: What Alice Forgot
Author: Liane Moriarty
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: Penguin Audio
Publish Date: 2015
ISBN: 1594138516
Price: $5.41

Quantity: 16
---------------------------------------------

Title: PERFUME - The Story of a Murderer
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: N/A
ISBN: N/A
Price: $11.98

Quantity: 20
---------------------------------------------

Title: And the Mountains Echoed
Author: Khaled Hosseini
Categories: Community life
Genres: Community life
Publisher: Piemme
Publish Date: 2015
ISBN: 9789927101908
Price: $10.17

Quantity: 10
---------------------------------------------

Title: John Adams
Author: David McCullough
Categories: Politics and government
Genres: Politics and government
Publisher: Simon & Schuster
Publish Date: 2001
ISBN: 0684813637
Price: $14.80

Quantity: 5
---------------------------------------------

Title: Norwegian wood
Author: Haruki Murakami
Categories: N/A
Genres: N/A
Publisher: Atlas Contact
Publish Date: Oct 16, 2013
ISBN: 9025442846
Price: $6.28

Quantity: 10
---------------------------------------------

Title: A Study in Scarlet
Author: Arthur Conan Doyle
Categories: Action & Adventure Fiction
Genres: Action & Adventure Fiction
Publisher: Lulu.com
Publish Date: November 2006
ISBN: 9798523298547
Price: $14.28

Quantity: 17
---------------------------------------------

Title: Heaven is for Real
Author: Todd Burpo
Categories: nyt:paperback_nonfiction=2010-11-13
Genres: nyt:paperback_nonfiction=2010-11-13
Publisher: Thomas Nelson on Brilliance Audio
Publish Date: 2011
ISBN: 9781543617849
Price: $9.81

Quantity: 5
---------------------------------------------

Title: The New Drawing on the Right Side of the Brain
Author: Betty Edwards
Categories: Technique
Genres: Technique
Publisher: JT Tarcher
Publish Date: 1999
ISBN: 9780874774245
Price: $21.25

Quantity: 12
---------------------------------------------

Title: Name of the Rose
Author: RH Value Publishing
Categories: N/A
Genres: N/A
Publisher: Random House Value Publishing
Publish Date: November 27, 1985
ISBN: 0517448424
Price: $11.67

Quantity: 14
---------------------------------------------

Title: When Breath Becomes Air
Author: Paul Kalanithi
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: ????
ISBN: 1785414747
Price: $9.82

Quantity: 17
---------------------------------------------

Title: Mansfield Park
Author: Jane Austen
Categories: Fiction, Romance, Historical, Regency
Genres: Fiction, Romance, Historical, Regency
Publisher: MARTIN CLARET
Publish Date: July 1997
ISBN: 9781695388277
Price: $5.58

Quantity: 6
---------------------------------------------

Title: Crescendo
Author: Charlotte Lamb
Categories: Fiction
Genres: Fiction
Publisher: Harlequin
Publish Date: September 1981
ISBN: 0263755258
Price: $14.36

Quantity: 9
---------------------------------------------

Title: Brisingr
Author: Christopher Paolini
Categories: Fiction
Genres: Fiction
Publisher: Knopf
Publish Date: 2004
ISBN: 9781407044781
Price: $16.71

Quantity: 2
---------------------------------------------

Title: The Pact
Author: Jodi Picoult
Categories: Literature
Genres: Literature
Publisher: Rebound by Sagebrush
Publish Date: May 1999
ISBN: 9780606217576
Price: $21.79

Quantity: 4
---------------------------------------------

Title: Evermore
Author: Alyson Noël
Categories: nyt:series_books=2010-07-11
Genres: nyt:series_books=2010-07-11
Publisher: St. Martin's Griffin
Publish Date: Jun 09, 2009
ISBN: 9781427208408
Price: $17.60

Quantity: 11
---------------------------------------------

Title: Stranger in a Strange Land
Author: Robert A. Heinlein
Categories: Hugo Award Winner
Genres: Hugo Award Winner
Publisher: Generic
Publish Date: 1980
ISBN: 0441788386
Price: $23.93

Quantity: 11
---------------------------------------------

Title: Spirit Bound
Author: Richelle Mead
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Razorbill an imprint of Penguin Group (USA) Inc.
Publish Date: May 18, 2010
ISBN: 9781595142504
Price: $24.02

Quantity: 14
---------------------------------------------

Title: The Scarlet Letter
Author: Nathaniel Hawthorne
Categories: Fiction
Genres: Fiction
Publisher: Econo-Clad Books
Publish Date: 1935
ISBN: 9781587886102
Price: $8.20

Quantity: 13
---------------------------------------------

Title: Man's Search for Meaning [adaptation]
Author: Viktor E. Frankl
Categories: Frankl, viktor emil, 1905-1997
Genres: Frankl, viktor emil, 1905-1997
Publisher: Perfection Learning Corporation
Publish Date: Apr 25, 2017
ISBN: 9780807067994
Price: $12.38

Quantity: 5
---------------------------------------------

Title: The Art of War
Author: Sun Tzu
Categories: Military art and science
Genres: Military art and science
Publisher: Shi jie shu ju
Publish Date: June 30, 2004
ISBN: 1883999103
Price: $24.70

Quantity: 2
---------------------------------------------

Title: The Thirteenth Tale
Author: Diane Setterfield
Categories: Solitarios
Genres: Solitarios
Publisher: Lumen
Publish Date: 2006
ISBN: 0743564510
Price: $23.14

Quantity: 9
---------------------------------------------

Title: Storm Front
Author: Jim Butcher
Categories: Mystery
Genres: Mystery
Publisher: Subterranean
Publish Date: Jun 01, 2015
ISBN: 1984805622
Price: $6.18

Quantity: 13
---------------------------------------------

Title: The three musketeers [adaptation]
Author: Malvina G. Vogel
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: Ta lian li gong ta xue chu ban she
Publish Date: 1970
ISBN: 1424006058
Price: $15.92

Quantity: 19
---------------------------------------------

Book The Amber Spyglass -Philip Pullman (2000) not found on Open Library.Title: The Runaway Jury
Author: John Grisham
Categories: Fiction
Genres: Fiction
Publisher: Century
Publish Date: August 2000
ISBN: 9788440692702
Price: $6.57

Quantity: 17
---------------------------------------------

Title: Before I Go to Sleep
Author: S. J. Watson
Categories: Sleep-wake cycle
Genres: Sleep-wake cycle
Publisher: Turtleback Books
Publish Date: Nov 07, 2012
ISBN: 9781443404075
Price: $8.86

Quantity: 18
---------------------------------------------

Book Fried Green Tomatoes at the Whistle Shop Café not found on Open Library.Title: Last Sacrifice
Author: Richelle Mead
Categories: Fantasy
Genres: Fantasy
Publisher: Tram-Anh Tran
Publish Date: 2010
ISBN: 1595143068
Price: $7.73

Quantity: 13
---------------------------------------------

Title: Life, the Universe and Everything
Author: Douglas Adams
Categories: sofas
Genres: sofas
Publisher: Audio Literature
Publish Date: May 1985
ISBN: 9781415930519
Price: $23.36

Quantity: 9
---------------------------------------------

Title: Things Fall Apart
Author: Chinua Achebe
Categories: 20th century literature
Genres: 20th century literature
Publisher: Knopf
Publish Date: November 19, 2008
ISBN: 9782266264
Price: $24.45

Quantity: 1
---------------------------------------------

Title: Dragonfly in Amber
Author: Diana Gabaldon
Categories: Historical Fiction
Genres: Historical Fiction
Publisher: Seal Books
Publish Date: 2016
ISBN: 0553714511
Price: $10.88

Quantity: 11
---------------------------------------------

Title: A Streetcar Named Desire
Author: Tennessee Williams
Categories: Drama
Genres: Drama
Publisher: New Directions
Publish Date: 1953
ISBN: 9789996375231
Price: $16.17

Quantity: 17
---------------------------------------------

Title: Where She Went
Author: Gayle Forman
Categories: Rock music
Genres: Rock music
Publisher: Penguin
Publish Date: 2012
ISBN: 9780525422945
Price: $15.84

Quantity: 13
---------------------------------------------

Title: Little House in the Big Woods
Author: Laura Ingalls Wilder, Garth Williams
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: LRS
Publish Date: 1959
ISBN: 9781974247653
Price: $15.62

Quantity: 14
---------------------------------------------

Title: Mere Christianity
Author: C.S. Lewis
Categories: Apologetics
Genres: Apologetics
Publisher: Harper San Francisco
Publish Date: Mar 15, 2012
ISBN: 0007461216
Price: $13.78

Quantity: 10
---------------------------------------------

Title: The story of art
Author: E. H. Gombrich
Categories: Art
Genres: Art
Publisher: Gweled/CAA
Publish Date: 1953
ISBN: 9780801492150
Price: $10.18

Quantity: 6
---------------------------------------------

Title: City of Heavenly Fire
Author: Cassandra Clare
Categories: Social Issues
Genres: Social Issues
Publisher: Margaret K. McElderry Books
Publish Date: 2014
ISBN: 9781442416901
Price: $18.54

Quantity: 15
---------------------------------------------

Title: V for Vendetta
Author: Alan Moore, David Lloyd
Categories: Fiction
Genres: Fiction
Publisher: Panini Comics
Publish Date: Oct 24, 2008
ISBN: 280940965X
Price: $18.75

Quantity: 6
---------------------------------------------

Title: A short history of nearly everything
Author: Bill Bryson
Categories: Science
Genres: Science
Publisher: Wilhelm Goldmann
Publish Date: 2004
ISBN: 9780552997041
Price: $10.05

Quantity: 1
---------------------------------------------

Title: The Undomestic Goddess
Author: Sophie Kinsella
Categories: Novel·la
Genres: Novel·la
Publisher: Random House Large Print
Publish Date: 2009
ISBN: 9780385338684
Price: $21.03

Quantity: 5
---------------------------------------------

Title: Crown of Midnight
Author: Sarah J. Maas
Categories: Kings and rulers
Genres: Kings and rulers
Publisher: Brilliance Audio MP3 CD
Publish Date: 2023
ISBN: 6050923523
Price: $17.31

Quantity: 13
---------------------------------------------

Title: Shatter Me
Author: Tahereh Mafi
Categories: Love
Genres: Love
Publisher: Turtleback Books
Publish Date: 2019
ISBN: 9780062741738
Price: $21.96

Quantity: 5
---------------------------------------------

Title: Hopeless
Author: Colleen Hoover
Categories: Fiction, Romance, Contemporary, Life change events
Genres: Fiction, Romance, Contemporary, Life change events
Publisher: Epsilon Yayıncılık
Publish Date: Nov 07, 2013
ISBN: 9788490326244
Price: $23.05

Quantity: 5
---------------------------------------------

Title: The Paris wife
Author: Paula McLain
Categories: Authors' spouses
Genres: Authors' spouses
Publisher: Little, Brown Book Group Limited
Publish Date: 2011
ISBN: 045148634X
Price: $19.56

Quantity: 1
---------------------------------------------

Title: I, Robot
Author: Isaac Asimov, Rowena Akinyemi, Tricia Reilly
Categories: smear campaigns
Genres: smear campaigns
Publisher: Turtleback Books
Publish Date: 1956
ISBN: 9782290227268
Price: $21.50

Quantity: 11
---------------------------------------------

Title: Station Eleven
Author: Emily St. John Mandel
Categories: Fiction
Genres: Fiction
Publisher: Papierowy ksiezyc
Publish Date: Jan 01, 2014
ISBN: 9781596068551
Price: $12.77

Quantity: 3
---------------------------------------------

Title: Rich Dad, Poor Dad
Author: Robert T. Kiyosaki, Sharon L. Lechter
Categories: Rich people
Genres: Rich people
Publisher: Brilliance Audio
Publish Date: Jun 05, 2012
ISBN: 0739413937
Price: $18.57

Quantity: 4
---------------------------------------------

Title: Kafka on the Shore
Author: Haruki Murakami
Categories: Japan, fiction
Genres: Japan, fiction
Publisher: RANDOM HOUSE @ TRADE
Publish Date: 2022
ISBN: 0307275264
Price: $8.38

Quantity: 1
---------------------------------------------

Title: Odd Thomas
Author: Dean Koontz, David Aaron Baker
Categories: Cooks
Genres: Cooks
Publisher: HarperCollins Publishers Ltd
Publish Date: Nov 15, 2003
ISBN: 9780739341438
Price: $24.27

Quantity: 3
---------------------------------------------

Title: Dead to the World
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: Orion Publishing Group
Publish Date: Jun 08, 2010
ISBN: 1596880163
Price: $17.05

Quantity: 9
---------------------------------------------

Title: A Farewell to Arms
Author: Ernest Hemingway
Categories: Cuentos de guerra
Genres: Cuentos de guerra
Publisher: Scribner
Publish Date: 1932
ISBN: 0684717972
Price: $17.54

Quantity: 15
---------------------------------------------

Title: Little House on the Prairie
Author: Laura Ingalls Wilder, Garth Williams
Categories: Osage Nation
Genres: Osage Nation
Publisher: Demco Media
Publish Date: 1953
ISBN: 9780060543990
Price: $8.85

Quantity: 10
---------------------------------------------

Title: Defending Jacob
Author: William Landay
Categories: Murder
Genres: Murder
Publisher: Orion (An Imprint Of The
Publish Date: Jan 31, 2012
ISBN: 9781444813715
Price: $21.33

Quantity: 5
---------------------------------------------

Title: Neuromancer
Author: William Gibson
Categories: Information superhighway
Genres: Information superhighway
Publisher: Editrice Nord
Publish Date: May 21, 2011
ISBN: 9781473217379
Price: $10.71

Quantity: 11
---------------------------------------------

Title: The Historian
Author: Elizabeth Kostova
Categories: Historical Fiction
Genres: Historical Fiction
Publisher: Little, Brown & Company
Publish Date: June 3, 2008
ISBN: 0316730300
Price: $14.37

Quantity: 3
---------------------------------------------

Title: For Whom the Bell Tolls
Author: Ernest Hemingway
Categories: Spain in fiction
Genres: Spain in fiction
Publisher: Blakiston Company
Publish Date: May 3, 2005
ISBN: 0881036277
Price: $8.45

Quantity: 16
---------------------------------------------

Title: Perfect chemistry
Author: Simone Elkeles
Categories: Fiction
Genres: Fiction
Publisher: COMPANY New York
Publish Date: Nov 01, 2010
ISBN: 1441888500
Price: $12.76

Quantity: 8
---------------------------------------------

Title: The Silence of the Lambs
Author: Thomas Harris
Categories: lambs
Genres: lambs
Publisher: Ullstein Hörverlag
Publish Date: 1990 04
ISBN: 1585471100
Price: $14.13

Quantity: 5
---------------------------------------------

Title: War and Peace
Author: Lev Nikolaevič Tolstoy
Categories: Classic
Genres: Classic
Publisher: Wildside Press, LLC
Publish Date: 1959
ISBN: 9781602528680
Price: $18.14

Quantity: 15
---------------------------------------------

Title: Peter Pan
Author: J. M. Barrie, Barbara Frith, Francis Donkin Bedford, Susan Cooper, Walt Disney, Jesús Aguado, Vicente Muñoz Puelles, Mauro Armiño
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Bantam Dell Pub Group (Trd)
Publish Date: June 30, 1970
ISBN: 1973116871
Price: $21.51

Quantity: 18
---------------------------------------------

Title: Betrayed
Author: P. C. Cast, Kristin Cast
Categories: Vampires
Genres: Vampires
Publisher: St. Martin's Griffin
Publish Date: October 2, 2007
ISBN: 0312596294
Price: $18.92

Quantity: 10
---------------------------------------------

Title: The Secret History
Author: Donna Tartt, Pierre Alien
Categories: Fiction
Genres: Fiction
Publisher: Pocket
Publish Date: 1995
ISBN: 2266188739
Price: $20.52

Quantity: 6
---------------------------------------------

Title: Where the heart is
Author: Billie Letts, Billie Letts
Categories: Fiction
Genres: Fiction
Publisher: Warner Books
Publish Date: 1999
ISBN: 1567406645
Price: $9.56

Quantity: 5
---------------------------------------------

Title: Dress Your Family in Corduroy and Denim
Author: David Sedaris, David Sedaris
Categories: Section 8
Genres: Section 8
Publisher: Hachette Book Group
Publish Date: 2006
ISBN: 0748125949
Price: $8.07

Quantity: 2
---------------------------------------------

Title: Just Listen
Author: Sarah Dessen
Categories: Young adult fiction
Genres: Young adult fiction
Publisher: Viking Children's Books
Publish Date: April 6, 2006
ISBN: 9781419394355
Price: $19.86

Quantity: 20
---------------------------------------------

Title: The invention of wings
Author: Sue Monk Kidd
Categories: Master and servant
Genres: Master and servant
Publisher: Penguin Audio
Publish Date: 2015
ISBN: 1594138869
Price: $23.51

Quantity: 13
---------------------------------------------

Title: Living dead in Dallas
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: Harris, Charlaine
Publish Date: March 2, 2010
ISBN: 0441018262
Price: $12.02

Quantity: 4
---------------------------------------------

Title: After You
Author: Jojo Moyes, Yujia He
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Inostranka
Publish Date: 2015
ISBN: 9788324035731
Price: $21.45

Quantity: 14
---------------------------------------------

Title: The Naked Sun
Author: Isaac Asimov
Categories: Fiction
Genres: Fiction
Publisher: HarperVoyager
Publish Date: 1985
ISBN: 9781400154227
Price: $13.30

Quantity: 18
---------------------------------------------

Title: Go Ask Alice
Author: Beatrice Sparks
Categories: homelessness
Genres: homelessness
Publisher: Arrow Books Ltd
Publish Date: July 1977
ISBN: 9780099557494
Price: $23.59

Quantity: 14
---------------------------------------------

Title: The 5 Love Languages
Author: Gary D. Chapman
Categories: N/A
Genres: N/A
Publisher: Turtleback
Publish Date: Jan 01, 2010
ISBN: 9780606269551
Price: $7.92

Quantity: 9
---------------------------------------------

Book Maus 1: A survivor’s tale not found on Open Library.Title: Bel Canto
Author: Ann Patchett, Oristelle Bonis
Categories: award:pen_faulkner_award=fiction
Genres: award:pen_faulkner_award=fiction
Publisher: Harper Audio
Publish Date: April 16, 2002
ISBN: 0060771607
Price: $24.49

Quantity: 13
---------------------------------------------

Failed: 503Failed: 503Title: A Brief History of Time
Author: Stephen Hawking
Categories: Espace et temps
Genres: Espace et temps
Publisher: Audio Literature
Publish Date: May 2002
ISBN: 9788020401694
Price: $15.36

Quantity: 12
---------------------------------------------

Title: Robinson Crusoe
Author: Daniel Defoe
Categories: Robinson Cusoe
Genres: Robinson Cusoe
Publisher: Ueberreuter
Publish Date: July 25, 2005
ISBN: 9780736689533
Price: $8.01

Quantity: 17
---------------------------------------------

Title: All the Pretty Horses
Author: Cormac McCarthy
Categories: Fiction
Genres: Fiction
Publisher: Büchergilde Gutenberg
Publish Date: 2011
ISBN: 9780606200691
Price: $12.55

Quantity: 10
---------------------------------------------

Title: Cress
Author: Marissa Meyer, Guillaume Fournier, Roxanna Erdman
Categories: Teenage girls
Genres: Teenage girls
Publisher: Feiwel and Friends
Publish Date: 2014
ISBN: 9877470330
Price: $16.37

Quantity: 8
---------------------------------------------

Title: The Things They Carried
Author: Tim O'Brien
Categories: Reading Level-Grade 9
Genres: Reading Level-Grade 9
Publisher: Broadway Books
Publish Date: December 29, 1998
ISBN: 000738680X
Price: $20.20

Quantity: 4
---------------------------------------------

Title: Voyage au Centre de la Terre
Author: Jules Verne
Categories: Fiction
Genres: Fiction
Publisher: French & European Pubns
Publish Date: 2001
ISBN: 9782090329193
Price: $19.79

Quantity: 19
---------------------------------------------

Title: Little Fires Everywhere
Author: Celeste Ng
Categories: Single mothers
Genres: Single mothers
Publisher: Penguin Audio
Publish Date: 2017
ISBN: 9781408709726
Price: $8.92

Quantity: 4
---------------------------------------------

Title: Tess of the d'Urbervilles
Author: Thomas Hardy
Categories: Fiction
Genres: Fiction
Publisher: Dell Publishing Company
Publish Date: 1959
ISBN: 9780192833624
Price: $10.36

Quantity: 12
---------------------------------------------

Title: Guns, germs, and steel
Author: Jared Diamond, Fabián Chueca
Categories: prize:pulitzer=1998
Genres: prize:pulitzer=1998
Publisher: Munhak Sasangsa
Publish Date: July 1998
ISBN: 1586638637
Price: $11.80

Quantity: 11
---------------------------------------------

Title: Little Bee
Author: Chris Cleave
Categories: Fiction
Genres: Fiction
Publisher: simon and schuester
Publish Date: 2011
ISBN: 9780385665308
Price: $12.40

Quantity: 15
---------------------------------------------

Title: Black Beauty
Author: Anna Sewell
Categories: Black Beauty
Genres: Black Beauty
Publisher: Lulu.com
Publish Date: Oct 07, 2018
ISBN: 1079624619
Price: $14.93

Quantity: 20
---------------------------------------------

Title: The Green Mile
Author: Stephen King
Categories: horror fiction
Genres: horror fiction
Publisher: Debolsillo
Publish Date: 2008
ISBN: 0743210891
Price: $5.50

Quantity: 4
---------------------------------------------

Title: The Hiding Place
Author: Corrie ten Boom, Elizabeth Sherrill, John Sherrill, John Scherrill, Corrie Ten Boom, Corrie ten Boom, Jill De Haan, Daniel Strange
Categories: World war, 1939-1945, personal narratives, dutch
Genres: World war, 1939-1945, personal narratives, dutch
Publisher: Christian Renewal Ministries
Publish Date: 2005
ISBN: 9781577489191
Price: $12.02

Quantity: 8
---------------------------------------------

Title: The Chosen
Author: Chaim Potok
Categories: Fathers and sons
Genres: Fathers and sons
Publisher: Ballantine Books
Publish Date: December 1994
ISBN: 0449213447
Price: $5.94

Quantity: 19
---------------------------------------------

Title: The Power of Habit
Author: Charles Duhigg, Johan-Frédérik Hel Guedj
Categories: Social aspects
Genres: Social aspects
Publisher: Vintage Espanol
Publish Date: Feb 28, 2012
ISBN: 0679603859
Price: $22.57

Quantity: 5
---------------------------------------------

Title: Madame Bovary
Author: Gustave Flaubert
Categories: literary fiction
Genres: literary fiction
Publisher: Garnier frères
Publish Date: 1995
ISBN: 9788806155902
Price: $16.77

Quantity: 4
---------------------------------------------

Title: The Phantom Tollbooth
Author: Norton Juster
Categories: letters
Genres: letters
Publisher: Anaya
Publish Date: August 1, 2001
ISBN: 0394815009
Price: $13.18

Quantity: 4
---------------------------------------------

Title: The namesake
Author: C. Walter Hodges
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: Coward-McCann
Publish Date: 1976
ISBN: 9780140301373
Price: $21.82

Quantity: 2
---------------------------------------------

Title: The Woman In Cabin 10
Author: Ruth Ware
Categories: Women journalists
Genres: Women journalists
Publisher: Gallery/Scout Press
Publish Date: 2017
ISBN: 8498387965
Price: $20.08

Quantity: 4
---------------------------------------------

Title: The Good Earth
Author: Pearl S. Buck, Nick Bertozzi, Ruth Goode, Donald F. Roden, Ernst Simon, Stephen Colbourn
Categories: China, fiction
Genres: China, fiction
Publisher: Shi bao wen hua chu ban qi ye gu fen you xian gong si
Publish Date: 1935
ISBN: 9788420677439
Price: $22.52

Quantity: 7
---------------------------------------------

Title: The Prince
Author: Niccolò Machiavelli
Categories: Political science, early works to 1800
Genres: Political science, early works to 1800
Publisher: Ediotes Mexicanos Unidos
Publish Date: June 30, 1992
ISBN: 1449547044
Price: $15.91

Quantity: 19
---------------------------------------------

Title: Club dead
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: LA Factoria De Ideas
Publish Date: Aug 24, 2009
ISBN: 9781407238685
Price: $21.29

Quantity: 3
---------------------------------------------

Title: Tarzan the Untamed (Book #7)
Author: Edgar Rice Burroughs
Categories: Fiction
Genres: Fiction
Publisher: Independently published
Publish Date: 2012-05-19
ISBN: 1414216750
Price: $16.84

Quantity: 10
---------------------------------------------

Title: The No. 1 Ladies' Detective Agency
Author: Alexander McCall Smith
Categories: Fiction
Genres: Fiction
Publisher: Anchor Books
Publish Date: 2013
ISBN: 226404554X
Price: $9.37

Quantity: 11
---------------------------------------------

Title: Snow Crash
Author: Neal Stephenson
Categories: American Science fiction
Genres: American Science fiction
Publisher: LGF
Publish Date: 2008
ISBN: 9781596061576
Price: $16.10

Quantity: 1
---------------------------------------------

Title: The Way of Kings
Author: Brandon Sanderson
Categories: New York Times Bestseller
Genres: New York Times Bestseller
Publisher: Tor: Tom Doherty Associates
Publish Date: Nov 01, 2011
ISBN: 0765326353
Price: $22.86

Quantity: 9
---------------------------------------------

Title: Message in a bottle
Author: Nicholas Sparks
Categories: Fiction
Genres: Fiction
Publisher: Warner Books
Publish Date: 1998
ISBN: 0446606812
Price: $18.99

Quantity: 5
---------------------------------------------

Title: The House of Hades
Author: Rick Riordan
Categories: JUVENILE FICTION / Action & Adventure / greek mythology / Percy Jackson
Genres: JUVENILE FICTION / Action & Adventure / greek mythology / Percy Jackson
Publisher: Rick Riordan
Publish Date: 2015
ISBN: 9781368051712
Price: $18.77

Quantity: 1
---------------------------------------------

Title: The Virgin Suicides
Author: Jeffrey Eugenides
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: Vintage Canada
Publish Date: Oct 02, 2018
ISBN: 9784444406727
Price: $17.03

Quantity: 5
---------------------------------------------

Title: The God of Small Things
Author: Arundhati Roy
Categories: Literary Fiction
Genres: Literary Fiction
Publisher: Zondervan
Publish Date: 1998-02-28
ISBN: 0606302417
Price: $9.56

Quantity: 11
---------------------------------------------

Title: Cold Mountain
Author: Charles Frazier
Categories: United States in fiction
Genres: United States in fiction
Publisher: HarperCollins Audio
Publish Date: 1997
ISBN: 9781574901016
Price: $18.91

Quantity: 9
---------------------------------------------

Title: Murder is Easy
Author: Agatha Christie
Categories: Police
Genres: Police
Publisher: Proszynski i S-ka
Publish Date: April 1987
ISBN: 9780396091592
Price: $8.98

Quantity: 8
---------------------------------------------

Title: Pandemonium
Author: Lauren Oliver
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Harpercollins
Publish Date: 2012
ISBN: 9788467547337
Price: $15.85

Quantity: 2
---------------------------------------------

Title: The Well of Ascension
Author: Brandon Sanderson
Categories: Courts and courtiers
Genres: Courts and courtiers
Publisher: Tor Teen
Publish Date: Feb 08, 2008
ISBN: 9781938570186
Price: $17.92

Quantity: 16
---------------------------------------------

Title: Killing floor
Author: Lee Child
Categories: Fiction
Genres: Fiction
Publisher: Bookcassette
Publish Date: June 10, 2004
ISBN: 9781410430106
Price: $19.32

Quantity: 5
---------------------------------------------

Title: A Confederacy of Dunces
Author: John Kennedy Toole
Categories: mothers
Genres: mothers
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: 2016
ISBN: 9780802197627
Price: $24.54

Quantity: 12
---------------------------------------------

Title: The Brief Wondrous Life of Oscar Wao
Author: Junot Díaz
Categories: Dominican Americans
Genres: Dominican Americans
Publisher: Riverhead Books
Publish Date: 2008
ISBN: 9780571239733
Price: $12.69

Quantity: 14
---------------------------------------------

Title: The War of the Worlds
Author: H. G. Wells
Categories: Imaginary wars and battles
Genres: Imaginary wars and battles
Publisher: Goldencraft
Publish Date: June 16, 2005
ISBN: 0899663771
Price: $24.37

Quantity: 6
---------------------------------------------

Title: Little House in the Big Woods
Author: Laura Ingalls Wilder, Garth Williams
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: LRS
Publish Date: 1959
ISBN: 9781974247653
Price: $22.14

Quantity: 13
---------------------------------------------

Title: 2001: a space odyssey
Author: Peter A. Rudge
Categories: 2001: a space odyssey (Motion picture)
Genres: 2001: a space odyssey (Motion picture)
Publisher: Derbyshire College of Higher Education
Publish Date: 1987
ISBN: N/A
Price: $14.35

Quantity: 15
---------------------------------------------

Title: The kitchen house
Author: Kathleen Grissom
Categories: Fiction
Genres: Fiction
Publisher: Charnwood
Publish Date: May 25, 2010
ISBN: 1594136440
Price: $22.29

Quantity: 5
---------------------------------------------

Title: The Angel Experiment
Author: James Patterson, Copyright Paperback Collection (Library of Congress) Staff
Categories: Fiction
Genres: Fiction
Publisher: Hachette Books
Publish Date: January 2001
ISBN: 9780755321926
Price: $17.10

Quantity: 6
---------------------------------------------

Title: The Hound of the Baskervilles
Author: Arthur Conan Doyle
Categories: crime novel
Genres: crime novel
Publisher: Econo-Clad Books
Publish Date: November 2006
ISBN: 9780486282145
Price: $9.72

Quantity: 11
---------------------------------------------

Title: The Clan of the Cave Bear
Author: Jean M. Auel
Categories: Neanderthals
Genres: Neanderthals
Publisher: Círculo de Lectores, S.A.
Publish Date: 1985
ISBN: 1590860861
Price: $12.65

Quantity: 9
---------------------------------------------

Title: Breakfast of Champions
Author: Kurt Vonnegut
Categories: Authorship
Genres: Authorship
Publisher: Delacorte Press/Seymour Lawrence
Publish Date: March 2, 2004
ISBN: 9780099842606
Price: $19.80

Quantity: 13
---------------------------------------------

Title: Remember Me
Author: Christopher Pike
Categories: Ghosts
Genres: Ghosts
Publisher: Hodder Children's Books
Publish Date: August 2002
ISBN: 9780340532362
Price: $12.07

Quantity: 19
---------------------------------------------

Title: A million little pieces
Author: James Frey
Categories: Drug addicts
Genres: Drug addicts
Publisher: John Murray
Publish Date: 2005
ISBN: 9780307276902
Price: $12.56

Quantity: 3
---------------------------------------------

Title: The God delusion
Author: Richard Dawkins
Categories: god
Genres: god
Publisher: Houghton Mifflin Company
Publish Date: 2006
ISBN: 9944315117
Price: $24.49

Quantity: 7
---------------------------------------------

Title: Tuck Everlasting
Author: Natalie Babbitt
Categories: Aging
Genres: Aging
Publisher: Square Fish
Publish Date: 1977
ISBN: 1400089999
Price: $18.44

Quantity: 10
---------------------------------------------

Title: The Purpose-Driven Life
Author: Rick Warren
Categories: Leefwijze
Genres: Leefwijze
Publisher: Zondervan Publishing House
Publish Date: March 13, 2007
ISBN: 9780310261704
Price: $12.64

Quantity: 13
---------------------------------------------

Title: I'll Give You the Sun
Author: Jandy Nelson
Categories: Romance
Genres: Romance
Publisher: Dial Books
Publish Date: Mar 20, 2015
ISBN: 9780803734968
Price: $20.53

Quantity: 2
---------------------------------------------

Title: Speakers of the dead
Author: J. Aaron Sanders
Categories: Murder
Genres: Murder
Publisher: Plume
Publish Date: 2016
ISBN: 1410491099
Price: $23.94

Quantity: 3
---------------------------------------------

Title: The To All the Boys I've Loved Before Collection
Author: Jenny Han
Categories: Romance
Genres: Romance
Publisher: Scholastic
Publish Date: Nov 13, 2019
ISBN: 9781534427037
Price: $23.08

Quantity: 2
---------------------------------------------

Title: American Psycho
Author: Bret Easton Ellis, Mariano Antolín Rato
Categories: Gothic & Horror
Genres: Gothic & Horror
Publisher: Random House Inc.
Publish Date: May 18, 2023
ISBN: 9781447277705
Price: $11.11

Quantity: 10
---------------------------------------------

Title: The truth about forever
Author: Sarah Dessen
Categories: Fiction
Genres: Fiction
Publisher: Viking
Publish Date: 2004
ISBN: 0670036390
Price: $23.40

Quantity: 11
---------------------------------------------

Title: The Brothers Karamazov
Author: Фёдор Михайлович Достоевский, Constance Garrett
Categories: N/A
Genres: N/A
Publisher: CreateSpace Independent Publishing Platform
Publish Date: Feb 18, 2016
ISBN: 1772753564
Price: $8.17

Quantity: 2
---------------------------------------------

Title: The Raven Boys
Author: Maggie Stiefvater
Categories: Children's fiction
Genres: Children's fiction
Publisher: CRUÏLLA
Publish Date: May 16, 2014
ISBN: 881707781X
Price: $11.48

Quantity: 16
---------------------------------------------

Title: The Andromeda Strain
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: N/A
ISBN: 1448730295
Price: $12.31

Quantity: 5
---------------------------------------------

Title: Torment (Fallen #2)
Author: Lauren Kate
Categories: Children's fiction
Genres: Children's fiction
Publisher: Delacorte
Publish Date: 2011
ISBN: 038573915X
Price: $20.15

Quantity: 4
---------------------------------------------

Title: All the bright places
Author: Jennifer Niven
Categories: Suicide
Genres: Suicide
Publisher: Alfred A. Knopf
Publish Date: January 6, 2015
ISBN: 0141357037
Price: $10.53

Quantity: 19
---------------------------------------------

Title: Obsidian prey
Author: Jayne Ann Krentz
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Penguin USA, Inc.
Publish Date: 2009
ISBN: 9781101130148
Price: $14.56

Quantity: 2
---------------------------------------------

Title: The Absolutely True Diary of a Part-Time Indian
Author: Sherman Alexie
Categories: Race relations
Genres: Race relations
Publisher: Turtleback Books
Publish Date: 2007-04
ISBN: 9780316465625
Price: $24.19

Quantity: 10
---------------------------------------------

Title: 84, Charing Cross Road
Author: Helene Hanff, Frank Doel
Categories: American Authors
Genres: American Authors
Publisher: French
Publish Date: Sep 02, 1970
ISBN: 9781559210546
Price: $22.52

Quantity: 17
---------------------------------------------

Title: The Restaurant at the End of the Universe
Author: Douglas Adams
Categories: Fiction
Genres: Fiction
Publisher: Audio Literature
Publish Date: 1985
ISBN: 0297786563
Price: $10.39

Quantity: 16
---------------------------------------------

Title: Fast Food Nation
Author: Eric Schlosser
Categories: politics
Genres: politics
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: January 8, 2002
ISBN: 9780553529005
Price: $9.63

Quantity: 1
---------------------------------------------

Title: Midnight in the Garden of Good and Evil
Author: John Berendt
Categories: Social life and customs
Genres: Social life and customs
Publisher: Belfond
Publish Date: March 26, 1998
ISBN: 2266075187
Price: $19.60

Quantity: 3
---------------------------------------------

Title: The Magician's Nephew
Author: C.S. Lewis
Categories: Fantasy
Genres: Fantasy
Publisher: Bonniers juniorförl.
Publish Date: October 2, 2001
ISBN: 9780871293688
Price: $24.08

Quantity: 3
---------------------------------------------

Title: Everything I never told you
Author: Celeste Ng
Categories: Grief
Genres: Grief
Publisher: Bollati Boringhieri
Publish Date: Sep 28, 2016
ISBN: 9781785410987
Price: $23.43

Quantity: 16
---------------------------------------------

Title: The Hero of Ages
Author: Brandon Sanderson
Categories: Fiction
Genres: Fiction
Publisher: Tor
Publish Date: April 28, 2009
ISBN: 9788498727951
Price: $9.42

Quantity: 9
---------------------------------------------

Title: Something blue
Author: Emily Giffin
Categories: Rejection (Psychology)
Genres: Rejection (Psychology)
Publisher: Thorndike Press
Publish Date: 2005
ISBN: 9780312323851
Price: $14.34

Quantity: 14
---------------------------------------------

Title: Candide
Author: Voltaire
Categories: Conduct of life
Genres: Conduct of life
Publisher: Collier Macmillan
Publish Date: Jun 30, 2005
ISBN: 0300106556
Price: $7.03

Quantity: 18
---------------------------------------------

Title: The World According to Garp
Author: John Irving
Categories: National Book Award Winner
Genres: National Book Award Winner
Publisher: Books On Tape
Publish Date: December 1, 1987
ISBN: 0739320890
Price: $13.10

Quantity: 12
---------------------------------------------

Title: A Court of Mist and Fury
Author: Sarah J. Maas
Categories: Fantasy
Genres: Fantasy
Publisher: Planeta
Publish Date: 05. August 2021
ISBN: 1681192713
Price: $5.15

Quantity: 9
---------------------------------------------

Title: Go Set A Watchman
Author: Harper Lee
Categories: Adult children of aging parents
Genres: Adult children of aging parents
Publisher: Harper
Publish Date: 2016
ISBN: 1784752460
Price: $15.39

Quantity: 3
---------------------------------------------

Title: Thinking, fast and slow
Author: Daniel Kahneman
Categories: Intuition
Genres: Intuition
Publisher: Penguin Verlag
Publish Date: Nov 14, 2017
ISBN: 8934956151
Price: $5.37

Quantity: 5
---------------------------------------------

Title: Slammed
Author: Colleen Hoover
Categories: Fiction, Romance, Contemporary, Life change events
Genres: Fiction, Romance, Contemporary, Life change events
Publisher: Wydawnictwo W.A.B.
Publish Date: 2015
ISBN: 1476715904
Price: $20.60

Quantity: 1
---------------------------------------------

Title: Shadow and Bone
Author: Leigh Bardugo
Categories: Magic
Genres: Magic
Publisher: Turtleback Books
Publish Date: 2013-05
ISBN: 9786051869346
Price: $11.57

Quantity: 10
---------------------------------------------

Title: Postmortem
Author: Patricia Cornwell
Categories: N/A
Genres: N/A
Publisher: Scribner
Publish Date: 1990
ISBN: 9780708848517
Price: $18.95

Quantity: 16
---------------------------------------------

Title: Cujo
Author: Stephen King
Categories: suspense
Genres: suspense
Publisher: Futura
Publish Date: 2002?
ISBN: 9780751526868
Price: $9.53

Quantity: 9
---------------------------------------------

Title: The Great Hunt
Author: Robert Jordan
Categories: Rand al'Thor (Fictitious character)
Genres: Rand al'Thor (Fictitious character)
Publisher: Tor
Publish Date: 2005-12-31
ISBN: 9781250901224
Price: $8.85

Quantity: 17
---------------------------------------------

Title: Hillbilly Elegy
Author: J. D. Vance
Categories: Mountain people
Genres: Mountain people
Publisher: Harper
Publish Date: 2016
ISBN: 9788423427239
Price: $15.58

Quantity: 11
---------------------------------------------

Title: Cloud Atlas
Author: David Mitchell
Categories: Fate and fatalism
Genres: Fate and fatalism
Publisher: Books on Tape, Inc.
Publish Date: 2013-02-03
ISBN: 1444780336
Price: $20.98

Quantity: 13
---------------------------------------------

Title: Things We Left Behind
Author: Collen hoover
Categories: Fiction, romance, romantic comedy
Genres: Fiction, romance, romantic comedy
Publisher: Center Point Large Print
Publish Date: Sep 05, 2023
ISBN: 9781728276120
Price: $14.93

Quantity: 20
---------------------------------------------

Title: Oryx and Crake
Author: Margaret Atwood
Categories: Literary Fiction
Genres: Literary Fiction
Publisher: Ōkeanida
Publish Date: 2006
ISBN: 7806578080
Price: $19.99

Quantity: 3
---------------------------------------------

Title: A Wizard of Earthsea
Author: Ursula K. Le Guin
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: January 1997
ISBN: 9788445075296
Price: $15.05

Quantity: 15
---------------------------------------------

Title: Dead as a doornail
Author: Charlaine Harris
Categories: Detective and mystery stories
Genres: Detective and mystery stories
Publisher: Cengage Gale
Publish Date: April 25, 2006
ISBN: 9780786556786
Price: $6.90

Quantity: 5
---------------------------------------------

Title: Assassin's Apprentice
Author: Robin Hobb
Categories: Fiction, fantasy, general
Genres: Fiction, fantasy, general
Publisher: Libros Sin Fronteras Inventory
Publish Date: 2011
ISBN: 0002246066
Price: $12.27

Quantity: 3
---------------------------------------------

Title: It's Kind of a Funny Story
Author: Ned Vizzini
Categories: Mental illness
Genres: Mental illness
Publisher: sjsjah
Publish Date: 2007
ISBN: 1467630470
Price: $17.42

Quantity: 20
---------------------------------------------

Title: Kai Wiedenhöfer : WALL and PEACE
Author: Kai Wiedenhöfer
Categories: N/A
Genres: N/A
Publisher: Steidl Druckerei und Verlag, Gerhard
Publish Date: 2019
ISBN: 9783958295711
Price: $10.14

Quantity: 15
---------------------------------------------

Title: In her shoes
Author: Jodi Picocell
Categories: Death
Genres: Death
Publisher: Thorndike Press
Publish Date: 2003
ISBN: 9780743267113
Price: $17.36

Quantity: 6
---------------------------------------------

Title: The Walking Dead, Vol. 1
Author: Robert Kirkman, Tony Moore
Categories: Horror comic books, strips
Genres: Horror comic books, strips
Publisher: Image Comics
Publish Date: 2004
ISBN: 1582406723
Price: $5.52

Quantity: 5
---------------------------------------------

Title: The Master and Margarita
Author: Edward Kemp
Categories: Stage adaptations
Genres: Stage adaptations
Publisher: Oberon
Publish Date: 2004
ISBN: 1840024488
Price: $5.29

Quantity: 11
---------------------------------------------

Title: The Mysterious Affair at Styles
Author: Agatha Christie
Categories: Fiction
Genres: Fiction
Publisher: SDE Classics
Publish Date: July 1997
ISBN: 9781604506761
Price: $8.47

Quantity: 1
---------------------------------------------

Title: The Scorch Trials
Author: James Dashner
Categories: Science fiction
Genres: Science fiction
Publisher: KaBOOM!
Publish Date: Jun 23, 2015
ISBN: 9780385907453
Price: $8.01

Quantity: 7
---------------------------------------------

Title: Mrs. Dalloway
Author: Virginia Woolf
Categories: Fiction
Genres: Fiction
Publisher: Hogarth Press
Publish Date: September 18, 2003
ISBN: 9781731523259
Price: $13.33

Quantity: 15
---------------------------------------------

Title: Eleanor Oliphant is Completely Fine
Author: Gail Honeyman
Categories: Women’s Fiction
Genres: Women’s Fiction
Publisher: Penguin Canada
Publish Date: 2018
ISBN: 1432847686
Price: $16.56

Quantity: 18
---------------------------------------------

Title: Heir of Fire
Author: Sarah J. Maas
Categories: Magic
Genres: Magic
Publisher: 城邦文化事業股份有限公司
Publish Date: Sep 06, 2021
ISBN: 9789571061535
Price: $20.83

Quantity: 3
---------------------------------------------

Title: Breakfast at Tiffany's
Author: Truman Capote
Categories: American Short stories
Genres: American Short stories
Publisher: Círculo de Lectores
Publish Date: 1956
ISBN: 3499104598
Price: $10.87

Quantity: 17
---------------------------------------------

Title: The Prophet
Author: Kahlil Gibran
Categories: American Prose poems
Genres: American Prose poems
Publisher: Aims Intl Books Corp
Publish Date: Mar 31, 2021
ISBN: 9781684223114
Price: $10.18

Quantity: 4
---------------------------------------------

Title: Milk and Honey
Author: Rupi Kaur
Categories: Canadian poetry
Genres: Canadian poetry
Publisher: Andrews McMeel
Publish Date: 2016
ISBN: 9781449474256
Price: $15.80

Quantity: 20
---------------------------------------------

Title: Year One (Batman
Author: Frank Miller
Categories: N/A
Genres: N/A
Publisher: Tandem Library
Publish Date: October 1997
ISBN: 0613919459
Price: $16.53

Quantity: 1
---------------------------------------------

Title: The Drawing of the Three
Author: Stephen King
Categories: sociopaths
Genres: sociopaths
Publisher: Penguin Random House Audio Publishing Group
Publish Date: Jun 19, 2015
ISBN: 5170034113
Price: $5.44

Quantity: 6
---------------------------------------------

Title: All Together Dead (Southern Vampire Mysteries, Book 7)
Author: Charlaine Harris
Categories: Mystery
Genres: Mystery
Publisher: 
Publish Date: March 2, 2010
ISBN: 0441019382
Price: $16.42

Quantity: 15
---------------------------------------------

Title: Inheritance Games
Author: Jennifer Lynn Barnes
Categories: Children's fiction
Genres: Children's fiction
Publisher: Media Rodzina
Publish Date: 2021
ISBN: 0241476186
Price: $22.59

Quantity: 7
---------------------------------------------

Title: Definitely Dead (Southern Vampire Mysteries, Book 6)
Author: Charlaine Harris
Categories: sookie stackhouse
Genres: sookie stackhouse
Publisher: Orion Publishing Group
Publish Date: Mar 27, 2007
ISBN: 0606121552
Price: $22.60

Quantity: 20
---------------------------------------------

Title: Saga, Vol. 1
Author: Brian K. Vaughan
Categories: N/A
Genres: N/A
Publisher: Image Comics
Publish Date: 2012
ISBN: 1607066017
Price: $5.41

Quantity: 10
---------------------------------------------

Title: The Wind-up Bird Chronicle
Author: 村上春樹
Categories: N/A
Genres: N/A
Publisher: Lulu Press, Inc.
Publish Date: 2016
ISBN: 9781860464690
Price: $22.77

Quantity: 13
---------------------------------------------

Title: The Silmarillion
Author: J.R.R. Tolkien
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: HarperCollins Publishers Ltd
Publish Date: Aug 31, 2004
ISBN: 9780261103665
Price: $8.25

Quantity: 13
---------------------------------------------

Title: The Dragon Reborn
Author: Robert Jordan
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Intrínseca
Publish Date: 1991-01-01
ISBN: 3492959342
Price: $22.52

Quantity: 17
---------------------------------------------

Title: David Copperfield
Author: Charles Dickens
Categories: Fiction
Genres: Fiction
Publisher: Independently published
Publish Date: 1986-01-01
ISBN: 0404091393
Price: $19.34

Quantity: 3
---------------------------------------------

Title: Prodigy
Author: Marie Lu
Categories: Criminals
Genres: Criminals
Publisher: Jian duan chu ban
Publish Date: Jan 05, 2013
ISBN: 9025751458
Price: $9.62

Quantity: 12
---------------------------------------------

Title: Pretty Little Liars
Author: Sara Shepard
Categories: Fiction
Genres: Fiction
Publisher: Little, Brown Book Group Limited
Publish Date: 2012
ISBN: 9781907410710
Price: $22.63

Quantity: 3
---------------------------------------------

Title: The Prince of Tides
Author: Pat Conroy
Categories: Fiction
Genres: Fiction
Publisher: AudioGO
Publish Date: 1988
ISBN: 0553172794
Price: $15.96

Quantity: 8
---------------------------------------------

Title: Behind closed doors
Author: Freida McFadden
Categories: Family secrets
Genres: Family secrets
Publisher: St. Martin's Griffin
Publish Date: Aug 09, 2016
ISBN: 1432840118
Price: $20.88

Quantity: 5
---------------------------------------------

Title: Mr. Mercedes
Author: Stephen King
Categories: horror
Genres: horror
Publisher: ALBIN MICHEL
Publish Date: 2021
ISBN: 8378859363
Price: $6.10

Quantity: 14
---------------------------------------------

Book On Writing: A Memoir of the Craft not found on Open Library.Title: Needful Things
Author: Stephen King
Categories: suspense
Genres: suspense
Publisher: HighBridge
Publish Date: Sep 16, 2008
ISBN: 0670779458
Price: $22.38

Quantity: 20
---------------------------------------------

Title: Redeeming Love
Author: Francine Rivers
Categories: Frontier and pioneer life in fiction
Genres: Frontier and pioneer life in fiction
Publisher: G.K. Hall
Publish Date: May 9, 2005
ISBN: 1576738167
Price: $24.72

Quantity: 5
---------------------------------------------

Title: The Martian Chronicles
Author: Ray Bradbury
Categories: American Science fiction
Genres: American Science fiction
Publisher: Booket
Publish Date: 1990
ISBN: 0380973839
Price: $15.04

Quantity: 1
---------------------------------------------

Title: The language of flowers
Author: Vanessa Diffenbaugh
Categories: Young women
Genres: Young women
Publisher: Pan Macmillan
Publish Date: Mar 01, 2012
ISBN: 9780230752580
Price: $18.44

Quantity: 20
---------------------------------------------

Title: Phantom of the Opera
Author: Gaston Leroux
Categories: Paris (france), fiction
Genres: Paris (france), fiction
Publisher: Independently Published
Publish Date: 2019
ISBN: 9781077194090
Price: $14.66

Quantity: 4
---------------------------------------------

Title: Lean In
Author: Sheryl Sandberg, Nell Scovell
Categories: Sandberg, Sheryl
Genres: Sandberg, Sheryl
Publisher: Alfred A. Knopf
Publish Date: 2013
ISBN: 9780385349949
Price: $21.23

Quantity: 3
---------------------------------------------

Title: Don Quixote
Author: Miguel de Cervantes Saavedra
Categories: Don Quixote (Cervantes Saavedra, Miguel de)
Genres: Don Quixote (Cervantes Saavedra, Miguel de)
Publisher: F. A. Brockhaus
Publish Date: April 2008
ISBN: 9788493496012
Price: $24.57

Quantity: 8
---------------------------------------------

Title: The mists of Avalon
Author: Marion Zimmer Bradley
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: Sep 17, 1983
ISBN: 0606255338
Price: $8.02

Quantity: 11
---------------------------------------------

Title: Along for the ride
Author: Sarah Dessen
Categories: Change in fiction
Genres: Change in fiction
Publisher: Penguin USA, Inc.
Publish Date: 2009
ISBN: 1101081465
Price: $9.83

Quantity: 18
---------------------------------------------

Title: The Iron King
Author: Julie Kagawa
Categories: Fiction
Genres: Fiction
Publisher: Mira
Publish Date: 2011
ISBN: 1426847807
Price: $20.42

Quantity: 9
---------------------------------------------

Title: The Life-Changing Magic of Tidying Up
Author: Marie Kondo, Marie Kondo
Categories: Home economics
Genres: Home economics
Publisher: Ten Speed Press
Publish Date: 2015
ISBN: 1410484408
Price: $5.43

Quantity: 12
---------------------------------------------

Title: Life after life
Author: Raymond A. Moody
Categories: Experiencias cercanas a la muerte
Genres: Experiencias cercanas a la muerte
Publisher: Bantam Books
Publish Date: February 1988
ISBN: 9788385475026
Price: $13.48

Quantity: 17
---------------------------------------------

Title: Choke
Author: Chuck Palahniuk
Categories: Literature
Genres: Literature
Publisher: 
Publish Date: Aug 26, 2008
ISBN: 9781417664689
Price: $16.43

Quantity: 10
---------------------------------------------

Title: The Lincoln Lawyer (Mickey Haller #1)
Author: Michael Connelly
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Little, Brown and Company
Publish Date: 2001
ISBN: 9780752873176
Price: $6.78

Quantity: 8
---------------------------------------------

Title: Franny and Zooey
Author: J. D. Salinger
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: 1977
ISBN: 9780553269734
Price: $14.52

Quantity: 6
---------------------------------------------

Title: Uncle Tom's Cabin
Author: Harriet Beecher Stowe
Categories: Master and servant
Genres: Master and servant
Publisher: Panamericana
Publish Date: June 30, 2004
ISBN: 9781425533250
Price: $14.83

Quantity: 19
---------------------------------------------

Title: Are You There God? It's Me, Margaret.
Author: Judy Blume
Categories: Children's Middle Grade Books
Genres: Children's Middle Grade Books
Publisher: Simon & Schuster Children's Publishing
Publish Date: 1976-05
ISBN: 1481409948
Price: $24.57

Quantity: 16
---------------------------------------------

Title: The storied life of A. J. Fikry
Author: Gabrielle Zevin
Categories: Widowers
Genres: Widowers
Publisher: Algonquin Books of Chapel Hill
Publish Date: 2015
ISBN: 9780670068241
Price: $17.07

Quantity: 12
---------------------------------------------

Title: The Subtle Art of Not Giving a F*ck
Author: Mark Manson
Categories: Self-realization
Genres: Self-realization
Publisher: Butik Yaynlar
Publish Date: Jul 03, 2018
ISBN: 855100249X
Price: $24.95

Quantity: 14
---------------------------------------------

Title: Timeline
Author: Michael Crichton
Categories: Fiction
Genres: Fiction
Publisher: ĖKSMO-Press
Publish Date: Nov 14, 2000
ISBN: 9780613336338
Price: $12.00

Quantity: 2
---------------------------------------------

Title: The Silkworm
Author: J. K. Rowling
Categories: missing persons
Genres: missing persons
Publisher: Little, Brown & Company
Publish Date: 2014
ISBN: 1405514973
Price: $12.76

Quantity: 14
---------------------------------------------

Title: Americanah
Author: Chimamanda Ngozi Adichie
Categories: Nigerians
Genres: Nigerians
Publisher: Large Print Press
Publish Date: 2016
ISBN: 0307455920
Price: $21.38

Quantity: 13
---------------------------------------------

Title: Jonathan Strange and Mr. Norrell
Author: Susanna Clarke
Categories: England, fiction
Genres: England, fiction
Publisher: Editorial Empúries
Publish Date: January 2, 2007
ISBN: 9781408803745
Price: $16.54

Quantity: 6
---------------------------------------------

Title: Zen and the Art of Motorcycle Maintenance
Author: Robert M. Pirsig
Categories: Pirsig, Robert M.
Genres: Pirsig, Robert M.
Publisher: Brand: Macmillan Audio
Publish Date: 2098
ISBN: 9780553138757
Price: $17.94

Quantity: 10
---------------------------------------------

Title: Christine
Author: Stephen King
Categories: carbon monoxide
Genres: carbon monoxide
Publisher: Signet
Publish Date: Jun 13, 2001
ISBN: 9780451139733
Price: $17.01

Quantity: 12
---------------------------------------------

Title: Truly Madly Guilty
Author: Liane Moriarty
Categories: Couples
Genres: Couples
Publisher: Turtleback Books
Publish Date: May 30, 2016
ISBN: 9781594139796
Price: $15.40

Quantity: 3
---------------------------------------------

Title: The forgotten garden
Author: Kate Morton
Categories: Mystery
Genres: Mystery
Publisher: Center Point Pub.
Publish Date: 2009
ISBN: 9781602854925
Price: $22.60

Quantity: 5
---------------------------------------------

Title: The Hate U Give
Author: Angie Thomas
Categories: black lives matter
Genres: black lives matter
Publisher: Harper Collins Publishers
Publish Date: 2021
ISBN: 0062872346
Price: $17.32

Quantity: 3
---------------------------------------------

Title: International Review of Cell and Molecular Biology
Author: Kwang W. Jeon
Categories: Molecular biology
Genres: Molecular biology
Publisher: Elsevier Science & Technology Books
Publish Date: 2015
ISBN: 0124078451
Price: $13.79

Quantity: 1
---------------------------------------------

Title: The Amazing Adventures of Kavalier & Clay
Author: Michael Chabon
Categories: American Humorous stories
Genres: American Humorous stories
Publisher: Picador
Publish Date: 2010
ISBN: 9781597371605
Price: $22.49

Quantity: 10
---------------------------------------------

Title: Anansi Boys
Author: Neil Gaiman, Mónica Faerna, Lenny Henry
Categories: Action and adventure fiction
Genres: Action and adventure fiction
Publisher: Taylor & Francis Group
Publish Date: October 1, 2006
ISBN: 0060515198
Price: $17.66

Quantity: 14
---------------------------------------------

Title: The Short Second Life of Bree Tanner
Author: Stephenie Meyer
Categories: Vampires
Genres: Vampires
Publisher: Morava
Publish Date: Jul 05, 2010
ISBN: 9780307746832
Price: $11.14

Quantity: 1
---------------------------------------------

Title: From dead to worse
Author: Charlaine Harris
Categories: Mystery
Genres: Mystery
Publisher: Ace Books
Publish Date: Apr 16, 2008
ISBN: 0575090022
Price: $13.63

Quantity: 2
---------------------------------------------

Title: Darkly dreaming Dexter
Author: Jeffry P. Lindsay
Categories: Serial murderers
Genres: Serial murderers
Publisher: Recorded Books
Publish Date: December 2004
ISBN: 9781402596322
Price: $11.68

Quantity: 6
---------------------------------------------

Title: Unwind (Unwind #1)
Author: Neal Shusterman
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: Simon & Schuster
Publish Date: 2021
ISBN: 9781416912040
Price: $8.01

Quantity: 3
---------------------------------------------

Title: Twenty Thousand Leagues Under the Sea
Author: Jules Verne
Categories: N/A
Genres: N/A
Publisher: Parents' Magazine's Cultural Institute
Publish Date: 1966-01-01
ISBN: 9781512093599
Price: $17.83

Quantity: 12
---------------------------------------------

Title: Life, the Universe and Everything
Author: Douglas Adams
Categories: sofas
Genres: sofas
Publisher: Audio Literature
Publish Date: May 1985
ISBN: 9781415930519
Price: $11.73

Quantity: 6
---------------------------------------------

Title: When You Are Engulfed in Flames
Author: David Sedaris
Categories: social life and customs
Genres: social life and customs
Publisher: Little, Brown and Co.
Publish Date: 2009-06
ISBN: 9780316032513
Price: $14.56

Quantity: 18
---------------------------------------------

Title: Drums of Autumn
Author: Diana Gabaldon, Geraldine James
Categories: Scottish Americans
Genres: Scottish Americans
Publisher: Random House Audio
Publish Date: 2004
ISBN: 9780099269939
Price: $22.64

Quantity: 12
---------------------------------------------

Title: Bared to You / Reflected in You / Entwined with You
Author: Sylvia Day
Categories: N/A
Genres: N/A
Publisher: Berkley
Publish Date: Apr 06, 2013
ISBN: 0425266060
Price: $5.75

Quantity: 5
---------------------------------------------

Title: Jonathan Livingston Seagull
Author: Richard Bach
Categories: Gulls
Genres: Gulls
Publisher: Scribner
Publish Date: 2015
ISBN: 9781439167298
Price: $23.15

Quantity: 11
---------------------------------------------

Title: I've Got Your Number
Author: Sophie Kinsella
Categories: Young women
Genres: Young women
Publisher: The Dial Press
Publish Date: 2011
ISBN: 9780385342063
Price: $5.01

Quantity: 17
---------------------------------------------

Title: Red Storm Rising
Author: Tom Clancy
Categories: World War III
Genres: World War III
Publisher: Sine nomine
Publish Date: 1986-01-01
ISBN: 1101002344
Price: $12.52

Quantity: 15
---------------------------------------------

Title: The Couple Next Door
Author: Shari Lapena
Categories: Neighbors
Genres: Neighbors
Publisher: Penguin Audio
Publish Date: Mar 06, 2018
ISBN: 9780525590156
Price: $10.18

Quantity: 18
---------------------------------------------

Title: Kitchen Confidential
Author: Anthony Bourdain
Categories: Cooks
Genres: Cooks
Publisher: Bloomsbury Publishing Plc
Publish Date: August 2000
ISBN: 8807880296
Price: $12.38

Quantity: 7
---------------------------------------------

Title: I'd Tell You I Love You, But Then I'd Have to Kill You (Gallagher Girls #1)
Author: Ally Carter
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Hyperinflation books for children
Publish Date: 2006
ISBN: 9781423100034
Price: $13.47

Quantity: 14
---------------------------------------------

Title: Nickel and Dimed
Author: Barbara Ehrenreich, Barbara Ehrenreich, Barbara Ehrenreich, B. EHRENREICH
Categories: Immigrants, united states
Genres: Immigrants, united states
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: 2017-11
ISBN: 1663635749
Price: $19.02

Quantity: 19
---------------------------------------------

Title: Preludes & Nocturnes
Author: Neil Gaiman, Sam Kieth
Categories: Dream
Genres: Dream
Publisher: Titan
Publish Date: Jan 01, 2000
ISBN: 9781417651634
Price: $14.89

Quantity: 18
---------------------------------------------

Title: Gone With the Wind
Author: Margaret Mitchell
Categories: survival
Genres: survival
Publisher: In the future,
Publish Date: 1947
ISBN: 9578477198
Price: $16.73

Quantity: 19
---------------------------------------------

Title: The Boys in the Boat
Author: Daniel James Brown
Categories: University of Washington
Genres: University of Washington
Publisher: Penguin Audio
Publish Date: Oct 01, 2015
ISBN: 9789751038043
Price: $23.78

Quantity: 11
---------------------------------------------

Title: Beastly
Author: Alex Flinn
Categories: Fantasy
Genres: Fantasy
Publisher: HarperCollins
Publish Date: 2007
ISBN: 8809742710
Price: $10.85

Quantity: 18
---------------------------------------------

Title: Every day
Author: David Levithan
Categories: Interpersonal relations
Genres: Interpersonal relations
Publisher: FISCHER FJB
Publish Date: Aug 28, 2012
ISBN: 9785389092891
Price: $18.09

Quantity: 6
---------------------------------------------

Title: This Lullaby
Author: Sarah Dessen
Categories: Juvenile Fiction
Genres: Juvenile Fiction
Publisher: Penguin USA, Inc.
Publish Date: March 8, 2004
ISBN: 0606296794
Price: $12.53

Quantity: 13
---------------------------------------------

Title: Patriot games
Author: Tom Clancy
Categories: Fiction
Genres: Fiction
Publisher: Putnam
Publish Date: 1992
ISBN: 0002231948
Price: $23.03

Quantity: 6
---------------------------------------------

Title: Dead and Gone
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: Orion Publishing Group
Publish Date: 2009-01-01
ISBN: 0575085517
Price: $19.34

Quantity: 18
---------------------------------------------

Title: World Without End
Author: Ken Follett
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: May 18, 2008
ISBN: 1429543620
Price: $15.07

Quantity: 4
---------------------------------------------

Book The DUFF: Designated Ugly Fat Friend not found on Open Library.Title: Ways of Seeing
Author: John Berger
Categories: Art
Genres: Art
Publisher: British Broadcasting Corporation
Publish Date: 1981
ISBN: 9780563122449
Price: $10.16

Quantity: 2
---------------------------------------------

Title: The Lies of Locke Lamora
Author: Scott Lynch
Categories: Fiction, fantasy, general
Genres: Fiction, fantasy, general
Publisher: Subterranean Press
Publish Date: June 27, 2006
ISBN: 9780553804676
Price: $15.33

Quantity: 1
---------------------------------------------

Title: Girl, interrupted
Author: Susanna Kaysen
Categories: Mental health
Genres: Mental health
Publisher: Thorndike Press
Publish Date: 2000
ISBN: 0679423664
Price: $18.21

Quantity: 18
---------------------------------------------

Title: Firestarter
Author: Stephen King
Categories: Genetic Engineering
Genres: Genetic Engineering
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: August 3, 1981
ISBN: 3404130014
Price: $15.85

Quantity: 9
---------------------------------------------

Title: Heidi
Author: Johanna Spyri
Categories: Johanna Spyri
Genres: Johanna Spyri
Publisher: Distributed by Random House
Publish Date: April 1991
ISBN: 9789626347850
Price: $6.87

Quantity: 16
---------------------------------------------

Title: Starship Troopers
Author: Robert A. Heinlein
Categories: Fiction
Genres: Fiction
Publisher: Putnam
Publish Date: 1959
ISBN: 9780425026052
Price: $8.55

Quantity: 9
---------------------------------------------

Title: Small Great Things
Author: Jodi Picoult
Categories: Race relations
Genres: Race relations
Publisher: Hodder & Stoughton
Publish Date: Jun 05, 2018
ISBN: 1432857622
Price: $11.32

Quantity: 7
---------------------------------------------

Title: Orange is the new black
Author: Piper Kerman
Categories: Large type books
Genres: Large type books
Publisher: Replika
Publish Date: 2015-02-01
ISBN: 9789113066455
Price: $19.38

Quantity: 12
---------------------------------------------

Title: Howl's Moving Castle (Howl's Moving Castle #1)
Author: Diana Wynne Jones
Categories: Blessing and cursing
Genres: Blessing and cursing
Publisher: Nocturna Ediciones
Publish Date: 2004
ISBN: 9786053750901
Price: $11.22

Quantity: 3
---------------------------------------------

Book The Hundred-Year-old Man Who Climbed Out a Window… not found on Open Library.Title: The Vampire Lestat
Author: Anne Rice
Categories: nobility
Genres: nobility
Publisher: Albin Michel
Publish Date: 2008
ISBN: 9780356130323
Price: $15.81

Quantity: 3
---------------------------------------------

Title: A Monster Calls
Author: Patrick Ness, Jim Kay, Siobhan Dowd
Categories: Mothers and sons
Genres: Mothers and sons
Publisher: Walker Books Ltd
Publish Date: 2021
ISBN: 0763669091
Price: $14.20

Quantity: 20
---------------------------------------------

Title: Le Morte d'Arthur
Author: Thomas Malory
Categories: Arthurian romances
Genres: Arthurian romances
Publisher: T. Nelson and Sons
Publish Date: 1935
ISBN: 1404317767
Price: $18.48

Quantity: 3
---------------------------------------------

Title: The Bourne supremacy
Author: Robert Ludlum
Categories: Jason Bourne (Fictitious character)
Genres: Jason Bourne (Fictitious character)
Publisher: ĖKSMO
Publish Date: May 6, 2004
ISBN: 9780752867977
Price: $16.50

Quantity: 10
---------------------------------------------

Title: The Underground Railroad
Author: Colson Whitehead
Categories: FICTION / African American / General
Genres: FICTION / African American / General
Publisher: Doubleday
Publish Date: Mar 26, 2016
ISBN: 0345804325
Price: $16.24

Quantity: 13
---------------------------------------------

Title: Aristotle and Dante discover the secrets of the universe
Author: Benjamin Alire Sáenz
Categories: Mexican-Americans
Genres: Mexican-Americans
Publisher: Thorndike Press Large Print
Publish Date: 2015
ISBN: 1398505242
Price: $22.46

Quantity: 14
---------------------------------------------

Title: High Fidelity
Author: Nick Hornby
Categories: Sound recordings
Genres: Sound recordings
Publisher: Penguin Group UK
Publish Date: 2008
ISBN: 9783462025248
Price: $8.17

Quantity: 8
---------------------------------------------

Title: The Omnivore's Dilemma
Author: Richie Chevat, Michael Pollan
Categories: Food supply
Genres: Food supply
Publisher: Dial Books
Publish Date: Jan 01, 2011
ISBN: 1101993839
Price: $11.69

Quantity: 14
---------------------------------------------

Title: Death of a Salesman
Author: Arthur Miller
Categories: flashback
Genres: flashback
Publisher: Viking Press
Publish Date: April 10, 2003
ISBN: 0891907297
Price: $7.59

Quantity: 20
---------------------------------------------

Title: Sophie's world
Author: Jostein Gaarder
Categories: Fiction
Genres: Fiction
Publisher: Orion Publishing Group, Limited
Publish Date: 1996
ISBN: 1857992911
Price: $19.24

Quantity: 6
---------------------------------------------

Title: King Lear
Author: William Shakespeare
Categories: Drama
Genres: Drama
Publisher: Hyperion Books
Publish Date: 1959
ISBN: 9798667113928
Price: $21.85

Quantity: 2
---------------------------------------------

Title: Lover Eternal
Author: J. R. Ward
Categories: Fiction
Genres: Fiction
Publisher: Signet
Publish Date: 2008
ISBN: 0451218043
Price: $21.66

Quantity: 14
---------------------------------------------

Title: 1Q84
Author: 村上春樹
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Brilliance Audio
Publish Date: Oct 27, 2012
ISBN: 9780099526148
Price: $7.67

Quantity: 12
---------------------------------------------

Title: Six of Crows
Author: Leigh Bardugo
Categories: Young adult fiction
Genres: Young adult fiction
Publisher: Square Fish
Publish Date: 2016
ISBN: 1780622279
Price: $12.66

Quantity: 2
---------------------------------------------

Title: The Passage
Author: Justin Cronin
Categories: FICTION
Genres: FICTION
Publisher: Random House Inc.
Publish Date: 2011-03
ISBN: 9780345528179
Price: $14.33

Quantity: 16
---------------------------------------------

Title: A heartbreaking work of staggering genius
Author: Dave Eggers
Categories: Death
Genres: Death
Publisher: Turtleback Books
Publish Date: April 10, 2003
ISBN: 0330484559
Price: $9.95

Quantity: 5
---------------------------------------------

Title: 1776
Author: David McCullough
Categories: Sources
Genres: Sources
Publisher: Shi bao wen hua chu ban qi ye gu fen you xian gong si
Publish Date: October 2, 2007
ISBN: 957134494X
Price: $20.55

Quantity: 18
---------------------------------------------

Title: Simon vs. the Homo Sapiens Agenda
Author: Becky Albertalli
Categories: LGBT
Genres: LGBT
Publisher: Urano
Publish Date: 2015
ISBN: 9780062348692
Price: $13.16

Quantity: 5
---------------------------------------------

Title: The rescue
Author: Nicholas Sparks
Categories: Handicapped children
Genres: Handicapped children
Publisher: Warner Books
Publish Date: September 17, 2001
ISBN: 9780446696128
Price: $7.26

Quantity: 4
---------------------------------------------

Book From the Mixed-Up Files of Mrs. Basil E. Frankenweiler not found on Open Library.Title: Specials
Author: Scott Westerfeld
Categories: Reading Level-Grade 9
Genres: Reading Level-Grade 9
Publisher: Simon & Schuster Children's
Publish Date: May 03, 2011
ISBN: 9781847389084
Price: $11.49

Quantity: 4
---------------------------------------------

Title: The Circle
Author: Dave Eggers
Categories: multiple sclerosis
Genres: multiple sclerosis
Publisher: Noordhoff
Publish Date: 2014
ISBN: 9781594139611
Price: $7.50

Quantity: 3
---------------------------------------------

Title: The Wind in the Willows
Author: Kenneth Grahame
Categories: Fiction
Genres: Fiction
Publisher: Audio Book Contractors, LLC
Publish Date: 1932
ISBN: 9780140350876
Price: $8.21

Quantity: 13
---------------------------------------------

Title: Bloodline.
Author: Sidney Sheldon
Categories: Translations into Russian
Genres: Translations into Russian
Publisher: Warner Books, Inc., A Time Warner Company
Publish Date: 1998
ISBN: 9780446852050
Price: $21.65

Quantity: 1
---------------------------------------------

Title: A People's History of the United States
Author: H. Zinn, Howard Zinn
Categories: nyt:paperback_nonfiction=2010-05-16
Genres: nyt:paperback_nonfiction=2010-05-16
Publisher: Brand: HarperAudio
Publish Date: October 1998
ISBN: 9780062397348
Price: $19.83

Quantity: 6
---------------------------------------------

Title: Hollow City
Author: Ransom Riggs
Categories: Orphanages
Genres: Orphanages
Publisher: Quirk
Publish Date: 2015
ISBN: 1594747350
Price: $13.59

Quantity: 2
---------------------------------------------

Title: Wallbanger
Author: Alice Clayton
Categories: Erotic stories
Genres: Erotic stories
Publisher: Omnific Publishing
Publish Date: 2015
ISBN: 1623420024
Price: $22.90

Quantity: 6
---------------------------------------------

Book A Visit from the Good Squad not found on Open Library.Title: Homegoing
Author: Yaa Gyasi
Categories: African American Historical Fiction
Genres: African American Historical Fiction
Publisher: Spring International Publishers
Publish Date: 2017 March
ISBN: 9788498389562
Price: $17.26

Quantity: 16
---------------------------------------------

Title: The Waste Lands
Author: Stephen King
Categories: thrillers
Genres: thrillers
Publisher: Ediciones B, S.A.
Publish Date: April 1992
ISBN: 9875666963
Price: $12.43

Quantity: 11
---------------------------------------------

Title: On Dublin Street
Author: Samantha Young
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Penguin Books
Publish Date: 2013
ISBN: 1405912987
Price: $10.16

Quantity: 2
---------------------------------------------

Title: Shōgun (Asian Saga
Author: James Clavell
Categories: Fiction
Genres: Fiction
Publisher: Librairie Générale Française
Publish Date: April 1989
ISBN: 0689105657
Price: $19.07

Quantity: 11
---------------------------------------------

Title: House of the Spirits
Author: N/A
Categories: Fiction, family life, general
Genres: Fiction, family life, general
Publisher: Penguin Random House
Publish Date: 2014
ISBN: 9780099593898
Price: $23.69

Quantity: 13
---------------------------------------------

Title: Dreams from My Father
Author: Barack Obama, FERNANDO MIRANDA MURO, EVARISTO PAEZ RASMUSSEN, EVARISTO PAEZ RASMUSSEN, Canongate
Categories: Racially mixed people
Genres: Racially mixed people
Publisher: Canongate
Publish Date: 2016
ISBN: 1921569204
Price: $17.43

Quantity: 20
---------------------------------------------

Title: The Remains of the Day
Author: Kazuo Ishiguro
Categories: Man Booker Prize Winner
Genres: Man Booker Prize Winner
Publisher: Knopf
Publish Date: December 31, 1998
ISBN: 9789750841729
Price: $5.18

Quantity: 5
---------------------------------------------

Title: Around The World In Eighty Days
Author: Jules Verne
Categories: N/A
Genres: N/A
Publisher: Dodd, Mead and Company
Publish Date: 2006-01-01
ISBN: 0333084411
Price: $13.46

Quantity: 16
---------------------------------------------

Title: Everything Is Illuminated
Author: Jonathan Safran Foer
Categories: Humorous stories
Genres: Humorous stories
Publisher: Turtleback Books
Publish Date: 2004
ISBN: 9788661450655
Price: $15.58

Quantity: 10
---------------------------------------------

Title: The Hunting of the Snark
Author: Lewis Carroll
Categories: Bibliography
Genres: Bibliography
Publisher: Manus Presse
Publish Date: December 30, 2005
ISBN: 9780913232989
Price: $21.78

Quantity: 4
---------------------------------------------

Title: The good girl's guide to murder
Author: McBride, Susan, SUSAN MCBRIDE
Categories: American Humorous stories
Genres: American Humorous stories
Publisher: Avon
Publish Date: 2005-02-01
ISBN: 0739450484
Price: $13.16

Quantity: 9
---------------------------------------------

Title: Walking disaster
Author: Jamie McGuire
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Simon & Schuster, Limited
Publish Date: 2013
ISBN: 9781476712987
Price: $24.31

Quantity: 12
---------------------------------------------

Title: Mrs. Frisby and the Rats of Nimh
Author: Robert C. O'Brien, Zena Bernstein
Categories: Ficción juvenil
Genres: Ficción juvenil
Publisher: Novel Units
Publish Date: 2011-03-28
ISBN: 9780745101330
Price: $22.05

Quantity: 3
---------------------------------------------

Title: Star Wars - Thrawn Trilogy - Heir to the Empire
Author: Timothy Zahn
Categories: star wars
Genres: star wars
Publisher: Turtleback Books
Publish Date: January 1991
ISBN: 0553296124
Price: $7.54

Quantity: 2
---------------------------------------------

Title: The Ontario readers
Author: Ontario. Ministry of Education.
Categories: N/A
Genres: N/A
Publisher: Copp, Clark
Publish Date: 1917
ISBN: 9781428051256
Price: $6.69

Quantity: 3
---------------------------------------------

Title: The Awakening
Author: Kate Chopin
Categories: Adultery
Genres: Adultery
Publisher: Lulu.com
Publish Date: 2011-09-19
ISBN: 9798477684113
Price: $7.27

Quantity: 3
---------------------------------------------

Title: The Blind Assassin
Author: Margaret Atwood
Categories: Death
Genres: Death
Publisher: Ōkeanida
Publish Date: Oct 01, 2008
ISBN: 9780007113606
Price: $16.16

Quantity: 3
---------------------------------------------

Title: Queen of Shadows
Author: Sarah J. Maas
Categories: Magic
Genres: Magic
Publisher: Audible Studios
Publish Date: 2017
ISBN: 1408858614
Price: $17.12

Quantity: 16
---------------------------------------------

Title: Different Seasons
Author: Stephen King
Categories: first-person narrative
Genres: first-person narrative
Publisher: Turtleback Books
Publish Date: 2004
ISBN: 6073125852
Price: $19.34

Quantity: 2
---------------------------------------------

Title: Fallen too far
Author: Abbi Glines
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Atria Books
Publish Date: 2014
ISBN: 9781476775982
Price: $22.93

Quantity: 18
---------------------------------------------

Title: The Rainmaker
Author: John Grisham
Categories: Fiction
Genres: Fiction
Publisher: Debolsillo
Publish Date: January 1, 2001
ISBN: 0307576051
Price: $23.12

Quantity: 15
---------------------------------------------

Title: Bag of Bones
Author: Stephen King
Categories: trials
Genres: trials
Publisher: Thorndike Press
Publish Date: November 30, 2003
ISBN: 9780340718209
Price: $16.83

Quantity: 18
---------------------------------------------

Title: Summary of Sapiens : a Brief History of Humankind
Author: BookNation
Categories: N/A
Genres: N/A
Publisher: Independently Published
Publish Date: 2020
ISBN: 9798573065472
Price: $18.18

Quantity: 15
---------------------------------------------

Title: The Capture (Guardians of Ga'Hoole, Book 1)
Author: Kathryn Lasky, Pamela Garelick
Categories: Juvenile fiction
Genres: Juvenile fiction
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: June 15, 2006
ISBN: 0606304703
Price: $24.23

Quantity: 6
---------------------------------------------

Title: Alex Haley's The autobiography of Malcolm X
Author: Harold Bloom
Categories: African American Muslims
Genres: African American Muslims
Publisher: Bloom's Literary Criticism
Publish Date: 2008
ISBN: 079109832X
Price: $9.08

Quantity: 7
---------------------------------------------

Title: Thinner
Author: Stephen King
Categories: gluttony
Genres: gluttony
Publisher: Penguin USA, Inc.
Publish Date: Feb 08, 2011
ISBN: 9780451190758
Price: $6.99

Quantity: 17
---------------------------------------------

Book Batman: The Dark Knight Returns not found on Open Library.Title: Snow Falling on Cedars
Author: David Guterson
Categories: Dear John letters
Genres: Dear John letters
Publisher: Random House Audio
Publish Date: Nov 15, 1998
ISBN: 9780747540731
Price: $12.14

Quantity: 4
---------------------------------------------

Title: Moon called
Author: Patricia Briggs, David Lawrence, Patricia Briggs
Categories: Fiction
Genres: Fiction
Publisher: Penguin Publishing Group
Publish Date: January 31, 2006
ISBN: 9780786579303
Price: $21.07

Quantity: 12
---------------------------------------------

Title: Lover Awakened
Author: J. R. Ward
Categories: Fiction
Genres: Fiction
Publisher: New American Library
Publish Date: 2008
ISBN: 9781429522434
Price: $10.28

Quantity: 15
---------------------------------------------

Title: The Dead Zone
Author: Stephen King
Categories: brain tumors
Genres: brain tumors
Publisher: Sperling paperback
Publish Date: 2006-11
ISBN: 9781101138144
Price: $13.97

Quantity: 3
---------------------------------------------

Title: The Girl with All the Gifts
Author: M. R. Carey
Categories: Zombies
Genres: Zombies
Publisher: Librairie L'Atalante
Publish Date: June 10, 2014
ISBN: 9780356502731
Price: $11.33

Quantity: 7
---------------------------------------------

Title: The Blood of Olympus
Author: Rick Riordan
Categories: Greek mythology
Genres: Greek mythology
Publisher: Disney - Hyperion
Publish Date: Oct 28, 2014
ISBN: 9789573276548
Price: $21.26

Quantity: 15
---------------------------------------------

Title: Firefly Lane
Author: Kristin Hannah
Categories: Friendship in adolescence in fiction
Genres: Friendship in adolescence in fiction
Publisher: Center Point Pub.
Publish Date: 2008
ISBN: 9781602851443
Price: $16.42

Quantity: 12
---------------------------------------------

Title: Aristotle and Dante Dive into the Waters of the World
Author: Benjamin Alire Sáenz
Categories: N/A
Genres: N/A
Publisher: Simon & Schuster, Limited
Publish Date: 2021
ISBN: 9781534496217
Price: $8.71

Quantity: 6
---------------------------------------------

Title: Scott Pilgrim's Precious Little Life (Scott Pilgrim, Vol. 1)
Author: Bryan Lee O'Malley
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Oni Press
Publish Date: Mar 18, 2022
ISBN: 0007362994
Price: $24.93

Quantity: 2
---------------------------------------------

Title: The Exorcist
Author: William Peter Blatty
Categories: Fiction
Genres: Fiction
Publisher: BLOND&BRIGGS
Publish Date: 1994-02
ISBN: 9780062125897
Price: $10.82

Quantity: 6
---------------------------------------------

Title: The Hunchback of Notre-Dame
Author: Victor Hugo
Categories: N/A
Genres: N/A
Publisher: Prakash Book Depot
Publish Date: 1968-01-01
ISBN: 9781613825365
Price: $18.36

Quantity: 4
---------------------------------------------

Title: State of wonder
Author: Ann Patchett
Categories: Medicine
Genres: Medicine
Publisher: Harper
Publish Date: 2011
ISBN: 0062049801
Price: $11.96

Quantity: 17
---------------------------------------------

Title: Prey
Author: Michael Crichton
Categories: programmers
Genres: programmers
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: 2002-01-01
ISBN: 9781417669899
Price: $9.92

Quantity: 4
---------------------------------------------

Title: Hyperbole and a Half
Author: Allie Brosh
Categories: hyperboleandahalf
Genres: hyperboleandahalf
Publisher: Alibri
Publish Date: Oct 17, 1900
ISBN: 9780606340670
Price: $8.39

Quantity: 5
---------------------------------------------

Title: Sphere
Author: Michael Crichton, Jacques Polanis
Categories: space ships
Genres: space ships
Publisher: Rowohlt TB-V. Rnb.
Publish Date: September 3, 1987
ISBN: 9781501216817
Price: $14.52

Quantity: 19
---------------------------------------------

Title: Turtles All the Way Down
Author: John Green
Categories: Anxiety disorders
Genres: Anxiety disorders
Publisher: Bukowy Las
Publish Date: 10 october 2017
ISBN: 1509460810
Price: $17.03

Quantity: 8
---------------------------------------------

Title: The Plain Truth
Author: Jodi Picoult
Categories: Amish
Genres: Amish
Publisher: Recorded Books
Publish Date: September 13, 2004
ISBN: 9781416547815
Price: $12.02

Quantity: 3
---------------------------------------------

Title: Mr. Penumbra's 24-hour bookstore
Author: Robin Sloan
Categories: Fiction
Genres: Fiction
Publisher: Farrar, Straus and Giroux
Publish Date: 2013
ISBN: 0374214913
Price: $14.95

Quantity: 20
---------------------------------------------

Title: Veronika decides to die
Author: Paulo Coelho
Categories: Paulo Coelho
Genres: Paulo Coelho
Publisher: Thorsons
Publish Date: 2000
ISBN: 9780722540442
Price: $13.24

Quantity: 12
---------------------------------------------

Title: The Invention of Hugo Cabret
Author: Brian Selznick
Categories: historical fiction
Genres: historical fiction
Publisher: Scholastic Audio
Publish Date: 2008
ISBN: 9788467520446
Price: $24.30

Quantity: 6
---------------------------------------------

Title: Hyperion
Author: Dan Simmons
Categories: American Science fiction
Genres: American Science fiction
Publisher: Brilliance Audio
Publish Date: Apr 22, 2014
ISBN: 9782266177474
Price: $20.31

Quantity: 7
---------------------------------------------

Title: The Summons
Author: John Grisham
Categories: Mississippi in fiction
Genres: Mississippi in fiction
Publisher: Century
Publish Date: 2004
ISBN: 8466616403
Price: $18.86

Quantity: 4
---------------------------------------------

Title: Harry Potter and the Goblet of Fire
Author: J. K. Rowling
Categories: orphans
Genres: orphans
Publisher: imusti
Publish Date: May 11, 2013
ISBN: 8532530818
Price: $24.13

Quantity: 13
---------------------------------------------

Title: Tempted
Author: Megan Hart
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Spice
Publish Date: January 1, 2008
ISBN: 1426810849
Price: $16.42

Quantity: 13
---------------------------------------------

Title: Dead in the family
Author: Charlaine Harris
Categories: Vampires
Genres: Vampires
Publisher: Isis Large Print
Publish Date: 2012
ISBN: 9780575097131
Price: $21.01

Quantity: 8
---------------------------------------------

Title: Summary and Analysis of Stiff : the Curious Lives of Human Cadavers
Author: Worth Books
Categories: N/A
Genres: N/A
Publisher: Worth Books
Publish Date: 2017
ISBN: 150404407X
Price: $15.79

Quantity: 5
---------------------------------------------

Title: Nights in Rodanthe
Author: Nicholas Sparks
Categories: Divorced people
Genres: Divorced people
Publisher: Vision
Publish Date: 2006
ISBN: 9780446531337
Price: $22.47

Quantity: 2
---------------------------------------------

Title: Congo
Author: Michael Crichton
Categories: kakundakari
Genres: kakundakari
Publisher: PLAZA & JANES
Publish Date: June 1994
ISBN: 8401492343
Price: $16.49

Quantity: 20
---------------------------------------------

Title: The CIDER HOUSE RULES
Author: John Irving
Categories: American fiction (fictional works by one author)
Genres: American fiction (fictional works by one author)
Publisher: Fabbri - RCS Libri
Publish Date: 1989
ISBN: 9780345417947
Price: $10.77

Quantity: 7
---------------------------------------------

Title: The Sound and the Fury
Author: William Faulkner
Categories: American Manuscripts
Genres: American Manuscripts
Publisher: Alianza
Publish Date: June 1946
ISBN: 8447309789
Price: $11.22

Quantity: 14
---------------------------------------------

Title: Witches, midwives, and nurses
Author: Barbara Ehrenreich
Categories: History
Genres: History
Publisher: Feminist Press
Publish Date: June 1972
ISBN: 0912670134
Price: $17.95

Quantity: 16
---------------------------------------------

Title: Beyond Pippi Longstocking
Author: Bettina Kümmerling-Meibauer
Categories: Lindgren, astrid, 1907-2002
Genres: Lindgren, astrid, 1907-2002
Publisher: Taylor & Francis Group
Publish Date: Sep 13, 2014
ISBN: 9781136741890
Price: $19.81

Quantity: 20
---------------------------------------------

Title: Batman Noir the Killing Joke
Author: Alan Moore, Brian Bolland
Categories: Comics & graphic novels, general
Genres: Comics & graphic novels, general
Publisher: DC Comics
Publish Date: 2016
ISBN: 140126364X
Price: $20.80

Quantity: 13
---------------------------------------------

Title: Are You There Vodka? It's Me, Chelsea
Author: Chelsea Handler
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: Downtown Press
Publish Date: 2009
ISBN: 9781448135929
Price: $13.12

Quantity: 18
---------------------------------------------

Title: Angelfall
Author: Susan Ee
Categories: Fantasy
Genres: Fantasy
Publisher: Brilliance Audio
Publish Date: 2012
ISBN: 1469222361
Price: $24.02

Quantity: 16
---------------------------------------------

Title: Let's Pretend This Never Happened (Dear Dumb Diary #1)
Author: Jim Benton
Categories: Humorous stories
Genres: Humorous stories
Publisher: Scholastic Inc.
Publish Date: 2004
ISBN: 9780545010306
Price: $5.73

Quantity: 11
---------------------------------------------

Title: Born a Crime Stories from a South African Childhood
Author: R. Rau
Categories: N/A
Genres: N/A
Publisher: Independently Published
Publish Date: 2021
ISBN: 9798736461943
Price: $20.05

Quantity: 5
---------------------------------------------

Title: The Shadow Rising
Author: Robert Jordan
Categories: Fiction
Genres: Fiction
Publisher: Tor
Publish Date: Sep 08, 1992
ISBN: 1250251923
Price: $5.54

Quantity: 1
---------------------------------------------

Title: Wicked Lovely (Wicked Lovely Series, Book 1)
Author: Melissa Marr
Categories: Fiction
Genres: Fiction
Publisher: HarperCollins
Publish Date: June 12, 2007
ISBN: 0061214655
Price: $9.11

Quantity: 10
---------------------------------------------

Title: Naked in Death
Author: Nora Roberts
Categories: Fiction
Genres: Fiction
Publisher: Brilliance Audio
Publish Date: 1999
ISBN: 9781593352776
Price: $14.24

Quantity: 10
---------------------------------------------

Title: Men are From Mars, Women are From Venus
Author: John Gray, John Gray, John [Ph.D] Gray
Categories: Communication
Genres: Communication
Publisher: Altn Kitaplar
Publish Date: May 1, 1996
ISBN: 0060739533
Price: $23.87

Quantity: 5
---------------------------------------------

Title: The Corrections
Author: Jonathan Franzen
Categories: dementia
Genres: dementia
Publisher: Picador USA
Publish Date: May 23, 2003
ISBN: 9780008329709
Price: $23.45

Quantity: 16
---------------------------------------------

Title: Love the one you're with
Author: Emily Giffin
Categories: Triangles (Interpersonal relations)
Genres: Triangles (Interpersonal relations)
Publisher: St. Martin's Griffin
Publish Date: April 21, 2009
ISBN: 9781410404657
Price: $8.43

Quantity: 3
---------------------------------------------

Title: The White Queen
Author: Philippa Gregory
Categories: Fiction
Genres: Fiction
Publisher: Planeta
Publish Date: August 18, 2009
ISBN: 1416563687
Price: $22.01

Quantity: 10
---------------------------------------------

Title: Unleash the Power of Storytelling
Author: Rob Biesenbach
Categories: Business
Genres: Business
Publisher: Eastlawn Media
Publish Date: 2017
ISBN: 0991081439
Price: $24.75

Quantity: 16
---------------------------------------------

Title: Danny, The Champion of the World
Author: Roald Dahl
Categories: Criminals
Genres: Criminals
Publisher: Livre de Poche Jeunesse
Publish Date: February 2002
ISBN: 849122128X
Price: $22.44

Quantity: 12
---------------------------------------------

Title: The Merchant of Venice
Author: William Shakespeare
Categories: Drama
Genres: Drama
Publisher: Printed by M.P. for Laurence Hayes
Publish Date: December 3, 2004
ISBN: 3125762707
Price: $9.49

Quantity: 10
---------------------------------------------

Book Julie and Julia: 365 Days, 524 Recipes, 1 Tiny Apartment… not found on Open Library.Title: Thoughts on Ishmeal Beah's Novel "A Long Way Gone, Memoirs of a Boy Soldier"
Author: Victoria Schwer
Categories: N/A
Genres: N/A
Publisher: GRIN Publishing
Publish Date: Mar 04, 2014
ISBN: 3656594716
Price: $21.35

Quantity: 8
---------------------------------------------

Title: A Lingering Melody
Author: Patricia Wilson
Categories: Fiction, Romance, Contemporary
Genres: Fiction, Romance, Contemporary
Publisher: Ulverscroft Large Print
Publish Date: 1994
ISBN: 0750507489
Price: $22.14

Quantity: 4
---------------------------------------------

Title: Beautiful Ruins
Author: Jess Walter
Categories: Italy, fiction
Genres: Italy, fiction
Publisher: HarperCollins Publishers
Publish Date: 2015
ISBN: 0062349554
Price: $20.48

Quantity: 8
---------------------------------------------

Title: The Unbecoming of Mara Dyer (Mara Dyer Series, Book 1)
Author: Michelle Hodkin
Categories: Post-traumatic stress disorder
Genres: Post-traumatic stress disorder
Publisher: imusti
Publish Date: Mar 01, 2012
ISBN: 1442421770
Price: $17.42

Quantity: 15
---------------------------------------------

Title: Twelth Night
Author: N/A
Categories: N/A
Genres: N/A
Publisher: Independently Published
Publish Date: 2019
ISBN: 9781692185077
Price: $11.33

Quantity: 4
---------------------------------------------

Title: Just kids
Author: Patti Smith
Categories: Women poets
Genres: Women poets
Publisher: HarperCollins Publishers
Publish Date: 2012
ISBN: 9783596188857
Price: $12.84

Quantity: 5
---------------------------------------------

Title: Interpreter of maladies
Author: Jhumpa Lahiri
Categories: East Indian Americans
Genres: East Indian Americans
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: April 20, 2004
ISBN: 9781722350215
Price: $7.97

Quantity: 4
---------------------------------------------

Title: Houghton Mifflin the Nation's Choice
Author: Houghton Mifflin Company Staff
Categories: Dolphins
Genres: Dolphins
Publisher: Houghton Mifflin
Publish Date: 2001
ISBN: 0618201076
Price: $15.49

Quantity: 2
---------------------------------------------

Title: Long Walk to Freedom
Author: Nelson Mandela, Chris Van Wyk, Paddy Bouma
Categories: Biography
Genres: Biography
Publisher: Grand Central Publishing
Publish Date: January 2, 2003
ISBN: 0759501386
Price: $13.36

Quantity: 7
---------------------------------------------

Title: Becoming attached
Author: Robert Karen
Categories: Attachment behavior
Genres: Attachment behavior
Publisher: Oxford University Press, Incorporated
Publish Date: 1998
ISBN: 0446671010
Price: $15.33

Quantity: 3
---------------------------------------------

Title: Winter's Tale
Author: William Shakespeare
Categories: Drama
Genres: Drama
Publisher: Ku ltu r Bakanlig i Yayinlari
Publish Date: 1935
ISBN: 9798748292504
Price: $12.57

Quantity: 6
---------------------------------------------

Title: Gathering Blue
Author: Lois Lowry
Categories: Fiction
Genres: Fiction
Publisher: Galeria Książki
Publish Date: November 2003
ISBN: 9782070545902
Price: $15.09

Quantity: 12
---------------------------------------------

Title: The Invisible Man
Author: H. G. Wells
Categories: Ciencia-ficción
Genres: Ciencia-ficción
Publisher: Companhia Editora Nacional
Publish Date: 1959
ISBN: 1561034886
Price: $22.95

Quantity: 20
---------------------------------------------

Title: Baby Proof
Author: Emily Giffin
Categories: Couples
Genres: Couples
Publisher: Audio Renaissance
Publish Date: 2010
ISBN: 9781593978976
Price: $6.11

Quantity: 17
---------------------------------------------

Title: A is for Alibi (Kinsey Millhone, #1)
Author: Sue Grafton
Categories: Foreign speakers
Genres: Foreign speakers
Publisher: Holt, Rinehart and Winston
Publish Date: December 1994
ISBN: 9780333466308
Price: $15.25

Quantity: 7
---------------------------------------------

Title: Maybe someday
Author: Colleen Hoover
Categories: College students
Genres: College students
Publisher: Wydawnictwo Otwarte
Publish Date: 2015
ISBN: 8375153419
Price: $9.68

Quantity: 19
---------------------------------------------

Title: Elon Musk
Author: Ashlee Vance, Francisco López Martín
Categories: SpaceX (Firm)
Genres: SpaceX (Firm)
Publisher: Hoepli
Publish Date: 2015
ISBN: 9781470859282
Price: $13.16

Quantity: 2
---------------------------------------------

Title: The Constant Princess
Author: Philippa Gregory
Categories: Fiction
Genres: Fiction
Publisher: Center Point Pub.
Publish Date: 2005
ISBN: 000719031X
Price: $15.46

Quantity: 7
---------------------------------------------

Title: The power of now : a guide to spiritual enlightenment
Author: Eckhart Tolle
Categories: Spiritual life
Genres: Spiritual life
Publisher: N
Publish Date: N/A
ISBN: N/A
Price: $24.48

Quantity: 4
---------------------------------------------

Title: Wizard and Glass
Author: Stephen King
Categories: crystal balls
Genres: crystal balls
Publisher: imusti
Publish Date: September 30, 2003
ISBN: 0340896248
Price: $7.61

Quantity: 6
---------------------------------------------

Title: The Wide Window
Author: Lemony Snicket, Brett Helquist, Michael Kupperman, Nestor Busquets
Categories: Brothers and sisters
Genres: Brothers and sisters
Publisher: Scholastic
Publish Date: October 2002
ISBN: 9780061550355
Price: $19.41

Quantity: 10
---------------------------------------------

Title: Twenties Girl
Author: Sophie Kinsella
Categories: Romance
Genres: Romance
Publisher: Transworld
Publish Date: 2009
ISBN: 9781410419279
Price: $19.36

Quantity: 1
---------------------------------------------

Title: Words of Radiance
Author: Brandon Sanderson, Michael Kramer, Kate Reading
Categories: Imaginary wars and battles
Genres: Imaginary wars and battles
Publisher: Brandon Sanderson
Publish Date: Mar 03, 2015
ISBN: 9788374806480
Price: $11.43

Quantity: 7
---------------------------------------------

Title: Dark Matter
Author: Blake Crouch
Categories: Kidnapping victims
Genres: Kidnapping victims
Publisher: Large Print Press
Publish Date: Mar 27, 2018
ISBN: 9781447297574
Price: $7.95

Quantity: 20
---------------------------------------------

Title: The Silver Linings Playbook
Author: Matthew Quick
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: imusti
Publish Date: 2010
ISBN: 0330456849
Price: $21.31

Quantity: 20
---------------------------------------------

Title: The Westing Game
Author: Ellen Raskin
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: December 1, 1998
ISBN: 0140386645
Price: $14.10

Quantity: 6
---------------------------------------------

Title: By Pike And Dyke A Tale Of The Rise Of The Dutch Republic
Author: G. A. Henty
Categories: Netherlands, fiction
Genres: Netherlands, fiction
Publisher: Pinnacle Press
Publish Date: 2004
ISBN: 1421995123
Price: $21.88

Quantity: 18
---------------------------------------------

Title: Think and Grow Rich
Author: Napoleon Hill, Napoleon Hill, Napolean Hill
Categories: Wealth
Genres: Wealth
Publisher: Lulu.com
Publish Date: Sep 26, 2016
ISBN: 9780857082015
Price: $5.73

Quantity: 6
---------------------------------------------

Title: Landline
Author: Rainbow Rowell
Categories: FICTION / Family Life
Genres: FICTION / Family Life
Publisher: N
Publish Date: 2014
ISBN: 1250064309
Price: $5.55

Quantity: 10
---------------------------------------------

Title: The tale of Despereaux
Author: Jamie Michalak
Categories: Mice
Genres: Mice
Publisher: Candlewick Press
Publish Date: 2008
ISBN: 9780763640767
Price: $9.02

Quantity: 6
---------------------------------------------

Title: Unravel me
Author: Tahereh Mafi
Categories: Love
Genres: Love
Publisher: HarperCollins
Publish Date: 2014
ISBN: 0062250930
Price: $15.26

Quantity: 18
---------------------------------------------

Title: The White Tiger
Author: Aravind Adiga
Categories: Fiction, mystery & detective, general
Genres: Fiction, mystery & detective, general
Publisher: Tantor Audio
Publish Date: Mar 01, 2012
ISBN: 1848870981
Price: $21.71

Quantity: 15
---------------------------------------------

Title: Lamb:the gospel according to Biff
Author: N/A
Categories: N/A
Genres: N/A
Publisher: William morrow
Publish Date: 2002
ISBN: N/A
Price: $23.27

Quantity: 11
---------------------------------------------

Title: Shutter Island
Author: Dennis Lehane
Categories: United States marshals
Genres: United States marshals
Publisher: HarperLargePrint
Publish Date: Jan 21, 2009
ISBN: 9780061897221
Price: $23.88

Quantity: 8
---------------------------------------------

Title: Between the World and Me
Author: Ta-Nehisi Coates
Categories: race discrimination
Genres: race discrimination
Publisher: Text Publishing Co
Publish Date: 2015
ISBN: 9783150199305
Price: $12.78

Quantity: 19
---------------------------------------------

Title: Born to Run
Author: Christopher McDougall
Categories: Tarahumara Indians
Genres: Tarahumara Indians
Publisher: PROFILE BOOKS
Publish Date: 2016
ISBN: 1846684226
Price: $13.30

Quantity: 16
---------------------------------------------

Title: The edge of never
Author: J. A. Redmerski
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: HarperCollins Publishers Limited
Publish Date: 2013
ISBN: 9781455548996
Price: $9.56

Quantity: 18
---------------------------------------------

Title: Darkfever
Author: Karen Marie Moning
Categories: Fiction
Genres: Fiction
Publisher: Random House Publishing Group
Publish Date: August 28, 2007
ISBN: 0786292997
Price: $10.69

Quantity: 10
---------------------------------------------

Title: Ender's Shadow
Author: Orson Scott Card
Categories: Child soldiers
Genres: Child soldiers
Publisher: B de Bolsillo
Publish Date: Jan 01, 2005
ISBN: 9781857239980
Price: $9.76

Quantity: 10
---------------------------------------------

Title: The Fiery Cross
Author: Diana Gabaldon
Categories: Fiction
Genres: Fiction
Publisher: Dell
Publish Date: October 2002
ISBN: 0440221668
Price: $10.11

Quantity: 18
---------------------------------------------

Title: Two for the dough
Author: Janet Evanovich
Categories: Bounty hunters
Genres: Bounty hunters
Publisher: Compass Press
Publish Date: January 10, 1996
ISBN: 9780684868530
Price: $24.36

Quantity: 9
---------------------------------------------

Title: On the origin of species by means of natural selection
Author: Charles Darwin
Categories: Evolution
Genres: Evolution
Publisher: N. Zanichelli
Publish Date: September 25, 2003
ISBN: 0521867096
Price: $10.53

Quantity: 15
---------------------------------------------

Title: Before We Were Yours
Author: Lisa Wingate
Categories: FICTION / Contemporary Women
Genres: FICTION / Contemporary Women
Publisher: ReadHowYouWant.com, Limited
Publish Date: Jun 06, 2016
ISBN: 9789578759312
Price: $16.87

Quantity: 13
---------------------------------------------

Title: Under the Banner of Heaven
Author: Jon Krakauer
Categories: True Crime
Genres: True Crime
Publisher: Brand: Random House Audio
Publish Date: Oct 04, 2003
ISBN: 9781405032803
Price: $14.40

Quantity: 6
---------------------------------------------

Title: Dreamcatcher
Author: Stephen King
Categories: male friendship
Genres: male friendship
Publisher: Albin Michel
Publish Date: June 30, 2004
ISBN: 3548256686
Price: $22.79

Quantity: 3
---------------------------------------------

Book The Throne of Fire- Rick Riordan (2011) not found on Open Library.Title: Modern Romance
Author: Aziz Ansari, Eric Klinenberg
Categories: relationships
Genres: relationships
Publisher: Penguin Audio
Publish Date: 2015
ISBN: 9780241211830
Price: $10.44

Quantity: 19
---------------------------------------------

Title: Burning Daylight
Author: Jack London
Categories: Bankruptcy
Genres: Bankruptcy
Publisher: Kessinger Publishing, LLC
Publish Date: 1913
ISBN: 9781647994860
Price: $10.34

Quantity: 6
---------------------------------------------

Title: In the garden of beasts
Author: Erik Larson
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Clipper Large Print
Publish Date: May 01, 2012
ISBN: 030740885X
Price: $21.92

Quantity: 13
---------------------------------------------

Title: The bone collector
Author: Jeffery Deaver
Categories: Serial murders
Genres: Serial murders
Publisher: Hodder Education Group
Publish Date: 2097
ISBN: 9780340992722
Price: $16.67

Quantity: 5
---------------------------------------------

Title: Steal like an artist
Author: Austin Kleon
Categories: Creative ability
Genres: Creative ability
Publisher: Workman Publishing Company, Incorporated
Publish Date: 2016
ISBN: 0761169253
Price: $11.59

Quantity: 10
---------------------------------------------

Title: Lock and Key
Author: Sarah Dessen
Categories: Child abuse
Genres: Child abuse
Publisher: Penguin Group UK
Publish Date: 2009
ISBN: 9780670010882
Price: $15.30

Quantity: 5
---------------------------------------------

Title: Fool Moon
Author: Jim Butcher, Mark Powers, Chase Conley, Tyler Walpole, James Marsters
Categories: magic
Genres: magic
Publisher: Buzzy Multimedia on Brilliance Audio
Publish Date: January 7, 2007
ISBN: 0356500284
Price: $19.79

Quantity: 17
---------------------------------------------

Title: Lola and the boy next door
Author: Stephanie Perkins
Categories: Neighbors
Genres: Neighbors
Publisher: Penguin Publishing Group
Publish Date: 2013
ISBN: 0142422010
Price: $20.68

Quantity: 14
---------------------------------------------

Title: Gabriel's Inferno
Author: Sylvain Reynard
Categories: collectionID:CDarkromance
Genres: collectionID:CDarkromance
Publisher: Omnific Publishing
Publish Date: April 2011
ISBN: 9781936305629
Price: $8.92

Quantity: 18
---------------------------------------------

Title: Guards! Guards!
Author: Terry Pratchett
Categories: Fiction in Spanish
Genres: Fiction in Spanish
Publisher: Turtleback Books
Publish Date: December 31, 1998
ISBN: 9780552166669
Price: $8.62

Quantity: 6
---------------------------------------------

Title: The Complete Grimm's Fairy Tales
Author: Jacob Grimm, Wilhelm Grimm
Categories: Folklore
Genres: Folklore
Publisher: Chartwell Books
Publish Date: 2020
ISBN: 0785834222
Price: $7.15

Quantity: 19
---------------------------------------------

Title: Passion simple
Author: Annie Ernaux
Categories: France
Genres: France
Publisher: Tusquets
Publish Date: Sep 05, 2022
ISBN: 0345382544
Price: $16.58

Quantity: 6
---------------------------------------------

Title: The Kill Order
Author: James Dashner
Categories: Science fiction
Genres: Science fiction
Publisher: Chicken House Ltd
Publish Date: August 4, 2012
ISBN: 9781908435590
Price: $6.46

Quantity: 14
---------------------------------------------

Title: Crazy Rich Asians
Author: Kevin Kwan
Categories: Rich people
Genres: Rich people
Publisher: PENGUIN RANDOM HOUSE
Publish Date: May 01, 2014
ISBN: 9781760528188
Price: $18.04

Quantity: 10
---------------------------------------------

Title: Artemis Fowl And The Lost Colony
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: N/A
ISBN: 024143467X
Price: $24.19

Quantity: 1
---------------------------------------------

Title: Ugly Love
Author: Colleen Hoover, Colleen Hoover
Categories: Fiction, romance, contemporary
Genres: Fiction, romance, contemporary
Publisher: Thorndike Press, A part of Gale, Cengage Learning
Publish Date: 2015
ISBN: 3423740213
Price: $10.38

Quantity: 14
---------------------------------------------

Title: Flowers in the Attic
Author: V. C. Andrews
Categories: coming of age
Genres: coming of age
Publisher: J'ai lu
Publish Date: June 24, 1980
ISBN: 9780007766741
Price: $19.11

Quantity: 15
---------------------------------------------

Title: Persepolis. The Story of a Childhood
Author: Marjane Satrapi
Categories: Comics & graphic novels, nonfiction, biography & memoir
Genres: Comics & graphic novels, nonfiction, biography & memoir
Publisher: Pantheon Books
Publish Date: 2006
ISBN: 0224080393
Price: $19.99

Quantity: 2
---------------------------------------------

Title: The Lean Startup
Author: Eric Ries
Categories: New business enterprises
Genres: New business enterprises
Publisher: Portfolio Penguin
Publish Date: 2011
ISBN: 0670921602
Price: $18.30

Quantity: 2
---------------------------------------------

Title: Why not me?
Author: Mindy Kaling
Categories: Conduct of life
Genres: Conduct of life
Publisher: Ebury Publishing
Publish Date: 2015
ISBN: 9780091960292
Price: $8.66

Quantity: 12
---------------------------------------------

Title: The four agreements
Author: Miguel Ruiz, Don Miguel Ruiz, D Ruiz
Categories: Conduct of life
Genres: Conduct of life
Publisher: Center Point Pub.
Publish Date: Nov 07, 1997
ISBN: 187842436X
Price: $7.86

Quantity: 10
---------------------------------------------

Title: Point Of Retreat
Author: Colleen Hoover
Categories: Fiction, romance, general
Genres: Fiction, romance, general
Publisher: San cai wen hua chu ban shi ye you xian gong si
Publish Date: 2014
ISBN: 9788328015425
Price: $6.54

Quantity: 5
---------------------------------------------

Title: Doctor Sleep
Author: Stephen King
Categories: Fiction
Genres: Fiction
Publisher: W F Howes Ltd
Publish Date: Oct 28, 2013
ISBN: 957333173X
Price: $16.13

Quantity: 19
---------------------------------------------

Title: The Bluest Eye
Author: Toni Morrison
Categories: foster care
Genres: foster care
Publisher: Debolsillo
Publish Date: 2021
ISBN: 9780375416521
Price: $19.29

Quantity: 1
---------------------------------------------

Title: Samuel Beckett, Waiting for Godot
Author: Lawrence Graver
Categories: English drama, irish authors, history and criticism
Genres: English drama, irish authors, history and criticism
Publisher: Cambridge University Press
Publish Date: 1989
ISBN: 9780521355131
Price: $18.87

Quantity: 8
---------------------------------------------

Title: Roots, The Saga of an American Family, Large Print Edition, Volume 3
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: ????
ISBN: N/A
Price: $20.21

Quantity: 3
---------------------------------------------

Title: In a Dark, Dark Wood
Author: Ruth Ware
Categories: Fiction, psychological
Genres: Fiction, psychological
Publisher: Gallery Books
Publish Date: 2019
ISBN: 9780099598244
Price: $22.97

Quantity: 12
---------------------------------------------

Title: Wolf Hall
Author: Hilary Mantel
Categories: Biographical fiction
Genres: Biographical fiction
Publisher: Alfa Yayınları
Publish Date: Nov 24, 2009
ISBN: 9781250077585
Price: $20.18

Quantity: 9
---------------------------------------------

Title: The Wedding
Author: Julie Garwood
Categories: Fiction, Romance, Historical
Genres: Fiction, Romance, Historical
Publisher: Pocket
Publish Date: December 1997
ISBN: 9578124708
Price: $23.20

Quantity: 8
---------------------------------------------

Title: We need to talk about Kevin
Author: Lionel Shriver
Categories: Fiction
Genres: Fiction
Publisher: HarperCollins
Publish Date: 2011
ISBN: 9780060724481
Price: $24.94

Quantity: 16
---------------------------------------------

Title: The Man Who Mistook His Wife for a Hat and Other Clinical Tales
Author: Oliver Sacks, Jonathan Davis, Margarida Trias
Categories: Neurology -
Genres: Neurology -
Publisher: Adelphi
Publish Date: June 1998
ISBN: 9785902626015
Price: $17.98

Quantity: 13
---------------------------------------------

Title: A Room with a View
Author: E. M. Forster
Categories: British
Genres: British
Publisher: Lulu.com
Publish Date: July 1988
ISBN: 1434639029
Price: $19.58

Quantity: 1
---------------------------------------------

Title: Suzanne's diary for Nicholas
Author: James Patterson
Categories: Fiction
Genres: Fiction
Publisher: Bastei-Verlag Gustav H Lubbe
Publish Date: February 2005
ISBN: 0759504881
Price: $12.27

Quantity: 8
---------------------------------------------

Title: It Ends With Us
Author: Colleen Hoover
Categories: Fiction, Romance, Contemporary, Life change events
Genres: Fiction, Romance, Contemporary, Life change events
Publisher: dtv Verlagsgesellschaft
Publish Date: Feb 04, 2020
ISBN: 8501112518
Price: $13.18

Quantity: 10
---------------------------------------------

Title: A Bend In The Road
Author: Nicholas Sparks
Categories: Hit-and-run drivers
Genres: Hit-and-run drivers
Publisher: Random House Large Print
Publish Date: 2003
ISBN: 9781863253048
Price: $23.50

Quantity: 10
---------------------------------------------

Title: The Man in the High Castle
Author: Philip K. Dick
Categories: award:hugo_award=1963
Genres: award:hugo_award=1963
Publisher: Ace Books
Publish Date: December 31, 1998
ISBN: 9780425025437
Price: $11.08

Quantity: 15
---------------------------------------------

Title: Wolves of the Calla
Author: Stephen King
Categories: lightsabers
Genres: lightsabers
Publisher: PLAZA & JANES
Publish Date: 2004
ISBN: 9752104541
Price: $16.30

Quantity: 6
---------------------------------------------

Title: Beautiful bastard
Author: Christina Lauren
Categories: FICTION / Contemporary Women
Genres: FICTION / Contemporary Women
Publisher: Gallery Books
Publish Date: Apr 14, 2015
ISBN: 1442381221
Price: $12.60

Quantity: 12
---------------------------------------------

Title: Dawn of Onyx
Author: Kate Golden
Categories: Fiction, fantasy, general
Genres: Fiction, fantasy, general
Publisher: Daisy Press, The
Publish Date: 2023
ISBN: 1529434017
Price: $21.68

Quantity: 5
---------------------------------------------

Title: Thoughtless
Author: S. C. Stephens
Categories: Friendship
Genres: Friendship
Publisher: Gallery Books
Publish Date: Dec 06, 2013
ISBN: 1476717478
Price: $13.04

Quantity: 8
---------------------------------------------

Title: The Elegance of the Hedgehog
Author: Muriel Barbery
Categories: Apartment dwellers
Genres: Apartment dwellers
Publisher: Isis
Publish Date: January 2008
ISBN: 1908313129
Price: $24.59

Quantity: 11
---------------------------------------------

Title: The Best of Me
Author: Nicholas Sparks, Sean Pratt
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Little, Brown Book Group Limited
Publish Date: 2013
ISBN: 1538764725
Price: $8.99

Quantity: 13
---------------------------------------------

Title: A Court of Wings and Ruin
Author: Sarah J. Maas
Categories: War stories
Genres: War stories
Publisher: Bloomsbury USA Childrens
Publish Date: Feb 21, 2017
ISBN: 9780606410823
Price: $15.26

Quantity: 20
---------------------------------------------

Title: The CIDER HOUSE RULES
Author: John Irving
Categories: American fiction (fictional works by one author)
Genres: American fiction (fictional works by one author)
Publisher: Fabbri - RCS Libri
Publish Date: 1989
ISBN: 9780345417947
Price: $19.09

Quantity: 16
---------------------------------------------

Title: Half broke horses
Author: Jeannette Walls
Categories: New York Times Bestseller
Genres: New York Times Bestseller
Publisher: Simon & Schuster
Publish Date: 2010-08-05
ISBN: 1602855722
Price: $19.19

Quantity: 18
---------------------------------------------

Title: Hex Hall
Author: Rachel Hawkins
Categories: witches
Genres: witches
Publisher: Hyperion
Publish Date: 2011
ISBN: 9781423121398
Price: $16.01

Quantity: 9
---------------------------------------------

Title: Incidents in the life of a slave girl
Author: Harriet A. Jacobs, Adam EVE, Karl Simrock, Harriet Jacobs, Monty, Lydia Maria Child, Francine L. Jacobs, l. maria child, Carolyn L. Karcher, Jacobs, Aberdeen Press, Hans Murray, Carla Fonte Sánchez, Carme Manuel Cuenca
Categories: Women slaves
Genres: Women slaves
Publisher: Independently published
Publish Date: Apr 04, 1861
ISBN: 9781593082833
Price: $5.99

Quantity: 6
---------------------------------------------

Book The Unlikely Pillgrimage of Harold Fry not found on Open Library.Title: Eleven Minutes
Author: Paulo Coelho
Categories: Brazilians
Genres: Brazilians
Publisher: TheBookPeople
Publish Date: 2003
ISBN: 0061194913
Price: $14.62

Quantity: 16
---------------------------------------------

Title: Foundation and Empire
Author: Isaac Asimov
Categories: Fiction
Genres: Fiction
Publisher: Debolsillo
Publish Date: 1971
ISBN: 0553803727
Price: $12.54

Quantity: 12
---------------------------------------------

Title: Shantaram
Author: Gregory David Roberts
Categories: Criminals
Genres: Criminals
Publisher: Blackstone Audio Inc.
Publish Date: September 29, 2005
ISBN: 0312330529
Price: $12.31

Quantity: 11
---------------------------------------------

Title: Elantris
Author: Brandon Sanderson
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Tor
Publish Date: Nov 04, 2020
ISBN: 9788466624237
Price: $17.55

Quantity: 11
---------------------------------------------

Title: Lonesome Dove
Author: Larry McMurtry
Categories: fiction
Genres: fiction
Publisher: Izd-vo AST
Publish Date: 1998
ISBN: 5553676142
Price: $24.59

Quantity: 9
---------------------------------------------

Title: The Way of Shadows
Author: Brent Weeks
Categories: fantasy
Genres: fantasy
Publisher: Orbit Books
Publish Date: 2009
ISBN: 9780748112586
Price: $10.43

Quantity: 19
---------------------------------------------

Book A New Earth: Awakening to Your Life’s Purpose not found on Open Library.Title: The Black Echo (Harry Bosch)
Author: Michael Connelly
Categories: Veterans
Genres: Veterans
Publisher: Brilliance Audio on CD Unabridged Lib Ed
Publish Date: July 28, 2001
ISBN: 9781596000971
Price: $16.77

Quantity: 9
---------------------------------------------

Title: Sh*t my dad says
Author: Justin Halpern
Categories: Quotations
Genres: Quotations
Publisher: It Books
Publish Date: 2010
ISBN: 0061992704
Price: $10.07

Quantity: 1
---------------------------------------------

Title: The Sense of an Ending
Author: Julian Barnes
Categories: Middle-aged men
Genres: Middle-aged men
Publisher: Center Point Pub.
Publish Date: 2012
ISBN: 9780224094153
Price: $24.33

Quantity: 18
---------------------------------------------

Book The Kife of Never Letting Go not found on Open Library.Title: When You Reach Me
Author: Rebecca Stead
Categories: Fiction
Genres: Fiction
Publisher: n/a
Publish Date: May 15, 2010
ISBN: 9781849392129
Price: $11.40

Quantity: 15
---------------------------------------------

Title: Seabiscuit : an American legend
Author: Laura Hillenbrand
Categories: Seabiscuit (Race horse)
Genres: Seabiscuit (Race horse)
Publisher: N
Publish Date: N/A
ISBN: N/A
Price: $12.30

Quantity: 5
---------------------------------------------

Title: Old Man’s War
Author: John Scalzi
Categories: Space warfare
Genres: Space warfare
Publisher: Subterranean
Publish Date: 2005
ISBN: 0765315246
Price: $7.52

Quantity: 18
---------------------------------------------

Title: Blue Bloods
Author: Melissa De La Cruz
Categories: Young adult fiction
Genres: Young adult fiction
Publisher: Hyperion
Publish Date: April 1, 2007
ISBN: 9781423101260
Price: $6.78

Quantity: 19
---------------------------------------------

Title: The girls' guide to hunting and fishing
Author: Melissa Bank
Categories: Fiction
Genres: Fiction
Publisher: Chivers Press
Publish Date: 2019
ISBN: 9780786221691
Price: $20.00

Quantity: 12
---------------------------------------------

Title: Three to Get Deadly
Author: Janet Evanovich
Categories: Fiction
Genres: Fiction
Publisher: St. Martin's Paperbacks
Publish Date: 2021
ISBN: 9783442445813
Price: $19.94

Quantity: 16
---------------------------------------------

Title: Watchers
Author: Dean Koontz
Categories: Accessible book
Genres: Accessible book
Publisher: Brilliance Audio
Publish Date: 1998
ISBN: 9781978637146
Price: $5.23

Quantity: 11
---------------------------------------------

Book Crazy Love: Overhelmed by a Relentless God not found on Open Library.Book Brain on Fire: My Month of Madness not found on Open Library.Title: Angus, Thongs and Full-Frontal Snogging
Author: Louise Rennison
Categories: Humorous stories
Genres: Humorous stories
Publisher: POINT
Publish Date: 2005
ISBN: 0007218672
Price: $18.54

Quantity: 7
---------------------------------------------

Title: Night Shift
Author: Stephen King
Categories: euthanasia
Genres: euthanasia
Publisher: Bastei Lübbe
Publish Date: January 1, 1996
ISBN: 9785170041640
Price: $24.90

Quantity: 18
---------------------------------------------

Title: One Flew Over the Cuckoo's Nest
Author: Ken Kesey
Categories: Allegories
Genres: Allegories
Publisher: Wydawnictwo Albatros Andrzej Kuryłowicz
Publish Date: March 6, 2002
ISBN: 9780451137098
Price: $6.01

Quantity: 3
---------------------------------------------

Title: Shadow of night
Author: Deborah E. Harkness
Categories: Vampires
Genres: Vampires
Publisher: Headline Book Publishing
Publish Date: Jul 24, 2013
ISBN: 0755395263
Price: $8.66

Quantity: 10
---------------------------------------------

Title: Xenocide
Author: Orson Scott Card
Categories: Space warfare
Genres: Space warfare
Publisher: Audio Literature
Publish Date: July 15, 1996
ISBN: 9782221073841
Price: $10.62

Quantity: 16
---------------------------------------------

Title: The Queen of the Damned  (The Vampire Chronicles Vol. 3)
Author: N/A
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: N/A
ISBN: N/A
Price: $14.63

Quantity: 7
---------------------------------------------

Title: The Age of Innocence
Author: Edith Wharton
Categories: Fiction
Genres: Fiction
Publisher: Adams Media Corporation
Publish Date: Sep 27, 2016
ISBN: 9781509890033
Price: $5.39

Quantity: 12
---------------------------------------------

Title: Team of Rivals
Author: Doris Kearns Goodwin
Categories: Union Army
Genres: Union Army
Publisher: Penguin
Publish Date: 2006
ISBN: 0684824906
Price: $20.33

Quantity: 18
---------------------------------------------

Title: The Blade Itself
Author: Joe Abercrombie
Categories: Fiction, fantasy, general
Genres: Fiction, fantasy, general
Publisher: Subterranean Press
Publish Date: Nov 02, 2015
ISBN: 1478935782
Price: $13.36

Quantity: 2
---------------------------------------------

Book Abrahan Lincoln: Vampire Hunter not found on Open Library.Title: The Alchemyst
Author: Michael Scott, Michael Dylan Scott
Categories: Magic
Genres: Magic
Publisher: Delacorte Books for Young Readers
Publish Date: May 22, 2007
ISBN: 9780385733571
Price: $9.62

Quantity: 14
---------------------------------------------

Title: The history of the great plague in London in the year 1665
Author: Daniel Defoe
Categories: Early works to 1800
Genres: Early works to 1800
Publisher: Dent & Sons
Publish Date: 1995
ISBN: 1425060080
Price: $19.10

Quantity: 14
---------------------------------------------

Title: Glass Sword
Author: Victoria Aveyard
Categories: Ability
Genres: Ability
Publisher: Turtleback Books
Publish Date: Apr 24, 2018
ISBN: 1410486680
Price: $24.60

Quantity: 6
---------------------------------------------

Title: Nine stories
Author: J. D. Salinger
Categories: Fiction
Genres: Fiction
Publisher: Back Bay Books
Publish Date: 1953
ISBN: 9780613707497
Price: $8.22

Quantity: 20
---------------------------------------------

Title: Shanghai girls
Author: Lisa See
Categories: Fiction
Genres: Fiction
Publisher: Random House Trade Paperbacks
Publish Date: 2013
ISBN: 9781400067114
Price: $12.72

Quantity: 19
---------------------------------------------

Title: An ember in the ashes
Author: Sabaa Tahir
Categories: Love
Genres: Love
Publisher: HarperCollins
Publish Date: 2015
ISBN: 9781410488756
Price: $7.68

Quantity: 9
---------------------------------------------

Title: The Bean Trees
Author: Barbara Kingsolver
Categories: Indian children
Genres: Indian children
Publisher: Virago Press
Publish Date: 1989
ISBN: 0833525182
Price: $24.39

Quantity: 20
---------------------------------------------

Title: Waiting for you
Author: Susane Colasanti
Categories: Anxiety Disorders
Genres: Anxiety Disorders
Publisher: Penguin USA, Inc.
Publish Date: 2009
ISBN: 9781441862440
Price: $8.48

Quantity: 20
---------------------------------------------

Title: Journey to the center of the earth
Author: Jules Verne
Categories: Explorers
Genres: Explorers
Publisher: Aerie Books
Publish Date: 2000
ISBN: 9781559027830
Price: $6.32

Quantity: 18
---------------------------------------------

Title: Guilty pleasures
Author: Laurell K. Hamilton
Categories: N/A
Genres: N/A
Publisher: Berkley Books
Publish Date: 2004
ISBN: 9780425187562
Price: $12.07

Quantity: 3
---------------------------------------------

Title: The One Plus One
Author: Jojo Moyes, Elizabeth Bower, Ben Elliot, Steven  France, Nicola  Stanton
Categories: Romance
Genres: Romance
Publisher: Penguin Audio
Publish Date: 2015
ISBN: 0718179714
Price: $12.05

Quantity: 8
---------------------------------------------

Title: Smile
Author: Raina Telgemeier
Categories: Dental care
Genres: Dental care
Publisher: Scholastic/Graphix
Publish Date: 2020
ISBN: 9780545132053
Price: $13.13

Quantity: 6
---------------------------------------------

Title: The Final Empire
Author: Brandon Sanderson
Categories: Courts and courtiers
Genres: Courts and courtiers
Publisher: Tor Books
Publish Date: July 25, 2006
ISBN: 076531178X 9780765311788 9780765350381 0765350386
Price: $12.94

Quantity: 14
---------------------------------------------

Title: The Summer I Turned Pretty
Author: Jenny Han
Categories: Beaches
Genres: Beaches
Publisher: Simon & Schuster Books For Young Readers
Publish Date: Jan 01, 2000
ISBN: 0141330538
Price: $9.27

Quantity: 3
---------------------------------------------

Title: The joy of cooking naturally
Author: Peggy Dameron
Categories: Vegetarian cookery
Genres: Vegetarian cookery
Publisher: The Joy of Cooking Naturally [distributor]
Publish Date: 1983
ISBN: 9780961064815
Price: $23.69

Quantity: 12
---------------------------------------------

Title: Halfway to the Grave
Author: Jeaniene Frost
Categories: Fiction
Genres: Fiction
Publisher: Avon
Publish Date: 2007
ISBN: 0061545791
Price: $12.72

Quantity: 11
---------------------------------------------

Title: Tales of a Fourth Grade Nothing
Author: Judy Blume
Categories: turtles
Genres: turtles
Publisher: Scholastic
Publish Date: 2004
ISBN: 9780333352878
Price: $11.76

Quantity: 18
---------------------------------------------

Title: Olive Kitteridge
Author: Elizabeth Strout
Categories: Retired teachers
Genres: Retired teachers
Publisher: Brilliance Audio on CD Unabridged Lib Ed
Publish Date: 2008
ISBN: 9781423350057
Price: $18.23

Quantity: 17
---------------------------------------------

Title: The Audacity of Hope
Author: Barack Obama, Erwin Dorado, Claudia Casanova, Esther Roig Giménez
Categories: Politics and government
Genres: Politics and government
Publisher: Fonolibro Inc
Publish Date: Mar 17, 2022
ISBN: 9780307237705
Price: $24.23

Quantity: 8
---------------------------------------------

Title: North and South
Author: Elizabeth Cleghorn Gaskell
Categories: Classic Literature
Genres: Classic Literature
Publisher: Dent
Publish Date: January 1914
ISBN: 9781406528053
Price: $15.89

Quantity: 15
---------------------------------------------

Title: So long, and thanks for all the fish
Author: Douglas Adams
Categories: Trilogy of Four
Genres: Trilogy of Four
Publisher: Heyne
Publish Date: Oct 03, 2006
ISBN: 1574534807
Price: $17.44

Quantity: 20
---------------------------------------------

Title: The Art Book 2004
Author: Art Book
Categories: N/A
Genres: N/A
Publisher: The John Pidgeon Consultancy Ltd.
Publish Date: 2004-01-01
ISBN: 9781899034451
Price: $7.14

Quantity: 9
---------------------------------------------

Title: The Witch of Blackbird Pond
Author: Elizabeth George Speare
Categories: Children's literature
Genres: Children's literature
Publisher: Sandpiper
Publish Date: February 1, 1999
ISBN: 9780812416985
Price: $10.53

Quantity: 2
---------------------------------------------

Title: This is where I leave you
Author: Jonathan Tropper
Categories: Fiction
Genres: Fiction
Publisher: Plume
Publish Date: Nov 10, 2003
ISBN: 1409102696
Price: $23.35

Quantity: 2
---------------------------------------------

Title: Trainspotting
Author: Irvine Welsh
Categories: Fiction
Genres: Fiction
Publisher: Vintage
Publish Date: 2004
ISBN: 8379981251
Price: $6.07

Quantity: 16
---------------------------------------------

Title: The Blind Assassin
Author: Margaret Atwood
Categories: Death
Genres: Death
Publisher: Ōkeanida
Publish Date: Oct 01, 2008
ISBN: 9780007113606
Price: $12.79

Quantity: 1
---------------------------------------------

Title: The Miserable Mill
Author: Lemony Snicket
Categories: Children's fiction
Genres: Children's fiction
Publisher: Scholastic
Publish Date: May 2002
ISBN: 8426437435
Price: $19.11

Quantity: 7
---------------------------------------------

Title: Inferno
Author: Dante Alighieri, Marcus Sanders, Doug Harvey
Categories: Poetry
Genres: Poetry
Publisher: NYRB Classics
Publish Date: Apr 02, 2014
ISBN: 9780007902095
Price: $24.78

Quantity: 11
---------------------------------------------

Title: Fifty Shades of Grey
Author: E. L. James
Categories: Man-woman relationships
Genres: Man-woman relationships
Publisher: 
Publish Date:  2012.
ISBN: 8804632534
Price: $23.65

Quantity: 3
---------------------------------------------

Title: No country for old men
Author: Cormac McCarthy, Tom Stechschulte
Categories: Fiction
Genres: Fiction
Publisher: Sapʻiensŭ
Publish Date: Jan 01, 2005
ISBN: 1405613947
Price: $20.61

Quantity: 6
---------------------------------------------

Title: Sweetness at the Bottom of the Pie
Author: Alan Bradley
Categories: Sisters, fiction
Genres: Sisters, fiction
Publisher: Orion Publishing Ome
Publish Date: Oct 17, 2009
ISBN: 1846526043
Price: $11.07

Quantity: 7
---------------------------------------------

Title: As I Lay Dying
Author: William Faulkner
Categories: American Manuscripts
Genres: American Manuscripts
Publisher: Demco Media
Publish Date: 1966?
ISBN: 0785922997
Price: $6.93

Quantity: 8
---------------------------------------------

Title: Insomnia
Author: Stephen King
Categories: Bram Stoker Award for Best Novel
Genres: Bram Stoker Award for Best Novel
Publisher: Albatros - A. Kuryłowicz
Publish Date: Sep 16, 2008
ISBN: 1598877658
Price: $16.32

Quantity: 17
---------------------------------------------

Title: The Dark Tower VII
Author: Stephen King
Categories: The Dark Tower
Genres: The Dark Tower
Publisher: Plaza y Janes
Publish Date: September 21, 2004
ISBN: 9788379855896
Price: $22.73

Quantity: 20
---------------------------------------------

Title: L'Assassin royal, tome 3
Author: Robin Hobb
Categories: Aventure
Genres: Aventure
Publisher: France Loisir
Publish Date: 2001-01-01
ISBN: 9782290316290
Price: $15.38

Quantity: 13
---------------------------------------------

Title: My life next door
Author: Huntley Fitzpatrick
Categories: Love
Genres: Love
Publisher: Dial Books
Publish Date: 2016
ISBN: 9780803736993
Price: $9.38

Quantity: 15
---------------------------------------------

Title: Between Shades of Gray
Author: Ruta Sepetys
Categories: Labor camps
Genres: Labor camps
Publisher: Penguin Audio
Publish Date: 2011
ISBN: 9781410440839
Price: $6.37

Quantity: 11
---------------------------------------------

Title: The alienist
Author: Caleb Carr
Categories: Fiction
Genres: Fiction
Publisher: ZETA BOLSILLO
Publish Date: 2014-03-30
ISBN: 9780751574173
Price: $11.86

Quantity: 2
---------------------------------------------

Title: Poison Study
Author: Maria V. Snyder
Categories: Fiction
Genres: Fiction
Publisher: LUNA
Publish Date: March 1, 2007
ISBN: 9781552549230
Price: $11.36

Quantity: 20
---------------------------------------------

Title: Middlemarch
Author: George Eliot
Categories: Young women
Genres: Young women
Publisher: Tandem Library
Publish Date: Sep 27, 2016
ISBN: 9780141196893
Price: $24.91

Quantity: 10
---------------------------------------------

Title: Lady Midnight
Author: Cassandra Clare
Categories: N/A
Genres: N/A
Publisher: Destino
Publish Date: 2016
ISBN: 8408157256
Price: $15.72

Quantity: 10
---------------------------------------------

Title: A Little Life
Author: Hanya Yanagihara
Categories: LGBTQ novels
Genres: LGBTQ novels
Publisher: Pan Macmillan
Publish Date: 2022
ISBN: 9788952776389
Price: $10.78

Quantity: 9
---------------------------------------------

Title: Naruto, Vol. 1
Author: Masashi Kishimoto
Categories: Pariahs
Genres: Pariahs
Publisher: Pujol & Amado S.L.L.
Publish Date: November 12, 2003
ISBN: 8484492753
Price: $23.63

Quantity: 8
---------------------------------------------

Title: Four to score
Author: Janet Evanovich
Categories: Women detectives
Genres: Women detectives
Publisher: Audio Renaissance
Publish Date: 2010
ISBN: 1250057965
Price: $9.51

Quantity: 16
---------------------------------------------

Title: The Shipping News
Author: Annie Proulx
Categories: Domestic fiction
Genres: Domestic fiction
Publisher: Bt Bound
Publish Date: 2002?
ISBN: 9780743225427
Price: $10.03

Quantity: 11
---------------------------------------------

Title: Major Pettigrew's last stand
Author: Helen Simonson
Categories: Literature
Genres: Literature
Publisher: Random House Audio
Publish Date: March 2, 2010
ISBN: 158836965X
Price: $14.47

Quantity: 4
---------------------------------------------

Book Schingler’s List not found on Open Library.Title: My Brilliant Friends
Author: Nancy K. Miller
Categories: Feminism
Genres: Feminism
Publisher: Columbia University Press
Publish Date: 2019
ISBN: 9780231548946
Price: $14.53

Quantity: 13
---------------------------------------------

Title: Falling Up
Author: Shel Silverstein
Categories: American poetry
Genres: American poetry
Publisher: National Braille Press, Inc.
Publish Date: 1996
ISBN: 0060513098
Price: $9.19

Quantity: 1
---------------------------------------------

Title: Carry On
Author: Rainbow Rowell
Categories: gay
Genres: gay
Publisher: St. Martin's Griffin
Publish Date: 2016
ISBN: 1250135028
Price: $7.80

Quantity: 2
---------------------------------------------

Title: Career of Evil
Author: J. K. Rowling
Categories: Private investigators
Genres: Private investigators
Publisher: LGF
Publish Date: Mar 29, 2017
ISBN: 9781478962663
Price: $14.95

Quantity: 11
---------------------------------------------

Title: The story of my life
Author: Helen Keller
Categories: Biography
Genres: Biography
Publisher: Collier-MacMillan International
Publish Date: 1905
ISBN: 4043142013
Price: $17.89

Quantity: 10
---------------------------------------------

Title: Jaws
Author: Peter Benchley
Categories: blue sharks
Genres: blue sharks
Publisher: [Wen yi shu wu]
Publish Date: 1975-01
ISBN: 0449219631
Price: $9.74

Quantity: 9
---------------------------------------------

Title: Anne of Avonlea
Author: Lucy Maud Montgomery
Categories: Anne Shirley (Fictitious character)
Genres: Anne Shirley (Fictitious character)
Publisher: Ren Kitap
Publish Date: 1942
ISBN: 9798487641076
Price: $17.29

Quantity: 18
---------------------------------------------

Title: Year of Wonders
Author: Geraldine Brooks
Categories: Fiction
Genres: Fiction
Publisher: G.K. Hall
Publish Date: Aug 01, 2010
ISBN: 073227902X
Price: $15.00

Quantity: 15
---------------------------------------------

Title: "Surely You're Joking, Mr. Feynman"
Author: Richard Phillips Feynman, Ralph Leighton
Categories: Anecdotes
Genres: Anecdotes
Publisher: Barnes &Noble
Publish Date: 1985
ISBN: 9780786196197
Price: $19.13

Quantity: 20
---------------------------------------------

Title: The Jungle
Author: Upton Sinclair
Categories: Slaughtering and slaughter-houses
Genres: Slaughtering and slaughter-houses
Publisher: JNMedia
Publish Date: 2005
ISBN: 9798534546682
Price: $14.24

Quantity: 13
---------------------------------------------

Title: David and Goliath
Author: Malcolm Gladwell
Categories: Motivation
Genres: Motivation
Publisher: Campus Verlag GmbH
Publish Date: 2015
ISBN: 9781306764391
Price: $21.84

Quantity: 3
---------------------------------------------

Title: About a Boy (Movie Tie-In) (Movie Tie-In)
Author: Nick Hornby
Categories: Divorced people, fiction
Genres: Divorced people, fiction
Publisher: Punto De Lectura
Publish Date: Jul 31, 2010
ISBN: 9780141039107
Price: $10.69

Quantity: 9
---------------------------------------------

Title: Fables   Vol. 1
Author: N/A
Categories: N/A
Genres: N/A
Publisher: French & European Pubns
Publish Date: October 1, 1964
ISBN: 0785946497
Price: $22.77

Quantity: 17
---------------------------------------------

Title: Réquiem por un campesino español
Author: Ramón J. Sender
Categories: Spanish language
Genres: Spanish language
Publisher: Distributed exclusively in the USA and Canada by St. Martin's Press
Publish Date: 1969
ISBN: 9788423361014
Price: $12.21

Quantity: 16
---------------------------------------------

Title: Grave Peril
Author: Jim Butcher, James Marsters
Categories: Ghost stories
Genres: Ghost stories
Publisher: ROC
Publish Date: January 25, 2007
ISBN: 0356500292
Price: $5.79

Quantity: 16
---------------------------------------------

Title: Deja Dead (Temperance Brennan #1)
Author: Kathy Reichs
Categories: Forensic anthropology
Genres: Forensic anthropology
Publisher: Scribner
Publish Date: October 23, 2007
ISBN: 0671011367
Price: $21.17

Quantity: 16
---------------------------------------------

Title: Steelheart (The Reckoners, Book 1)
Author: Brandon Sanderson, MacLeod Andrews, Rafael Marín Trechera
Categories: fantasy
Genres: fantasy
Publisher: Brilliance Audio
Publish Date: Apr 28, 2016
ISBN: 9788576573463
Price: $14.37

Quantity: 7
---------------------------------------------

Title: Anthem
Author: Ayn Rand, Erin Bateman
Categories: Fiction
Genres: Fiction
Publisher: Boomer Books
Publish Date: July 1977
ISBN: 0451000536
Price: $19.09

Quantity: 3
---------------------------------------------

Title: Clear and Present Danger
Author: Tom Clancy
Categories: Clark, john (fictitious character), fiction
Genres: Clark, john (fictitious character), fiction
Publisher: G. P. Putnam's sons
Publish Date: Feb 15, 2010
ISBN: 9780671898007
Price: $9.06

Quantity: 2
---------------------------------------------

Title: The happiness project
Author: Gretchen Craft Rubin
Categories: Biography & Autobiography
Genres: Biography & Autobiography
Publisher: HarperCollins
Publish Date: 2009
ISBN: 9781554682805
Price: $20.14

Quantity: 7
---------------------------------------------

Title: Pretty Girls
Author: Karin Slaughter
Categories: Sisters
Genres: Sisters
Publisher: William Morrow
Publish Date: 2015
ISBN: 0062499556
Price: $5.59

Quantity: 19
---------------------------------------------

Title: Curious George
Author: H. A. Rey, Margret Rey
Categories: Monkeys
Genres: Monkeys
Publisher: Iwanami Shoten
Publish Date: 1941
ISBN: 0395698030
Price: $23.95

Quantity: 13
---------------------------------------------

Title: Vision in White
Author: Nora Roberts
Categories: Weddings
Genres: Weddings
Publisher: Penguin USA, Inc.
Publish Date: 2009-05
ISBN: 0425274950
Price: $13.27

Quantity: 2
---------------------------------------------

Title: Second Foundation
Author: Isaac Asimov
Categories: Fiction
Genres: Fiction
Publisher: Doubleday
Publish Date: 2008
ISBN: 0007384858
Price: $9.80

Quantity: 19
---------------------------------------------

Title: Luckiest Girl Alive
Author: Jessica Knoll
Categories: Life change events
Genres: Life change events
Publisher: Jian duan chu ban
Publish Date: 2015
ISBN: 6055016702
Price: $18.64

Quantity: 8
---------------------------------------------

Book Days of Blood & Starlight (Daughter #2) not found on Open Library.Title: A Gentleman in Moscow
Author: Amor Towles
Categories: historical fiction
Genres: historical fiction
Publisher: Bolinda/Audible audio
Publish Date: 2018
ISBN: 9780735221673
Price: $22.09

Quantity: 2
---------------------------------------------

Title: The hours
Author: Michael Cunningham, Jaime Zulaika Goicoechea
Categories: Fiction
Genres: Fiction
Publisher: Audio Renaissance
Publish Date: January 2003
ISBN: 9578119674
Price: $20.27

Quantity: 18
---------------------------------------------

Title: Equal Rites
Author: Terry Pratchett
Categories: Fantasy
Genres: Fantasy
Publisher: Martinez Roca
Publish Date: November 16, 1995
ISBN: 9781804990148
Price: $16.13

Quantity: 4
---------------------------------------------

Title: I am the messenger
Author: Markus Zusak
Categories: Bank robberies
Genres: Bank robberies
Publisher: Alfred A. Knopf
Publish Date: 2012
ISBN: 9780375836671
Price: $21.48

Quantity: 7
---------------------------------------------

Title: Harold and the Purple Crayon
Author: Crockett Johnson
Categories: Animals
Genres: Animals
Publisher: HarperCollinsChildrenâ€TMsBooks
Publish Date: September 1982
ISBN: 607111649X
Price: $13.74

Quantity: 3
---------------------------------------------

Title: Gerald's Game
Author: Stephen King, Lindsay Crouse
Categories: Horror tales
Genres: Horror tales
Publisher: Grijalbo Mondadori
Publish Date: 1995-09-18
ISBN: 843970660X
Price: $9.58

Quantity: 20
---------------------------------------------

Title: A Breath of Snow and Ashes
Author: Diana Gabaldon, Diana Palmer, Davina Porter
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: Seal Books
Publish Date: 2011
ISBN: 0440335655
Price: $18.65

Quantity: 8
---------------------------------------------

Title: The Awakening
Author: Kate Chopin
Categories: Adultery
Genres: Adultery
Publisher: Lulu.com
Publish Date: 2011-09-19
ISBN: 9798477684113
Price: $6.76

Quantity: 17
---------------------------------------------

Title: The Austere Academy
Author: Lemony Snicket, Brett Helquist, Michael Kupperman
Categories: Humour
Genres: Humour
Publisher: Turtleback Books Distributed by Demco Media
Publish Date: May 2002
ISBN: 1405208716
Price: $15.82

Quantity: 16
---------------------------------------------

Title: Crank
Author: Ellen Hopkins
Categories: Dysfunctional families
Genres: Dysfunctional families
Publisher: Simon & Schuster, Limited
Publish Date: 2004-10
ISBN: 9781439106518
Price: $18.33

Quantity: 9
---------------------------------------------

Title: The Murder at the Vicarage
Author: Agatha Christie
Categories: Women detectives
Genres: Women detectives
Publisher: Proszynski i S-ka
Publish Date: 1990
ISBN: 5555531729
Price: $14.96

Quantity: 15
---------------------------------------------

Title: The Forever War
Author: Joe Haldeman, Marvano, Edith Zilli, Patrick Imbert
Categories: Aging
Genres: Aging
Publisher: Avon/AvoNova
Publish Date: August 1, 2001
ISBN: 345247671150
Price: $11.75

Quantity: 11
---------------------------------------------

Title: The Fires of Heaven
Author: Robert Jordan
Categories: Fantasy
Genres: Fantasy
Publisher: Intrínseca
Publish Date: March 15, 1994
ISBN: 8580579856
Price: $6.02

Quantity: 1
---------------------------------------------

Title: Rework
Author: Jason Fried
Categories: Business
Genres: Business
Publisher: Crown Business
Publish Date: 2010
ISBN: 9780307463760
Price: $12.26

Quantity: 19
---------------------------------------------

Title: The Secret Keeper
Author: Kate Morton
Categories: nyt:combined-print-and-e-book-fiction=2012-11-04
Genres: nyt:combined-print-and-e-book-fiction=2012-11-04
Publisher: Atria Books
Publish Date: 2013
ISBN: 9781439163092
Price: $17.66

Quantity: 20
---------------------------------------------

Title: The Girl You Left Behind
Author: Jojo Moyes, Ana Momplet Chico;
Categories: Fiction, romance, suspense
Genres: Fiction, romance, suspense
Publisher: Turtleback Books
Publish Date: Mar 16, 2017
ISBN: 9786053433552
Price: $8.62

Quantity: 14
---------------------------------------------

Title: Siege and Storm
Author: Leigh Bardugo
Categories: Monsters -- Fiction
Genres: Monsters -- Fiction
Publisher: Square Fish
Publish Date: Feb 01, 2017
ISBN: 9781480563797
Price: $15.14

Quantity: 14
---------------------------------------------

Title: Paradise Lost
Author: John Milton
Categories: Bible
Genres: Bible
Publisher: Libreria de Perlado, Paez y Ca
Publish Date: 1857
ISBN: 1554455359
Price: $24.71

Quantity: 12
---------------------------------------------

Title: Beautiful Darkness (Beautiful Creatures Series, Book 2)
Author: Kami Garcia, Margaret Stohl
Categories: Romance fiction
Genres: Romance fiction
Publisher: Little, Brown
Publish Date: Jun 30, 2010
ISBN: 9786090102619
Price: $8.33

Quantity: 3
---------------------------------------------

Title: The Woman in White
Author: Wilkie Collins
Categories: Fiction
Genres: Fiction
Publisher: Wildside Press, LLC
Publish Date: Jun 19, 1973
ISBN: 0192834290
Price: $8.04

Quantity: 13
---------------------------------------------

Title: Harry Potter and the Chamber of Secrets
Author: J. K. Rowling
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Der Hörverlag
Publish Date: 2011
ISBN: 9781408865613
Price: $14.26

Quantity: 18
---------------------------------------------

Title: Unearthly (Unearthly #1)
Author: Cynthia Hand
Categories: Household Moving
Genres: Household Moving
Publisher: Harper Collins
Publish Date: 2012
ISBN: 9780061996160
Price: $19.89

Quantity: 10
---------------------------------------------

Title: For One More Day
Author: Mitch Albom
Categories: Future life
Genres: Future life
Publisher: Da kuai wen hua chu ban gu fen you xian gong si
Publish Date: 2008
ISBN: 9787532742387
Price: $9.39

Quantity: 14
---------------------------------------------

Title: A darker shade of magic
Author: V. E. Schwab, Julieta María Gorlero
Categories: Quantum theory
Genres: Quantum theory
Publisher: Titan Books Ltd
Publish Date: 2015
ISBN: 9780765376466
Price: $12.35

Quantity: 4
---------------------------------------------

Title: Shopaholic & Baby (Shopaholic Series, Book 5)
Author: Sophie Kinsella
Categories: Shopping
Genres: Shopping
Publisher: RH Audio
Publish Date: February 27, 2007
ISBN: 1409081192
Price: $8.80

Quantity: 7
---------------------------------------------

Title: Rendezvous with Rama
Author: Arthur C. Clarke
Categories: Fiction
Genres: Fiction
Publisher: Ballantine Books
Publish Date: April 13, 2006
ISBN: 0816130388
Price: $22.80

Quantity: 6
---------------------------------------------

Title: The Year of Magical Thinking
Author: Joan Didion
Categories: American Novelists
Genres: American Novelists
Publisher: Knopf Doubleday Publishing Group
Publish Date: May 15, 2007
ISBN: 9780739327791
Price: $10.80

Quantity: 7
---------------------------------------------

Title: The Big Short: Inside the Doomsday Machine
Author: Michael Lewis
Categories: Financial crises
Genres: Financial crises
Publisher: W. W. Norton & Co
Publish Date: Aug 27, 2011
ISBN: 0141043539
Price: $6.65

Quantity: 9
---------------------------------------------

Title: The Power of Six
Author: Pittacus Lore
Categories: Science fiction
Genres: Science fiction
Publisher: HarperCollins
Publish Date: 2011
ISBN: 9780061974557
Price: $18.66

Quantity: 17
---------------------------------------------

Title: Lover Revealed
Author: J. R. Ward
Categories: Fiction
Genres: Fiction
Publisher: Onyx
Publish Date: March 6, 2007
ISBN: 9781429530224
Price: $16.12

Quantity: 3
---------------------------------------------

Title: House of Sand and Fog
Author: Andre Dubus III
Categories: Home ownership
Genres: Home ownership
Publisher: Vintage Contemporaries
Publish Date: May 3, 2001
ISBN: 9780393338119
Price: $14.16

Quantity: 20
---------------------------------------------

Title: The selfish gene
Author: Richard Dawkins
Categories: Evolution (Biology)
Genres: Evolution (Biology)
Publisher: TU BI TAK
Publish Date: May 1, 1996
ISBN: 9788434501782
Price: $19.13

Quantity: 17
---------------------------------------------

Title: A Beautiful Mind
Author: Sylvia Nasar
Categories: Schizophrenics
Genres: Schizophrenics
Publisher: Altin Kitaplar
Publish Date: February 2002
ISBN: 0743226372
Price: $14.78

Quantity: 11
---------------------------------------------

Title: A Fine Balance
Author: Rohinton Mistry
Categories: literary fiction
Genres: literary fiction
Publisher: Knopf
Publish Date: 2004
ISBN: 0771034806
Price: $24.88

Quantity: 14
---------------------------------------------

Title: The Girl Who Loved Tom Gordon
Author: Stephen King
Categories: Little House on the Prairie
Genres: Little House on the Prairie
Publisher: Ullstein
Publish Date: 2019
ISBN: 9788882745608
Price: $19.39

Quantity: 8
---------------------------------------------

Title: Bird box
Author: Josh Malerman
Categories: Fiction, horror
Genres: Fiction, horror
Publisher: HarperCollins Audio and Blackstone Audio
Publish Date: Oct 10, 2001
ISBN: 9780007586332
Price: $7.35

Quantity: 13
---------------------------------------------

Title: A Portrait of the Artist as a Young Man
Author: James Joyce
Categories: Fiction
Genres: Fiction
Publisher: Gece Kitapligi Yayinlari
Publish Date: Apr 14, 2018
ISBN: 9781904919544
Price: $13.85

Quantity: 17
---------------------------------------------

Title: The History of Love
Author: Nicole Krauss
Categories: Immigrants
Genres: Immigrants
Publisher: W. W. Norton
Publish Date: May 1, 2006
ISBN: 9781419342240
Price: $15.39

Quantity: 14
---------------------------------------------

Title: Dinner at the Homesick Restaurant
Author: Anne Tyler
Categories: Fiction
Genres: Fiction
Publisher: Markaz Al Ahram
Publish Date: 2004
ISBN: 0425098680
Price: $5.11

Quantity: 1
---------------------------------------------

Title: The Sword of Summer
Author: Rick Riordan
Categories: Action
Genres: Action
Publisher: Thorndike Press, A part of Gale, Cengage Learning
Publish Date: 2015
ISBN: 9781410483164
Price: $10.05

Quantity: 5
---------------------------------------------

Title: Dead reckoning
Author: Charlaine Harris
Categories: FICTION / Mystery & Detective / General
Genres: FICTION / Mystery & Detective / General
Publisher: Wheeler Pub.
Publish Date: 2012
ISBN: 0575131403
Price: $16.26

Quantity: 2
---------------------------------------------

Title: Lover Unbound
Author: J. R. Ward
Categories: Fiction
Genres: Fiction
Publisher: Signet Book
Publish Date: September 25, 2007
ISBN: 9781429544559
Price: $9.09

Quantity: 7
---------------------------------------------

Title: The People of Sparks (Book of Ember #2)
Author: Jeanne DuPrau
Categories: Agriculture
Genres: Agriculture
Publisher: Random House
Publish Date: October 30, 2004
ISBN: 9781407049885
Price: $10.68

Quantity: 8
---------------------------------------------

Title: Lilac Girls
Author: Martha Hall Kelly
Categories: Ravensbrück (Concentration camp)
Genres: Ravensbrück (Concentration camp)
Publisher: Penguin Books, Limited
Publish Date: Feb 28, 2017
ISBN: 9781760892579
Price: $11.62

Quantity: 16
---------------------------------------------

Title: The deep end of the ocean
Author: Jacquelyn Mitchard
Categories: Fiction
Genres: Fiction
Publisher: Atlántida
Publish Date: March 1, 1999
ISBN: 9789500817844
Price: $17.81

Quantity: 4
---------------------------------------------

Title: Leaving Time
Author: Jodi Picoult
Categories: Mothers and daughters
Genres: Mothers and daughters
Publisher: Hodder Paperback
Publish Date: Apr 28, 2015
ISBN: 9780345544940
Price: $18.28

Quantity: 10
---------------------------------------------

Title: Rodrick Rules
Author: Jeff Kinney
Categories: New York Times bestseller
Genres: New York Times bestseller
Publisher: Turtleback Books
Publish Date: 2012
ISBN: 9788880334842
Price: $11.42

Quantity: 7
---------------------------------------------

Title: The Surgeon (Jane Rizzoli, Book 1)
Author: Tess Gerritsen, Tess Gerritsen
Categories: Fiction, mystery & detective, police procedural
Genres: Fiction, mystery & detective, police procedural
Publisher: Ballantine Books
Publish Date: Oct 03, 2004
ISBN: 9780345447845
Price: $9.31

Quantity: 18
---------------------------------------------

Title: Effortless
Author: Greg McKeown
Categories: nyt:advice-how-to-and-miscellaneous=2021-05-16
Genres: nyt:advice-how-to-and-miscellaneous=2021-05-16
Publisher: Crown/Archetype
Publish Date: Apr 27, 2021
ISBN: 9780593135648
Price: $11.00

Quantity: 16
---------------------------------------------

Title: The Bonesetter's Daughter
Author: Amy Tan, Amy Tan, AMY TAN
Categories: domestic fiction
Genres: domestic fiction
Publisher: Plaza & Janes Editores, S.A.
Publish Date: Sep 16, 2003
ISBN: 0007124449
Price: $11.93

Quantity: 14
---------------------------------------------

Title: The Gathering Storm
Author: Robert Jordan, Brandon Sanderson
Categories: Rand al'Thor (Fictitious character)
Genres: Rand al'Thor (Fictitious character)
Publisher: ORBIT
Publish Date: Apr 28, 2020
ISBN: 1841491659
Price: $18.38

Quantity: 18
---------------------------------------------

Title: Der Steppenwolf
Author: Hermann Hesse
Categories: Fiction
Genres: Fiction
Publisher: Livraphone
Publish Date: 1996
ISBN: 9780613923002
Price: $9.54

Quantity: 13
---------------------------------------------

Title: Reconstructing Amelia
Author: Kimberly McCreight
Categories: Private schools
Genres: Private schools
Publisher: Simon & Schuster, Limited
Publish Date: 2013
ISBN: 1471258408
Price: $15.76

Quantity: 10
---------------------------------------------

Title: Hot Six
Author: Janet Evanovich
Categories: Women detectives
Genres: Women detectives
Publisher: Audio Renaissance
Publish Date: February 1, 2002
ISBN: 1559279656
Price: $20.47

Quantity: 10
---------------------------------------------

Title: The Scarlet Pimpernel
Author: Emmuska Orczy, Baroness Orczy
Categories: Classic Literature
Genres: Classic Literature
Publisher: Wildside Press, LLC
Publish Date: April 1992
ISBN: 9798795006581
Price: $22.23

Quantity: 18
---------------------------------------------

Title: The Invisible Man
Author: H. G. Wells
Categories: Ciencia-ficción
Genres: Ciencia-ficción
Publisher: Companhia Editora Nacional
Publish Date: 1959
ISBN: 1561034886
Price: $5.25

Quantity: 15
---------------------------------------------

Title: The Darkest Minds
Author: Alexandra Bracken, Amy McFadden, Montserrat Triviño Gonzalez
Categories: JUVENILE FICTION / Action & Adventure / General
Genres: JUVENILE FICTION / Action & Adventure / General
Publisher: Disney-Hyperion
Publish Date: Jun 14, 2018
ISBN: 1368027237
Price: $12.04

Quantity: 19
---------------------------------------------

Title: Anne of the Island
Author: Lucy Maud Montgomery
Categories: College students
Genres: College students
Publisher: Simon & Schuster, Limited
Publish Date: Nov 24, 2016
ISBN: 9780141955247
Price: $21.72

Quantity: 13
---------------------------------------------

Title: Beneath a Scarlet Sky
Author: Mark Sullivan
Categories: Fiction, historical, general
Genres: Fiction, historical, general
Publisher: Brilliance Audio
Publish Date: May 01, 2017
ISBN: 9781503902374
Price: $8.06

Quantity: 10
---------------------------------------------

Title: Song of Susannah
Author: Stephen King
Categories: horror fiction
Genres: horror fiction
Publisher: Turtleback Books
Publish Date: June 2004
ISBN: 9780340891681
Price: $13.72

Quantity: 8
---------------------------------------------

Title: Empire of Storms
Author: Sarah J. Maas
Categories: Magic
Genres: Magic
Publisher: Bloomsbury USA
Publish Date: Apr 13, 2019
ISBN: 9786073156042
Price: $23.48

Quantity: 14
---------------------------------------------

Title: The Tenth Circle
Author: Jodi Picoult
Categories: Date rape
Genres: Date rape
Publisher: Recorded Books
Publish Date: 2007
ISBN: 1419375695
Price: $6.97

Quantity: 9
---------------------------------------------

Title: My Ántonia
Author: Willa Cather
Categories: Literature
Genres: Literature
Publisher: Creative Media Partners, LLC
Publish Date: Sep 26, 2016
ISBN: 0737701803
Price: $19.22

Quantity: 14
---------------------------------------------

Title: Maniac Magee
Author: Jerry Spinelli
Categories: Fiction
Genres: Fiction
Publisher: Little, Brown Books for Young Readers
Publish Date: May 10, 2005
ISBN: 059018377X
Price: $17.27

Quantity: 11
---------------------------------------------

Title: Far From the Madding Crowd
Author: Thomas Hardy
Categories: Fiction
Genres: Fiction
Publisher: Gramercy
Publish Date: 1935
ISBN: 9781627301138
Price: $22.83

Quantity: 11
---------------------------------------------

Title: The eye of the needle
Author: Ben Stoltzfus
Categories: Fiction, general
Genres: Fiction, general
Publisher: Faber
Publish Date: 1967
ISBN: 9780670303328
Price: $16.07

Quantity: 1
---------------------------------------------

Title: Dolores Claiborne
Author: Stephen King
Categories: Women
Genres: Women
Publisher: G.K. Hall
Publish Date: 2009
ISBN: 9781101137970
Price: $23.02

Quantity: 4
---------------------------------------------

Title: Artemis Fowl. The Opal Deception
Author: Eoin Colfer, Adrian Dunbar
Categories: Fiction
Genres: Fiction
Publisher: Disney-Hyperion
Publish Date: 2014
ISBN: 0606320938
Price: $14.01

Quantity: 13
---------------------------------------------

Title: Never Too Far
Author: Abbi Glines
Categories: Family secrets
Genres: Family secrets
Publisher: Simon & Schuster UK
Publish Date: 2013
ISBN: 9781471118630
Price: $5.73

Quantity: 17
---------------------------------------------

Title: Childhood’s End
Author: Arthur C. Clarke
Categories: Human-alien encounters
Genres: Human-alien encounters
Publisher: Turtleback Books
Publish Date: 1956
ISBN: 1439557160
Price: $19.03

Quantity: 11
---------------------------------------------

Title: Pushing the Limits (Pushing the Limits Series, Book 1)
Author: Katie McGarry
Categories: Life change events
Genres: Life change events
Publisher: Black Star Crime
Publish Date: 2017
ISBN: 9780373211838
Price: $14.27

Quantity: 16
---------------------------------------------

Title: NOT THAT KIND OF GIRL
Author: Siobhan Vivian
Categories: Interpersonal relations
Genres: Interpersonal relations
Publisher: PUSH
Publish Date: 2011
ISBN: 0545169151
Price: $24.74

Quantity: 15
---------------------------------------------

Title: Summer Knight
Author: Jim Butcher
Categories: Harry Dresden (Fictitious character)
Genres: Harry Dresden (Fictitious character)
Publisher: Roc
Publish Date: March 31, 2007
ISBN: 0979074932
Price: $15.94

Quantity: 20
---------------------------------------------

Title: Leviathan wakes
Author: James S. A. Corey
Categories: Space warfare
Genres: Space warfare
Publisher: İthaki yayınları
Publish Date: 2021
ISBN: 1456121650
Price: $6.29

Quantity: 9
---------------------------------------------

Title: Jemima J
Author: Jane Green
Categories: Literature
Genres: Literature
Publisher: Broadway
Publish Date: 2009
ISBN: 9780767905183
Price: $20.04

Quantity: 12
---------------------------------------------

Title: Towers Of Midnight
Author: Robert Jordan, Brandon Sanderson
Categories: Fiction, fantasy, epic
Genres: Fiction, fantasy, epic
Publisher: Tor
Publish Date: Jun 30, 2020
ISBN: 9781427210227
Price: $21.92

Quantity: 16
---------------------------------------------

Title: Me and Earl and the Dying Girl
Author: Jesse Andrews
Categories: Humorous stories
Genres: Humorous stories
Publisher: Imprint unknown
Publish Date: 2012
ISBN: 9781459698857
Price: $15.76

Quantity: 7
---------------------------------------------

Title: High five
Author: Janet Evanovich
Categories: Women detectives
Genres: Women detectives
Publisher: Recorded Books
Publish Date: February 2002
ISBN: 0312971346
Price: $10.41

Quantity: 12
---------------------------------------------

Title: The Ersatz Elevator
Author: Lemony Snicket, Brett Helquist, Michael Kupperman, Veronica Canales
Categories: Humorous stories
Genres: Humorous stories
Publisher: Scholastic
Publish Date: October 30, 2003
ISBN: 9780061550447
Price: $10.48

Quantity: 18
---------------------------------------------

Title: Lord of Chaos
Author: Robert Jordan
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Tor
Publish Date: October 1995
ISBN: 187937174X
Price: $17.01

Quantity: 12
---------------------------------------------

Title: Middle school, get me out of here!
Author: David Baldacci, Chris Tebbetts
Categories: Conduct of life
Genres: Conduct of life
Publisher: 
Publish Date: Jul 27, 2012
ISBN: 9780099567547
Price: $10.33

Quantity: 20
---------------------------------------------

Book Maus II: And here my troubles began not found on Open Library.Title: Superfreakonomics
Author: Steven D. Levitt, Stephen J. Dubner
Categories: Economics
Genres: Economics
Publisher: HarperCollins
Publish Date: Jun 28, 2011
ISBN: 9780061959936
Price: $6.33

Quantity: 1
---------------------------------------------

Title: The Dark Half
Author: Stephen King, Grover Gardner narrator, Stephen  King
Categories: alcohol abuse
Genres: alcohol abuse
Publisher: Turtleback Books
Publish Date: 1990-10
ISBN: 9780142428207
Price: $15.36

Quantity: 17
---------------------------------------------

Title: Desperation
Author: Stephen King
Categories: Fiction
Genres: Fiction
Publisher: Turtleback Books
Publish Date: November 11, 1996
ISBN: 9780340654286
Price: $10.32

Quantity: 4
---------------------------------------------

Title: Ignite Me
Author: Tahereh Mafi
Categories: Science fiction
Genres: Science fiction
Publisher: Farshore
Publish Date: February 4th 2014
ISBN: 1484444450
Price: $9.12

Quantity: 18
---------------------------------------------

Title: Across the Universe
Author: Beth Revis
Categories: Interplanetary voyages
Genres: Interplanetary voyages
Publisher: Penguin
Publish Date: 2011
ISBN: 1595143971
Price: $8.12

Quantity: 10
---------------------------------------------

Title: Rules of Civility
Author: Amor Towles
Categories: Fiction
Genres: Fiction
Publisher: viking adult
Publish Date: Nov 10, 2015
ISBN: 0670022691
Price: $15.55

Quantity: 12
---------------------------------------------

Title: To the Lighthouse
Author: Virginia Woolf
Categories: Fiction
Genres: Fiction
Publisher: Distributed by Random House
Publish Date: 1988
ISBN: 1523923865
Price: $22.26

Quantity: 1
---------------------------------------------

Title: Aesop's Fables
Author: Aesop
Categories: Fables
Genres: Fables
Publisher: Murray
Publish Date: February 28, 2006
ISBN: 0706412664
Price: $13.76

Quantity: 11
---------------------------------------------

Title: Tell the wolves I'm home
Author: Carol Rifka Brunt
Categories: Loss (Psychology)
Genres: Loss (Psychology)
Publisher: Pan Macmillan
Publish Date: Aug 15, 2012
ISBN: 9781447213611
Price: $7.84

Quantity: 17
---------------------------------------------

Title: Helter skelter; the true story of the Manson murders
Author: Vincent Bugliosi
Categories: Murder
Genres: Murder
Publisher: Bantam Books
Publish Date: 1974
ISBN: N/A
Price: $8.92

Quantity: 18
---------------------------------------------

Title: Vanity Fair
Author: William Makepeace Thackeray
Categories: Social life and customs
Genres: Social life and customs
Publisher: Dent
Publish Date: January 30, 1987
ISBN: 0140620850
Price: $23.20

Quantity: 18
---------------------------------------------

Title: The Coincidence of Callie & Kayden
Author: Jessica Sorensen
Categories: College students
Genres: College students
Publisher: Forever
Publish Date: Aug 06, 2013
ISBN: 9781455576500
Price: $9.34

Quantity: 14
---------------------------------------------

Title: The Vile Village
Author: Lemony Snicket, Brett Helquist, Michael Kupperman
Categories: Brothers and sisters
Genres: Brothers and sisters
Publisher: Scholastic
Publish Date: Feb 20, 2001
ISBN: 9780060566227
Price: $19.41

Quantity: 13
---------------------------------------------

Title: Mystic river
Author: Dennis Lehane
Categories: Mystery
Genres: Mystery
Publisher: Círculo de Lectores
Publish Date: Jan 30, 2001
ISBN: 9780061238383
Price: $14.26

Quantity: 1
---------------------------------------------

Title: Shopaholic takes Manhattan
Author: Sophie Kinsella
Categories: Fiction
Genres: Fiction
Publisher: Dell Pub.
Publish Date: 2003
ISBN: 9780440334484
Price: $19.59

Quantity: 9
---------------------------------------------

Title: Contact
Author: Carl Sagan
Categories: Exploration
Genres: Exploration
Publisher: GZH
Publish Date: August 28, 1997
ISBN: 9789573314745
Price: $24.07

Quantity: 3
---------------------------------------------

Title: The Tommyknockers
Author: Stephen King
Categories: aliens
Genres: aliens
Publisher: DEBOLSILLO
Publish Date: 2004
ISBN: 0451178424
Price: $18.53

Quantity: 7
---------------------------------------------

Title: Reading Lolita in Tehran
Author: Azar Nafisi
Categories: Sociology
Genres: Sociology
Publisher: Random House Trade Paperbacks
Publish Date: May 2004
ISBN: 9781587244872
Price: $17.42

Quantity: 14
---------------------------------------------

Title: The Dream Thieves
Author: Maggie Stiefvater
Categories: Children's fiction
Genres: Children's fiction
Publisher: Turtleback
Publish Date: 2013
ISBN: 9780606360296
Price: $6.85

Quantity: 3
---------------------------------------------

Title: Life As We Knew It
Author: Susan Beth Pfeffer
Categories: Families
Genres: Families
Publisher: Harcourt Paperbacks
Publish Date: 2006
ISBN: 0152061541
Price: $17.49

Quantity: 3
---------------------------------------------

Title: The Marriage Plot
Author: Jeffrey Eugenides, Jeffery Eugenides
Categories: Appreciation
Genres: Appreciation
Publisher: Macmillan USA
Publish Date: 2012
ISBN: 9780007441273
Price: $18.30

Quantity: 6
---------------------------------------------

Title: A Crown of Swords
Author: Robert Jordan
Categories: Fantasy fiction
Genres: Fantasy fiction
Publisher: Tor
Publish Date: 2010
ISBN: 1593979762
Price: $16.14

Quantity: 17
---------------------------------------------

Title: Annihilation
Author: Jeff VanderMeer
Categories: Nebula Award Winner
Genres: Nebula Award Winner
Publisher: Farrar, Straus and Giroux
Publish Date: Mar 01, 2017
ISBN: 0007550707
Price: $8.74

Quantity: 10
---------------------------------------------

Title: The Mysterious Benedict Society (The Mysterious Benedict Society #1)
Author: Trenton Lee Stewart
Categories: Adventure and adventurers
Genres: Adventure and adventurers
Publisher: Books on Tape
Publish Date: May 2007
ISBN: 9780316265010
Price: $19.40

Quantity: 5
---------------------------------------------

Title: Dirk Gently's Holistic Detective Agency
Author: Douglas Adams, Benito Gómez Ibáñez
Categories: abiogenesis
Genres: abiogenesis
Publisher: Pan Macmillan
Publish Date: 2021
ISBN: 9781590070635
Price: $16.73

Quantity: 8
---------------------------------------------

Title: Seven Up
Author: Janet Evanovich
Categories: Novela de misterio
Genres: Novela de misterio
Publisher: Brilliance Audio Unabridged Lib Ed
Publish Date: October 2003
ISBN: 9781587885327
Price: $11.83

Quantity: 7
---------------------------------------------

Title: The Iron Daughter (Iron Fey #2)
Author: Julie Kagawa
Categories: Fantasy
Genres: Fantasy
Publisher: Harlequin Teen
Publish Date: 2010
ISBN: 9781299321427
Price: $15.53

Quantity: 5
---------------------------------------------

Title: The war dead of the Commonwealth
Author: Commonwealth War Graves Commission
Categories: Commonwealth of Nations
Genres: Commonwealth of Nations
Publisher: N
Publish Date: 1960
ISBN: N/A
Price: $21.87

Quantity: 19
---------------------------------------------

Title: Golden Son
Author: Pierce Brown
Categories: Fiction, science fiction, action & adventure
Genres: Fiction, science fiction, action & adventure
Publisher: Whole Story Audiobooks
Publish Date: Oct 07, 2015
ISBN: 1471292010
Price: $22.37

Quantity: 16
---------------------------------------------

Title: Uprooted
Author: Naomi Novik
Categories: Young women
Genres: Young women
Publisher: Del Rey
Publish Date: 2015
ISBN: 0804179034
Price: $24.21

Quantity: 17
---------------------------------------------

Title: All Creatures Great and Small (All Creatures Great and Small #1-2)
Author: James Herriot
Categories: Open Library Staff Picks
Genres: Open Library Staff Picks
Publisher: G K Hall & Co
Publish Date: April 15, 1998
ISBN: 0553138596
Price: $20.41

Quantity: 13
---------------------------------------------

Title: Attack On Titan, Vol. 1
Author: Hajime Isayama
Categories: Giants
Genres: Giants
Publisher: Carlsen Verlag GmbH
Publish Date: Mar 18, 2014
ISBN: 1612620248
Price: $10.98

Quantity: 15
---------------------------------------------

Title: Hard eight
Author: Janet Evanovich
Categories: Detective and mystery stories
Genres: Detective and mystery stories
Publisher: St. Martin's Press
Publish Date: Jun 09, 2003
ISBN: 1250058007
Price: $6.29

Quantity: 16
---------------------------------------------

Title: Among the Hidden (Shadow Children #1)
Author: Margaret Peterson Haddix
Categories: Science fiction
Genres: Science fiction
Publisher: Recorded Books
Publish Date: June 2004
ISBN: 9781402576171
Price: $16.27

Quantity: 15
---------------------------------------------

Title: The complete idiot's guide to wicca and witchcraft
Author: Denise Zimmermann, Katherine A. Gleason
Categories: Nonfiction
Genres: Nonfiction
Publisher: Penguin USA, Inc.
Publish Date: August 1, 2006
ISBN: 9781101097496
Price: $20.19

Quantity: 5
---------------------------------------------

Title: Daughter of Fortune
Author: Carla Kelly
Categories: Fiction, romance, historical
Genres: Fiction, romance, historical
Publisher: D.I. Fine
Publish Date: 1985
ISBN: 9780917657238
Price: $6.16

Quantity: 4
---------------------------------------------

Title: The Murder of Roger Ackroyd
Author: Agatha Christie
Categories: detective fiction
Genres: detective fiction
Publisher: Editions du Masque
Publish Date: November 3, 1980
ISBN: 0062986147
Price: $20.53

Quantity: 18
---------------------------------------------

Title: The Statistical Probability of Love at First Sight
Author: Jennifer E. Smith
Categories: Fate and fatalism
Genres: Fate and fatalism
Publisher: Little, Brown Books for Young Readers
Publish Date: 2013
ISBN: 0316122394
Price: $5.94

Quantity: 7
---------------------------------------------

Title: The Infinite Sea
Author: Rick Yancey
Categories: Aliens
Genres: Aliens
Publisher: Speak
Publish Date: November 3, 2015
ISBN: 0399162429
Price: $20.04

Quantity: 4
---------------------------------------------

Title: The Awakening
Author: Kate Chopin
Categories: Adultery
Genres: Adultery
Publisher: Lulu.com
Publish Date: 2011-09-19
ISBN: 9798477684113
Price: $21.50

Quantity: 19
---------------------------------------------

Title: Handle with care
Author: Jodi Picoult
Categories: Wrongful life
Genres: Wrongful life
Publisher: Allen & Unwin Pty Ltd
Publish Date: 2009
ISBN: 9780743296427
Price: $14.50

Quantity: 15
---------------------------------------------

Title: Dead Witch Walking (Rachel Morgan, Book 1)
Author: Kim Harrison, Gavin Marguerite
Categories: Vampires
Genres: Vampires
Publisher: Tantor Media
Publish Date: 2009
ISBN: 9780007236916
Price: $14.10

Quantity: 11
---------------------------------------------

Title: The Lost World
Author: Arthur Conan Doyle
Categories: Adventure stories
Genres: Adventure stories
Publisher: Tor
Publish Date: May 30, 2016
ISBN: 9798548240996
Price: $23.60

Quantity: 8
---------------------------------------------

Title: The Goose Girl (Books of Bayern #1)
Author: Shannon Hale
Categories: Books of Bayern
Genres: Books of Bayern
Publisher: Bloomsbury USA Childrens
Publish Date: 2013
ISBN: 9781417685707
Price: $12.30

Quantity: 15
---------------------------------------------

Title: Fullmetal Alchemist Novel Vol. 1
Author: Square Enix
Categories: N/A
Genres: N/A
Publisher: N
Publish Date: Aug 12, 2003
ISBN: 9784757508712
Price: $14.00

Quantity: 7
---------------------------------------------

Title: The Girl in the Spider's Web
Author: David Lagercrantz
Categories: Reporters and reporting
Genres: Reporters and reporting
Publisher: Alfred A. Knopf
Publish Date: 2015
ISBN: 9780385354288
Price: $16.66

Quantity: 7
---------------------------------------------

Title: Steelheart (The Reckoners, Book 1)
Author: Brandon Sanderson, MacLeod Andrews, Rafael Marín Trechera
Categories: fantasy
Genres: fantasy
Publisher: Brilliance Audio
Publish Date: Apr 28, 2016
ISBN: 9788576573463
Price: $15.77

Quantity: 12
---------------------------------------------

Title: Gabriels Rapture
Author: Sylvain Reynard
Categories: collectionID:CDarkromance
Genres: collectionID:CDarkromance
Publisher: Penguin Random House
Publish Date: 2012
ISBN: 9780425265956
Price: $13.44

Quantity: 16
---------------------------------------------

Title: The Eyre Affair
Author: Jasper Fforde
Categories: Books and reading
Genres: Books and reading
Publisher: Eksmo
Publish Date: Dec 30, 2009
ISBN: 1444784269
Price: $6.28

Quantity: 7
---------------------------------------------

Title: Colorless Tsukuru Tazaki and His Years of Pilgrimage
Author: 村上春樹, Philip Gabriel
Categories: Fiction, fantasy, contemporary
Genres: Fiction, fantasy, contemporary
Publisher: Penguin Random House
Publish Date: 2015
ISBN: 0099590387
Price: $5.22

Quantity: 1
---------------------------------------------

Title: Confessions
Author: Augustine of Hippo
Categories: Religious aspects of Truth
Genres: Religious aspects of Truth
Publisher: Christian Library
Publish Date: 1990
ISBN: 0451608992
Price: $15.35

Quantity: 17
---------------------------------------------

Title: The Amulet of Samarkand
Author: Jonathan Stroud
Categories: Genies
Genres: Genies
Publisher: Vassallucci
Publish Date: June 2004
ISBN: 142311146X
Price: $17.36

Quantity: 13
---------------------------------------------

Title: El invierno del mundo / Winter of the World
Author: Ken Follett
Categories: Fiction
Genres: Fiction
Publisher: Pan
Publish Date: Feb 01, 2013
ISBN: 1447231139
Price: $23.85

Quantity: 2
---------------------------------------------

Title: The One and Only Ivan
Author: Katherine Applegate
Categories: Animals
Genres: Animals
Publisher: Turtleback Books
Publish Date: Mar 27, 2012
ISBN: 9788494258220
Price: $15.59

Quantity: 13
---------------------------------------------

Title: The Billionaire's Marriage Bargain
Author: Carole Mortimer
Categories: Fiction
Genres: Fiction
Publisher: Harlequin Mills & Boon, Limited
Publish Date: September 1, 2007
ISBN: 0373688997
Price: $14.68

Quantity: 5
---------------------------------------------

Title: Dubliners
Author: James Joyce
Categories: Daily Express
Genres: Daily Express
Publisher: CSA Word
Publish Date: June 30, 2004
ISBN: 1870539249
Price: $6.95

Quantity: 16
---------------------------------------------

Title: Under the Never Sky
Author: Veronica Rossi
Categories: JUVENILE FICTION / Science Fiction
Genres: JUVENILE FICTION / Science Fiction
Publisher: Harper Audio
Publish Date: 2013
ISBN: 9780748133727
Price: $7.88

Quantity: 9
---------------------------------------------

Title: The Big Sleep
Author: Raymond Chandler
Categories: Fiction
Genres: Fiction
Publisher: Penguin Books, Limited
Publish Date: November 14, 1991
ISBN: 9789100480349
Price: $14.02

Quantity: 13
---------------------------------------------

Book One Thousand White Women: The Journals of Mary Dodd not found on Open Library.Title: The Ruins of Gorlan
Author: John Flanagan
Categories: nyt:series_books=2010-06-26
Genres: nyt:series_books=2010-06-26
Publisher: Puffin Books
Publish Date: Aug 27, 2004
ISBN: 0759320756
Price: $21.03

Quantity: 20
---------------------------------------------

Title: White Teeth
Author: Zadie Smith, Jenny Sterlin, Ana María de la Fuente Suárez
Categories: Fiction
Genres: Fiction
Publisher: Rose & Rose Associates
Publish Date: Mar 30, 2023
ISBN: 9780753169469
Price: $9.72

Quantity: 4
---------------------------------------------

Title: Rise of the Evening Star
Author: Brandon Mull
Categories: Mythical Creatures
Genres: Mythical Creatures
Publisher: Roca Editorial
Publish Date: April 22, 2008
ISBN: 3442268206
Price: $18.57

Quantity: 7
---------------------------------------------

Title: The Psychopath Test
Author: Jon Ronson
Categories: Psychology, pathological
Genres: Psychology, pathological
Publisher: Macmillan
Publish Date: Jun 01, 2011
ISBN: 9780330451369
Price: $10.61

Quantity: 12
---------------------------------------------

Title: Mark Z. Danielewski's House of leaves
Author: Mark Z. Danielewski
Categories: Holes
Genres: Holes
Publisher: random house
Publish Date: July 6, 2000
ISBN: 9780375703768
Price: $18.45

Quantity: 3
---------------------------------------------

Title: Moloka'i
Author: Alan Brennert
Categories: Fiction
Genres: Fiction
Publisher: Guy Saint-Jean éditeur
Publish Date: 2003
ISBN: 9781429902281
Price: $8.68

Quantity: 17
---------------------------------------------

Title: Chocolat
Author: Joanne Harris
Categories: Literature
Genres: Literature
Publisher: Hodder & Stoughton Audio Books
Publish Date: March 1, 2002
ISBN: 0385257430
Price: $12.91

Quantity: 18
---------------------------------------------

Title: The Complete Fairy Tales
Author: Jacob and Grimm
Categories: Fiction, fantasy, general
Genres: Fiction, fantasy, general
Publisher: Routledge
Publish Date: September 18, 2003
ISBN: 041528595X
Price: $14.12

Quantity: 14
---------------------------------------------

Title: The Glass Menagerie
Author: Tennessee Williams
Categories: memory plays
Genres: memory plays
Publisher: New Directions
Publish Date: 1975
ISBN: 0822204509
Price: $24.29

Quantity: 20
---------------------------------------------

Title: A moveable feast
Author: Ernest Hemingway
Categories: Correspondence
Genres: Correspondence
Publisher: Collier Books
Publish Date: 2009
ISBN: 0140024239
Price: $17.06

Quantity: 7
---------------------------------------------
"""

# Regular expressions to extract data
title_pattern = re.compile(r"Title: (.+)")
author_pattern = re.compile(r"Author: (.+)")
genre_pattern = re.compile(r"Genres?: (.+)")
publisher_pattern = re.compile(r"Publisher: (.+)")
publish_date_pattern = re.compile(r"Publish Date: (.+)")
isbn_pattern = re.compile(r"ISBN: (\d+)")
price_pattern = re.compile(r"Price: (.+)")
quantity_pattern = re.compile(r"Quantity: (.+)")

# Function to extract data
def extract_info(text):
    titles = title_pattern.findall(text)
    authors = author_pattern.findall(text)
    genres = genre_pattern.findall(text)
    publishers = publisher_pattern.findall(text)
    publish_dates = publish_date_pattern.findall(text)
    isbns = isbn_pattern.findall(text)
    prices = price_pattern.findall(text)
    quantity = quantity_pattern.findall(text)

    # Create list of dictionaries
    books_info = []
    for title, author, genre, publisher, publish_date, isbn, price, quantity in zip(titles, authors, genres, publishers, publish_dates, isbns, prices, quantity):
        book_info = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Publisher": publisher,
            "Publish Date": publish_date,
            "ISBN": isbn,
            "Price": price,
            "Quantity": quantity
        }
        books_info.append(book_info)

    return books_info

# Extracted information
books_info = extract_info(text)

# Create SQLite database and table
conn = sqlite3.connect('../books.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books
             (Title TEXT, Author TEXT, Genre TEXT, Publisher TEXT, Publish_Date TEXT, ISBN TEXT, Price TEXT, Quantity TEXT)''')

# Insert data into the table
for book in books_info:
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (book['Title'], book['Author'], book['Genre'], book['Publisher'], book['Publish Date'], book['ISBN'], book['Price'], book['Quantity']))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully into the database.")