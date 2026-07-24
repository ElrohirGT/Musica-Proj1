from music import *

introScore = Score("Song of Storms", 200)
# introScore = Score("Song of Storms", 200)

introDrum = Part("Drums", 0, 9)
introFlute = Part(FLUTE, 1)
introMarimba = Part(MARIMBA, 2)
introTrombone = Part(TUBA, 3)

melodyPhrase = Phrase()
chordPhrase = Phrase()
bassPhrase = Phrase()

### Drums
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

melodyPitch = [
   D4, F4, D5,
   D4, F4, D5,

   E5, F5, E5, F5,
   E5, C5, A4,

   A4, D4, F4, G4,
   A4,
   A4, D4, F4, G4,
   E4,

   D4, F4, D5,
   D4, F4, D5,

   E5, F5, E5, F5,
   E5, C5, A4,

   A4, D4, F4, G4,
   A4, A4,
   D4,
]

melodyDur = [
   EN, EN, HN,
   EN, EN, HN,

   DQN, EN, EN, EN,
   EN, EN, HN,

   QN, QN, EN, EN,
   DHN,
   QN, QN, EN, EN,
   DHN,

   EN, EN, HN,
   EN, EN, HN,

   DQN, EN, EN, EN,
   EN, EN, HN,

   QN, QN, EN, EN,
   HN, QN,
   DWN,
]

chordPitch = [
    REST, [F3, A3], [F3, A3], # 1
    REST, [G3, B3],
    REST, [A3, C4], [A3, C4],
    REST, [G3, B3],
] * 3
chordDur = [
    QN, QN, QN,
    QN, HN,
    QN, QN, QN,
    QN, HN
] * 3

bassPitch = [
    D3, REST,
    D3, REST,
    D3, REST,
    D3, REST,
] * 3
bassDur = [
    QN, HN,
    QN, HN,
    QN, HN,
    QN, HN,
] * 3

# print("pitch: ", len(melodyPitch), "dur: ", len(melodyDur))

delta = 12
repeatN = 8

## Drums
bassPitches   = [REST] * delta + [BDR, REST, REST] * repeatN
bassDurations = [QN] * delta + [QN,  QN,   QN] * repeatN
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

snarePitches   = [REST] * delta + [REST, SNR, SNR] * repeatN
snareDurations = [QN] * delta + [QN,   QN,  QN] * repeatN
snareDrumPhrase.addNoteList(snarePitches, snareDurations)

melodyPhrase.addNoteList(melodyPitch, melodyDur)
chordPhrase.addNoteList(chordPitch, chordDur)
bassPhrase.addNoteList(bassPitch, bassDur)

introFlute.addPhrase(melodyPhrase)
introMarimba.addPhrase(chordPhrase)
introTrombone.addPhrase(bassPhrase)

introDrum.addPhrase(bassDrumPhrase)
introDrum.addPhrase(snareDrumPhrase)

introScore.addPart(introFlute)
introScore.addPart(introMarimba)
introScore.addPart(introTrombone)
introScore.addPart(introDrum)

# View.sketch(introScore)
Write.midi(introScore, "P1_Transcripcion_Volawebo.mid")
Play.midi(introScore)