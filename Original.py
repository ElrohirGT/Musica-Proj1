from music import *

originalCompositionBasedOnStorms = Score("Original Composition", 140) # nombre y tempo

# Key: D minor

# Key measure: 4/4

AccordionPart = Part(OCARINA, 0) # Partes y el instrumento que representan
FlutePart = Part(FLUTE, 1)
PianoPart = Part(PIANO, 2)
BassPart = Part(ACOUSTIC_BASS, 3)
PercussionPart = Part("Drums", 0, 9)


melodyPhrase = Phrase() # Frase que contiene la melodia
contramelodyPhrase = Phrase() # Frase que contiene la contramelodia
harmonyPhrase = Phrase() # Frase que contiene la armonia
bassPhrase = Phrase() # Frase que contiene el bajo
percussionPhrase = Phrase() # Frase que contiene la percusion

# Melodia ---------------------------------------------------------------------

melodyIntroRest = [
   REST
] * 32

melodyIntroRestDur = [
   QN
] * 32

melodyEnd = [
   D4, F4, A4, D4, A4, F4, 
   E4, C4, A3, REST,
   BF3, BF3, D4, F4, BF4,
   A3, A4, G4, F4, E4, D4, REST,
   D5
]

melodyEndDur = [
   DQN, DQN, DQN, DQN, QN, QN,
   DQN, DQN, WN, QN,
   DHN, EN, DQN, QN, HN,
   WN, QN, EN, QN, EN, EN, DQN,
   QN
]

melodyPitch = [ # Notas de la melodia
   A5, D5, F5, D5, F5, A5, D5, F5, A5, G5, F5, D5, REST,
   A5, D5, F5, D5, F5, A5, D5, F5, A5, G5, F5, D5, REST,
   BF5, D5, F5, D5, F5, BF5, D5, F5, BF5, G5, F5, D5, REST,
   A5, DF6, E6, DF6, E6, A6, DF7, E7, A7,
]

melodyDur = [ # Duraciones de las notas de la melodia
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, HN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, HN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, HN,
   EN, EN, EN, EN, EN, EN, EN, EN, WN,
]

melodySolo = [
   REST
] * 64

melodySoloDur = [
   QN
] * 64

# Contramelodia ---------------------------------------------------------------------

contramelodyIntro = [ # Notas de la contramelodia
   D5, F5, A5, D5, F5, A5, D5, F5, D5, F5, A5, D5, F5, A5, D5, F5,
   C5, E5, G5, C5, E5, G5, C5, E5, C5, E5, G5, C5, E5, G5, C5, E5,
   BF4, D5, F5, BF4, D5, F5, BF4, D5, BF4, D5, F5, BF4, D5, F5, BF4, D5,
   A4, DF5, E5, A4, DF5, E5, A4, DF5, A5, A5, A5, A6
]

contramelodyIntroDur = [ # Duraciones de las notas de la contramelodia
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, DQN, QN, QN
]

contramelodyEnd = [
   D5, F5, A5, D5, F5, A5, D5, F5, D5, F5, A5, D5, F5, A5, D5, F5,
   C5, E5, G5, C5, E5, G5, C5, E5, C5, E5, G5, C5, E5, G5, C5, E5,
   BF4, D5, F5, BF4, D5, F5, BF4, D5, BF4, D5, F5, BF4, D5, F5, BF4, D5,
   A4, DF5, E5, A4, DF5, E5, A4, DF5, A4, DF5, E5, A4, DF5, E5, D5, REST,
   D6,
]
 
contramelodyEndDur = [  
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, DQN, 
   QN,
]

contramelodyPitch = [
   D5, F5, A5, D5, F5, A5, D5, F5, D5, F5, A5, D5, F5, A5, D5, F5,
   C5, E5, G5, C5, E5, G5, C5, E5, C5, E5, G5, C5, E5, G5, C5, E5,
   BF4, D5, F5, BF4, D5, F5, BF4, D5, BF4, D5, F5, BF4, D5, F5, BF4, D5,
   A4, DF5, E5, A4, DF5, E5, A4, DF5, A4, DF4, E5, A4, DF4, E5, A5, DF5,
]

contramelodyDur = [
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
   EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN,
]

contramelodySolo = [
   REST
] * 64

contramelodySoloDur = [
   QN
] * 64

# Armonia ---------------------------------------------------------------------

harmonyIntro = [
   REST, [D3, F3, A3], [D3, F3, A3], REST, [D3, F3, A3], [D3, F3, A3],
   REST, [C3, E3, G3], [C3, E3, G3], REST, [C3, E3, G3], [C3, E3, G3],
   REST, [BF2, D3, F3], [BF3, D3, F3], REST, [BF2, D3, F3], [BF3, D3, F3],
   REST, [A3, DF3, E3], [A3, DF3, E3], REST, [A3, DF3, E3], [A3, DF3, E3],
]

