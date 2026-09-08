import random

# Lista enorme de frases bonitas 💖
frases = [
    "🌟 Hoy es un día perfecto para empezar algo nuevo.",
    "💚 Cree en ti, tienes todo lo necesario para brillar.",
    "🌍 El cambio empieza por ti, ¡hazlo con amor!",
    "💪 Los retos hacen la vida más interesante. ¡Tú puedes!",
    "☀️ Sé la luz que ilumina el camino de otros.",
    "🌱 Pequeños pasos, grandes cambios. ¡Nunca te rindas!",
    "💛 La bondad es el lenguaje que todos entienden.",
    "🌈 Después de la tormenta siempre sale el sol.",
    "🚀 Tu potencial es infinito, ¡solo atrévete a descubrirlo!",
    "🤝 Juntos somos más fuertes. ¡Ayuda a quien puedas!",
    "💙 Cuida tu mente, ama tu vida, cuida nuestro planeta.",
    "🔥 Tu esfuerzo de hoy es tu éxito de mañana.",
    "🌸 Sé como la flor: hermosa y fuerte ante cualquier viento.",
    "⚡ La esperanza es como el sol: siempre brilla.",
    "🏆 No importa cuántas veces caigas, levántate y sigue."
]

# Mensajes para enviar a alguien 💌
mensajes = [
    "¡Que tengas un día maravilloso! 💖",
    "Te mando un abrazo lleno de energía positiva! 🤗✨",
    "Sonríe, el mundo te necesita feliz! 😊🌈",
    "¡Gracias por existir y hacer el mundo mejor! 💚🌍",
    "Que la alegría llene tu corazón hoy y siempre! 💛☀️",
    "Eres más especial de lo que crees. ¡Nunca lo olvides! 🌟",
    "¡Todo saldrá bien! Confía y sigue adelante. 💪✨"
]

print("\n" + "="*55)
print("    ✨  MENSAJES QUE ILUMINAN EL MUNDO  ✨")
print("="*55)
print("  🌟 Frase inspiradora del día")
print("  💌 Enviar un mensaje bonito a alguien")
print("  🎲 ¡Sorpréndeme! (Te doy algo especial)")
print("  👋 Salir")
print("="*55)

while True:
    opcion = input("\n🎯 Elige una opción (1-4): ")

    if opcion == "4":
        print("\n" + "="*55)
        print("  💖 ¡Gracias por usar este programa! 💖")
        print("  🌍 Que llenes el mundo de luz y alegría 🌍")
        print("="*55)
        break

    elif opcion == "1":
        frase = random.choice(frases)
        print("\n" + "~"*50)
        print(f"  ✨ {frase}")
        print("~"*50)

    elif opcion == "2":
        nombre = input("  ✍️ ¿A quién quieres dedicárselo? ")
        msg = random.choice(mensajes)
        print("\n" + "💌"*25)
        print(f"  Para: {nombre} 💝")
        print(f"  {msg}")
        print("💌"*25)

    elif opcion == "3":
        print("\n" + "🎁"*20)
        print("  🎉 ¡SORPRESA! 🎉")
        f1 = random.choice(frases)
        f2 = random.choice(mensajes)
        print(f"  {f1}")
        print(f"  💫 {f2}")
        print("  🌍 ¡El mundo es mejor porque tú estás en él! 💚")
        print("🎁"*20)

    else:
        print("⚠️ Opción no válida, intenta de nuevo")
