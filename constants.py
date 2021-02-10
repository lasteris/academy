###################################################
LOGGED = "Bot Logged in as id: {}, name: {} \n"
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
###################################################

###################################################
#paths
CHARACTERS_JSON_PATH = "resources/characters.json"
BUILDS_JSON_PATH = "resources/builds.json"
###################################################

###################################################
#welcome
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
**V**ipers raid around 1-2 AM GMT. (T7)
**P**redators raid around 5-7 PM GMT. (T7)
**E**ternals raid around 3-4 PM GMT. (T6)
**R**ebels raid free hits any hour (T6)
**S**tars raid around 1 PM-2 PM GMT. (T6).
To see in-game code of chosen league, please type one of these commands:
    -predators, -stars, -vipers, eternals
To see chats of chosen league, you need to have corresponding role.
So, type: -join <league name here> (-join stars)"""

LEFT_SERVER = "{0.display_name} left the Academy!"
#special for akpro
AKPRO = "Hey, new guy arrived into server. His name - {0.name}"
###################################################

###################################################
#main constant (mostly usable)
HOURS_FORMAT = "%H:%M:%S"
TIME = '{0}\n***This is Academy time (GMT)***'
DATE_TIME_FORMAT = "%d %B %Y %I:%M %p"
###################################################

###################################################
#role tracking
ROLE_ALREADY_ADDED = "{0.mention}, you have already promoted to {1.name} earlier!"
ROLE_ADDED_SUCCESSFULLY = "Congratulations, {0.mention}, you have been promoted to the {1.name}. :thumbsup:"
ROLE_ALREADY_REMOVED = "{0.mention}, you have already demoted from {1.name} earlier!"
ROLE_REMOVED_SUCCESSFULLY = "Congratulations, {0.mention}, you have been demoted from {1.name}. :thumbsup:"
ERROR_ON_ROLES_INTERACTION = '**Warning!**\nYou should interact only with these roles:\npredators, vipers, stars, eternals, jumpers, rebels, among us!'
LEAGUE_RAID_WARNING = """Hello, {0.name}

Since you joined {1.name}, you need to know how we attack raids.

We __**coordinate**__ our attacks. (**always read raid-plan**, we can add instructions before each raid)

1. When a **raid captain** says to prepare for a boss
    - Captain Cold (CC)
    - Gorilla Grodd (GG)
    - Scarecrow (HSC)
    - Doctor Fate (DF)
    - Brainiac (Brainy or Brnc)
You are supposed to make your teams and say "ready" when done.
2. The captain will ask for "ready check" or "final call", everyone will respond with "ready" to show they are attentive and not away from the game.
3. Finally, the captain will say "Go", then you can attack the boss.

Next, we conduct either one day or two day raids. (check the raid plan)

One day raid means we finish the entire raid in 3 pips, so we must plan our teams wisely for maximum damage wherever needed,
Two day raid means we finish the raid in 6 pips, over 2 days."""
AT_LEAST_4 = "Please enter at least 4 characters to search for roles."
###################################################

###################################################
#gear calculator
GEAR_COST = """Up to {0}, a single gear costs {1} gear materials.
Full set costs {2} gear materials"""
GEAR_COST_MULTI = """For levels {0} to {1}, it costs {2} gear materials.
Full set costs {3} gear materials
"""
GEAR_COST_OUT_RANGE = "Gear level out of range, only from 1 to 70"
GEAR_COST_WHOLE_NUM = "Must be a whole number"
GEAR_SECOND_LESS_THAN_FIRST = "First number ({}) cannot be more than or equal to second number ({})"
###################################################

###################################################
#jump
JUMP_WATCH_USAGE = """
            Wrong usage of command.
            For managing of process youi should use of these parameters:
            \start, status, stop"""
NEXT_WATCH_CHECK_AT = "Watching is **active**.\nNext expiration check occurs at **{0}**"
WATCH_INACTIVE = "Watching is **inactive**."
WATCH_STARTED = "Watching **started**."
WATCH_CANCELLED = "Watching **cancelled**."
PARAMETER_NOT_RECOGNIZED = "Parameter not recognized."
CD_STATUS = '{0.mention}, {1} days before your cooldown expires.'
CD_EXPIRED = '{0.mention}, cooldown expired.'
CD_START_MESSAGE = """**cooldown** (re)started for {0.mention} at {1} AT.
**It** will end on {2} AT.
**You** *will recieve a warning*.
"""
###################################################

###################################################
#league codes
LEAGUES = """
```yaml
Academy Vipers
GKETR1 | Raid 7 | 1-2 AM GMT
```
```yaml
Academy Predator
2EH9EW | Raid 7| 5-7 PM GMT
```
```yaml
Academy Eternals
R66C8M | Raid 6 | 3-4 PM GMT
```
```yaml
Academy Stars
P87X95 | Raid 6 | 1-2 PM GMT
```
```yaml
Academy Rebels
1R125Q | Raid 6 | Free Hits Anytime
```
"""
PREDATORS = '2EH9EW'
VIPERS = 'GKETR1'
STARS = 'P87X95'
TOWER = 'AP1BS1'
KNIGHTS = '8R5QGE'
REVERSE = 'EFQGZ2'
ETERNAL = 'R66C8M'
REBEL = '1R125Q'
###################################################

###################################################
#messages
NO_ACCESS = "sorry, {0.mention}, but you have no access to that feature."
ALL_REPEAT_STOP = "Repeating of all messages stopped."
MSG_REPEAT_STOP = "Repeating of {} stopped !"
MSG_REPEAT_RESTART = "Repeating of {} restarted !"
MSG_ALREADY_IN = "Message with given name already exists.\nGive it other name or use -repeat *restart* {}"
MSG_NOT_FOUND = "Message with given name not found."
MSG_FORMAT = "{}: {}"
WRONG_BEHAVIOUR = "something went wrong!"
###################################################

###################################################
#characters
## name list command output - { abbreviation - name }
LINE_FORMAT = "{} - {}"
ABBR_NOT_RECOGNIZED = "Abbreviation not recognized.\n Try `-name list` to see all abbreviations."
###################################################

###################################################
#builds
BUILD_NOT_EXISTS = "No build has been added for character."
CHARACTER_NOT_RECOGNIZED = " Character not recognized."
###################################################

###################################################
#formatted
BOLD = "**{}**"
ITALIC = "*{}*"
STD = "{}"
CHUNKED = "```\n{}\n```"
###################################################

###################################################
#unscheduled
INVALID_NUMBER_ARGUMENTS = "Invalid number of arguments."
DEBUG_MESSAGE = "{0.display_name} sent message '{1.content}' to {2.mention}."
NOT_ENOUGH_POWER = "Sorry, you have not enough power."
DELETION_STARTED = "deletion started."
DELETION_PROCESS = "{} messages deleted. Goal is {}"
DELETION_STOPPED = "{} messages deleted. Stopped."
NOT_VALID_NUMBER = "Please, try valid number."