harmonyIntroDur = [
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
]

harmonyEnd = [
   REST, [D3, F3, A3], [D3, F3, A3], REST, [D3, F3, A3], [D3, F3, A3],
   REST, [C3, E3, G3], [C3, E3, G3], REST, [C3, E3, G3], [C3, E3, G3],
   REST, [BF2, D3, F3], [BF3, D3, F3], REST, [BF2, D3, F3], [BF3, D3, F3],
   REST, [A3, DF3, E3], [A3, DF3, E3], REST, [A3, DF3, E3], [A3, DF3, E3], [D3, F3, A3],
   [F3, A3, D4],
]

harmonyEndDur = [
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, EN, HN,
   QN,
]

harmonyPitch = [ # Notas de la armonia
   REST, [D3, F3, A3], [D3, F3, A3], REST, [D3, F3, A3], [D3, F3, A3],
   REST, [C3, E3, G3], [C3, E3, G3], REST, [C3, E3, G3], [C3, E3, G3],
   REST, [BF2, D3, F3], [BF3, D3, F3], REST, [BF2, D3, F3], [BF3, D3, F3],
   REST, [A3, DF3, E3], [A3, DF3, E3], REST, [A3, DF3, E3], [A3, DF3, E3],
]

harmonyDur = [ # Duraciones de las notas de la armonia
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
   QN, DQN, DQN, QN, DQN, DQN,
]

harmonySolo = [
   REST, [D3, F3, A3], REST, [D3, F3, A3], REST, [D3, F3, A3], REST, [D3, F3, A3], REST,
   REST, [C3, E3, G3], REST, [C3, E3, G3], REST, [C3, E3, G3], REST, [C3, E3, G3], REST,
   REST, [BF2, D3, F3], REST, [BF3, D3, F3], REST, [BF2, D3, F3], REST, [BF3, D3, F3], REST,
   REST, [A3, DF3, E3], REST, [A3, DF3, E3], REST, [A3, DF3, E3], REST, [A3, DF3, E3], REST,
] * 2

harmonySoloDur = [
   QN, SN, QN+SN, SN, HN+SN, SN, QN+SN, SN, QN+SN,
   QN, SN, QN+SN, SN, HN+SN, SN, QN+SN, SN, QN+SN,
   QN, SN, QN+SN, SN, HN+SN, SN, QN+SN, SN, QN+SN,
   QN, SN, QN+SN, SN, HN+SN, SN, QN+SN, SN, QN+SN,
] * 2

# Bajo ---------------------------------------------------------------------

bassIntro = [
   D2, D2, D2, D3, D2, D2, D2,
   C2, C2, C2, C2, C2, C2, C2,
   BF1,BF1, BF1, BF1, BF1, BF1,
   A1, A1, A1, A1, A1, A1,
]

bassIntroDur = [
   DQN, DQN, EN, EN, DQN, DQN, QN,
   DQN, DQN, QN, DQN, QN, QN, QN,
   DQN, DQN, QN, DQN, QN, QN,
   DQN, DQN, QN, DQN, DQN, DQN, 
]

bassEnd = [
   D2, D2, D2, D2, D2, D2,
   C2, C2, C2, C2, C2, C2, C2,
   BF1, BF1, BF1, BF1, BF1, BF1,
   A1, A1, A1, A1, A1, A1, A1,
   D2
]

bassEndDur = [
   DQN, DQN, EN, DQN, QN, QN,
   DQN, DQN, QN, DQN, QN, QN, QN,
   DQN, DQN, QN, DQN, QN, DQN,
   DQN, DQN, QN, DQN, QN, DQN, QN,
   QN
]

bassPitch = [ # Notas del bajo
   D2, D2, D2, D3, D2, D2, D2,
   C2, C2, C2, C2, C2, C2, C2,
   BF1,BF1, BF1, BF1, BF1, BF1,
   A1, A1, A1, A1, A1, A1,
]

bassDur = [ # Duraciones de las notas del bajo
   DQN, DQN, EN, EN, DQN, DQN, QN,
   DQN, DQN, QN, DQN, QN, QN, QN,
   DQN, DQN, QN, DQN, QN, QN,
   DQN, DQN, QN, DQN, DQN, DQN, 
]

bassSolo = [
   D2, D3, A2, F3, F2, D3, D2,
   C2, G2, E2, C2, C3, E2, G2,
   BF1, BF2, BF1, F2, F1, BF1, BF2, BF1, BF1,
   A1, E1, A1, A2, E1, DF2,
] * 2

bassSoloDur = [
   DQN, DQN, EN, EN, DQN, DQN, QN,
   EN, QN, QN, DQN, QN, DQN, DQN,
   EN, EN, DQN, EN, QN, DQN, EN, QN, QN,
   DQN, DQN, QN, DQN, DQN, QN,
] * 2

