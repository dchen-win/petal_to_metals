# 🌸 Petals to the Metal: Flower Classification  
**Authors:** Cindy Chen & Aiden Gray  
**Mentor:** Tarek Radi  
**Date:** Spring 2025  

---

## 📄 Overview  
This project classifies flowers into 104 categories using convolutional neural networks (CNNs). We deployed models on Intel’s Developer Cloud (CPU), Kaggle (TPU), and local machines. The dataset, provided in binary TFRecord format, includes labeled and unlabeled flower images. We used TensorFlow with Keras to build and evaluate image classification models.

---

## 🎯 Objectives  
- Build accurate image classifier using ResNet50/ResNet50V2  
- Compare performance across CPU vs. TPU platforms  
- Measure performance using accuracy, precision, recall, and F1-score  
- Visualize classification results and confusion matrix  

---

## 🧾 Dataset Description  
- **Training:** 12,753 labeled images (192×192 and 512×512)  
- **Validation:** 3,712 labeled images  
- **Test:** 7,382 unlabeled images  
- **Format:** Binary TFRecord (image + label)  

---

## 🔍 Methodology  

### 1. Data Pipeline & Preprocessing  
- Dynamic distribution strategy for TPU/CPU  
- Image scaling and data augmentation  

### 2. Model Architecture & Training  
- Models: ResNet50 and ResNet50V2 (pretrained on ImageNet)  
- Epochs: 90 | Batch Size: 128 (Kaggle), 16×8 (DevCloud)  
- Callbacks: `EarlyStopping`, `ReduceLROnPlateau`, `LearningRateScheduler`  

### 3. Evaluation Metrics  
- **Intel DevCloud (CPU, ResNet50V2):**  
  - Precision: 0.872 | Recall: 0.836 | F1-score: 0.848  
- **Kaggle (TPU, ResNet50):**  
  - Precision: 0.933 | Recall: 0.931 | F1-score: 0.929  
- **Local (CPU):**  
  - Limited to small images (192x192), slow runtime (~13 min/epoch)  

---

## 📊 Visualizations  
- Batch image predictions (visual validation)  
- Accuracy and loss plots by epoch  
- Confusion matrix heatmaps  

---

## ⚙️ Tools & Platforms  
- **Frameworks:** TensorFlow, Keras  
- **Compute Platforms:** Intel DevCloud (CPU), Kaggle (TPU), Local (CPU)  
- **Callbacks Used:**  
  - `ReduceLROnPlateau`  
  - `EarlyStopping`  
  - `LearningRateScheduler`  

---

## 🚧 Limitations  
- DevCloud: Long training time, potential server interruptions  
- Local: Cannot handle large image sizes (512x512), slow processing  
- Kaggle: Most efficient (TPU), best model performance  

---

## 🌱 Learning Reflections  

**Cindy:**  
Started as a beginner in ML, developed skills by researching, experimenting, and adopting a growth mindset.  

**Aiden:**  
Learned by reading documentation, exploring sample code, iteratively testing, and refining the model.  

---
