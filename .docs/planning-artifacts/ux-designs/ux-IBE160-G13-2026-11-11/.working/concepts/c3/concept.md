# c3 — Pixel-RPG

**Idea.** LifeMode is a 16-bit life RPG. Markus is a pixel sprite standing in a pixel room. Menus are classic bone-bordered RPG windows with a blinking cursor, and every money or wellbeing change pops up like a damage or heal number. It is a game first. The finance lives inside rules teenagers already know by heart: stats, inventory, quests and level-ups.

## Game dynamics
- **Monthly loop = a turn.** The hub is an overworld screen. At the top sits a 12-block year track, with gold notches on the active months. Below it is the room, the TRIVSEL stat panel (64/100, a marker at 50, and Stress/Fritid/Sosialt as segmented bars with numbers and ± deltas), four command tiles (Telefon, Månedsplan, Jobb, Penger) and a big gold **FORTSETT** button. A quiet month is one tap. An "!" speech bubble over the avatar's head says "2 NYE".
- **Year = world map / quest log.** Months are nodes on a winding path. Highlight months are gold star tiles, an echo month carries the callback glyph, a storm cloud warns "krise?", and "NIVÅ 16 – mopedlappen låst opp" is a level-up gate. The quest log lists what is coming: an April event, a dated summer-job offer, an echo due in August, and the open moped licence with 4 150 kr missing.
- **Month plan = party/skill slots.** School and work are locked equipment. There are 3 activity slots because extra shifts lock slot 4 ("tilbake i juni"). Activities are a skill list with cost and effects, placed by tapping. A missing amount shows as a locked row ("Mangler 250 kr"). There is also "Samme som forrige måned".
- **Event = dialogue with portrait + menu.** Emma's pixel portrait asks the question. Each option is an action with kroner, sosialt and stress, and one is marked GRATIS.
- **Consequence = floating numbers.** "−450 kr hyttetur", "+120 kr fra Emma", "+4 sosialt". The **EKKO** badge is a callback card that links back to the month-10 quest. **Hvorfor?** splits the net amount by cause. ÅPNET/LUKKET lines and the target progress (72 % → 70 %) follow. Room layers act as loot: the new piggy bank gets a "NY!" tag.

## Visual language
Night-ink ground and deep menu-blue windows with notched bone borders. Gold is kroner, green is a gain, coral is a loss. Every value also carries a sign and a word. Art is crisp SVG rect grids with `crispEdges`, all original: Markus, Emma, Norwegian town, påskehytte. Silkscreen sets headings and labels. DotGothic16 sets body text, because it keeps long Norwegian sentences and digits readable. For motion, numbers float up and fade, the cursor blinks, and a level-up banner flashes once.

## Why it works
Teens already read HP bars, loot and quest logs fluently. Money becomes stats they manage, not schoolwork. The "why" sits in the place a game always puts it: the combat log.

## Risks
Retro can read as nostalgia for older players. The look is dense on small screens. Pixel faces are weak at small text sizes, which is why DotGothic16 carries the body text. Floating numbers must not replace the Hvorfor? panel.

## Prototype first
The hub → FORTSETT → event → floating-number result → Hvorfor? loop, timed on a phone on a bus.