# Percusion ---------------------------------------------------------------------

percussionIntro = [ # Notas de la percusion
    ACOUSTIC_BASS_DRUM
] * 32

percussionIntroDur = [ # Duraciones de las notas de la percusion
    QN
] * 32

percussionPitch = [
   [ACOUSTIC_BASS_DRUM, CLOSED_HI_HAT], [SNARE, CLOSED_HI_HAT]
] * 16

percussionDur = [
   QN, QN,
] * 16

percussionSolo = [ # Notas de la percusion
    ACOUSTIC_BASS_DRUM
] * 64

percussionSoloDur = [ # Duraciones de las notas de la percusion
    QN
] * 64

percussionFill = [
   ACOUSTIC_BASS_DRUM, SNARE, SNARE, ACOUSTIC_BASS_DRUM, SNARE, SNARE, [SNARE, CRASH_CYMBAL_1]
]

percussionFillDur = [
   EN, EN, QN, QN, SN, SN, QN 
]

percussionSolo2 = [ # Notas de la percusion
    ACOUSTIC_BASS_DRUM
] * 32

percussionSoloDur2 = [ # Duraciones de las notas de la percusion
    QN
] * 32

percussionEnd = [
   [ACOUSTIC_BASS_DRUM, CLOSED_HI_HAT], [SNARE, CLOSED_HI_HAT]
] * 16

percussionEndDur = [
   QN, QN,
] * 16


# INTRO
melodyPhrase.addNoteList(melodyIntroRest, melodyIntroRestDur)
contramelodyPhrase.addNoteList(contramelodyIntro, contramelodyIntroDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonyIntro, harmonyIntroDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassIntro, bassIntroDur) # Agrega las notas y duraciones a la frase
percussionPhrase.addNoteList(percussionIntro, percussionIntroDur) # Agrega las notas y duraciones a la frase

# FRASE
melodyPhrase.addNoteList(melodyPitch, melodyDur) # Agrega las notas y duraciones a la frase
contramelodyPhrase.addNoteList(contramelodyPitch, contramelodyDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonyPitch, harmonyDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassPitch, bassDur) # Agrega las notas y duraciones a la frase
percussionPhrase.addNoteList(percussionPitch, percussionDur) # Agrega las notas y duraciones a la frase

# SOLO DE BAJO
melodyPhrase.addNoteList(melodySolo, melodySoloDur) # Agrega las notas y duraciones a la frase
contramelodyPhrase.addNoteList(contramelodySolo, contramelodySoloDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonySolo, harmonySoloDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassSolo, bassSoloDur) # Agrega las notas y duraciones a la frase
percussionPhrase.addNoteList(percussionSolo, percussionSoloDur) # Agrega las notas y duraciones a la frase

# FRASE
melodyPhrase.addNoteList(melodyPitch, melodyDur) # Agrega las notas y duraciones a la frase
contramelodyPhrase.addNoteList(contramelodyPitch, contramelodyDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonyPitch, harmonyDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassPitch, bassDur) # Agrega las notas y duraciones a la frase
percussionPhrase.addNoteList(percussionPitch, percussionDur) # Agrega las notas y duraciones a la frase

# FINAL
melodyPhrase.addNoteList(melodyEnd, melodyEndDur)
contramelodyPhrase.addNoteList(contramelodyEnd, contramelodyEndDur) # Agrega las notas y duraciones a la frase
harmonyPhrase.addNoteList(harmonyEnd, harmonyEndDur) # Agrega las notas y duraciones a la frase
bassPhrase.addNoteList(bassEnd, bassEndDur) # Agrega las notas y duraciones a la frase
percussionPhrase.addNoteList(percussionEnd, percussionEndDur) # Agrega las notas y duraciones a la frase

# Partes e instrumentos

AccordionPart.addPhrase(melodyPhrase) # Agrega la frase a la parte del instrumento
FlutePart.addPhrase(contramelodyPhrase) # Agrega la frase a la parte del instrumento
PianoPart.addPhrase(harmonyPhrase) # Agrega la frase a la parte del instrumento
BassPart.addPhrase(bassPhrase) # Agrega la frase a la parte del instrumento
PercussionPart.addPhrase(percussionPhrase) # Agrega la frase a la parte del instrumento

originalCompositionBasedOnStorms.addPart(AccordionPart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(FlutePart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(PianoPart) # Agrega la parte del instrumento
originalCompositionBasedOnStorms.addPart(BassPart) # Agrega la parte del instrumento a la partitura
originalCompositionBasedOnStorms.addPart(PercussionPart) # Agrega la parte del instrumento a la partitura

Play.midi(originalCompositionBasedOnStorms) # Reproduce la partitura en formato MIDI

Write.midi(originalCompositionBasedOnStorms, "Original.mid") # Guarda la partitura en un archivo MIDI
