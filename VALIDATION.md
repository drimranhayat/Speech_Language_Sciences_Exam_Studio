# Validation record

Validated on 18 October 2026.

- 938 MCQs and 286 glossary entries; eight lecture counts reconciled.
- 296 easy, 326 moderate and 316 challenging items.
- Exactly four unique options and a valid correct-answer key for every question.
- Unique question IDs and no duplicate question statements within a lecture.
- Default lecture ordering follows increasing editorial difficulty.
- Every reference ID resolves to the supplied reading guide.
- Browser data file exactly matches the JSON data.
- All 24 answer-display permutations preserve the correct canonical option.
- Wrong-answer retry, correction/removal and earlier-error retention passed.
- Import validation, scoring and backup filtering passed.
- DOM-free interface smoke tests passed for overview, study, scoring, unscored reveal, wrong-answer revision, bookmarks, glossary, reading guide, progress and theme saving.
- White labels on all eight solid lecture-tab backgrounds meet WCAG AA normal-text contrast (4.5:1).
- JavaScript syntax checks passed.

These automated checks establish data and interaction properties, not independent expert review of every question. Browser rendering and physical mobile/tablet/desktop testing were not performed in this environment. Responsive CSS includes breakpoints for these screen sizes.

## Essay and visual update

- Eight original lecture essays: 8,219 words total, with 6–8 sections each.
- Essay word counts, lecture mapping, source IDs and JavaScript/JSON parity verified.
- All 286 glossary entries receive a local, topic-selected SVG icon; 20 distinct icon designs are used.
- Essay index, individual lecture route, cross-navigation, text-size changes and read markers passed interaction smoke tests.
- MCQ data, question IDs, answer keys and progress engine remain byte-for-byte unchanged from the earlier ZIP.
- Main navigation uses a visible grid on small screens; lecture cards link separately to essays, glossary and MCQs.
- Day/night styles and responsive reading layouts are included. Visual browser and physical-device testing remain unperformed.

## Paged navigation update — 19 October 2026

- A Show 10 / 20 / 50 / 100 selector controls page size, with 20 as default. The final page contains only remaining items.
- Every question appears exactly once, tested for all four sizes at all set lengths 0–1,200 and across all eight lectures.
- Page-size preference persists, and changing size preserves the active question, saved answers and option order.
- Option clicks immediately reveal and score a single attempt; repeated clicks cannot change it or increment attempts.
- Feedback updates only the attempted card. The next-question action smoothly scrolls/focuses its successor and crosses page boundaries correctly.
- Direct page selection, question-map jumps, deep links, previous-question actions and next-unanswered navigation are included.
- Wrong-answer revision opens blind attempts; later correct answers clear its queue.
- Unscored reveal, bookmarks, essays, glossary, reading settings and original progress backups remain compatible.
- Question and essay data are unchanged. The progress engine adds pagination without changing the answer schema.
- Smooth scrolling respects reduced-motion preferences. Actual browser/device rendering remains untested.
