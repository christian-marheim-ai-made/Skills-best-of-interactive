---
name: sketch-before-you-settle
description: >-
  FIRES the moment a conversation about a spatial or temporal mechanism (what is seen, hidden, moved,
  opened, swept, transitioned) shows any of these signs: the user answers a choice with a question or asks
  you to "draw"/"show" a concept; the user says they do not understand a term the design or you introduced
  ("I barely know the word X"); the user gives a multi-step description of an effect or says it is hard to
  describe; a windowed check, screenshot or playtest contradicts the plan; you are about to offer the user a
  choice named by a technical term; the user has just said a design is wrong and you are about to build
  its opposite; or you are about to type an ASCII picture or a table of moments yourself. Then STOP building and planning: gather the user's own steps, variables and words as the spec,
  trace any confusing term to the ruling or doc it entered by and flag it, and hand the spec to
  `interactive-mechanism-sketch` — a computed, slider-driven picture, animated where that helps, never ASCII,
  that the user checks in one turn — before any plan, code or further question. Choices you still have to offer name what the user would SEE. Silent for
  non-spatial asks and single-number tuning.
---

# sketch-before-you-settle — when a mechanism is not converging, sketch it before you build it

## Why
Mechanisms fail between heads, not in code: each party holds a picture and the words between them name
different pictures. The cost compounds — a plan, commits, tests and a re-implementation can all be built on
one misread word. The signs are recognisable early; each one is the cheapest moment to sketch.

## The triggers (stop and sketch on any)
- **T1 a visual counter-question** — the user answers your choice with a question, or asks you to draw/show it.
  This includes a request that rides inside an answer, such as a choice's free-text field used for a new
  instruction ("research the reference and make a sketch"). That is the instruction to follow, not an answer to the
  choice.
- **T2 term confusion** — "I don't understand X", "I barely know the word X", or the user REJECTS a term ("X makes no
  sense here"), about a term YOU or a doc introduced.
- **T3 a described effect** — a numbered or multi-step description of how something should look or move, or
  "this is hard to describe", before you plan it — or the user ANNOUNCES one ("one more important feature … I need
  your entire focus"): freeze work on that mechanism at the announcement, not when the description lands. Then ask
  for the narration (`interactive-mechanism-sketch` M0) and sketch only when it arrives; a sketch drawn before it
  models your answer, not theirs.
- **T4 evidence against the plan** — a screenshot, windowed check or playtest that does not look like the
  design promised.
- **T5 a jargon choice** — you are about to offer options named by a term ("parallax", "window semantics"), or a
  choice between SPATIAL designs in prose (a BLOCKER, a plan question, options named by their mechanism). Rename
  them by what the user would SEE, and sketch them before sending.
- **T6 a correction** — "X is wrong": that says what is wrong, not what is right. Sketch the candidate and ask
  what effect they want BEFORE building the opposite.
- **T8 your own ASCII** — you are about to type an ASCII picture or a table of moments to restate a mechanism, even
  when a prompt asked for "one ASCII diagram". Text cannot be driven and bakes every moment into one frame. Look for
  the sketch skills in the library first (`interactive-mechanism-sketch`, this skill,
  `real-knobs-as-sliders`; they may not be installed live), load them, then sketch.
- **T7 silence** — none of the above, or a non-spatial / single-number question: do not fire.

## The move
Anchors (`T1`…`T8`, `S1`…`S5`) are stable ids: project twins attach their notes to them.

- **S1 · Freeze the build.** No new plan, commit or design rule on the mechanism until the sketch is agreed. Work
   already in flight stays uncommitted if it rests on the doubted model; say so in one line.
- **S2 · Gather the spec from the user's words** — their steps as they numbered them, every variable that changes
   the outcome, what they want to see; quote them. No narration yet? Ask for one, moment by moment from every
   side (`interactive-mechanism-sketch` M0). Add the domain facts the sketch must respect (the camera
   model, the objects' shapes, existing systems such as fog of war).
- **S3 · Audit inherited terms.** For a term the user does not know or rejects (T2, T6), find where it entered (ADR, plan, ruling, an
   earlier annotation) — `grep` the docs — quote it, and flag it in the reply: a ratified word is not a shared
   model, and the user's original intent may be recorded beside it.
- **S4 · Hand off** to `interactive-mechanism-sketch` with the spec: a drawn, driven picture (scrub, sliders, play
   where motion matters), never ASCII; `real-knobs-as-sliders` for the knobs. Its reply is the rule in one sentence + "does
   this match?". A term from T2 becomes a control in the sketch whose positions are its readings, and the reply
   explains it in plain words with one household example (for example: hysteresis as a thermostat; the toggle
   "exactly at the line" / "only after a margin", whose counts the user watches change).
- **S5 · After agreement**, record the rule in the plan in the user's words (and supersede the inherited term's
   ruling with a dated banner if it misled), then resume.

## Pitfalls
- **Explaining harder.** More paragraphs about the term the user does not know.
- **Overcorrecting.** Building the opposite rule end to end the moment the first is called wrong.
- **Asking in your vocabulary.** A multiple choice between abstractions returns a counter-question.
- **Trusting a ratified word.** It may label the user's idea and carry a different one.
- **Explaining in ASCII.** A text picture of the mechanism bakes every moment into one frame nobody can read, and the
  skills that would have sketched it may sit uninstalled in the library (T8).

Sibling: `interactive-mechanism-sketch` (the producer).
