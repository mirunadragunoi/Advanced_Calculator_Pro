# 🧮 Advanced Calculator Pro

Professional multi-language calculator application demonstrating comprehensive localization practices.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Languages](https://img.shields.io/badge/Languages-5-orange.svg)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-952-brightgreen.svg)

## 🌟 Overview

Advanced Calculator Pro is a desktop application that showcases professional software localization techniques. Built with Python and Tkinter, it features complete support for 5 languages and requires zero external dependencies.

**Key Highlight:** Unlike typical calculator projects, this implementation demonstrates real-world internationalization (i18n) practices with 200+ professional translations and cultural adaptations.

## ✨ Features

### 🧮 Calculator Functionality
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: Trigonometric (sin, cos, tan), logarithmic (log, ln), powers, roots
- **Mathematical Constants**: π (pi), e (Euler's number)
- **Advanced Operations**: Factorial, reciprocal, absolute value, percentages

### 🌍 Localization
- **5 Languages**: English, Romanian, Spanish, French, German
- **200+ Translations**: Complete UI localization
- **Diacritics Support**: Perfect rendering (ă, ș, ț, á, é, ñ, ü, etc.)
- **Real-time Switching**: Change language without restart
- **Cultural Adaptation**: Context-appropriate translations

### 🔄 Unit Converter
- **Length**: meters, kilometers, miles, feet, inches
- **Weight**: kilograms, grams, pounds, ounces
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Currency**: USD, EUR, RON, GBP, JPY

### 📊 Additional Features
- **Persistent History**: Automatic calculation saving
- **Export Functionality**: TXT and CSV formats
- **Memory Functions**: M+, MR, MC operations
- **Usage Statistics**: Track calculations, conversions, errors
- **Visual Themes**: Light and Dark mode
- **Tabbed Interface**: Organized 4-section UI

## 📸 Screenshots

> *Add your screenshots here after taking them*

<table>
  <tr>
    <td><img src="screenshots/main.png" width="300" alt="Main Interface"/><br/><sub><b>Main Interface</b></sub></td>
    <td><img src="screenshots/scientific.png" width="300" alt="Scientific"/><br/><sub><b>Scientific Calculator</b></sub></td>
  </tr>
  <tr>
    <td><img src="screenshots/converter.png" width="300" alt="Converter"/><br/><sub><b>Unit Converter</b></sub></td>
    <td><img src="screenshots/history.png" width="300" alt="History"/><br/><sub><b>History Tab</b></sub></td>
  </tr>
</table>

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.7 or higher (Tkinter included)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/advanced-calculator-pro.git

# Navigate to project directory
cd advanced-calculator-pro

# Run the application
python calculator_app.py
```

**That's it!** No `pip install` needed. No external dependencies.

## 💻 Usage

### Basic Calculator
```python
# Simple arithmetic
5 + 3 = 8
10 - 4 = 6
7 * 6 = 42
20 / 4 = 5
```

### Scientific Functions
```python
# Trigonometry (angles in radians)
sin(0) = 0
cos(0) = 1
sqrt(16) = 4

# Logarithms
log(10) = 1
ln(e) = 1

# Powers and factorials
5² = 25
5! = 120
```

### Unit Conversion
1. Select conversion type (Length, Weight, Temperature, Currency)
2. Enter value
3. Select source and destination units
4. Click "Convert"

Example:
```
100 cm = 1 m
32°F = 0°C
1 USD = 4.56 RON
```

### Changing Language
Use the **Language** dropdown at the top:
- English
- Română
- Español
- Français
- Deutsch

Interface updates instantly! ⚡

## 🏗️ Project Structure

```
advanced-calculator-pro/
│
├── calculator_app.py          # Main application (952 lines)
│   ├── Class: AdvancedCalculator
│   ├── Methods: 30+ functions
│   └── Features: 25+ capabilities
│
├── locales/                   # Translation files
│   ├── en/translations.json   # English (40+ keys)
│   ├── ro/translations.json   # Romanian (40+ keys)
│   ├── es/translations.json   # Spanish (40+ keys)
│   ├── fr/translations.json   # French (40+ keys)
│   └── de/translations.json   # German (40+ keys)
│
├── calculator_history.json    # Auto-generated - calculation history
├── calculator_stats.json      # Auto-generated - usage statistics
│
├── docs/                      # Documentation
│   ├── LOCALIZATION_REPORT.md # Detailed localization report
│   └── GITHUB_SETUP_GUIDE.md  # This guide
│
└── README.md                  # You are here
```

## 📊 Technical Details

### Statistics
| Metric | Value |
|--------|-------|
| Lines of Code | 952 |
| Functions/Methods | 30+ |
| Supported Languages | 5 |
| Localizable Strings | 40+ |
| Total Translations | 200+ |
| External Dependencies | 0 |
| Python Version | 3.7+ |

### Technology Stack
- **Language**: Python 3.7+
- **GUI Framework**: Tkinter (built-in)
- **Data Format**: JSON
- **Character Encoding**: UTF-8
- **Architecture**: MVC pattern
- **Localization**: i18n best practices

### Why No External Dependencies?
This project intentionally avoids external libraries (matplotlib, numpy, etc.) to:
- ✅ Ensure instant execution on any Python installation
- ✅ Simplify deployment and distribution
- ✅ Demonstrate pure Python capabilities
- ✅ Minimize compatibility issues

## 🌍 Localization Approach

This project demonstrates professional localization through:

### 1. Externalized Strings
All translatable text separated from code in JSON files.

### 2. Complete Coverage
Every UI element is localizable:
- Window titles
- Button labels
- Tab names
- Error messages
- Dialog content
- Tooltips

### 3. Cultural Adaptation
Not just word-for-word translation:
- Number formatting considerations
- Date/time format awareness
- Cultural context in messages
- Appropriate formality levels

### 4. Diacritics Support
Perfect rendering of special characters:
- Romanian: ă, â, î, ș, ț
- Spanish: á, é, í, ó, ú, ñ
- French: à, é, è, ê, ç
- German: ä, ö, ü, ß

### 5. Real-time Switching
Change language instantly without restart - a key UX feature.

## 🔧 Adding New Languages

Want to add more languages? It's easy!

**Step 1:** Create language directory
```bash
mkdir -p locales/it  # For Italian
```

**Step 2:** Copy template
```bash
cp locales/en/translations.json locales/it/translations.json
```

**Step 3:** Translate values
```json
{
    "app_title": "Calcolatrice Avanzata Pro",
    "result_label": "Risultato:",
    ...
}
```

**Step 4:** Update code
```python
# In calculator_app.py, line ~XX
languages = ["en", "ro", "es", "fr", "de", "it"]  # Add "it"

# In language selector
values=["English", "Română", "Español", "Français", "Deutsch", "Italiano"]
```

**Step 5:** Test!
```bash
python calculator_app.py
```

## 🤝 Contributing

Contributions are welcome! Here's how:

### Ways to Contribute
- 🌍 Add new language translations
- 🐛 Report bugs
- ✨ Suggest features
- 📝 Improve documentation
- 🧪 Add tests

### Process
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Translation Guidelines
When contributing translations:
- Use UTF-8 encoding
- Maintain JSON structure (don't change keys)
- Provide context in PR description
- Test with the application
- Follow existing formality level

## 📄 License

This project is created for educational purposes as part of CIVIS BIP 2024-2025 coursework.

**Subject**: Basis and Methods of Localisation, Translation of Computer Products and Video Games

You are free to:
- Use this code for learning
- Fork and modify for your own projects
- Reference in your academic work

Please credit the original project if you use or reference this code.

## 👤 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🎓 Academic Context

This project was developed as the final assignment for:
- **Course**: Basis and Methods of Localisation, Translation of Computer Products and Video Games
- **Program**: CIVIS BIP 2024-2025
- **Professors**: Aranzazu Gil, Irene Atalaya, José Ramón Trujillo
- **Institution**: [Your University]
- **Year**: 2024-2025

### Learning Objectives Met
- ✅ Software internationalization (i18n)
- ✅ Localization (l10n) best practices
- ✅ CAT tools usage (JSON, Python)
- ✅ Multi-language UI design
- ✅ Cultural adaptation
- ✅ Translation management
- ✅ Character encoding handling

## 🙏 Acknowledgments

- **Course Professors** for guidance on localization best practices
- **CIVIS BIP Program** for the international learning opportunity
- **Python Community** for excellent documentation
- **Tkinter** for the robust GUI framework
- **Open Source Community** for inspiration

## 📚 Related Resources

### Localization
- [Python i18n and l10n](https://docs.python.org/3/library/i18n.html)
- [Unicode Standard](https://unicode.org/)
- [GNU gettext](https://www.gnu.org/software/gettext/)

### Python & Tkinter
- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [Real Python Tkinter](https://realpython.com/python-gui-tkinter/)

## 📈 Project Evolution

### Version 1.0 (Current)
- ✅ Basic and scientific calculator
- ✅ 5 language support
- ✅ Unit converter
- ✅ History and statistics
- ✅ Theme support

### Potential Future Enhancements
- [ ] More languages (Italian, Portuguese, etc.)
- [ ] Graphing calculator features
- [ ] Mobile app version
- [ ] Web version (using Flask/Django)
- [ ] Advanced unit conversions
- [ ] Equation solver
- [ ] Plugins system

## 🐛 Known Issues

Currently no known issues. If you find a bug:
1. Check if it's already reported in [Issues](https://github.com/yourusername/advanced-calculator-pro/issues)
2. If not, create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Your environment (OS, Python version)

## ❓ FAQ

**Q: Why use Tkinter instead of modern frameworks?**  
A: Tkinter is cross-platform, comes with Python, and requires no installation. Perfect for demonstrating localization without dependency hassles.

**Q: Can I use this code in my own project?**  
A: Yes! It's educational code. Just credit the original project.

**Q: How do I add more scientific functions?**  
A: Edit `calculator_app.py`, add buttons in `setup_scientific_calculator()`, and implement the function logic.

**Q: Can this be converted to a mobile app?**  
A: The logic can be reused, but the UI would need to be rebuilt with a mobile framework (Kivy, React Native, etc.).

**Q: How accurate are the currency conversions?**  
A: Current rates are fixed for demonstration. In production, you'd fetch real-time rates from an API.

## 📞 Support

Need help?

1. **Documentation**: Check [docs/](docs/) folder
2. **Issues**: Open an issue on GitHub
3. **Email**: your.email@example.com
4. **LinkedIn**: Message me on [LinkedIn](https://linkedin.com/in/yourprofile)

## ⭐ Show Your Support

If you find this project helpful or interesting:
- ⭐ Star this repository
- 🍴 Fork it for your own use
- 📣 Share it with others
- 💬 Provide feedback

## 📜 Changelog

### Version 1.0.0 (November 2024)
- Initial release
- 5 language support
- Scientific calculator
- Unit converter
- History and statistics
- Theme support
- 952 lines of code
- 200+ translations

---

<div align="center">

**Advanced Calculator Pro** © 2024

Made with ❤️ and Python

[Report Bug](https://github.com/yourusername/advanced-calculator-pro/issues) · 
[Request Feature](https://github.com/yourusername/advanced-calculator-pro/issues) · 
[View Demo](#) · 
[Documentation](docs/)

</div>
