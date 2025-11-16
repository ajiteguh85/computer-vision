# 🚀 Quick Start Guide

Get started with Computer Vision in 3 easy steps!

## Option 1: Google Colab (Recommended for Beginners) ⭐

**No installation needed! Everything runs in your browser.**

1. Click here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ajiteguh85/computer-vision/blob/main/notebooks/complete_colab_workflow.ipynb)

2. Run all cells (Runtime → Run all)

3. Click the generated ngrok link to access your webcam classifier!

**That's it!** ✅

---

## Option 2: Local Setup (For Advanced Users)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Webcam (optional, for real-time detection)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ajiteguh85/computer-vision.git
cd computer-vision
```

### Step 2: Run Setup Script

**On Linux/Mac:**
```bash
./setup.sh
```

**On Windows:**
```batch
setup.bat
```

### Step 3: Train the Model

Open Jupyter Notebook:
```bash
jupyter notebook
```

Navigate to `notebooks/01_train_model.ipynb` and run all cells.

This will:
- Download CIFAR-10 dataset (~170 MB)
- Train a CNN model (~5-10 minutes)
- Save the model to `models/cifar10_model.h5`

### Step 4: Run the Web App

```bash
python app/app.py
```

Open your browser to: `http://localhost:5000`

### Step 5 (Optional): Share Your App with ngrok

In a new terminal:
```bash
ngrok http 5000
```

Share the generated URL with anyone!

---

## 📊 What You'll Build

- **Model**: CNN trained on 60,000 images
- **Accuracy**: ~70% on 10 object classes
- **Real-time**: Live webcam classification
- **Web Interface**: Beautiful, responsive UI
- **Shareable**: Accessible from any device

---

## 🎯 CIFAR-10 Classes

Your model can recognize:
1. ✈️ Airplane
2. 🚗 Automobile
3. 🐦 Bird
4. 🐱 Cat
5. 🦌 Deer
6. 🐕 Dog
7. 🐸 Frog
8. 🐴 Horse
9. 🚢 Ship
10. 🚚 Truck

---

## 💡 Tips for Best Results

### For Training:
- Use GPU runtime in Colab (Runtime → Change runtime type → GPU)
- Train for at least 20 epochs
- Monitor the accuracy graphs

### For Webcam Detection:
- Ensure good lighting
- Show objects clearly to the camera
- Keep objects centered in frame
- Remember: CIFAR-10 images are small (32x32), so accuracy may vary

### For Deployment:
- ngrok free tier has 2-hour session limit
- Restart the app to get a new ngrok URL
- For production, consider Heroku, AWS, or Google Cloud

---

## 🆘 Troubleshooting

### Issue: "Module not found"
**Solution**: Run the setup script or install requirements:
```bash
pip install -r requirements.txt
```

### Issue: "Cannot access webcam"
**Solution**:
- Grant browser permission to access camera
- Check if another app is using the webcam
- Try a different browser (Chrome works best)

### Issue: "Low accuracy"
**Solution**:
- Train for more epochs (try 30-50)
- Add data augmentation
- The model is trained on 32x32 images, so results vary with webcam

### Issue: "ngrok tunnel expired"
**Solution**:
- Restart the Flask app
- Run ngrok again
- Free tier has time limits

### Issue: "Out of memory"
**Solution**:
- In Colab: Use GPU runtime
- Locally: Reduce batch size in training

---

## 📖 Next Steps

1. **Understand the Code**: Read through the notebooks with comments
2. **Experiment**: Change hyperparameters and see what happens
3. **Improve**: Try data augmentation, more layers, different architectures
4. **Share**: Show your friends and family!
5. **Learn More**: Check out the resources in README.md

---

## 🎓 Learning Path

### Beginner
1. Run the complete Colab notebook
2. Understand what each cell does
3. Try changing simple parameters

### Intermediate
1. Modify the model architecture
2. Add data augmentation
3. Try different datasets (MNIST, Fashion-MNIST)

### Advanced
1. Implement transfer learning
2. Add object detection
3. Deploy to cloud platforms
4. Build a mobile app

---

## 🤝 Need Help?

- Check the [README.md](README.md) for detailed documentation
- Open an issue on GitHub
- Review the code comments in notebooks

---

**Happy Learning! 🎉**

Built with ❤️ for Computer Vision beginners
