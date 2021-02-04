import clases

persona = clases.Persona()
persona.setNombre("Alex")
persona.setApellidos("González")
persona.setAltura(190)
persona.setEdad(23)

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("--------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Alex")
informatico.setApellidos("González")
informatico.setAltura(190)
informatico.setEdad(23)

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"{informatico.programar()} en {informatico.getLenguajes()}")

print("--------------------------------------")

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
print(tecnico.getLenguajes())
