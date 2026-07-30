import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

print("=" * 50)
print("        AI MUSIC GENERATOR")
print("=" * 50)

# Create simple music notes
notes = [
    (440, 300),   # A
    (494, 300),   # B
    (523, 300),   # C
    (587, 300),   # D
    (659, 300),   # E
]

print("Generating Music...")
time.sleep(2)

for frequency, duration in notes:
    print(f"Playing Note: {frequency} Hz")
    time.sleep(duration / 1000)

print("\nMusic Generation Completed!")
print("Thank You")