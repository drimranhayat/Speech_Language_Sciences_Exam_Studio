# Speech & Language Sciences — Exam Studio

A self-contained, GitHub Pages-ready revision website based on the eight supplied lecture handouts, with labelled supplementary concepts.

## Included

- **Eight complete lecture essays**, approximately 900–1,150 words each, with section navigation, reference links and cross-links to every lecture's concepts and MCQs.
- Colourful local SVG icons throughout the glossary and lecture cards; no external icon downloads.
- Adjustable essay text size, reading completion marks, clear content tabs and a mobile navigation grid.

- **938 MCQs** across all eight lectures, with four options and one best answer.
- **286 key concepts** with definitions, examples, distinctions and common misconceptions.
- A gradual lecture sequence: **Easy → Moderate → Challenging**, plus difficulty and topic filters.
- Definition, application, misconception and worked-analysis questions; the same concepts are deliberately revisited from different angles.
- Shuffled answer positions for every attempt, with correct scoring independent of displayed letters.
- Shuffled question sets on request; the ordinary lecture route retains the gradual sequence.
- Clicking an option immediately scores the attempt and opens the correct answer and explanation inline.
- Choose **Show 10 / 20 / 50 / 100 MCQs** per page (default 20). Your choice saves locally and keeps your current question. The final page shows the remaining available questions.
- Smooth next-question navigation, automatic page-boundary transitions, page numbers, direct page selection, question map, jump-to-question and next-unanswered controls.
- Wrong-answer revision, bookmarks, resume, question navigator and search.
- Progress and day/night preferences saved locally; progress export/import for backups and moving devices.
- Distinct lecture colours with tested white-on-colour contrast; responsive CSS for phones, tablets and desktop screens.
- A reading guide and explicit corrections to errors in the original handouts.

## Open locally

Extract the ZIP and open `index.html` in a modern browser. Question data loads from a local JavaScript file; no server, build tools, account or network connection is required for study. External reading links need internet access.

Local-file browser storage behaviour can vary. For regular use, serve the files on GitHub Pages, then study consistently at that same URL. Export a backup before changing devices, browsers or hosting addresses.

## Publish on GitHub Pages

1. Create or open your GitHub repository.
2. Upload **the contents** of this folder so `index.html`, `styles.css`, `app.js`, `engine.js` and `data.js` are at the repository root.
3. In **Settings → Pages**, select **Deploy from a branch**, select your branch, and choose **/(root)**.
4. Save and open the Pages URL when GitHub finishes deployment.

All links and asset paths are relative, so the site also supports GitHub project URLs. `.nojekyll` is included. There are no build dependencies or API keys.

## Study and scoring

Select an option to score the attempt and open the answer and explanation immediately. Further option clicks cannot rescore that attempt. Use **Retry question** for a new attempt with shuffled options. Revealing without selecting is recorded as viewed, not as a correct answer. A later correct attempt removes an item from the wrong-answer queue while preserving its earlier-error flag and attempt count.

The wrong-answer route opens a new unselected attempt. Its question queue stays stable while you work through it; reopen the route to refresh the list. Returning to a previously answered question in a normal lecture restores its selected answer and explanation. Wrong-answer review opens fresh, unselected attempts instead. Explanations stay open until you choose to continue; the site does not skip ahead before you can read them.

Accuracy uses the latest scored answer for each answered question. It is a revision measure, not a proctored assessment. Browser storage is device/browser specific. **Progress → Export progress** downloads a JSON backup. Import replaces the current progress after confirmation.

## Files

- `index.html`, `styles.css`, `app.js`, `engine.js`: interface and study logic.
- `data.js`: browser-ready question bank and glossary.
- `data.json`: the same data in an editable, reusable format.
- `essays.js` and `essays.json`: the eight original lecture essays.
- `visuals.js`: lightweight topic-based SVG illustrations.
- `COVERAGE.md`: lecture map, question counts, difficulty distribution and source scope.
- `tools/`: reproducible Python generation source using the standard library.
- `tests/`: Node.js data, scoring, state and interface smoke checks.

## Validate or regenerate

From this folder:

```bash
node tests/check.js
node tests/interface.js
node --check app.js
node tests/essays.js
node tests/pagination.js
python3 tools/build_essays.py
python3 tools/generate_bank.py
```

Run checks after regenerating. Do not manually edit only one of `data.js` and `data.json`; regenerate both together. Existing question IDs should remain stable to preserve saved progress. If changing an existing question's option meanings or canonical order, also plan a progress migration or increment the storage schema.

## Academic scope

The handouts determine lecture organization, not every clinical topic that might occur in another speech-science course. Supplementary material fills introductory linguistic gaps. Historical frameworks are qualified, and accent-sensitive sound examples identify relevant variation.

Open textbook content and official phonetic references support accessible concept checking. The reading guide also contains verified publisher/university links to specialist books; publisher contents and descriptions are distinguished from access to a full book. Questions and explanations are original revision material, not copied textbook question banks. No invented textbook page numbers or quotations are included.

## Verification

Automated checks cover counts, unique IDs and stems within lectures, answer integrity, gradual difficulty ordering, reference links by ID, all 24 answer-display permutations, wrong-answer correction, import validation, JSON/JavaScript parity and lecture-tab contrast. DOM-free interaction smoke tests cover study, revealing, scoring, revision, bookmarks, glossary, progress and theme persistence.

Responsive CSS is provided, but visual browser/device rendering was not tested in this environment.

Essay reading marks and text-size preferences save separately on this browser. They do not alter MCQ scoring. The question-progress export/import continues to back up answers, viewed questions, bookmarks and the MCQ resume position.

## Paged navigation update

- Default lecture pages show 20 questions. Choose 10, 20, 50 or 100 using **MCQs per page**. For example, 94 questions at 20 per page become pages of 20, 20, 20, 20 and 14.
- Question order still increases in editorial difficulty unless you request shuffling.
- Final pages, wrong-answer queues, bookmarks and narrow filters can have fewer questions than the selected page size. Questions are never duplicated merely to fill a page.
- Instant feedback updates the attempted question rather than rebuilding all question cards, preserving the order of its options and the surrounding page.
- “Next question” scrolls and focuses the next card. From the last card of a page it opens the following page automatically. No timed auto-advance interrupts explanations.
- Page controls are above and below the set; the question map, page selector, question-number jump and next-unanswered button provide direct routes.
- Saved question IDs, answer keys, scoring schema, essays and glossary remain compatible with the previous version. Continue using the same hosting URL/browser to retain local progress.

The selected MCQ page size is a browser-local preference and is separate from the progress export. Changing it preserves existing answers, open explanations, option order and the active question.
