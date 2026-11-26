---
name: interactive-mechanism-sketch
description: >-
  FIRES when a spatial or temporal MECHANISM must be agreed with the user before it is built — how
  something looks, moves, hides, opens, sweeps or transitions (a portal you see and walk through, a
  vision/fog mask, a camera, a door, a spell area, a UI animation, a map seam) — and words, a still image or
  a multiple-choice question are not converging; or when the user asks to "draw", "show" or "visualise"
  such a concept; when the mechanism is who OWNS, decides or talks to whom as something moves (a hand-off
  between servers, a lock, a queue); or when `sketch-before-you-settle` hands one over. The whole process, misunderstood to
  buildable: get the user's NARRATION moment by moment from every side (ask for it if missing); build an
  INTERACTIVE sketch (inline widget) whose every frame is COMPUTED BY ONE RULE from the user's own variables,
  labelled in their step names, with a scrubbable time axis, the abstract view beside what the user really
  sees, and a reveal toggle for what is hidden; read the rule back over every narrated moment as a DESIGN
  REVIEW; state the rule in one sentence, ask "does this match?", build nothing until it does. Exports the
  sketch as a committed page on request; when it becomes a feature, carries the rule, every control and
  every constant over as the feature's pure function and configurator knobs.
  Never an ASCII picture. Not for chart numbers or static layout.
---

# interactive-mechanism-sketch — agree on a mechanism by letting the user drive it

## The claim
A user describing a mechanism holds a model in their head; words make you guess it, a still image freezes
one moment of it, and a multiple-choice question asks them to translate their model into your vocabulary.
A sketch they can DRIVE — their variables on sliders, every frame computed by one rule — lets them check
your model against theirs directly: they drag, they see the frame they expected or they don't. Because the
picture is computed, a match proves the RULE, not one hand-drawn frame. The user's narration is half of it:
told moment by moment from every side, it is both the sketch's spec and a walk-through of their own design.

## The method
Anchors (`M0`…`M7`, `V1`…`V20`) are stable ids: project twins attach their notes to them.

- **M0 · Get the narration.** If the user has not described the mechanism moment by moment, ask for exactly
  that in one message, with an empty grid. The rows are the moments in order, in plain words ("before",
  "right in front", "inside", "after"). The columns are every place the viewer can look and every party that
  sees (ahead, behind, each side; this world, the other world; the viewer, the people at the far end). Ask what
  each cell shows. Offer no options. If they already narrated, use their grid and go to M1. A cell they cannot
  fill is a design question they did not know they had. That is how narrating "from all angles" surfaces
  issues in the design.
