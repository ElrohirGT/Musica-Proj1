from music import *

originalCompositionBasedOnStorms = Score("Original Composition", 120) # nombre y tempo

# Key: D minor

# Key measure: 3/4

AccordionPart = Part(OCARINA, 0) # Partes y el instrumento que representan
FlutePart = Part(FLUTE, 1)
PianoPart = Part(PIANO, 2)
BassPart = Part(PIANO, 3)
PercussionPart = Part("Drums", 0, 9)

# Melodia ---------------------------------------------------------------

melodyIntro = [
   REST
] * 8

melodyIntroDur = [
   DHN
] * 8

melodyPitch = melodyIntro + [
   A5, D5, E5, F5, G5, C6, D6, A5,
   BF5, F6, F6, E6, D6, BF5, A5, C6, D6, A5,
   A5, D5, E5, F5, G5, C6, D6, A6,
   G6, F6, E6, D6, A5, C6, D6, A5,
]

melodyDur = melodyIntroDur + [
   QN, HN, EN, EN, HN, QN, HN, HN,
   QN, QN, EN, EN, QN, HN, HN, QN, QN, DHN,
   QN, HN, EN, EN, HN, QN, HN, HN,
   HN, QN, QN, HN, HN, QN, QN, HN,
]

# Contramelodia ----------------------------------------------------------

contramelodyIntro = [
   REST
] * 8

contramelodyIntroDur = [
   DHN
] * 8

contramelodyPitch = contramelodyIntro + [
   REST, REST, E6, F6, G6,
   BF4, F5, F5, E5, D5, BF4, REST, C5, D5, A4,
   A4, D4, E4, F4, G4, C5, D5, A5,
   G5, F5, E5, D5, A4, C5, D5, A4,
]

contramelodyDur = contramelodyIntroDur + [
   QN, HN, EN, EN, WN,
   QN, QN, EN, EN, QN, HN, HN, QN, QN, DWN,
   QN, HN, EN, EN, HN, QN, HN, HN,
   HN, QN, QN, HN, HN, QN, QN, HN,
]

# Harmonia --------------------------------------------------------------
harmonyPitch = [
   REST, [D3, F3, A3], [D3, F3, A3],
   REST, [C3, E3, G3],
   REST, [BF2, D3, F3], [BF2, D3, F3],
   REST, [A2, DF3, E3], [A2, DF3, E3],
   REST, [BF2, D3, F3], [BF2, D3, F3],
   REST, [C3, E3, G3], [C3, E3, G3],
   REST, [D3, F3, A3], [D3, F3, A3],
   REST, [A2, DF3, E3],
] * 3

harmonyDur = [
   QN, QN, QN,
   QN, HN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, HN,
] * 3

harmonyVariation = [

]

harmonyVariationDur = [

]

# Bajo --------------------------------------------------------------------
bassPitch = [
   D2, REST, REST,
   C2, REST, REST,
   BF1, REST, REST,
   A1, REST, REST,
   BF1, REST, REST,
   C2, REST, REST,
   D2, REST, REST,
   A1, REST, REST,
] * 3

bassDur = [
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
   QN, QN, QN,
] * 3

bassVariation = [

]

bassVariationDur = [

]

# Percusion ----------------------------------------------------------------
repeatN = 12
delta = 24

bassDrumPit = [REST] * delta + [BDR, REST, REST] * repeatN
bassDrumDur = [QN] * delta +   [QN,  QN,   QN] * repeatN

snareDrumPit = [REST] * delta + [REST, SNR, SNR] * repeatN
snareDrumDur = [QN] * delta +   [QN,   QN,  QN] * repeatN

hihatDelta = 36
hihatRepeat = 4
hiHatDrumPit = [REST] * hihatDelta + [REST, CHH, CHH, CHH] * hihatRepeat + [REST] * 21 + [REST, REST, CHH, CHH]
hiHatDrumDur = [QN] * hihatDelta + [QN,   QN,  EN,  EN] * hihatRepeat +    [QN]   * 21 + [QN,   QN,   EN,  EN]
# hiHatDrumPit = [REST, SNR, SNR, SNR] * repeatN
# hiHatDrumDur = [QN,   QN,  EN,  EN, ] * repeatN

# Percusion
bassDrumPhrase = Phrase(0.0)
bassDrumPhrase.addNoteList(bassDrumPit, bassDrumDur)
snareDrumPhrase = Phrase(0.0)
snareDrumPhrase.addNoteList(snareDrumPit, snareDrumDur)
hiHatPhrase = Phrase(0.0)
hiHatPhrase.addNoteList(hiHatDrumPit, hiHatDrumDur)

# Melody Phrases
melodyPhrase = Phrase() # Frase que contiene la melodia
contramelodyPhrase = Phrase() # Frase que contiene la contramelodia
harmonyPhrase = Phrase() # Frase que contiene la armonia
bassPhrase = Phrase() # Frase que contiene el bajo
percussionPhrase = Phrase() # Frase que contiene la percusion

# Intro + Frase 1 
melodyPhrase.addNoteList(melodyPitch, melodyDur) # Agrega las notas y duraciones a la frase
contramelodyPhrase.addNoteList(contramelodyPitch, contramelodyDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonyPitch, harmonyDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassPitch, bassDur) # Agrega las notas y duraciones a la frase
#percussionPhrase.addNoteList(percussionPitch, percussionDur) # Agrega las notas y duraciones a la frase

# Frase 2
#melodyPhrase.addNoteList(melodyVariation, melodyVariationDur)
#contramelodyPhrase.addNoteList(contramelodyVariation, contramelodyVariationDur)
#harmonyPhrase.addNoteList(harmonyVariation, harmonyVariationDur) # Agrega las notas y duraciones a la frase
#bassPhrase.addNoteList(bassVariation, bassVariationDur) # Agrega las notas y duraciones a la frase

AccordionPart.addPhrase(melodyPhrase) # Agrega la frase a la parte del instrumento
FlutePart.addPhrase(contramelodyPhrase) # Agrega la frase a la parte del instrumento
PianoPart.addPhrase(harmonyPhrase) # Agrega la frase a la parte del instrumento
BassPart.addPhrase(bassPhrase) # Agrega la frase a la parte del instrumento
## Percusión
PercussionPart.addPhrase(bassDrumPhrase)
PercussionPart.addPhrase(hiHatPhrase)
PercussionPart.addPhrase(snareDrumPhrase)

originalCompositionBasedOnStorms.addPart(AccordionPart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(FlutePart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(PianoPart) # Agrega la parte del instrumento
originalCompositionBasedOnStorms.addPart(BassPart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(PercussionPart) # Agrega la parte del instrumento a la partitura

Play.midi(originalCompositionBasedOnStorms) # Reproduce la partitura en formato MIDI

Write.midi(originalCompositionBasedOnStorms, "Original2.mid") # Guarda la partitura en un archivo MIDI