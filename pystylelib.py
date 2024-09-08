from pystyle import Colors, Colorate, Write, Box
print(Colors.blue + 'Blue text')
print(Colorate.Horizontal(Colors.yellow_to_red, "Gradient text"))

name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Animated text!", Colors.blue_to_green, interval=0.05)

print()
print(Box.Lines("Box1"))
print(Box.DoubleCube("Box2"))
