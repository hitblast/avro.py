from avro import parse, to_bijoy, to_unicode

demo_text = parse("amar sOnar bangla")
print(demo_text)

bijoy = to_bijoy(demo_text)
print(bijoy)

unicode = to_unicode(bijoy)
print(unicode)

if unicode == demo_text:
    print("Success!")
