import tensorflow as tf

model = tf.keras.models.load_model('dog_cat_final_model.keras')
model.save('dog_cat_final_model.keras', save_format='keras')
print("Done! TF version:", tf.__version__)  