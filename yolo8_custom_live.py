from ultralytics import YOLO

model = YOLO('voiceVoyage_8_best.pt')

results = model(source=0, show=True, conf=0.6, save=True, save_crop=True, project='runs/detect', name='inference', exist_ok=True)
# source=0 laptop cam
# source=1 web cam (external cam)

# results1 = model.predict(source='test_images/bathroom.jpg', show=True, conf=0.6, save=True)
# results2 = model.predict(source='test_images/bathroom_2.jpg', show=True, conf=0.6, save=True)
# results3 = model.predict(source='test_images/bathroom_3.jpg', show=True, conf=0.6, save=True)
# results4 = model.predict(source='test_images/bedroom.jpg', show=True, conf=0.6, save=True)
# results5 = model.predict(source='test_images/bedroom_2.jpeg', show=True, conf=0.6, save=True)
# results6 = model.predict(source='test_images/bedroom_3.jpg', show=True, conf=0.6, save=True)
# results7 = model.predict(source='test_images/closet.jpg', show=True, conf=0.6, save=True)
# results8 = model.predict(source='test_images/kitchen.jpg', show=True, conf=0.6, save=True)
# results9 = model.predict(source='test_images/livingroom.jpg', show=True, conf=0.6, save=True)
# results10 = model.predict(source='test_images/livingroom_2.jpg', show=True, conf=0.6, save=True)
# results11 = model.predict(source='test_images/livingroom_3.jpg', show=True, conf=0.6, save=True)
# results12 = model.predict(source='test_images/livingroom_4.jpg', show=True, conf=0.6, save=True)




