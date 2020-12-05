NEW_PLAYER = """1. Select your league in {0.mention}.
2. Buy only heroes from the league store, that are described in {1.mention}.
3. From arena store buy only JSGL for start.
4. Fund every raid a reasonable amount.
5. Be present at raids or write us how much time you will be inactive.
**Have fun**"""

JOIN_MESSAGE = """Hey {0.mention}, welcome to **The Academy!**

Before entering a league keep in mind that raids are:
In vipers around 1-2 AM GMT.
In stars around 12:30 AM - 2 PM GMT.
In predators around 5-6 PM GMT.
To see code of chosen league in the game just type:
    -predators
    -stars
    -vipers
To see chats of chosen league just type:
    -join predators
    -join vipers
    -join stars"""

TIME = '{0}\n***This is Academy time (GMT)***'

PREDATORS = '2EH9EW'
VIPERS = 'GKETR1'
STARS = 'P87X95'
TOWER = 'AP1BS1'
KNIGHTS = '8R5QGE'
REVERSE = 'EFQGZ2'
HENTAI = 'R66C8M'

CHARACTERS_JSON_PATH = "characters.json"
BUILDS_JSON_PATH = "characters/builds.json"

BUILD_NOT_EXISTS = "No build has been added for character."
CHARACTER_NOT_RECOGNIZED = " Character not recognized."

HELP = """**List of Academy bot commands**
*commands to see some league codes(to find them in game):*
\t*major league codes:*
```
-predators (Academy Predator)
-vipers (Academy Vipers)
-stars (Academy Stars)
```
\t*additional league codes (for jumps):*
```
-tower (Academy Tower)
-reverse (Reverse Academy)
-knights (Academy Knights)
```
*command to see current time by Academy timezone (GMT):*
```
-time
```
*commands to add/remove on yourself a role to see chats, corresponding to a specific league*:
```
-join
-remove
```*parameters:*
```
predators/stars/vipers/jumpers
```*usage:*
```
-join predators
```*result output from bot:*
\trole **stars** added to **@user**

*command for new players:*
```
-newplayer
```
*commands for getting some useful info about characters:*
```
-name (full name of character from abbreviation)
-passives (passives retyped from game)
-specials (specials retyped from game)
-supermove (supermoves retyped from game)
-build (assemblies selected for better character development)
```*parameters:*
\tThe character\'s abbreviation is used as a parameter.
*usage:*
```
-name koaam
```*result output from bot:*
\tKing of Atlantis Aquaman

*command for cooldown tracking:*
```
-jump-cd
```*parameters:*
```status```optional parameter for getting current state of cooldown expiration.
*usage:*
```
-jump-cd status
```*result output from bot:*
\t**@user**, 10 days before your cooldown expires.
"""

CD_START_MESSAGE = """**cooldown** (re)started for {0.mention} at {1} AT.
**It** will end on {2} AT.
**You** *will recieve a warning*.
"""
DATE_TIME_FORMAT = "%d %B %Y %I:%M %p"

CD_STATUS = '{0.mention}, {1} days before your cooldown expires.'
CD_EXPIRED = '{0.mention}, cooldown expired.'

ERROR_ON_ROLES_INTERACTION = 'You can interact only with these roles:\npredators, vipers, stars, jumpers'
LITTLE_BOY = 'you can not change anything except your role, little boy.'
