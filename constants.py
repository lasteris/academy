NEW_PLAYER = """1. Select your league in {0.mention}.
2. Buy only heroes from the league store, that are described in {1.mention}.
3. From arena store buy only JSGL for start.
4. Fund every raid a reasonable amount.
5. Be present at raids or write us how much time you will be inactive.
**Have fun**"""

JOIN_MESSAGE = """Hey {0.mention}, welcome to **The Academy!**
Just visiting? Feel free to cruise with us at the Academy!
Or maybe you are looking for a league.
In our arsenal, we have four, depends on your raid preference time:
Vipers raid around 1-2 AM GMT.
Stars raid around 12:30 PM-2 PM GMT.
Predators raid around 5-7 PM GMT.
Eternals raid around 2-3 PM GMT.
To see in-game code of chosen league, please type one of these commands:
    -predators, -stars, -vipers, eternals
To see chats of chosen league, you need to have corresponding role.
So, type: -join <league name here> (-join stars)"""

TIME = '{0}\n***This is Academy time (GMT)***'

PREDATORS = '2EH9EW'
VIPERS = 'GKETR1'
STARS = 'P87X95'
TOWER = 'AP1BS1'
KNIGHTS = '8R5QGE'
REVERSE = 'EFQGZ2'
ETERNAL = 'R66C8M'

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
-eternal (Academy Eternals)
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
predators/stars/vipers/eternals/jumpers
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

*command to calculate gear material cost:*
```
-gear-cost
```*parameters:*
As parameters you can pass one **number** (to get cost from **1** to this **number**) or range
(to get cost from **left** to **right** boundary).
*usage:*
```
-gear-cost 1 2
```*result output from bot:*
\tFor levels 1 to 2, it costs 20 gear materials.
"""

CD_START_MESSAGE = """**cooldown** (re)started for {0.mention} at {1} AT.
**It** will end on {2} AT.
**You** *will recieve a warning*.
"""
DATE_TIME_FORMAT = "%d %B %Y %I:%M %p"

CD_STATUS = '{0.mention}, {1} days before your cooldown expires.'
CD_EXPIRED = '{0.mention}, cooldown expired.'

ROLE_ALREADY_ADDED = "{0.mention}, you have already joined in {1}!"
ROLE_ADDED_SUCCESSFULLY = "role {0} is added to {1}"
ROLE_ALREADY_REMOVED = "{0}, you have already removed from {1}!"
ROLE_REMOVED_SUCCESSFULLY = "role {0} is removed from {1}"
ERROR_ON_ROLES_INTERACTION = 'You can interact only with these roles:\npredators, vipers, stars, eternals, jumpers'
LITTLE_BOY = 'you can not change anything except your role, little boy.'

GEAR_COST = """Up to {0}, a single gear costs {1} gear materials.
Full set costs {2} gear materials"""
GEAR_COST_MULTI = """For levels {0} to {1}, it costs {2} gear materials.
Full set costs {3} gear materials
"""
GEAR_COST_OUT_RANGE = "Gear level out of range, only from 1 to 70"
GEAR_COST_WHOLE_NUM = "Must be a whole number"

JUMP_WATCH_USAGE = """
            Wrong usage of command.
            For managing of process youi should use of these parameters:
            \start, status, stop"""
NEXT_WATCH_CHECK_AT = "Watching is **active**.\nNext expiration check occurs at **{0}**"
WATCH_INACTIVE = "Watching is **inactive**."
WATCH_STARTED = "Watching **started**."
WATCH_CANCELLED = "Watching **cancelled**."
PARAMETER_NOT_RECOGNIZED = "Parameter not recognized."
LEAGUES = """
```
Academy Vipers
GKETR1/Raid 7/1-2 AM GMT
```
```
Academy Predator
2EH9EW/Raid 6-7/5-7 PM GMT
```
```
Academy Eternals
R66C8M/Raid 6/2-3 PM GMT
```
```
Academy Stars
P87X95/Raid 6/12:30 PM-2 PM GMT
```
"""
