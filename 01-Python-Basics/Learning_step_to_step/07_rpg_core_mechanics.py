char_name = "Archer"
health = 100
is_alive = True
damage = 110
new_health = health - damage

if new_health <= 0:
    is_alive = False
    print("Archer is defeated!")
else:
    print(f"Archer is still standing! Current health: {new_health}")    