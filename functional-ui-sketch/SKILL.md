---
name: functional-ui-sketch
description: >-
  FIRES when someone asks for a sketch, mockup, wireframe or "how will it look / how will I use it" of screens, pages,
  panels or forms; when a plan names a UI only in words and the build is about to start; or when a review of a built
  UI shows the layout or the path between screens was never agreed. Produces simplistic graphics (SVG boxes with real
  labels and real sample data, one accent for the primary action, no styling) for every screen, the flow between them
  with the action on each arrow, and the states that change the layout, in one committed HTML file, so the user can
  feel the user-flow before anything is built. Never ASCII art. Not for how something moves, hides or transitions
  (that is interactive-mechanism-sketch), not for tuning numbers (real-knobs-as-sliders), not for visual identity.
mission: >-
  Let a person agree on which screens exist, what each shows and does, and how they get from one to the next, before a
  line of UI code is written, with a sketch cheap enough to redraw on every correction.
aliases: []
---

# functional-ui-sketch — agree on screens and flow with grey boxes

> **DRAFT** (designer, 2026-11-01), cut from the live case below. Grade `[SPIKE]` until a fresh agent produces a
> sketch from this skill alone on a case the author did not pick. Technique: no paths, no project names.

## The claim

Words describe a UI in the order the writer thinks; a person uses it in the order the screen allows. The gap is
invisible until something is built, and then it is expensive. A grey-box sketch of every screen, plus the arrows
between them, makes the user's path visible in one look, at a cost low enough to redraw after every correction. The
sketch's job is agreement, so everything that invites taste (colour, type, icons, polish) is left out on purpose.

## The method

