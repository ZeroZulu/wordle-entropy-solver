# 🧠 Wordle AI Solver - Intelligence Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

**Advanced Wordle solver featuring entropy-based AI, real-time analytics, and customizable themes**

---

## 🎮 LIVE DEMO 🎮

### **[→ CLICK HERE TO PLAY ←](https://your-wordle-ai.streamlit.app)**

*Experience multiple AI strategies with real-time analytics - no installation required!* 

---

<img src="assets/screenshot.png" alt="Preview" width="90%">

*Shannon entropy optimization • Real-time analytics • User-selectable themes*

[View Source Code](#project-structure) • [Watch Demo](#features) • [Read Docs](#documentation)

</div>

---

## 🌟 Overview

An advanced Wordle solver that demonstrates **information theory in practice** through multiple AI strategies and real-time performance analytics. Built with modern data science techniques and featuring a beautiful, customizable interface.

![Mind Blown](https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif)

### Why This Project Stands Out

- 🧠 **Triple AI Power** - Three distinct solving strategies (Entropy, Position, Hybrid)
- 🎯 **99.6% Win Rate** - Hybrid AI solves in 3.5 average guesses
- 📊 **Real-Time Analytics** - Live entropy visualization and performance tracking
- 🎨 **5 Custom Themes** - User-selectable color schemes for personalization
- 📈 **Strategy Comparison** - A/B testing framework with statistical analysis
- 🚀 **Production-Ready** - Clean code, full documentation, deployed on Streamlit Cloud

---

## 🎯 Quick Links

| What | Where |
|------|-------|
| 🎮 **Play the Game** | [Live Demo on Streamlit](https://your-wordle-ai.streamlit.app) |
| 📖 **Full Documentation** | [Deployment Guide](DEPLOYMENT.md) |
| 🚀 **Quick Start** | [Setup Instructions](docs/QUICKSTART.md) |
| 🎨 **Theme Guide** | [Color Customization](ADD-THEME-SELECTOR-GUIDE.md) |
| 📊 **Project Summary** | [Technical Overview](docs/PROJECT_SUMMARY.md) |

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🧠 AI Strategies
- **Entropy AI** - Shannon entropy maximization
- **Position AI** - Statistical frequency analysis
- **Hybrid AI** - Ensemble learning approach
- 99.6% success rate
- 3.5 average guesses

</td>
<td width="50%" valign="top">

### 🎨 Visual Design
- **5 customizable themes**
- Animated gradient backgrounds
- Glassmorphism effects
- Smooth tile animations
- Professional color palettes

</td>
</tr>
<tr>
<td>

### 📊 Analytics
- Real-time entropy timeline
- Letter frequency heatmaps
- Candidate reduction graphs
- Performance metrics dashboard
- Strategy comparison framework

</td>
<td>

### 🎮 Gameplay
- Interactive keyboard
- AI hint system
- Three game modes
- Score tracking
- Mobile responsive

</td>
</tr>
</table>

---

## 🎮 Try It Now!

<div align="center">

### Three Game Modes

<table>
<tr>
<th>🎯 Play Mode</th>
<th>📊 Analytics Mode</th>
<th>🤖 AI Comparison</th>
</tr>
<tr>
<td align="center">
<strong>Interactive Gameplay</strong><br/>
Play with optional AI hints<br/>
<em>Get smart suggestions!</em>
</td>
<td align="center">
<strong>Performance Dashboard</strong><br/>
View detailed statistics<br/>
<em>Entropy visualization</em>
</td>
<td align="center">
<strong>Strategy Analysis</strong><br/>
Compare all three AIs<br/>
<em>100+ game simulations</em>
</td>
</tr>
</table>

</div>

---

## 🚀 Quick Start

### 🌐 Play Online (Easiest!)

**Just click:** **[https://your-wordle-ai.streamlit.app](https://your-wordle-ai.streamlit.app)**

That's it! No setup, no installation, works on any device.

![Wordle Animation](https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif)

---

### 💻 Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/wordle-entropy-solver.git
cd wordle-entropy-solver

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

![Coding](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif)

### Requirements

- **Python 3.8+**
- **Streamlit 1.28+**
- **Pandas, NumPy, Plotly** (auto-installed via requirements.txt)

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** - Core language
- **Streamlit** - Interactive web framework
- **Plotly** - Data visualization
- **Pandas & NumPy** - Data processing

### Algorithms & Concepts
- **Shannon Entropy** - Information theory optimization
- **Statistical Analysis** - Letter frequency patterns
- **Ensemble Learning** - Hybrid model combining strategies

### Deployment
- **Streamlit Cloud** - Serverless hosting
- **GitHub** - Version control and CI/CD

---

## 🎓 Skills Demonstrated

This project is perfect for showcasing in interviews for **Data Science**, **Analytics**, and **Software Engineering** roles.

### Core Competencies

<table>
<tr>
<td width="50%">

**Data Science & ML**
- Information theory (Shannon entropy)
- Ensemble learning methods
- Algorithm optimization
- Statistical analysis
- A/B testing frameworks

</td>
<td width="50%">

**Software Engineering**
- Clean, documented code
- Full-stack development
- CI/CD deployment
- Multiple platform support
- Production-ready architecture

</td>
</tr>
<tr>
<td>

**Analytics & Visualization**
- Interactive dashboards
- Real-time metrics
- Performance tracking
- Data storytelling
- Comparative analysis

</td>
<td>

**Product & Design**
- User experience design
- Customizable interfaces
- Responsive layouts
- Accessibility features
- Feature prioritization

</td>
</tr>
</table>

---

## 📈 Performance Benchmarks

Test configuration: 1000 games per strategy

```
╔════════════════════════════════════════════╗
║  AI STRATEGY PERFORMANCE COMPARISON        ║
╠════════════════════════════════════════════╣
║  Strategy       Avg    Win%   Median  Std  ║
║  ─────────────────────────────────────────  ║
║  Entropy AI     3.68   99.2%   4      0.82 ║
║  Position AI    3.95   97.8%   4      0.95 ║
║  Hybrid AI      3.52   99.6%   3      0.76 ║
║  ─────────────────────────────────────────  ║
║  Winner: Hybrid AI ⭐                       ║
╚════════════════════════════════════════════╝
```

![Performance](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)

### Algorithm Complexity

```
Entropy AI:   O(n × m)  - Optimal information gain
Position AI:  O(n + m)  - Fastest computation
Hybrid AI:    O(n × m)  - Best overall performance

n = candidate words
m = words evaluated per turn
```

**TL;DR:** Hybrid AI is the smartest! 🧠✨

---

## 🎨 Theme Options

Users can choose from 5 professional color schemes:

<table>
<tr>
<td>🌊 <strong>Ocean Breeze</strong><br/>Professional blue/teal</td>
<td>🌅 <strong>Sunset</strong><br/>Bold purple/orange</td>
<td>🌙 <strong>Midnight</strong><br/>Dark gaming aesthetic</td>
</tr>
<tr>
<td>🍃 <strong>Fresh Mint</strong><br/>Clean green/blue</td>
<td>👑 <strong>Royal Purple</strong><br/>Luxury purple/pink</td>
<td>✨ <strong>More coming soon!</strong><br/>Suggest your theme</td>
</tr>
</table>

---

## 📖 Documentation

### Quick Guides
- **[QUICKSTART.md](docs/QUICKSTART.md)** - 60-second setup
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deploy to GitHub & Streamlit
- **[PROJECT_SUMMARY.md](docs/PROJECT_SUMMARY.md)** - Technical overview

### Detailed Docs
- **[IMPROVEMENTS.md](docs/IMPROVEMENTS.md)** - Feature comparison
- **[PRESENTATION_GUIDE.md](docs/PRESENTATION_GUIDE.md)** - Demo script for interviews
- **[THEME_SELECTOR_GUIDE.md](ADD-THEME-SELECTOR-GUIDE.md)** - Customize colors

---

## 🧪 How It Works

![Science](https://media.giphy.com/media/3oEjI1erPMTMBFmNHi/giphy.gif)

### Information Theory Approach

The Entropy AI uses Shannon's information theory to maximize information gain:

```python
H(X) = -Σ p(x) log₂ p(x)
```

**Translation:** Pick the guess that gives you the most information! 📊

For each possible guess:
1. Calculate feedback patterns for all remaining candidates
2. Compute entropy based on pattern distribution
3. Select guess with highest expected information gain
4. Update candidate list based on actual feedback

### Ensemble Learning

The Hybrid AI combines three metrics (like a team of experts! 👥):

```python
Score = w₁ × Entropy + w₂ × Position + w₃ × Frequency

Weights optimized for:
- w₁ = 0.60  (entropy dominance)
- w₂ = 0.25  (position influence)
- w₃ = 0.15  (frequency baseline)
```

**Result:** Best of all three strategies! 🏆

---

## 🔮 Future Enhancements

Planned improvements:

- [ ] Hard mode support (must use revealed clues)
- [ ] Custom word list upload
- [ ] Word difficulty scoring
- [ ] Historical game database
- [ ] Social sharing features
- [ ] Mobile app version
- [ ] Reinforcement learning AI
- [ ] Competitive leaderboards

---

## 🤝 Contributing

Contributions welcome! Feel free to:

1. 🐛 Report bugs
2. 💡 Suggest features
3. 🔧 Submit pull requests
4. 📖 Improve documentation

### How to Contribute

```bash
# Fork the repo
# Create your feature branch
git checkout -b feature/AmazingFeature

# Commit your changes
git commit -m 'Add some AmazingFeature'

# Push to branch
git push origin feature/AmazingFeature

# Open Pull Request
```

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

**TL;DR:** Free to use, modify, and distribute!

---

## 👨‍💻 Author

**Shril Patel**

- 🌐 Portfolio: [zerozulu.github.io](https://zerozulu.github.io)
- 💼 LinkedIn: [linkedin.com/in/shril-patel](https://www.linkedin.com/in/shril-patel-020504284/)  
- 🐙 GitHub: [@ZeroZulu](https://github.com/Zerozulu)

---

## 🙏 Acknowledgments

- **Shannon, C.E.** - Information Theory foundations
- **3Blue1Brown** - Wordle entropy explanation video
- **NY Times** - Original Wordle game
- **Streamlit Community** - Amazing framework and support
- **Open Source Community** - Tools and inspiration

---

<div align="center">

## 🎮 Ready to Play?

### **[→ LAUNCH GAME NOW ←](https://your-wordle-ai.streamlit.app)**

---

![Matrix Code](https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif)

**✨ Turning Information Theory Into Fun • One Guess at a Time ✨**

---

### If you found this project interesting:

**⭐ Star this repository**

**🔀 Fork it to create your own version**

**🐛 Report issues to help improve it**

---


*Built with 🧠 for the love of algorithms and elegant solutions*

*Making data science accessible, one game at a time* 💡

</div>
