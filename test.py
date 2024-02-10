import avro

# parse some text
text = 'ami amar ami ke cirodin ei banglay khu^je pai'
print(avro.parse(text, bijoy=True))