1. **Jobs before screens.** Write the user's jobs as one-sentence outcomes in the user's words ("see which skills
   were never visible last week"). Each job names the screen that serves it. A screen that serves no job is cut; a
   job with no screen is the first finding.
2. **One grey-box drawing per screen.** A fixed frame, regions as rectangles, each region labelled with what it
   shows and filled with real sample content from the domain (actual names, plausible numbers, never placeholder
   text). Controls are labelled with the verb of what they do. One accent colour marks the primary action and
   nothing else. No fonts, icons, colours or spacing decisions: those are not what is being agreed.
3. **The flow.** The screens in a row, arrows between them labelled with the action that moves the user, the happy
   path first, and the count of steps written on it. A second path (the beginner's, the error's) is a second row.
4. **The states that change the layout.** For each screen: empty (nothing recorded yet), blocked or failed (what
   the user is told and can do), and many (what happens when the list is long). Draw a small variant only where the
   layout differs; otherwise one line of text.
5. **Numbered callouts, one list.** Anything that needs a sentence gets a number on the drawing and a line in the
   notes under it. The notes are the only prose.
6. **The review.** Walk the user through one job per screen: "does this get you to X?" Each correction gets the next
   number, the sketch is redrawn, and nothing is built until the walk-through passes with no new numbers.
7. **Hand-over.** The agreed sketch becomes the build's acceptance list: each region is a component with the data it
   shows, each arrow is a navigation or action, each state is a test. The sketch file is committed beside the plan.

## The medium

One self-contained HTML file, each screen an inline `<svg>` with a stable id, drawn from a small data list
(frame, boxes, buttons, callouts) by a few lines of script so a correction is a data edit, not a redraw by hand. It
renders without a build, diffs in git, and can be published for viewing.

Never: ASCII art (no proportion, unreadable at a glance, reads as code); a screenshot of a drawing tool nobody can
edit; a styled mock (the conversation turns to taste); an animation (that is a mechanism sketch).

## A second form: decision cards — Before | Now | Gate | Gate needed? (amended 2026-11-09, [SPIKE])

When the thing to agree is a PLANNED CHANGE to a pipeline or a rule about how a part must look or sit in use (a border
that may not repeat a motif, a header centred on a line, a part that must not stretch), draw one card per change,
never a table of words. The owner's names for the columns (2026-11-09), used verbatim:

| Column | What | Why |
|---|---|---|
| **Before** | the situation before the planned change: the owner's own mark or crop, captioned with their words | the change answers their finding, not a hypothetical |
| **Now** | the situation after the change: a grey-box drawing (a small ✗ "before" schematic beside the ✓ "now"), numbered callouts, the change in one sentence | a change in words cannot be said yes to by eye |
| **Gate** | how the pipeline will check it, with TODAY's measured values against the proposed limit | the owner rules on the threshold too, not only the wording |
| **Gate needed?** | yes / no, and the VALUE: what the gate would catch on the current data, and why | "if you see the value then we decide to make it" — a gate that can catch nothing yet is proposed as no |

Rules: the owner's words name the states — never "now" for the current state, which inverts every card for a reader
who uses "Now" for the result (2026-11-09: the first version did exactly that). A gate's value is what it would catch
and WHY; a count that is zero by construction is not a measurement.
Each card shows its ruling status ("Ruled 2026-11-09: …" / "Waiting for your ruling")
and carries the feedback controls; when the owner rules, the card is redrawn with the ruled change, and the ruling goes
verbatim into the rule record beside the sketch. Evidence images are embedded in the file (a repo may ignore *.jpg).
Same medium as screens: one HTML file, every drawing a short list of primitive calls (box, text, line,
callout, ✗, ✓, checkerboard for transparency).

## The UI notation: every part shows the rule it obeys (amended 2026-11-09, [SPIKE])

A grey box says where a part is; it does not say what happens when the window grows, the part is pressed, or the
art repeats — and those are exactly what the owner's gates judge. So every part in a sketch carries marks from one
fixed notation, and every mark names the gate that will check it (owner, 2026-11-09: "extend the skill with all the
features we have for our UI based on the gates we plan to use"). Draw only the marks a part has; a part with none is
fixed-size, fixed-place, one state.

| Mark | Means | Drawn as |
|---|---|---|
| **F** fixed size | drawn at its own size, never scaled (close X, icons, dots, slots — slots do not grow with the window) | badge `F` + size in design px |
| **S** stretch | 9-slice: corners native, edges and centre stretched — only a region with ONE profile along the stretch | badge `S`, double arrow on the axis that grows |
| **T** tile | the region repeats — only when it is ONE colour or one cross-section (no motif) | badge `T`, a short run of repeats |
| **★** opt-in special | a configured exception: a patterned repeat or a stretched detail that is MEANT (named flag) | `★ <flag name>` beside S or T, in the accent |
| **R** relative | position or width follows the parent (flex, a fraction, a fitted grid's column count) | `R` + the rule (`fills`, `cols = width ÷ slot`) and a dashed parent outline |
| **A** absolute | fixed position inside a relative box (slot ring positions) | `A` + the offset |
| **⚓** anchored | placed beside an anchor, clamped to the screen, never over the anchor; hidden until measured | anchor pin + arrow to the popup, the preferred side named |
| **—** aligned | sits on a line (a header's centre on the top border's centre line); may overhang if stated | dashed line + `—` |
| **states** | the derived variants (hover, pressed, disabled, selected, focused, danger) | a strip of small copies, each labelled, the derived ones marked `d` |
| **motion** | an animation (a press: the cap sinks N px and shrinks, the frame stays; a drag ghost; a fill clipped at its fraction) | 3-4 still frames left to right with the time and the travel written under each |

Two rules for the notation: a stretch or tile of DETAIL without ★ is drawn red as a defect, never as the design; and a
mark without a gate is a finding — the gate is missing, name it in the notes. Primitives: `badge(s, x, y, "S")`,
`arrow2(s, …)` (growth), `pin(s, …)` (anchor), `frames(s, [...])` (motion) — added to the worked example's script.

## Feedback on every card (amended 2026-11-09, owner)

A sketch exists to get a decision, and decisions come in batches ("we might have a lot of sketches + answers to go
through"), so every card carries its own answer controls and the answers land in a file the agent reads — never in
chat prose the agent has to parse:

**Start from the template**: `templates/decision-sketch.template.html` — the drawing primitives, a `CARDS` list to fill,
and the FEEDBACK block to keep as it is. Serve the folder with `bin/sketch_answers_server.py --dir <folder>`.

- Each `.card[id]` gets **Yes / No / Change** and a note field (the note is where "more than A/B" goes); a sticky bar
  counts `k of n answered`.
- **Writes** (owner, 2026-11-09): the FIRST change is written to disk at once; later changes are throttled (one write
  per `THROTTLE_MS`, default 1000, the last change always written) and **every write is a complete copy** of all
  current answers, never an increment: `{sketch, rev, answers: {<card id>: {choice, note}}, counts, saved}`, replaced
  atomically on the server. Measured on the template: first write 1 ms after the click; 20 changes in 1 s → 2 more writes.
- **A green ✓ at the right of each note field** appears only when the server has confirmed the write that carried that
  card's latest change; "saving…" while it is in flight, a red "not saved" (and the bar says so) when the server did
  not answer. A reload restores the answers from disk with their ✓.
- Opened from disk (`file://`), the answers stay in the browser and **Download answers** saves the same JSON.
- Test it, then delete your test answers — the file AND the browser's copy — before the owner opens the page; when
  the owner may already be using the page, test in a separate tab or on a copy, never in theirs.

## A third form: the spec page — whose decision each part is, the rule running live, a card per backend arc (amended 2026-11-13, [SPIKE])

For the question "show me how you have specified this, and what the backend needs", asked of a feature that is
investigated and not yet ruled. One page, three parts:

1. **The window, with a tag on every part saying whose decision it is**: *the owner's words* · *my outline, not ruled*
   · *open question* · *not in the product*. A part without a tag is a decision smuggled in. *Self-check:* every box
   carries exactly one tag, and every "owner's words" tag matches a quote you can point at.
2. **Every rule the owner gave runs live, on the product's REAL numbers**, never on round sample numbers. Real
   numbers show the holes sample numbers hide, and the page says each hole in one plain line as the controls reach
   it. *Self-check:* pick the smallest real row and the largest; the verdict line changes between them.
3. **A card per backend arc**: what a user sees when it is done · what exists today · what is missing · what it
   waits for, with a chip (built, partly there, not built). *Self-check:* no card says "exists" without a place in
   the notes behind the page.

Then: the page's words are the product's words (a label is part of the spec); drive the page in a browser through a
local server and read its numbers back before showing it; keep it as a file beside the feature's documents; and when
the owner corrects it, make a second version and keep the first, with his words between them.

## Rubric (self-check before sending)

- R1 every screen serves a named job; every job has a screen.
- R2 every region says what it shows, with real sample content; every control carries a verb.
- R3 exactly one accent, on the primary action only.
- R4 the flow has arrows with actions and a step count; the happy path is first.
- R5 empty, blocked and many states are stated per screen.
- R6 callouts are numbered and listed; corrections continue the numbering.
- R7 the file renders standalone, at phone width without sideways scroll, in light and dark.
- R8 no text overlaps another, runs past its drawing's edge, or spills out of the shape it labels (a badge, a box)
  — checked by a script over every `<text>` (getBBox overlap, inside the viewBox, inside its container); shapes
  around text are sized from the measured text, served over http (a `file://` preview may be a static snapshot with no script).
- R9 (pipeline design cards) every card has Before (the owner's evidence), Now (✗ before / ✓ now, callouts), the Gate
  with today's measured values, and Gate needed? with the value in the owner's terms; the states use the owner's names.
- R10 every part that grows, repeats, moves, anchors or changes state carries its notation mark and the gate's name;
  a stretched or repeated detail without ★ is drawn as a defect.
- R11 a sketch that asks for a decision is built from `templates/decision-sketch.template.html` (the feedback block
  unchanged), has the answers server running when it is handed over, and starts at "0 of n answered"; a ✓ shows only
  after a confirmed write.

## Pitfalls

- **Fidelity creep.** A colour, a font or an icon invites a taste discussion and hides a layout problem.
- **Placeholder content.** Lorem ipsum and "Item 1" give no feel; the sketch must show the real kind of data.
- **Drawing the system instead of the path.** Boxes for modules are architecture; the user never sees them.
- **A mechanism drawn still.** If the question is how something moves or reveals, hand over; a still frame lies.
- **Building because the sketch was close.** The sketch's success is an agreement, not a prototype.
- **Patching in prose.** "Imagine the button on the left" is a correction without a number; redraw it.

## Worked example (the agent-and-skills-manager UI, 2026-11-01)

Jobs: see which skills were visible and which fired (dashboard); understand why one skill keeps failing (skill page);
judge whether a set overlaps or is thin (set page); run the checks and the audit queue (workbench); make a first skill
and see it fire (create). Five screens, one happy path of five steps from a finding on the dashboard to a new skill's
first firing, a beginner path of two. States: no ledger yet; a set over budget; a thin capture session.
Corrections from the owner's walk-through were numbered from
C1. v1 (2026-11-02) applied C1-C4: the owner's three directions (several apps, a foundational set
first, measured numbers only) and one render fix; it added a sixth screen (the set builder) and redrew every number
from the registry and the usage scan rather than from samples, which is what the method's step 2 means by real
sample content: measured content whenever the data exists.

## Related

`sketch-before-you-settle` and `interactive-mechanism-sketch` (mechanisms) · `real-knobs-as-sliders` (tuning) ·
`sketch-to-standalone-tool` (when an agreed sketch should become a kept tool).

