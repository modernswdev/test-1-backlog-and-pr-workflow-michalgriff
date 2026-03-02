# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  # Problem: Attack doesn't reduce Boss HP, so game is infinite
  # Solution: Take damage from b_hp (e.g., b_hp -= 10).
  b_hp -= 10
  print("You deal 10 damage!")

def heal():
  global p_hp
  # Problem: No guardrail parameter. Player can heal above MAX HP and while "dead" (p_hp <= 0).
  # Solution: Don't allow healing if p_hp <= 0, and clamp to MAX_HP (50).
  MAX_HP = 50
  if p_hp <= 0:
    print("You can't heal when you're down!")
    return
  p_hp = min(MAX_HP, p_hp + 20)
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  # Problem: Removed cheat option to eliminate backdoor vulnerability.
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()

  # WIN: When boss reaches 0 HP, declare victory and end loop.
  if b_hp <= 0:
    print("Victory!")
    break

  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
