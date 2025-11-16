# 🎥 Beginner Computer Vision: Real-Time Image Classification

A complete beginner-friendly Computer Vision project for real-time image classification using webcam. This project demonstrates end-to-end deep learning workflow from training to deployment.

## 📚 What You'll Learn

- Train a Convolutional Neural Network (CNN) on CIFAR-10 dataset
- Build a real-time webcam classifier
- Deploy a web interface using Flask and ngrok
- Run everything in Google Colab (no local setup needed!)

## 🎯 Project Features

- **Dataset**: CIFAR-10 (60,000 images across 10 classes)
- **Classes**: Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck
- **Model**: Custom CNN built with TensorFlow/Keras
- **Real-time Detection**: Live webcam classification via web browser
- **Deployment**: Flask web app with ngrok tunneling

## 🚀 Quick Start (Google Colab)

The easiest way to get started is using Google Colab:

1. Open `notebooks/complete_colab_workflow.ipynb` in Google Colab
2. Run all cells
3. Click the ngrok link to access your webcam classifier!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ajiteguh85/computer-vision/blob/main/notebooks/complete_colab_workflow.ipynb)

## 📂 Project Structure

```
computer-vision/
├── notebooks/
│   ├── 01_train_model.ipynb          # Train CIFAR-10 classifier
│   └── complete_colab_workflow.ipynb  # All-in-one Colab notebook
├── app/
│   ├── app.py                         # Flask web application
│   ├── templates/
│   │   └── index.html                 # Web interface
│   └── static/
│       └── style.css                  # Styling
├── models/
│   └── cifar10_model.h5               # Saved trained model
├── requirements.txt                    # Python dependencies
└── README.md                          # This file
```

## 🔧 Local Setup (Optional)

If you want to run locally instead of Colab:

### 1. Clone the repository
```bash
git clone https://github.com/ajiteguh85/computer-vision.git
cd computer-vision
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
```bash
jupyter notebook notebooks/01_train_model.ipynb
```

### 4. Run the web app
```bash
python app/app.py
```

### 5. Access via ngrok (optional)
```bash
ngrok http 5000
```

## 🧠 Understanding the Code

### Model Architecture
- **Input Layer**: 32x32x3 RGB images
- **Convolutional Layers**: Extract features from images
- **Pooling Layers**: Reduce dimensions
- **Dense Layers**: Classification
- **Output**: 10 classes with softmax activation

### Training Process
1. Load CIFAR-10 dataset
2. Normalize pixel values (0-1 range)
3. Build CNN architecture
4. Train for ~20 epochs
5. Save model weights

### Real-Time Classification
1. Capture webcam frame
2. Resize to 32x32 pixels
3. Normalize pixel values
4. Predict class using trained model
5. Display result with confidence score

## 📊 CIFAR-10 Dataset

- **Training Images**: 50,000
- **Test Images**: 10,000
- **Image Size**: 32x32 pixels (RGB)
- **Classes**: 10 everyday objects

## 🎓 Learning Resources

### For Absolute Beginners
1. Start with `notebooks/complete_colab_workflow.ipynb` - it has detailed comments
2. Read through each code cell and understand what it does
3. Experiment by changing parameters (learning rate, epochs, etc.)

### Next Steps
- Try different datasets (MNIST, Fashion-MNIST)
- Improve model accuracy by adding more layers
- Add data augmentation
- Try transfer learning with pre-trained models

## 🛠️ Technologies Used

- **Python 3.8+**
- **TensorFlow 2.x** - Deep learning framework
- **Keras** - High-level neural network API
- **OpenCV** - Computer vision library
- **Flask** - Web framework
- **ngrok** - Secure tunneling

## 📝 Common Issues & Solutions

### Issue: Low accuracy
**Solution**: Train for more epochs or use data augmentation

### Issue: Webcam not detected
**Solution**: Grant browser permission to access camera

### Issue: ngrok tunnel expired
**Solution**: Restart the Flask app (ngrok tunnels expire after 2 hours on free tier)

### Issue: Out of memory in Colab
**Solution**: Use GPU runtime (Runtime → Change runtime type → GPU)

## 🤝 Contributing

Feel free to fork this project and improve it! Some ideas:
- Add more datasets
- Improve UI/UX
- Add object detection capabilities
- Create mobile app version

## 📄 License

MIT License - feel free to use this for learning!

## 🙏 Acknowledgments

- CIFAR-10 dataset by Alex Krizhevsky
- TensorFlow and Keras teams
- Flask framework
- ngrok for easy tunneling

## 📧 Questions?

If you have questions or run into issues:
1. Check the code comments in the notebooks
2. Review the Common Issues section above
3. Open an issue on GitHub

---

**Happy Learning! 🎉**

Built with ❤️ for beginners in Computer Vision
