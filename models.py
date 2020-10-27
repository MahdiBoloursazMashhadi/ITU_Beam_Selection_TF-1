from tensorflow.keras import layers, models, initializers

Lidar2D = models.Sequential([
    layers.Input(shape=(1, 20, 200)),
    layers.Conv2D(10, 3, 1, padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Conv2D(10, 3, 1, padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Conv2D(10, 3, 2, padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Conv2D(10, 3, 1, padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Conv2D(10, 3, 2, padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Conv2D(10, 3, (1, 2), padding='same', kernel_initializer=initializers.HeUniform, data_format='channels_first'),
    layers.BatchNormalization(axis=1),
    layers.PReLU(),
    layers.Flatten(),
    layers.Dense(256),
    layers.ReLU(),
    layers.Dropout(0.7),
    layers.Dense(256),
    layers.Softmax()
])

LidarMarcus = models.Sequential([
    layers.Input(shape=(10, 20, 200)),
    layers.Conv2D(10, kernel_size=(13, 13),
                   activation='relu',
                   padding="same"),
    layers.Conv2D(30, (11, 11), padding="SAME", activation='relu', data_format='channels_first'),
    layers.Conv2D(25, (9, 9), padding="SAME", activation='relu', data_format='channels_first'),
    layers.MaxPooling2D(pool_size=(2, 1), data_format='channels_first'),
    layers.Dropout(0.3),
    layers.Conv2D(20, (7, 7), padding="SAME", activation='relu', data_format='channels_first'),
    layers.MaxPooling2D(pool_size=(1, 2), data_format='channels_first'),
    layers.Conv2D(15, (5, 5), padding="SAME", activation='relu', data_format='channels_first'),
    layers.Dropout(0.3),
    layers.Conv2D(10, (3, 3), padding="SAME", activation='relu', data_format='channels_first'),
    layers.Conv2D(1, (1, 1), padding="SAME", activation='relu', data_format='channels_first'),
    layers.Flatten(),
    layers.Dense(256, activation='softmax')
])