- **M1 · Take the spec from the user's own words.** List their steps (numbered as they numbered them), their
  variables (anything that changes the outcome: position, size, depth, time), and the one thing they want to
  SEE. The narration's axes are the sketch's axes. For a mechanism of PARTIES (who owns, who sends, who receives) the
  rows are still the moments, the columns are the parties, and the thing to see is what each party believes at that
  moment (for example: the client, the origin node, the destination node). Use their framing of the decision, not yours, and leave out
  any design term they did not use. **First search the record for an earlier sketch or contract of the same
  mechanism** (an ADR banner, a ratified simulator, a plan's acceptance steps). If one exists, start from it, quote
  it, and say what is new; re-deriving a ratified design costs a day and can contradict it. **Then list the object's
  existing variants** (the shapes, kinds or modes the product already has) and make them a control. A sketch fixed to
  one variant hides whether the rule holds for the rest.
- **M1b · Research a named reference.** When the user points at outside material (a film's effect, a game, a style),
  research it before sketching. Say what the sources establish and what they do not, and cite them. In the sketch,
  mark which parts come from the reference and which are the user's own change.
- **M2 · Find the one rule.** Write the mechanism as a single function from (controls, cell or point) → what is
  drawn there. If you cannot, you do not understand it yet: ask before drawing. (Portal example: "a ray from the
  character's eye through the opening sees the other world; beside the portal it sees this world; into a pillar,
  a wall or past sight range it sees black; the world you are in flips at the line".) Write its constants as
  named values; M7 needs them. If the rule has MEMORY (a margin that must be passed before a flip, a latch, a
  hand-off that waits), say so: the sketch then computes the whole timeline from the start at every control change
  and the scrub reads from it, because a function of the current frame alone cannot show hysteresis.
  Two things that move together are driven by ONE progress
  variable, never sequenced: a twist that "happened at the end, then got undone" read as silly; a twist undone BY the growth reads as the gate
  being built and landing. And every clock in the rule has a speed and an end the user can set: a
  clock that only runs (aging, fading, spinning) hides the question of when it stops, which the user asks at once.
- **M3 · Build the widget** (inline with `show_widget`; load its design guide first). It needs:
  - a grid or canvas the rule paints cell by cell;
  - a slider or toggle for every variable from M1;
  - the time or progress axis as a **scrub slider** with steps fine enough that the critical instant (a line
    crossed, a door half open) can be stepped through frame by frame, plus a play button (playback alone passes
    that instant in one frame);
  - a live state label in the user's step names ("1 · approaching" … "4 · through");
  - BOTH the abstract view and the user's real view (top-down plus the game camera, side plus front, …);
  - for a mechanism of parties the real view is the WIRE: the parties as boxes, live, silent and wrong messages drawn
    between them, and a table of what each party believes at this frame (for example: two nodes, the client, a red
    arrow for a message sent to a node that stopped simulating);
  - when the narration holds several SITUATIONS (a straight crossing, a dance on the line, a meeting of three, a thrown
    object), each is a SCENE button with its own path and the rule stays one; never bake them into one picture;
  - a "show what is hidden" toggle when the mechanism hides something;
  - when the question is a CHOICE between designs, the choice itself as a control: one toggle, the same rule computing
    every option, and a live verdict line in plain words with a number ("Nothing of the world shows · 0 tiles"); a
    term the user does not know is a choice in disguise: its readings become the positions of one control, so the user
    sees the difference instead of reading a paragraph;
  - the verdict also counts over the WHOLE scene (flips, late messages, frames with two owners or none), beside the live
    frame, so the design review has numbers;
  - a legend of at most 4 plain entries, light and dark themes, and a screen-reader summary;
  - for a LOOK the user will configure: a colour control for every visible part, and for every sub-part that could
    differ (a stem and its spikes, a bead and its centre); and any motion the user named (a trail, a spray) drawn,
    with its own control. Adding them later costs a round trip.
  - the controls grouped the way the user described them (tabs, pages, a shared section): the grouping is part of
    the design under review, and a sketch that regroups them hides a disagreement.
  - when the user points at an existing effect to build from,
    read that effect's parameter NAMES and give the sketch's knobs the same names, so the carry-over
    (M7) maps one to one and the user recognises them.

  - `[SPIKE]` a **rule-check file beside the sketch** when the sketch will become a design reference: the page's
    own script run in node against a stub DOM (no browser), one row per sentence of the user's narration,
    plus two or three planted mistakes
    that must turn rows red. Expose the rule on one global for it (`window.__sk = {lines, foe, v}`). The sketch
    then has a test the carried-over code (M7) can be held to, and a corrected rule (M8) shows as changed rows.
  - `[SPIKE]` when the engine has no depth buffer and the mechanism passes behind AND in front of a body: draw
    the sketch in the engine's own order (the far part, the body, the near part), cutting the shape where it
    changes side. The sketch then proves the METHOD the engine will use, not only the picture, and "show what is
    hidden" draws the far part dashed over the body.
  - `[SPIKE]` for a look with knobs: ONE table drives the sliders, the picture and a **"send these settings"
    button** (`sendPrompt` with the values as JSON), so the user's tuning comes back as numbers
    (`real-knobs-as-sliders` owns the scales). `sendPrompt` exists only in the chat host: in a plain browser the
    button copies the changed knobs and shows them in a box, for the user to paste. Pause on Space and a Reset belong on any sketch whose feature will
    have them.

  Start from `template.widget.html` (the portal walk-through) and replace the rule and the controls.
- **M4 · Read the rule back as a design review.** Run the rule over every cell of the narration grid, and over any
  older narration on record (a plan's acceptance steps, an earlier ruling's scenario): find it, quote it. Each cell
  where the rule's output differs from the narration, or where the narration has no answer, is a finding. List
  the findings as "what this changes in the design", meaning consequences for the design and the systems around
  it. Add at most ONE question, worded by what the user would see. Never resolve a finding silently in the sketch.
  `[SPIKE]` **An approved look is not an approved rule.** A rule that plays out over many seconds, or that turns
  on chance, is not seen in a first look: state each such rule as one sentence and ask about it even when the
  sketch is approved.
- **M5 · Reply in three parts only:** the rule in one or two plain sentences, M4's findings, and "does this
  match what you have in mind?". That is the reply that carries a sketch. For a choice only the user can make by
  looking, say what each option SHOWS and ask. Any recommendation of yours comes last, labelled as yours, with its
  reason in terms of what the user would see, never as the frame of the question.
  Before sending, DRIVE the sketch to every state a sentence of the reply claims and read its verdict
  line: a claim the controls cannot reach is a defect of the sketch, cheapest found by you.
  `[SPIKE]` A reply that only asks for the narration
  (M0) is its own short message: the freeze line, the grid, and a plain answer to anything else the user asked. No design changes, no plan and no code until it does. If they correct it,
  change the rule and redraw: the sketch is the conversation.
- **M6 · Export when asked** (or when the sketch becomes a design reference):
  1. Save the widget code byte for byte.
  2. Wrap it: `widget_to_standalone.py <widget.html> <out.html> "<Title>"`.
  3. Open it through a local static server. A `file://` preview is a static snapshot whose script never runs,
     so it proves nothing.
  4. Check that the console is clean.
  5. Commit by pathspec where the feature's docs live, with a README line saying what it shows and whether it is
     the agreed design or a superseded one.
  6. When a sketch went through reviews, the extract keeps the FIRST and the LAST iteration side by side, with the
     user's words between and the lesson of each changed slider or view in general form:
     the distance between them is what a replay is scored on,
     and it teaches more than the last sketch alone.
- **M7 · When the mechanism becomes a feature, carry the sketch over; do not re-derive it.**
  - The rule becomes ONE pure, testable function with the sketch's inputs.
  - Every control AND every constant OF THE RULE becomes a configurator knob, with the sketch's name, range and
    step, unless an invariant fixes it (an anti-cheat or authority rule): that one stays a constant, with the reason
    written beside it. The sketch's scene (the walls, the test layout) is not a knob: it is the fixture the golden
    frames use.
  - The step labels become the configurator's phase or scrub names.
  - Frames of the agreed sketch become golden test cases: control values → the expected output per cell, generated
    by running the sketch's OWN code, not by retyping its rule. The sketch is the spec, not an infallible oracle.
    Where its frames contradict its stated rule, follow the rule, keep the
    sketch page as the record, and pin the exact shape of the difference in the golden test. `[SPIKE]`
  - The sketch's PHYSICAL constants (gravity, tick rate, units, drag model) are its own unless they were read from
    the engine. Before carrying a number over, read the engine's constant and re-derive the defaults at it: the
    sketch is the oracle for the SHAPE of the motion, not for constants it invented. Golden frames compare shape
    (lands on its point, falls steeply) rather than raw positions when the constants differ.
  - First inventory what the product does at that moment today and which tuning tools it already has. Copy the
    existing tool's idiom rather than inventing a new one.

  The sketch's code is thrown away; its rule, names, ranges and frames are kept (`go-fast-where-being-wrong-is-cheap`).
  Build the knobs themselves (ranges, scales, the Model/ViewModel split, the numbers saved for the agent) by
  `real-knobs-as-sliders`.

- **M8 · Revise from the user's marked-up screenshot of your sketch.** When the user answers a sketch by drawing on a
  screenshot of it (boxes, arrows, labels), that drawing IS the new narration:
  1. Number every mark as one instruction, in the user's words, and add the instructions the message gives in prose.
  2. Make one sketch per instruction, carrying everything the user did not mark forward unchanged from the last
     sketch. Do not redesign the parts they accepted.
  3. Before drawing a control whose meaning depends on the assets ("flip it if it has a flipped version", "every
     graphic for that type"), read the real asset list: which variants exist, which have the second facing, how many
     per type. Show the control only where it applies, and say which variants lack it.
  4. Read back where an instruction collides with a recorded ruling, or changes what the authority decides (a
     resize changes a footprint), as a design-review finding (M4). Never silently pick one side.
  5. Real art cannot load inside a widget (the sandbox blocks local files), and hundreds of kilobytes of base64 cannot
     be retyped safely. Inline sketches use stand-ins. A served page that a script builds from the asset files
     carries the real art (M6).

## Rubric (self-check before sending; the replay gate scores against it)
- **V1** the user's steps in the user's words
- **V2** every variable is a control
- **V3** one rule computes every frame
- **V4** the abstract view and the user's real view
- **V5** what is hidden can be revealed
- **V6** time is scrubbable (finely at the critical instant) and playable
- **V7** a legend of at most 4 plain entries, no jargon
- **V8** the rule in one or two plain sentences plus "does this match"; nothing built
- **V9** light and dark themes, accessible
- **V10** exportable, verified rendered, committed
- **V11** every narrated moment × view is answered by the sketch or listed as an open question
- **V12** the design review is read back: findings plus at most one question, worded by what the user would see
- **V13** for a feature: the rule as one function, every control and constant as a same-named knob, golden frames,
  and the inventory done first
- **V14** the object's existing variants (shapes, kinds, modes) are a control, and the rule holds for each
- **V15** for a look: every visible part and differing sub-part has its own colour control, and named motion is drawn
- **V16** a named outside reference was researched: sources cited, what they do not establish said, reference and
  user's change told apart
- **V17** a marked-up screenshot: every mark numbered as an instruction, one sketch each, the rest carried forward;
  asset-dependent controls checked against the real asset list; collisions with rulings read back
- **V18** several situations are separate scenes under one rule, never one baked picture
- **V19** the verdict counts over the whole scene, not only the current frame
- **V20** a rule with memory is computed as a timeline from the start, and the scrub reads it

## Pitfalls
- **Sketching your question instead of theirs.** A sketch can have the right
  medium and still model the agent's own question, not the user's. M1
  guards against this.
- **Keyframes.** Hand-drawn states agree with any rule; only a computed picture tests one.
- **Jargon in labels.** A label the user cannot picture ("parallax cone") brings the confusion back.
- **Asking for the narration with options.** Offering choices brings your vocabulary back. Give an empty grid
  (M0).
- **Playback only.** A played animation crosses the critical instant in one frame, so give a scrub (M3).
- **Building the design in the same turn.** The sketch exists to be corrected cheaply; code is expensive.
- **Only the abstract view.** The user judges by what they will actually see (the game camera).
- **One variant.** A sketch of the default shape only. It says nothing about the variants the product already
  ships, and the user is left asking whether they still work (M1, V14).
- **Re-deriving the feature from prose.** The agreed sketch IS the spec; rebuilding it from the conversation
  drifts. A hidden constant becomes a hard-coded number nobody can tune (M7).
- **ASCII first.** Restating the mechanism as an ASCII picture or a table of moments, even when a prompt asked for
  one: it cannot be driven and bakes every moment into one frame (`sketch-before-you-settle` T8).
- **One baked picture.** Several situations in one frame. Make them scenes (M3, V18).
- **Two views, two handednesses.** A "from behind" drawn from the front puts the left wing on the other side from the
  top view; the user reads it as the views disagreeing with the slider. One object, one
  handedness, and each view's label says which side is which. And a slider that shapes a target pose opens ON that
  pose; opened on the start pose it changes nothing visible.
- **A claim the controls cannot reach.** The reply says "set X and you will see Y", and no position of X shows Y. The
  console is clean, the page renders, and the sketch still lies. Drive it to each claimed state first (M5).
- **Answering a "do we need X?" with an opinion.** When X is a part of the model (a bone, a seam, a channel), measure
  the thing first, then make X a toggle: off = as it is, on = with X, and let the verdict line show the difference.
- **A motion verb built as a timeline.** "Jump", "fall", "bounce", "settle" sketched as rise / hold / fall in
  seconds reads as mechanical. Build it as physics from the first version: a throw
  under gravity with knobs for gravity, how early it leaves, how much later the followers leave, and the bounce.
- **A sketch that knows more than the screen.** A reaction drawn from where a hidden caster stands, or from where a
  caught ball touched, is a picture the game cannot draw when the server withholds those facts. Use only what the
  player's screen is told, and say so in the reply.
- **A mode as a 0/1 slider.** The user cannot find it ("how do i change to the wave mode?"). A mode is a select at
  the top, named by its choices.
- **A top-level name that the browser owns.** The sketch's script runs in the page's global scope, where `top`,
  `name`, `status`, `length`, `parent`, `self`, `open`, `close`, `stop`, `print` and `event` are already `window`
  properties: `function top()` throws "Identifier 'top' has already been declared" before the first frame, and the
  chat host shows blank canvases without saying so. Read the served page's console before any pixel check (V10) and
  name helpers after what they draw (`topView`).

**Tools:** `extract_widgets.py` pulls a session's widgets out of its transcript byte-for-byte; `widget_to_standalone.py`
wraps one into a page.

Sibling: `sketch-before-you-settle` (WHEN to sketch and what to gather).
Related: `image-annotation-clarify` (a still, annotated image for static
geometry), `sketch-to-standalone-tool` (building an HTML tool you keep).

