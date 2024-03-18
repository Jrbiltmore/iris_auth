# Unique ID: 0455d3be-4e19-4f5d-9a63-27521fa2018b
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def create_deep_learning_model(input_shape: tuple, num_classes: int) -> tf.keras.Model:
    """
    Creates a deep learning model for feature extraction from iris images.

    Parameters:
    - input_shape: The shape of the input iris images (height, width, channels).
    - num_classes: The number of output classes (features) for iris recognition.

    Returns:
    - A compiled deep learning model.
    """
    model = Sequential([
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, kernel_size=(3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model

    
