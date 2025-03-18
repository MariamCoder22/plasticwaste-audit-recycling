import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def build_model():
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights=None,
        input_shape=(224, 224, 3)
    )
    x = base_model.output
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(256, activation='relu')(x)
    predictions = tf.keras.layers.Dense(6, activation='softmax')(x)
    return tf.keras.Model(inputs=base_model.input, outputs=predictions)

def train():
    train_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        '/data/plastic_images',
        target_size=(224, 224),
        batch_size=32
    )
    
    model = build_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_generator, epochs=20)
    model.save('/app/vision_model/inference/model.h5')