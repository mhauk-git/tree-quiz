#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌳 Bäume-Quiz 🌳
Ein lustiges Quiz über verschiedene Bäume!
"""

def quiz():
    # Willkommen!
    print("\n" + "="*50)
    print("🌳 WILLKOMMEN ZUM BÄUME-QUIZ! 🌳")
    print("="*50)
    print("Beantworte die Fragen richtig und gewinne Punkte!\n")
    
    # Eingabe für Namen
    name = input("Wie heißt du? ")
    print(f"\nLos geht's, {name}!\n")
    
    punkte = 0
    
    # Frage 1
    print("❓ Frage 1: Welcher Baum hat im Herbst orange-rote Blätter?")
    print("A) Eiche")
    print("B) Ahorn")
    print("C) Birke")
    antwort1 = input("Deine Antwort (A/B/C): ").upper()
    if antwort1 == "B":
        print("✅ Richtig! Der Ahorn hat wunderschöne orange-rote Blätter!\n")
        punkte += 1
    else:
        print("❌ Falsch! Die richtige Antwort ist B) Ahorn.\n")
    
    # Frage 2
    print("❓ Frage 2: Wie heißt die Frucht der Eiche?")
    print("A) Kastanie")
    print("B) Eichel")
    print("C) Zapfen")
    antwort2 = input("Deine Antwort (A/B/C): ").upper()
    if antwort2 == "B":
        print("✅ Richtig! Die Eichel ist die Frucht der Eiche!\n")
        punkte += 1
    else:
        print("❌ Falsch! Die richtige Antwort ist B) Eichel.\n")
    
    # Frage 3
    print("❓ Frage 3: Welcher Baum ist der höchste Baum der Welt?")
    print("A) Douglasie")
    print("B) Fichte")
    print("C) Küstenmammutbaum")
    antwort3 = input("Deine Antwort (A/B/C): ").upper()
    if antwort3 == "C":
        print("✅ Richtig! Der Küstenmammutbaum kann über 110 Meter hoch werden!\n")
        punkte += 1
    else:
        print("❌ Falsch! Die richtige Antwort ist C) Küstenmammutbaum.\n")
    
    # Frage 4
    print("❓ Frage 4: Aus welchem Holz macht man gerne Möbel?")
    print("A) Fichte")
    print("B) Buche")
    print("C) Kiefer")
    antwort4 = input("Deine Antwort (A/B/C): ").upper()
    if antwort4 == "B":
        print("✅ Richtig! Buchenholz ist sehr schön für Möbel!\n")
        punkte += 1
    else:
        print("❌ Falsch! Die richtige Antwort ist B) Buche.\n")
    
    # Frage 5
    print("❓ Frage 5: Welcher Baum verliert im Winter alle Blätter?")
    print("A) Fichte")
    print("B) Lärche")
    print("C) Kiefer")
    antwort5 = input("Deine Antwort (A/B/C): ").upper()
    if antwort5 == "B":
        print("✅ Richtig! Die Lärche ist einer der wenigen Nadelbäume, die ihre Nadeln abwerfen!\n")
        punkte += 1
    else:
        print("❌ Falsch! Die richtige Antwort ist B) Lärche.\n")
    
    # Endergebnis
    print("="*50)
    print(f"🎉 QUIZ VORBEI, {name}! 🎉")
    print("="*50)
    print(f"Du hast {punkte} von 5 Punkten geschafft!")
    
    if punkte == 5:
        print("⭐⭐⭐ SUPER! Du bist ein Bäume-Experte! ⭐⭐⭐")
    elif punkte >= 3:
        print("⭐⭐ Sehr gut! Du kennst dich gut mit Bäumen aus!")
    elif punkte >= 1:
        print("⭐ Gut versucht! Lerne mehr über Bäume!")
    else:
        print("💪 Keine Sorge, beim nächsten Mal besser!")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    quiz()
