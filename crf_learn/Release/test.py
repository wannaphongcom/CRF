from scikitcrf_ner import entityRecognition as ner
ner.train("test.json")
entities = ner.predict("กูเกิลokไหม")
print(entities)
entities = ner.predict("กูเกิลเปิดตัวบริการใหม่")
print(entities)
entities = ner.predict("สวัสดี")
print(entities['entitiesPredicted'])
input()