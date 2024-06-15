from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# Load pre-trained StyleGAN model
model = load_model('stylegan2.h5')

# Generate a random vector
latent_vector = np.random.randn(1, 512)

# Generate image
generated_image = model.predict(latent_vector)

# Display image
plt.imshow((generated_image[0] * 0.5 + 0.5))
plt.show()