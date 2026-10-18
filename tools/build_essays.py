"""Original lecture essays for the eight supplied handouts. Standard library only."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
essays=[]
def add(lecture,title,subtitle,body):
 sections=[]
 for piece in body.strip().split('## ')[1:]:
  heading,content=piece.split('\n',1)
  sections.append({'id':f'section-{len(sections)+1}','heading':heading.strip(),'paragraphs':[p.strip().replace('\n',' ') for p in content.strip().split('\n\n') if p.strip()]})
 words=sum(len(p.split()) for s in sections for p in s['paragraphs'])
 essays.append({'lecture':lecture,'title':title,'subtitle':subtitle,'sections':sections,'wordCount':words,'readingMinutes':max(1,round(words/180)), 'sourceIds':{1:['anderson','yule'],2:['anderson','radford','yule'],3:['anderson','ipa','phonetics'],4:['anderson','lieber','huddleston'],5:['anderson','radford','huddleston'],6:['anderson','huddleston','radford'],7:['anderson','essentials2','saeed'],8:['essentials2','levinson','saeed']}[lecture]})
add(1,'Language: its nature, properties and functions','How language combines a structured system with human communication.', '''
## What language is
Language is a conventional system through which people express meanings, interact and organize experience. It is more than a collection of words because its elements participate in patterned relations. A speaker who knows English recognizes that The child has arrived follows a familiar structure, whereas an arbitrary rearrangement may not. Linguistic knowledge therefore includes sounds or signs, word formation, sentence organization and meaning. Communication is the broader category: a traffic light can communicate information, but it does not possess the full grammatical organization of a natural human language.

The historical definitions in the handout emphasize different aspects of this system. Sapir foregrounds the symbolic communication of ideas, emotions and desires, describing it as human and non-instinctive. Bloch and Trager emphasize arbitrary vocal symbols and social cooperation. Hall presents language as an institution for communication and interaction through established symbols. Chomsky offers a formal characterization in terms of sentences constructed from a finite inventory. These are paraphrases of the handout, not fresh quotations from the original publications. Their different emphases should be compared rather than combined into one unqualified definition.

## Symbols, convention and linguistic organization
A linguistic sign associates a form with a meaning. The English word tree is a sign; it is not the physical tree outside a window. Arbitrariness means that the association generally depends on convention rather than necessary resemblance. English dog and Urdu kutta refer to the same kind of animal using different forms. Arbitrariness does not make communication random: community conventions constrain how a form is interpreted. Iconicity is a partial counterpoint, where form resembles an aspect of meaning, as in sound imitation. Iconic patterns can still be conventional and differ across languages.

Language is a system of interacting systems. Sound patterns constrain permissible sequences, morphology organizes word formation, and syntax relates words in phrases and clauses. Meaning emerges through these structures and their use in context. Discreteness concerns distinguishable linguistic units or categories. Duality of patterning instead concerns two levels: individually meaningless elements combine into meaningful units, which enter larger combinations. The sounds of cat do not each mean an animal; their organized combination constitutes a meaningful form. Discreteness and duality are related, but they are not interchangeable labels.

## Creativity, displacement and transmission
Productivity is the capacity to create and understand new messages from familiar resources. A listener can interpret a previously unheard sentence about a robot playing cricket on Mars. This does not require memorizing every possible sentence. In a formal characterization, a finite inventory can support an unbounded set of expressions while every individual expression remains finite. Productivity is constrained creativity, since novel combinations still depend on a language's patterns.

Displacement permits reference beyond the immediate situation. People discuss yesterday, plan next year and imagine fictional worlds. Cultural transmission concerns acquiring a particular language through experience with its users. A child's ancestry does not deliver a ready-made vocabulary; interaction and exposure shape the language or languages acquired. Interchangeability means participants can alternate between producing and receiving messages. Reflexivity is the capacity to discuss language using language itself. These properties are useful analytical distinctions, although individual features should not automatically be treated as completely absent from every nonhuman communication system.

## Language modality, speech and writing
The claim that language is necessarily vocal requires correction. Spoken language uses a vocal-auditory modality, while natural signed languages principally use a visual-gestural modality. Signed languages have conventional forms, productive word formation and grammatical structure. They are not merely pantomime, and different signing communities do not all share one universal sign language. The existence of signed languages shows why speech and language must be distinguished.

Writing uses visible conventional symbols to represent aspects of language. It is historically later than speech, and many communities have full languages without established writing systems. Learning to read and write is therefore not the same process as initially acquiring a language. Speech, signing and writing may interact, but no community needs a printed grammar book before its linguistic system can be systematic.

## The functions language serves
Language functions describe communicative purposes rather than mutually exclusive sentence categories. The informative function predominates when someone reports that the library closes at five. The interpersonal function concerns relationships and attitudes, as when a student chooses Professor as a respectful address. A performative use carries out an act under appropriate conditions: an authorized chairperson can declare a meeting open. The formula alone is insufficient when authority and circumstances are missing.

Emotive language expresses feelings, as in a spontaneous expression of surprise. Phatic communion maintains social contact through greetings and similar exchanges, even when little new factual information is conveyed. Recreational use involves pleasure in rhyme, jokes or verbal play. The metalingual function appears when language explains its own expressions, as in What does morpheme mean? A poem can be both emotive and recreational, while an informative statement can also express a relationship. Identifying the dominant function requires attention to context.

## Knowledge, use and scientific inquiry
Competence, in the theoretical distinction introduced in the course, concerns underlying linguistic knowledge. Performance is actual use under conditions involving memory, attention and social circumstances. A tired speaker's slip does not automatically establish a new grammatical rule. A descriptive orientation investigates the patterns speakers use, including those of nonstandard varieties, without confusing social prestige with structural superiority.

Linguistics studies these matters through evidence and explicit analysis. Its questions concern not only correct-looking sentences but how linguistic systems are structured, acquired and used. Understanding this first lecture requires connecting its definitions, design features, modalities and functions: language is a structured symbolic resource, while communication explains what people accomplish with it.
''')
add(2,'The branches of linguistics and how they connect','A coherent map of language structure, processing, society and practical applications.', '''
## Why linguistics has several branches
Linguistics investigates language from complementary perspectives. A spoken sentence is simultaneously a physical signal, a sequence of linguistic units, a meaningful structure and an action within a social situation. No single branch explains all these aspects. The division into branches helps formulate precise questions, but actual research often crosses boundaries. A study of language learning, for example, may require evidence about sound contrasts, mental processing and educational context.

The handout distinguishes microlinguistics from macrolinguistics. Microlinguistics is a broad teaching label for internal structural investigation, commonly including phonetics, phonology, morphology, syntax and semantics. Pragmatics is sometimes placed alongside these core branches and sometimes treated as part of wider language use. Macrolinguistics relates language to social, psychological, cultural, computational and practical domains. These boundaries are organizational conventions, not fixed divisions followed identically by all textbooks.

## The structural branches
Phonetics examines the physical production, transmission and perception of speech sounds. Articulatory work investigates vocal organs and gestures, acoustic work measures signals, and auditory work concerns hearing and perception. Phonology asks how a particular linguistic system organizes sounds into contrasts and patterns. Measuring the duration of a consonant is a phonetic task; asking whether a contrast distinguishes words is a phonological task. Both perspectives may contribute to one study.

Morphology investigates the structure of words and relations among their forms. Unhelpful can be analyzed into un-, help and -ful. Syntax investigates how words and phrases combine into clauses and sentences. The difference between Sara greeted Ali and Ali greeted Sara depends on grammatical relations, not merely the inventory of words. Semantics studies conventional linguistic meaning and relations such as synonymy and entailment. Pragmatics investigates interpretation in context, including how Can you open the window? can function as a request rather than an examination of physical ability.

Lexicology studies vocabulary and the organization of lexical items, including their relationships. Lexicography concerns dictionary theory and compilation. A lexicologist might investigate a semantic field, while a lexicographer decides how senses and examples should be represented in an entry. The distinction is between the study of lexical organization and the work of designing dictionary descriptions; modern dictionaries often draw on corpus research.

## Language in social and cultural life
Sociolinguistics examines relationships between language and social life. It investigates variation, language attitudes, multilingual choices and the meanings attached to ways of speaking. Dialectology traditionally emphasizes geographical patterns of dialect variation. A dialect can differ in vocabulary and grammar as well as pronunciation, whereas accent principally concerns pronunciation. These distinctions prevent a regional accent from being mistaken for an absence of grammar.

Register concerns variation associated with a situation, activity or purpose. The same person can write an academic paragraph and then send an informal family message. Language planning involves deliberate intervention in language status, use or resources, such as developing educational terminology or deciding institutional language policies. Anthropological linguistics and linguistic anthropology investigate language within culture and social practice, including kinship, ritual and identity. Their emphases overlap, although institutional traditions differ.

Discourse analysis examines connected language in texts and interaction. It considers how utterances relate across turns, how references remain interpretable and how larger stretches form meaningful units. Stylistics studies linguistic choices and their effects. Literary stylistics applies such analysis to literature, using evidence from sound, vocabulary, grammar and discourse. A claim that repeated short clauses create urgency should be supported by the actual pattern and its role in the text.

## Language in the mind and brain
Psycholinguistics investigates acquisition, comprehension and production as mental processes. It asks how people recognize words, plan utterances and process sentences under memory limitations. Its scope therefore extends beyond childhood acquisition and language disorders. Neurolinguistics examines the neural mechanisms supporting language, using evidence such as lesion patterns and brain measurements. Language functions depend on interacting networks, so a simple one-region-one-ability formula is inadequate.

Cognitive linguistics is a family of approaches linking language to general cognition, conceptualization and experience. An analysis of TIME IS MONEY explores how one domain structures another. It should not be used merely as a synonym for every experiment involving the mind. Second-language acquisition studies the development of additional languages, including the influence of experience, existing knowledge and learning conditions. Its findings may inform teaching, but studying learning and designing instruction remain distinguishable activities.

## Comparison, history and evidence
Historical linguistics investigates change and relationships through time. Systematic correspondences across related languages support reconstruction more strongly than isolated similarities. Linguistic typology compares structural properties across languages, such as dominant word order. Two unrelated languages can share SOV order without sharing a recent ancestor. Structural grouping and genetic classification answer different questions.

Corpus linguistics uses organized collections of authentic language data to investigate patterns. It involves design, sampling, annotation and interpretation, rather than collection alone. A small corpus's failure to contain a construction does not establish that the construction is impossible. Corpus evidence is especially valuable when its composition matches the question being asked.

## Applications and collaboration
Applied linguistics addresses real-world language problems in areas such as teaching, assessment, translation and policy. Computational linguistics models and processes natural language, including parsing, speech recognition and translation. Programming is a means of investigating or processing human language, not the exclusive object of the field. Forensic linguistics studies language in legal and investigative settings, including interviews, documents and authorship evidence. Its conclusions must acknowledge limitations, particularly with short samples.

The central skill developed by this lecture is identifying the question before naming the field. A project can be computational in method, phonological in its linguistic focus and applied in its purpose. The branches form a network of perspectives that together explain how language works and why it matters.
''')
add(3,'Speech sounds: production, signals and linguistic contrasts','From articulation and acoustic evidence to phonemes, syllables and connected speech.', '''
## Three perspectives on speech
Phonetics studies speech as a physical and perceptual phenomenon. Articulatory phonetics asks how the vocal apparatus produces sounds, acoustic phonetics examines the resulting signal, and auditory phonetics investigates hearing and speech perception. These perspectives connect production to transmission and reception. A researcher might observe the lips during a consonant, measure the recording and ask listeners to identify it. The observations address related aspects of the same event without being interchangeable.

Ordinary English speech primarily uses pulmonic egressive airflow: the lungs supply air moving outward. The larynx regulates phonation, while the tongue, lips and other articulators shape the vocal tract. Voicing involves vocal-fold vibration. The usual contrast between [s] and [z] is therefore a voicing contrast within the same broad place and manner. Voicing does not simply mean loudness, and a voiceless sound can be loud.

## Place of articulation
Place identifies where the relevant constriction is formed. Bilabial sounds involve both lips, as in [p], [b] and [m]. Labiodental [f] and [v] involve the lower lip and upper teeth. Dental or interdental descriptions apply to English [θ] and [ð]. Alveolar sounds such as [t], [d], [n], [s] and [z] involve the ridge behind the upper teeth. English [l] is also commonly classified as alveolar, though its precise articulation varies.

Postalveolar sounds, including a common realization of [ʃ], are articulated behind the alveolar ridge. Palatal [j] involves the hard-palate region, whereas velar [k], [ɡ] and [ŋ] involve the tongue dorsum and soft palate. The glottal stop [ʔ] is produced by closure at the vocal folds. Broad labels differ in some introductory descriptions, so a more precise IPA classification may distinguish categories that an older account groups together.

## Manner of articulation
Manner describes how airflow is obstructed or channelled. An oral stop involves complete closure, followed by release or a transition to another gesture. A fricative creates turbulence through a narrow constriction. An affricate combines a stop closure with a closely coordinated fricative release, as in [tʃ]. A nasal consonant has an open nasal passage, normally through a lowered velum, while an oral closure directs airflow through the nose. Thus [m] and [p] share a bilabial place but differ in manner.

Approximants involve constrictions without the turbulent airflow characteristic of ordinary fricatives. English [j] and [w] are familiar examples. A lateral approximant such as [l] permits airflow around the side or sides of the tongue. A complete consonant description commonly states voicing, place and manner: [m] is a voiced bilabial nasal, and [k] is a voiceless velar stop. Each label supplies a different part of the description.

## Vowels, diphthongs and syllables
Vowels are commonly described through height, backness and rounding. Height concerns the tongue body's relative high or low position; backness concerns its front-central-back dimension. Lip rounding is a separate property. [i] is a high front unrounded vowel and [u] a high back rounded vowel in the standard IPA reference description. Languages also have front rounded vowels, so rounding cannot simply be equated with backness.

A diphthong changes quality within one syllable. Many English pronunciations of my contain [aɪ], but accents differ in their vowel inventories and realizations. Schwa, [ə], is a mid central vowel commonly found in unstressed English syllables, such as the first syllable of about in many varieties. It is not universally restricted to unstressed positions across all languages. A syllable is often analyzed into onset, nucleus and coda: a simple analysis of cat assigns /k/, /æ/ and /t/ to these positions. Some syllables lack an onset or coda, and some languages permit consonants as nuclei.

## Acoustic measures and displays
A waveform displays signal amplitude over time. Duration is a time interval, measured in seconds or milliseconds; fundamental frequency is a repetition rate, measured in hertz. In voiced speech, fundamental frequency is closely related to vocal-fold vibration and perceived pitch. Amplitude and intensity concern physical magnitude and energy, while loudness is perceptual. These dimensions can interact, but they should not be collapsed into one property.

A conventional spectrogram displays time horizontally and frequency vertically, with shading representing energy in particular time-frequency regions. Formants are resonant frequency regions shaped by the vocal tract. F1 and F2 provide useful evidence about vowel quality. They differ from fundamental frequency: resonances of the tract are not identical to the rate at which the sound source repeats. Spectrogram settings affect the appearance of energy, so darkness alone should not be treated as a universal category label.

## Phones, phonemes and allophones
A phone is a physical speech sound considered phonetically. A phoneme is a contrastive category within a particular linguistic system. English sip and zip form a minimal pair because replacing their initial sound changes meaning while the remaining segments match. This supports a contrast between /s/ and /z/. It does not establish that every measurable difference between two speech tokens represents a phonemic difference.

Allophones are realizations of one phoneme. In a common English pattern, /p/ is aspirated in a stressed syllable-initial position, as in pin, but not ordinarily after /s/ in spin. Aspiration is marked [ʰ]. Complementary distribution means two realizations occur in mutually exclusive environments; phonetic similarity and other evidence help determine whether they are allophones. A distinction that is allophonic in one language can be phonemic in another.

Broad transcription emphasizes contrastive categories, while narrow transcription records more phonetic detail. Slashes conventionally mark phonemic representations and brackets phonetic representations. The transcription [spɪn] contains four segments. Sound counts and spelling counts must remain separate, because English letters do not map perfectly onto individual sounds.

## Connected speech and larger patterns
Stress is relative syllabic prominence, supported by patterns of duration, pitch and intensity. Intonation concerns pitch contours across phrases or utterances. Not every question has a rising contour; interpretation depends on construction, variety and context. Assimilation occurs when a sound becomes more similar to a nearby sound, as when a nasal becomes bilabial before a bilabial consonant in suitable connected speech.

Phonotactics describes permissible sound sequences and syllable patterns. English permits some initial clusters and excludes others that may be ordinary in another language. The distinction between phonetics and phonology is therefore essential: phonetics describes physical realizations, while phonology investigates the contrasts and patterns of a linguistic system. Together they explain speech more fully than either spelling or impressionistic listening alone.
''')
add(4,'Morphology and the organization of grammatical units','How words are built, how forms alternate, and how words enter phrases and clauses.', '''
## The grammatical scale and the morpheme
Grammar organizes units at several scales. A common introductory rank scale proceeds through sentence, clause, phrase, word and morpheme. The scale is a model of structural units; syntax names an area of analysis and should not replace sentence as if it were another unit. Not every framework defines each rank identically, but the distinction between a unit and a field of study remains important.

Morphology examines word structure and relations among word forms. A morpheme is the smallest unit with lexical meaning or grammatical function in an analysis. Cats has cat and a plural marker. Unhelpfulness contains un-, help, -ful and -ness, so it has four morphemes under the ordinary analysis. Morphemes are not the same as syllables: banana has several syllables but is ordinarily one morpheme in English. Nor should every familiar-looking letter sequence be treated as an independent meaningful unit.

## Forms, meanings and classes of morpheme
A morph is an observable realization of a morpheme; allomorphs are alternative realizations of the same morpheme. The plural marker can be realized differently without changing its grammatical number contribution. Free morphemes can occur as words, whereas bound morphemes normally require attachment. The root book is free, and the regular plural suffix is bound. Duster is an independent word, but that does not make the entire word a single morpheme: dust and derivational -er can be distinguished.

Lexical morphemes carry substantial content meaning, while functional morphemes contribute grammatical organization and relationships. Function words include articles, pronouns and prepositions in introductory accounts. Open classes, such as nouns and verbs, readily gain new members. Closed classes have comparatively restricted membership and are less open to new additions. Closed does not mean historically incapable of any change. The free/bound distinction and the lexical/functional distinction answer different questions and should not be treated as identical classifications.

## Roots, bases and affixes
A root is a lexical core. A base is a form to which a morphological operation applies, and it can already contain several morphemes. A stem, in a common introductory usage, is the form receiving inflection. Worker can therefore be a stem for workers while containing the root work and derivational -er. Terminology varies across frameworks, so examination answers should identify the definition being used rather than assume complete uniformity.

Prefixes precede a base, suffixes follow it, and infixes are inserted within it. Re- in rewrite is a prefix; -ness in kindness is a suffix. Tagalog sulat and sumulat provide a conventional introductory example of an inserted -um-. English men and women are not ordinary infixation examples. Their number relation involves internal vowel change. Similarly, sing, sang and sung illustrate different kinds of morphological marking rather than one uniform operation of attaching a suffix.

## Derivation and inflection
Derivation creates a new lexeme or lexical meaning and may change category. Happy becomes the noun happiness with -ness, but unhappy remains an adjective. A category change is therefore not required for derivation. Inflection expresses grammatical contrasts within a lexeme's paradigm, normally preserving core lexical identity and category. Walked is a past form of walk, while teacher is a derived noun related to teach.

The conventional introductory list of eight English inflectional suffix categories includes plural, possessive, third-person singular present, past tense, present participle, past participle, comparative and superlative. This is a list of categories, not eight different spellings. Past and past participle may both use -ed, while derivational agentive -er and inflectional comparative -er share a spelling without sharing a grammatical role. In teachers, derivational -er occurs closer to the root than plural -s. Such ordering is a useful English generalization, not an exceptionless universal for all languages.

## Allomorphy and irregular patterns
The regular English plural commonly has [s] in cats, [z] in dogs and a syllabic realization in buses, often transcribed [ɪz] or [əz]. The preceding sound, not simply the final letter, conditions the choice. The regular past similarly has [t] in walked, [d] in played and a syllabic ending in wanted. A written -ed does not necessarily introduce a separate syllable. These patterns connect morphological function with phonological environment.

Morphology also uses nonconcatenative and irregular resources. Internal vowel change appears in man/men and sing/sang. Suppletion involves substantially different roots within a grammatical paradigm, as in go/went. A zero plural is illustrated by one sheep and three sheep, where context and syntax express number without an overt change to the noun. Lack of a visible ending does not establish absence of grammatical meaning.

## Other routes to new words
Compounding combines lexical bases, as in toothbrush. Spaces and hyphens do not by themselves determine whether an expression is a compound. Conversion changes a lexical category without an overt derivational affix, as when bottle is used as a verb. Blending combines portions of words, as in brunch, while clipping shortens a word, as in exam. In a narrow pronunciation-based distinction, NASA is an acronym pronounced as a word, while BBC is an initialism pronounced through letter names. Terminology can vary across sources.

Borrowing introduces forms from another language. Borrowed words can adapt to the receiving language's sounds and morphological patterns. Word formation therefore concerns more than affix lists: it includes relations between forms, changes of category, lexical innovation and interaction between languages.

## Phrase category and grammatical function
Words enter phrases organized around heads. A noun phrase can contain a noun with dependents, or consist of a single nominal element in an introductory analysis. An adjective phrase is headed by an adjective, as in very proud of her work. An adverb phrase is headed by an adverb, as in quite slowly. A prepositional phrase is headed by a preposition, as in under the table. Nice blue shirt is a noun phrase, not an adjective phrase, because shirt is its head.

Category must be distinguished from function. From China remains a prepositional phrase when it modifies boy. In a loud voice can function as an adverbial without becoming an adverb phrase by head category. Verb phrase boundaries depend on the framework: many syntactic accounts include the verb and its objects, while some teaching accounts use a narrower auxiliary-plus-main-verb group. The analysis should make its convention explicit.

## Nonfinite constructions and clauses
Traditional grammar calls to read novels an infinitive phrase and reading novels in subject position a gerund phrase. Modern accounts often analyze these as nonfinite clauses. An -ing form is not automatically a gerund in every use: compare the progressive is reading. Participial modifiers, such as wearing a red hat, can modify a noun. Restrictive modifiers do not always require commas; supplementary constructions often do.

An absolute construction has its own subject-like element and a predicative relation, as in Her eyes on the clock, Sara waited. A finite independent clause can function as a sentence, while a dependent clause is subordinate to another construction. Dependent clauses can contain both subjects and verbs, and nonfinite clauses may lack an overt subject. Understanding these distinctions links morphology to the next scale of grammar: how built words participate in meaningful phrase and clause structures.
''')
add(5,'Grammar as knowledge, description and explanation','Understanding grammatical approaches, language acquisition and linguistic evidence.', '''
## Grammar beyond a rulebook
Grammar can mean a speaker's internalized linguistic knowledge, an explicit description of that knowledge, or a theory explaining its organization. These meanings should be separated. A child may use a complex pattern without being able to name its grammatical category. Conversely, an adult may recite a classroom rule without applying it fluently in rapid conversation. Mental grammar concerns the system that supports linguistic ability; a published grammar is an analyst's representation of relevant patterns.

The competence-performance distinction separates underlying knowledge from actual use in a particular theoretical account. Performance depends on attention, memory, time pressure and circumstances. An isolated hesitation or slip may reveal processing constraints rather than a different underlying rule. Implicit knowledge is expressed through skilled use without necessarily being consciously stated. Explicit knowledge is accessible to reflection and verbal explanation. Both can support learning, but they are not identical achievements.

## Descriptive, prescriptive and pedagogical grammar
A descriptive grammar investigates patterns found in actual language varieties. If a regional variety uses a systematic agreement construction, its descriptive grammar records the relevant conditions. Prescriptive grammar recommends forms for particular purposes, often formal or institutional settings. A style guide may therefore be useful without providing a full scientific description of every variety. The difference concerns aims and evidence, not whether people may ever receive advice about writing.

Pedagogical grammar organizes explanations to support learning. It may simplify, sequence and illustrate patterns according to learners' needs. Some teaching grammars compare a new language with a language the learner already knows, but this is not a necessary feature of every pedagogical grammar. A successful explanation should remain clear about where a simplification stops being adequate. Learning to use a register for an examination and investigating how all speakers use language are related but distinguishable tasks.

## Grammaticality, acceptability and variation
Grammaticality concerns conformity to the patterns of a specified linguistic system. It differs from truth, social approval and plausibility. A grammatical sentence can describe a fictional event. An expression with an unacceptable word order may still communicate a true proposition. Acceptability concerns how natural or usable a form seems to speakers in context. A structurally licensed sentence can be difficult to process, especially when it contains deep embedding or burdensome dependencies.

Natural dialects are systematic. Socially prestigious varieties are not inherently the only logical or grammatical ones. A standard variety gains institutional status in areas such as education or administration, and mastering it can have practical value. That status does not erase the grammar of other varieties. Accent concerns pronunciation; dialect is broader and can include vocabulary and grammar. Idiolect concerns patterns associated with an individual. These distinctions help separate the scale of variation from evaluations attached to it.

## Acquisition and Universal Grammar
Children develop language through experience, interaction and learning, supported by human biological capacities. Broad developmental patterns do not imply that every child follows an identical timetable or produces the same first words. Overregularization provides evidence of pattern learning: a child who says goed or foots extends a productive pattern to an irregular item. Such forms are not mere exact imitation of adult went or feet. Learning requires both generalization and knowledge of exceptions.

Universal Grammar is a theoretical proposal associated with generative approaches, concerning innate properties or constraints relevant to language. Its content, scope and evidential basis are debated. It is not an established list of identical surface sentences, and it should not be confused with a linguistic universal discovered by comparing languages. A linguistic universal is a proposed cross-linguistic generalization, which may be absolute or statistical. Testing it requires an appropriate language sample and a clear formulation of the claim.

## Lexical knowledge and theoretical representations
The lexicon includes information about lexical forms, meanings and grammatical behaviour. Knowing give involves more than spelling; it includes knowledge about its possible argument patterns. In generative models using the terms PF and LF, Phonetic Form concerns a pronunciation-related interface representation and Logical Form concerns an interpretation-related representation. These labels belong to theoretical architectures. PF is not a font choice, and LF is not simply a microphone recording or an ordinary prose translation of meaning.

A linguistic theory proposes representations and principles to describe or explain patterns. Its assumptions should be distinguished from the observations it addresses. Different frameworks may analyze the same construction differently, so a theoretical term should be presented with its scope rather than treated as a universal fact requiring no qualification.

## Levels, comparison and methods
Levels of linguistic analysis offer complementary perspectives. Phonetics studies physical speech, phonology its linguistic patterns, morphology word structure, syntax phrase and clause organization, semantics conventional meaning, and pragmatics interpretation in use. Lexical analysis investigates vocabulary. These levels interact: a plural ending has a morphological function, a phonological realization and a syntactic distribution. Explaining one dimension does not automatically replace analysis of the others.

A synchronic analysis examines a system in a particular period; a diachronic analysis investigates development through time. Typology compares structural properties, while historical genealogy concerns relationships of descent. Sociology of language often emphasizes language distribution and functions within societal institutions, overlapping with sociolinguistics while foregrounding a different scale of inquiry. The labels organize questions rather than excluding collaboration.

Corpus evidence comes from systematically collected language data, while elicitation uses targeted tasks, questions or judgments to obtain observations. Both require careful interpretation. A form missing from one small corpus may still be possible, and elicited judgments can depend on context and task design. A strong grammatical analysis therefore combines explicit concepts with evidence suited to the question. The lecture's central lesson is that grammar is both a human capacity and an object of investigation, not simply a catalogue of socially preferred expressions.
''')
add(6,'Syntax: how sentences are organized and interpreted','Constituents, clause patterns, sentence types and the limits of linear analysis.', '''
## Structure rather than word lists
Syntax investigates how words combine into phrases, clauses and sentences. Its objects are hierarchical structures rather than alphabetically arranged inventories. A constituent is a unit within a larger structure. In The child with a red hat waved, the subject noun phrase contains a smaller prepositional phrase, and that phrase contains another noun phrase. Immediate constituents are the next-level divisions of a unit; terminal units are the leaves of the particular analysis, commonly individual words in an introductory tree.

A head determines important properties of its phrase. Proud heads very proud of her work, even though it is not the first written word. Constituency tests, including substitution, movement and coordination, provide evidence about grouping. Replacing the old house with it supports treating it as a unit. No single diagnostic works without restriction in every construction, so converging evidence is preferable to an automatic verdict from one unsuccessful test.

## Grammatical relations and functions
The subject is a grammatical relation, identified through properties such as clause organization and agreement in a relevant language. It is not defined as whoever intentionally acts. In The window was broken by Ali, the window is subject but Ali is the semantic agent. The direct object is another grammatical relation associated with a transitive construction. An expression does not become an object merely because it follows a verb: to school is not a direct object in She goes to school.

A subject complement identifies or describes the subject, as in Ali is a doctor or Ali is tired. An object complement predicates a property or identity of an object, as in They made Ali captain. Adjuncts add modifying information not selected as required complements in the relevant construction. Optionality can help distinguish adjuncts from complements, but is not a complete universal test. Grammatical function, semantic role and phrase category should always be kept conceptually separate.

## The basic clause patterns
Traditional clause-pattern descriptions provide a useful starting point. SV appears in The baby slept. SVO appears in Sara opened the door, where the door is direct object. SVC appears in Ali is tired, where tired is a subject complement. The C stands for complement, not consonant. SVA includes an adverbial, commonly a required adverbial in stricter classifications, as in She lives in Lahore. Adverbial names a function and need not be a single-word adverb.

SVOO contains an indirect and direct object, as in Sara gave Ali a book. SVOC contains an object and a complement predicated of it, as in They painted the door green. SVOA contains an object and a required adverbial, as in Sara put the book on the shelf. In that placement construction, the location completes the verb's pattern. She goes to school must not be classified as SVO merely because school is a noun after goes; the intervening preposition and the function of the whole phrase matter.

## Clause forms and communicative uses
Declarative, interrogative, imperative and exclamative labels describe forms and their conventional functions. The train is late is a declarative; Is the train late? is an interrogative. Close the door is an imperative with an understood addressee, although some imperative patterns can have overt subjects. What a lovely day it is! has characteristic exclamative syntax. An exclamation mark alone does not determine the grammatical form.

Form and speech-act function can diverge. Could you close the door? is interrogative in form but commonly a request in use. This does not erase its syntax; it shows why syntax and pragmatics address different aspects of one utterance. An adequate analysis identifies both rather than forcing every question form to be an actual request for information.

## Simple, compound and complex sentences
A simple sentence has one independent clause and no subordinate clause in the basic classification. Ali and Sara laughed contains a coordinated subject but remains simple. A compound sentence combines independent clauses, as in Ali cooked, and Sara washed the dishes. A complex sentence has a main clause and at least one subordinate clause, as in Although it rained, we played. A compound-complex sentence combines at least two independent clauses with at least one subordinate clause.

Count clauses and their relations rather than conjunctions alone. In When it rained, Ali stayed home, but Sara went out, the initial subordinate clause combines with two coordinated independent clauses. The number of written words and the sophistication of vocabulary do not determine this structural classification. Nonfinite clauses add further complexity, which is why the introductory subject-plus-finite-verb description of every clause needs qualification.

## Ambiguity, voice and dependencies
Structural ambiguity arises when the same word sequence supports different groupings or attachments. I saw the man with binoculars can describe seeing with an instrument or identify a man carrying binoculars. The ambiguity does not require a word with unrelated dictionary meanings. Paraphrases express substantially similar meanings through different forms, as in the two familiar give constructions, although information structure and emphasis can differ.

A typical English passive relates an active object to passive subject position: Ali opened the door becomes The door was opened by Ali. The agent remains Ali even when expressed in a by-phrase rather than as subject. Questions can involve subject-auxiliary inversion, as in Can Sara swim? With no suitable auxiliary, do-support supplies one: Did Sara leave? The lexical verb remains in its base form because did carries past tense. A wh-dependency, as in What did Sara buy?, links the initial expression to its interpreted argument position.

## Order, parallelism and rhetorical arrangement
Fronting an adverbial does not necessarily invert subject and verb. In Lahore, oranges grow retains the subject before grow, while Here comes the bus has a different order. Parallel structure uses appropriately matched forms in coordination, as in reading and swimming. Parallelism improves clarity, but analysis should consider the particular construction rather than treat every surface mismatch as equally unacceptable.

Loose and periodic sentences are rhetorical labels. A loose sentence states its main assertion before elaboration, whereas a periodic sentence delays completion of the main assertion. These labels concern the arrangement of information and expectations; they do not replace simple, compound or complex classification.

## Generative and transformational perspectives
Generative grammar aims to characterize the structures licensed by a linguistic system through explicit principles or rules. Generation is a formal idea, not a claim that speakers consciously run written instructions. Transformational grammar is a family of models relating structures through transformations. Earlier accounts distinguished deep structure, an underlying representation, from surface structure after transformations. Even surface structure was an abstract representation, not simply ink or a sound waveform.

These historical terms should be learned in their framework, rather than presented as universal commitments of every contemporary theory. The broader conclusion remains useful across approaches: syntax explains systematic relations among constituents, and these relations help account for grammaticality, ambiguity and interpretation.
''')
add(7,'Semantics: words, reference and sentence meaning','Understanding lexical relations, semantic roles and the logic of meaning.', '''
## The subject matter of semantics
Semantics studies conventional linguistic meaning. Lexical semantics concerns words and morphemes; compositional semantics examines how larger meanings arise through combination. Dog bites man and Man bites dog contain the same lexical items but describe different events because their grammatical relations differ. Word meanings therefore matter, but a sentence's meaning cannot normally be obtained by ignoring its structure. Pragmatics complements this account by investigating interpretation in a particular context.

The mental lexicon represents knowledge of lexical forms, meanings and relevant grammatical properties. Semantic features can help analyze contrasts, such as adulthood or animacy, but no small agreed feature list automatically captures every possible meaning. Some categories resist simple necessary-and-sufficient descriptions, and different frameworks assign features differently. An analysis should show what the chosen representation explains and where its limitations remain.

## Denotation, sense and association
Denotation concerns what an expression applies to in an interpretation. Reference concerns using an expression to identify a particular entity in context. A speaker can use that student to pick out someone in a room, while the descriptive content of student is not exhausted by that one individual. Sense concerns meaning and relations within the language. Morning star and evening star can refer to Venus while differing in how they present it. Shared reference does not require identical sense.

Connotation involves emotional, social or evaluative associations. Home may evoke belonging beyond identifying a dwelling. Conceptual meaning concerns central descriptive content; the fear associated with needle does not replace its relevant descriptive meaning. These distinctions are useful because associations can differ among speakers while a shared linguistic meaning still supports communication.

Extension is the set of entities satisfying an expression in a specified world or situation. Intension concerns the descriptive content or rule determining extensions across situations; formal semantics often models it as a function from worlds to extensions. The membership of student can change while its descriptive interpretation remains stable. Intension should therefore not be defined simply as a private mental image or emotional association. Semantic models can also represent fictional and hypothetical domains rather than requiring every expression to identify a visible real object.

## Senses, ranges and compatibility
A word's semantic range includes the senses or uses it can have in a particular analysis. Run can describe movement, management or machine operation, but not every sense fits every context. Lexical ambiguity occurs when a form permits more than one lexical interpretation, as in an isolated reference to a bank. Context commonly selects an interpretation. Structural ambiguity, by contrast, concerns alternative groupings or attachments rather than lexical senses alone.

Selectional restrictions concern compatibility expectations between predicates and their arguments. The cupboard drank the soup has familiar syntax but is anomalous under an ordinary literal interpretation because cupboards do not drink. Personification or a fictional setting could change its interpretation. A semantic anomaly must therefore be assessed relative to a reading, rather than automatically classified as ungrammatical word order.

## Similarity and opposition
Synonymy relates identical or close meanings in the relevant sense. Couch and sofa are near synonyms, but near synonyms need not be interchangeable in every collocation, register or idiom. Antonymy is a broad label for opposition. Gradable opposites, such as hot and cold, allow intermediate values. Not hot therefore need not mean cold: something may be warm or mild.

Complementary opposites divide an idealized domain into alternatives, as with alive and dead in an ordinary binary biological classification. Borderline cases or figurative uses require care. Relational converses describe a situation from reversed participant perspectives: if A sells a book to B, B buys it from A. Buy and sell do not merely name opposing points on a temperature-like scale. Distinguishing these types explains which inferences an opposition supports.

## Shared forms and category relations
Homonymy relates distinct lexical items with unrelated meanings sharing a form, as in familiar financial and river-edge senses of bank. Polysemy concerns related senses of one lexical item, as in a body head and an organization's head. Their boundary may be debated, and historical origin alone does not settle every current analysis. Homophony concerns shared pronunciation, as in flour and flower in many varieties; homography concerns shared spelling, as with lead meaning guide and lead meaning the metal. Spelling and pronunciation are separate dimensions.

Hyponymy is the subtype relation: rose is a hyponym of flower, while flower is a hypernym of rose. If something is a rose, it follows that it is a flower, but not every flower is a rose. Bus and car are co-hyponyms under vehicle. Meronymy concerns part and whole: a wheel is part of a car, not a kind of car. Confusing these relations reverses valid inferences and obscures category structure.

## Figurative association and typicality
Metaphor interprets one entity or domain through another, as when a fierce competitor is called a tiger. Metonymy uses a salient association, as when The White House refers to officials or an institution. Its basis is association or contiguity, not necessarily resemblance. An informal synonym such as cops for policemen is therefore not a strong diagnostic example of metonymy by itself.

A prototype is a particularly representative category member for a person or community. A robin or sparrow may be judged more typical as a bird than a penguin, depending on experience. Typicality is not membership: being less typical does not stop a penguin from being a bird. Prototype judgments help explain aspects of categorization while allowing variation across communities and contexts.

## Semantic roles and grammatical relations
Semantic roles describe participants' contributions to events or states. An agent typically intentionally initiates an action. A theme undergoes relevant motion, change or a state, while some frameworks distinguish patient more narrowly. An experiencer feels or perceives, as with Sara in Sara fears spiders. An instrument is a means, such as the key in opening a door with a key. Location identifies where an event occurs, source its origin and goal its destination.

A possessor has or owns something, while a natural force can function as cause or causer without intentional agency. Role inventories differ across theories. In Sara sent a parcel from Lahore to Karachi, Sara is agent, the parcel theme, Lahore source and Karachi goal. If the sentence is made passive, the parcel may become grammatical subject without becoming the agent. Syntax and semantic roles therefore intersect without being identical.

## Meaning relations between propositions
Entailment holds when one proposition's truth guarantees another's truth under the intended interpretation. Owning a red car entails owning a car. Contradiction occurs when propositions cannot both be true with the relevant reference, time and sense held fixed. Tautology concerns truth by logical form in an adopted system, as with P or not P in classical logic. An analytic statement is true by meanings under the stated interpretation, rather than requiring a fresh empirical investigation of the world.

These relations differ from a conversational suggestion. An entailment cannot simply be cancelled while the original proposition remains true in the same interpretation. Recognizing this boundary prepares the transition to pragmatics, where listeners infer additional meanings from context, shared assumptions and communicative purposes.
''')
add(8,'Pragmatics: meaning, inference and action in context','How people communicate more than the literal words alone encode.', '''
## From sentence meaning to speaker meaning
Pragmatics studies language use and interpretation in context. Speaker meaning is what a person communicates through a particular utterance, which may go beyond the conventional meanings of its words. There is a car coming can be a warning beside a road, but a comment about an expected delivery in another situation. An analyst should use contextual evidence rather than invent one intention and assume it must hold everywhere.

Linguistic context, or co-text, consists of surrounding language. In Sara bought a book. She read it, preceding expressions support interpretation of she and it. Situational context includes participants, place, time, purposes and relevant background. Common ground is information treated as shared for the interaction. It need not be universal knowledge or even perfectly accurate; participants can negotiate or challenge assumptions as a conversation develops.

## Cooperation and conversational expectations
Grice's cooperative principle provides a framework for reasoning about contributions appropriate to an accepted conversational purpose. It is not a guarantee that people are friendly or truthful. The quantity maxim concerns appropriate informativeness: a reply should provide what the exchange requires without unnecessary excess. Quality concerns avoiding falsehood and unsupported claims. Relation concerns relevance, and manner concerns clarity, order and avoidance of obscurity or unnecessary ambiguity.

These maxims address different dimensions. Asked for an exact appointment time, sometime is insufficiently informative. Giving an unrelated history of clocks fails to address relevance. Presenting a guess as certain raises an evidential quality problem, while a needlessly confusing explanation concerns manner. One utterance can raise several issues, so the most direct evidence should guide an examination answer rather than a mechanical one-label rule.

## Implicature, flouting and violation
Conversational implicature is additional meaning inferred through context and conversational reasoning rather than guaranteed by what is explicitly said. Some students passed may suggest not all when the speaker is expected to know the result. Yet the speaker can add in fact all did without contradicting the minimal assertion that some passed. The not-all inference is therefore not an ordinary logical entailment of some. Particular contexts can remove or alter the inference.

Flouting involves an overt apparent failure to satisfy a maxim that invites interpretation beyond the literal words. During a severe storm, Lovely picnic weather! may conspicuously conflict with literal quality and communicate irony. Violating a maxim is covert, as when someone gives a false alibi intending it to be believed. The difference lies in how the contribution is presented and expected to be understood, not simply in whether a sentence is literally false.

## Doing things with utterances
Speech-act analysis distinguishes three aspects of an utterance. The locutionary act concerns saying something with a linguistic form and meaning. The illocutionary act is what is done in saying it, such as warning, requesting or promising. A perlocutionary effect is a consequence for a hearer's beliefs, feelings or actions. A warning may make a child step away from traffic, but it can still be a warning if the child ignores it. The intended act and actual effect are not identical.

A direct speech act aligns a conventional clause form with its typical function, as with Close the door used as a command. An indirect speech act communicates an act through another form, as when Could you close the door? functions as a request. In a medical assessment, an ability question might instead be intended literally. Interpretation depends on conventions together with the particular circumstances.

## Performative language and speech-act classes
An explicit performative names the act it performs, as in I promise to return the book. Reporting I promised yesterday does not necessarily make a new promise now. Felicity conditions are requirements for a speech act's appropriateness or success, and they differ across acts. Institutional declarations depend on suitable authority and procedures. An unauthorized passer-by cannot impose a prison sentence merely by repeating a judge's formula.

A familiar classification distinguishes assertives, directives, commissives, expressives and declarations. Assertives commit a speaker to a proposition's truth; directives seek action from an addressee. Commissives commit the speaker to a future course, as with a promise. Expressives communicate attitudes, as in apologies or congratulations. Successful declarations change an institutional state. These classes concern communicative acts rather than merely verb tense or punctuation.

## Presupposition and background assumptions
A presupposition is information presented as taken for granted. Sara stopped smoking normally presupposes that she smoked previously. Negating the sentence often preserves that background: Sara did not stop smoking commonly retains the previous-smoking assumption. This tendency is called presupposition projection. It is useful diagnostically but not an exceptionless rule across all triggers and contexts.

Factive expressions such as regret commonly presuppose the truth of their complements. Sara regrets that she missed the bus presents the missed bus as background. Believe does not have the same property: believing something does not make it true. Presuppositions need not actually be true, and hearers can challenge them. In response to My sister is visiting, a hearer may ask You have a sister? rather than accept the assumption silently.

Accommodation is a contextual adjustment in which a hearer provisionally accepts a previously unshared assumption to make the utterance interpretable. It is not an obligation to accept every claim. Presupposition, entailment and implicature must therefore be distinguished: they differ in how information is presented, inferred and related to truth under an interpretation.

## Deixis, reference and discourse
Deixis concerns reference anchored to a communicative situation. Person deixis includes I and you; I conventionally identifies the speaker role, but context identifies the individual. Spatial deixis includes here and there, interpreted relative to an established viewpoint. Temporal deixis includes now, tomorrow and yesterday. Tomorrow does not denote one permanent calendar date; it normally depends on a day of speaking or another relevant anchor.

Social deixis indexes relationships through forms such as honorifics and respectful address. Discourse deixis points to a stretch of discourse, as when That was strange refers to a preceding statement. Anaphora instead connects an expression to an antecedent, as when it refers to a previously introduced key. A pronoun can be anaphoric or deictic, so its form alone does not settle how reference is established. Narrative and quotation can also shift a deictic centre.

## A connected approach to interpretation
Metaphorical and other nonliteral uses show how conventional meanings interact with contextual reasoning. Calling a person a tiger need not literally classify the person as an animal; the hearer identifies a relevant interpretation using shared knowledge and the situation. Such interpretations should still be justified by evidence. When a short conversation is presented without a clear setting, several reasonable readings can remain available.

The central achievement of pragmatics is explaining the relationship between words, assumptions and communicative action. Understanding an utterance requires recognizing its form and conventional meaning, identifying relevant reference, and reasoning about what the speaker is doing. The course therefore ends by reconnecting structural analysis with the social use of language introduced in the first lecture.
''')
assert len(essays)==8
(root/'essays.json').write_text(json.dumps(essays,ensure_ascii=False,indent=2))
(root/'essays.js').write_text('window.LECTURE_ESSAYS = '+json.dumps(essays,ensure_ascii=False,separators=(',',':'))+';\n')
for e in essays:print(e['lecture'],e['wordCount'],'words',len(e['sections']),'sections')
