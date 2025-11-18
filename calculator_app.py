#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Calculator Application with Localization Support
Professional calculator demonstrating comprehensive localization features
WITHOUT external dependencies (no matplotlib/numpy required!)
"""

import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext, filedialog
import json
import os
import math
import datetime
import csv
from typing import Dict, List


class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.current_language = "en"
        self.translations = {}
        self.current_theme = "light"
        self.history = []
        self.memory = 0
        self.statistics = {'calculations': 0, 'conversions': 0, 'errors': 0}

        # Calculator state
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Conversion rates (example data)
        self.conversion_rates = {
            'length': {
                'm': 1, 'km': 0.001, 'cm': 100, 'mm': 1000,
                'mi': 0.000621371, 'ft': 3.28084, 'in': 39.3701
            },
            'weight': {
                'kg': 1, 'g': 1000, 'mg': 1000000,
                'lb': 2.20462, 'oz': 35.274
            },
            'temperature': {
                'C': 'base',
                'F': lambda c: c * 9 / 5 + 32,
                'K': lambda c: c + 273.15
            },
            'currency': {
                'USD': 1, 'EUR': 0.92, 'RON': 4.56,
                'GBP': 0.79, 'JPY': 149.50
            }
        }

        self.load_translations()
        self.load_history()
        self.load_statistics()
        self.setup_ui()
        self.apply_theme()
        self.apply_localization()

    def load_translations(self):
        """Load translation files for all supported languages"""
        default_translations = {
            "en": {
                "app_title": "Advanced Calculator Pro",
                "result_label": "Result:",
                "history_label": "History:",
                "clear_button": "Clear",
                "clear_history": "Clear History",
                "language_label": "Language:",
                "theme_label": "Theme:",
                "about_menu": "About",
                "about_title": "About Calculator",
                "about_message": "Advanced Calculator Pro v2.0\n\nFeatures:\n• Scientific calculations\n• Unit conversions\n• History tracking\n• 5-language support\n• Theme customization\n• Statistics\n\nCreated for: CIVIS BIP 2024-2025",
                "error_title": "Error",
                "error_message": "Invalid expression. Please try again.",
                "memory_store": "Memory+",
                "memory_recall": "Recall",
                "memory_clear": "Clear Mem",
                "export_button": "Export",
                "stats_button": "Statistics",
                "basic_tab": "Basic",
                "scientific_tab": "Scientific",
                "converter_tab": "Converter",
                "history_tab": "History",
                "light_theme": "Light",
                "dark_theme": "Dark",
                "length_label": "Length",
                "weight_label": "Weight",
                "temperature_label": "Temperature",
                "currency_label": "Currency",
                "from_label": "From:",
                "to_label": "To:",
                "convert_label": "Convert",
                "value_label": "Value:",
                "export_success": "Results exported successfully!",
                "export_error": "Error exporting results.",
                "stats_title": "Usage Statistics",
                "stats_calculations": "Calculations:",
                "stats_conversions": "Conversions:",
                "stats_errors": "Errors:",
                "close_button": "Close"
            },
            "ro": {
                "app_title": "Calculator Avansat Pro",
                "result_label": "Rezultat:",
                "history_label": "Istoric:",
                "clear_button": "Șterge",
                "clear_history": "Șterge Istoric",
                "language_label": "Limba:",
                "theme_label": "Temă:",
                "about_menu": "Despre",
                "about_title": "Despre Calculator",
                "about_message": "Calculator Avansat Pro v2.0\n\nFuncționalități:\n• Calcule științifice\n• Conversii unități\n• Istoric calcule\n• Suport 5 limbi\n• Personalizare temă\n• Statistici\n\nCreat pentru: CIVIS BIP 2024-2025",
                "error_title": "Eroare",
                "error_message": "Expresie invalidă. Vă rugăm încercați din nou.",
                "memory_store": "Memorie+",
                "memory_recall": "Recuperează",
                "memory_clear": "Șterge Mem",
                "export_button": "Exportă",
                "stats_button": "Statistici",
                "basic_tab": "Bază",
                "scientific_tab": "Științific",
                "converter_tab": "Convertor",
                "history_tab": "Istoric",
                "light_theme": "Luminos",
                "dark_theme": "Întunecat",
                "length_label": "Lungime",
                "weight_label": "Greutate",
                "temperature_label": "Temperatură",
                "currency_label": "Valută",
                "from_label": "Din:",
                "to_label": "În:",
                "convert_label": "Convertește",
                "value_label": "Valoare:",
                "export_success": "Rezultate exportate cu succes!",
                "export_error": "Eroare la exportare.",
                "stats_title": "Statistici Utilizare",
                "stats_calculations": "Calcule:",
                "stats_conversions": "Conversii:",
                "stats_errors": "Erori:",
                "close_button": "Închide"
            },
            "es": {
                "app_title": "Calculadora Avanzada Pro",
                "result_label": "Resultado:",
                "history_label": "Historial:",
                "clear_button": "Borrar",
                "clear_history": "Borrar Historial",
                "language_label": "Idioma:",
                "theme_label": "Tema:",
                "about_menu": "Acerca de",
                "about_title": "Acerca de la Calculadora",
                "about_message": "Calculadora Avanzada Pro v2.0\n\nCaracterísticas:\n• Cálculos científicos\n• Conversiones\n• Historial\n• 5 idiomas\n• Temas personalizados\n• Estadísticas\n\nCreado para: CIVIS BIP 2024-2025",
                "error_title": "Error",
                "error_message": "Expresión inválida. Inténtelo de nuevo.",
                "memory_store": "Memoria+",
                "memory_recall": "Recuperar",
                "memory_clear": "Borrar Mem",
                "export_button": "Exportar",
                "stats_button": "Estadísticas",
                "basic_tab": "Básico",
                "scientific_tab": "Científico",
                "converter_tab": "Conversor",
                "history_tab": "Historial",
                "light_theme": "Claro",
                "dark_theme": "Oscuro",
                "length_label": "Longitud",
                "weight_label": "Peso",
                "temperature_label": "Temperatura",
                "currency_label": "Moneda",
                "from_label": "De:",
                "to_label": "A:",
                "convert_label": "Convertir",
                "value_label": "Valor:",
                "export_success": "¡Resultados exportados!",
                "export_error": "Error al exportar.",
                "stats_title": "Estadísticas de Uso",
                "stats_calculations": "Cálculos:",
                "stats_conversions": "Conversiones:",
                "stats_errors": "Errores:",
                "close_button": "Cerrar"
            },
            "fr": {
                "app_title": "Calculatrice Avancée Pro",
                "result_label": "Résultat:",
                "history_label": "Historique:",
                "clear_button": "Effacer",
                "clear_history": "Effacer Historique",
                "language_label": "Langue:",
                "theme_label": "Thème:",
                "about_menu": "À propos",
                "about_title": "À propos",
                "about_message": "Calculatrice Avancée Pro v2.0\n\nFonctionnalités:\n• Calculs scientifiques\n• Conversions\n• Historique\n• 5 langues\n• Thèmes\n• Statistiques\n\nCréé pour: CIVIS BIP 2024-2025",
                "error_title": "Erreur",
                "error_message": "Expression invalide. Réessayez.",
                "memory_store": "Mémoire+",
                "memory_recall": "Rappeler",
                "memory_clear": "Effacer Mém",
                "export_button": "Exporter",
                "stats_button": "Statistiques",
                "basic_tab": "Base",
                "scientific_tab": "Scientifique",
                "converter_tab": "Convertisseur",
                "history_tab": "Historique",
                "light_theme": "Clair",
                "dark_theme": "Sombre",
                "length_label": "Longueur",
                "weight_label": "Poids",
                "temperature_label": "Température",
                "currency_label": "Devise",
                "from_label": "De:",
                "to_label": "À:",
                "convert_label": "Convertir",
                "value_label": "Valeur:",
                "export_success": "Résultats exportés!",
                "export_error": "Erreur d'exportation.",
                "stats_title": "Statistiques",
                "stats_calculations": "Calculs:",
                "stats_conversions": "Conversions:",
                "stats_errors": "Erreurs:",
                "close_button": "Fermer"
            },
            "de": {
                "app_title": "Erweiterter Rechner Pro",
                "result_label": "Ergebnis:",
                "history_label": "Verlauf:",
                "clear_button": "Löschen",
                "clear_history": "Verlauf Löschen",
                "language_label": "Sprache:",
                "theme_label": "Thema:",
                "about_menu": "Über",
                "about_title": "Über",
                "about_message": "Erweiterter Rechner Pro v2.0\n\nFunktionen:\n• Wissenschaftliche Berechnungen\n• Umrechnungen\n• Verlauf\n• 5 Sprachen\n• Themen\n• Statistiken\n\nErstellt für: CIVIS BIP 2024-2025",
                "error_title": "Fehler",
                "error_message": "Ungültiger Ausdruck. Bitte erneut versuchen.",
                "memory_store": "Speicher+",
                "memory_recall": "Abrufen",
                "memory_clear": "Speicher Löschen",
                "export_button": "Exportieren",
                "stats_button": "Statistiken",
                "basic_tab": "Basis",
                "scientific_tab": "Wissenschaftlich",
                "converter_tab": "Umrechner",
                "history_tab": "Verlauf",
                "light_theme": "Hell",
                "dark_theme": "Dunkel",
                "length_label": "Länge",
                "weight_label": "Gewicht",
                "temperature_label": "Temperatur",
                "currency_label": "Währung",
                "from_label": "Von:",
                "to_label": "Nach:",
                "convert_label": "Umrechnen",
                "value_label": "Wert:",
                "export_success": "Erfolgreich exportiert!",
                "export_error": "Exportfehler.",
                "stats_title": "Statistiken",
                "stats_calculations": "Berechnungen:",
                "stats_conversions": "Umrechnungen:",
                "stats_errors": "Fehler:",
                "close_button": "Schließen"
            }
        }

        languages = ["en", "ro", "es", "fr", "de"]
        for lang in languages:
            file_path = f"locales/{lang}/translations.json"
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        loaded_trans = json.load(f)
                        # Merge with defaults to ensure all keys exist
                        self.translations[lang] = {**default_translations[lang], **loaded_trans}
                except Exception as e:
                    print(f"Error loading {lang}: {e}")
                    self.translations[lang] = default_translations[lang]
            else:
                print(f"Creating translation file: {file_path}")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                self.translations[lang] = default_translations[lang]
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(default_translations[lang], f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(f"Warning: Could not create {file_path}: {e}")

    def load_history(self):
        """Load calculation history from file"""
        if os.path.exists('calculator_history.json'):
            try:
                with open('calculator_history.json', 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
            except:
                self.history = []

    def save_history(self):
        """Save calculation history to file"""
        try:
            with open('calculator_history.json', 'w', encoding='utf-8') as f:
                json.dump(self.history[-100:], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_statistics(self):
        """Load usage statistics"""
        if os.path.exists('calculator_stats.json'):
            try:
                with open('calculator_stats.json', 'r', encoding='utf-8') as f:
                    self.statistics = json.load(f)
            except:
                self.statistics = {'calculations': 0, 'conversions': 0, 'errors': 0}

    def save_statistics(self):
        """Save usage statistics"""
        try:
            with open('calculator_stats.json', 'w', encoding='utf-8') as f:
                json.dump(self.statistics, f, indent=2)
        except Exception as e:
            print(f"Error saving statistics: {e}")

    def setup_ui(self):
        """Create the comprehensive user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)

        # Top control bar
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Language selector
        self.lang_label = ttk.Label(control_frame, text="Language:")
        self.lang_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))

        self.lang_combo = ttk.Combobox(control_frame,
                                       values=["English", "Română", "Español", "Français", "Deutsch"],
                                       state="readonly", width=12)
        self.lang_combo.set("English")
        self.lang_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 15))
        self.lang_combo.bind("<<ComboboxSelected>>", self.change_language)

        # Theme selector
        self.theme_label = ttk.Label(control_frame, text="Theme:")
        self.theme_label.grid(row=0, column=2, sticky=tk.W, padx=(0, 5))

        self.theme_combo = ttk.Combobox(control_frame,
                                        values=["Light", "Dark"],
                                        state="readonly", width=10)
        self.theme_combo.set("Light")
        self.theme_combo.grid(row=0, column=3, sticky=tk.W, padx=(0, 15))
        self.theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        # Stats and About buttons
        self.stats_btn = ttk.Button(control_frame, text="Statistics",
                                    command=self.show_statistics, width=10)
        self.stats_btn.grid(row=0, column=4, sticky=tk.W, padx=(0, 5))

        self.about_btn = ttk.Button(control_frame, text="About",
                                    command=self.show_about, width=10)
        self.about_btn.grid(row=0, column=5, sticky=tk.W)

        # Display frame
        display_frame = ttk.LabelFrame(main_frame, text="", padding="10")
        display_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        self.result_label = ttk.Label(display_frame, text="Result:")
        self.result_label.grid(row=0, column=0, sticky=tk.W)

        self.result_display = ttk.Entry(display_frame, textvariable=self.result_var,
                                        font=('Arial', 18), justify='right',
                                        state='readonly', width=30)
        self.result_display.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        display_frame.columnconfigure(0, weight=1)

        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        # Tab 1: Basic Calculator
        self.basic_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.basic_frame, text="Basic")
        self.setup_basic_calculator()

        # Tab 2: Scientific Calculator
        self.scientific_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.scientific_frame, text="Scientific")
        self.setup_scientific_calculator()

        # Tab 3: Unit Converter
        self.converter_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.converter_frame, text="Converter")
        self.setup_converter()

        # Tab 4: History
        self.history_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.history_frame, text="History")
        self.setup_history()

    def setup_basic_calculator(self):
        """Setup basic calculator buttons"""
        buttons = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '←'],
            ['1', '2', '3', '-', 'M+'],
            ['0', '.', '=', '+', 'MR']
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '=':
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=lambda: self.calculate())
                elif btn_text == 'C':
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=self.clear_input)
                elif btn_text == '←':
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=self.backspace)
                elif btn_text == 'M+':
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=self.memory_store)
                elif btn_text == 'MR':
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=self.memory_recall)
                else:
                    btn = ttk.Button(self.basic_frame, text=btn_text, width=8,
                                     command=lambda x=btn_text: self.button_click(x))
                btn.grid(row=i, column=j, padx=3, pady=3, sticky=(tk.W, tk.E))
                self.basic_frame.columnconfigure(j, weight=1)

    def setup_scientific_calculator(self):
        """Setup scientific calculator buttons"""
        sci_buttons = [
            ['sin', 'cos', 'tan', 'π', 'e'],
            ['asin', 'acos', 'atan', 'log', 'ln'],
            ['x²', 'x³', '√', '(', ')'],
            ['1/x', 'n!', '%', 'abs', 'MC']
        ]

        button_functions = {
            'sin': lambda: self.button_click('sin('),
            'cos': lambda: self.button_click('cos('),
            'tan': lambda: self.button_click('tan('),
            'asin': lambda: self.button_click('asin('),
            'acos': lambda: self.button_click('acos('),
            'atan': lambda: self.button_click('atan('),
            'log': lambda: self.button_click('log10('),
            'ln': lambda: self.button_click('log('),
            'x²': lambda: self.button_click('**2'),
            'x³': lambda: self.button_click('**3'),
            '√': lambda: self.button_click('sqrt('),
            'π': lambda: self.button_click(str(math.pi)),
            'e': lambda: self.button_click(str(math.e)),
            'n!': self.factorial_input,
            '%': lambda: self.button_click('/100'),
            '1/x': self.reciprocal,
            'abs': lambda: self.button_click('abs('),
            'MC': self.memory_clear
        }

        for i, row in enumerate(sci_buttons):
            for j, btn_text in enumerate(row):
                cmd = button_functions.get(btn_text, lambda x=btn_text: self.button_click(x))
                btn = ttk.Button(self.scientific_frame, text=btn_text, width=8, command=cmd)
                btn.grid(row=i, column=j, padx=3, pady=3, sticky=(tk.W, tk.E))
                self.scientific_frame.columnconfigure(j, weight=1)

    def setup_converter(self):
        """Setup unit converter"""
        # Converter type selection
        type_frame = ttk.Frame(self.converter_frame)
        type_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(type_frame, text="Conversion Type:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))

        self.conv_type = ttk.Combobox(type_frame,
                                      values=["Length", "Weight", "Temperature", "Currency"],
                                      state="readonly", width=15)
        self.conv_type.set("Length")
        self.conv_type.grid(row=0, column=1, sticky=tk.W)
        self.conv_type.bind("<<ComboboxSelected>>", self.update_converter_units)

        # Value input
        input_frame = ttk.Frame(self.converter_frame)
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        self.value_label = ttk.Label(input_frame, text="Value:")
        self.value_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))

        self.conv_value = ttk.Entry(input_frame, width=20)
        self.conv_value.grid(row=0, column=1, sticky=(tk.W, tk.E))
        input_frame.columnconfigure(1, weight=1)

        # From unit
        from_frame = ttk.Frame(self.converter_frame)
        from_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        self.from_label = ttk.Label(from_frame, text="From:")
        self.from_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))

        self.from_unit = ttk.Combobox(from_frame, state="readonly", width=15)
        self.from_unit.grid(row=0, column=1, sticky=(tk.W, tk.E))
        from_frame.columnconfigure(1, weight=1)

        # To unit
        to_frame = ttk.Frame(self.converter_frame)
        to_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        self.to_label = ttk.Label(to_frame, text="To:")
        self.to_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))

        self.to_unit = ttk.Combobox(to_frame, state="readonly", width=15)
        self.to_unit.grid(row=0, column=1, sticky=(tk.W, tk.E))
        to_frame.columnconfigure(1, weight=1)

        # Convert button
        self.convert_btn = ttk.Button(self.converter_frame, text="Convert",
                                      command=self.perform_conversion)
        self.convert_btn.grid(row=4, column=0, columnspan=2, pady=15)

        # Result
        self.conv_result = ttk.Label(self.converter_frame, text="",
                                     font=('Arial', 12, 'bold'), foreground='#0066cc')
        self.conv_result.grid(row=5, column=0, columnspan=2, pady=10)

        self.update_converter_units()

    def setup_history(self):
        """Setup history display tab"""
        # History text area
        history_label_frame = ttk.LabelFrame(self.history_frame, text="", padding="10")
        history_label_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        self.history_frame.rowconfigure(0, weight=1)
        self.history_frame.columnconfigure(0, weight=1)

        self.history_text = scrolledtext.ScrolledText(history_label_frame,
                                                      height=15, width=50,
                                                      font=('Courier', 9))
        self.history_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        history_label_frame.rowconfigure(0, weight=1)
        history_label_frame.columnconfigure(0, weight=1)

        # Buttons frame
        button_frame = ttk.Frame(self.history_frame)
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.clear_history_btn = ttk.Button(button_frame, text="Clear History",
                                            command=self.clear_history, width=15)
        self.clear_history_btn.grid(row=0, column=0, padx=5)

        self.export_btn = ttk.Button(button_frame, text="Export Results",
                                     command=self.export_results, width=15)
        self.export_btn.grid(row=0, column=1, padx=5)

        self.update_history_display()

    def button_click(self, value):
        """Handle button clicks"""
        if value == '=':
            self.calculate()
        else:
            self.current_input += str(value)
            self.result_var.set(self.current_input)

    def calculate(self):
        """Perform calculation"""
        try:
            expr = self.current_input.replace('×', '*').replace('÷', '/')

            # Safe namespace for eval
            safe_dict = {
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                'log': math.log, 'log10': math.log10,
                'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e,
                'pow': pow, 'abs': abs
            }

            result = eval(expr, {"__builtins__": {}}, safe_dict)
            self.result_var.set(str(result))

            # Add to history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                'expression': self.current_input,
                'result': str(result),
                'timestamp': timestamp,
                'type': 'calculation'
            })
            self.save_history()
            self.update_history_display()

            # Update statistics
            self.statistics['calculations'] += 1
            self.save_statistics()

            self.current_input = str(result)
        except Exception as e:
            self.statistics['errors'] += 1
            self.save_statistics()
            self.show_error()
            self.current_input = ""
            self.result_var.set("0")

    def clear_input(self):
        """Clear current input"""
        self.current_input = ""
        self.result_var.set("0")

    def backspace(self):
        """Remove last character"""
        self.current_input = self.current_input[:-1]
        self.result_var.set(self.current_input if self.current_input else "0")

    def factorial_input(self):
        """Calculate factorial"""
        try:
            num = int(float(self.current_input))
            if num < 0:
                raise ValueError("Negative number")
            result = math.factorial(num)
            self.result_var.set(str(result))
            self.current_input = str(result)

            # Add to history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                'expression': f'{num}!',
                'result': str(result),
                'timestamp': timestamp,
                'type': 'calculation'
            })
            self.save_history()
            self.update_history_display()
            self.statistics['calculations'] += 1
            self.save_statistics()
        except Exception:
            self.statistics['errors'] += 1
            self.save_statistics()
            self.show_error()

    def reciprocal(self):
        """Calculate reciprocal"""
        try:
            num = float(self.current_input)
            result = 1 / num
            self.result_var.set(str(result))
            self.current_input = str(result)

            # Add to history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                'expression': f'1/{num}',
                'result': str(result),
                'timestamp': timestamp,
                'type': 'calculation'
            })
            self.save_history()
            self.update_history_display()
            self.statistics['calculations'] += 1
            self.save_statistics()
        except Exception:
            self.statistics['errors'] += 1
            self.save_statistics()
            self.show_error()

    def memory_store(self):
        """Store current value in memory"""
        try:
            self.memory = float(self.result_var.get())
            trans = self.translations[self.current_language]
            messagebox.showinfo("Memory", f"{trans.get('memory_store', 'Stored')}: {self.memory}")
        except:
            pass

    def memory_recall(self):
        """Recall value from memory"""
        self.current_input = str(self.memory)
        self.result_var.set(self.current_input)

    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        trans = self.translations[self.current_language]
        messagebox.showinfo("Memory", trans.get('memory_clear', 'Memory cleared'))

    def update_converter_units(self, event=None):
        """Update converter unit options"""
        conv_type = self.conv_type.get().lower()

        units_map = {
            'length': ['m', 'km', 'cm', 'mm', 'mi', 'ft', 'in'],
            'weight': ['kg', 'g', 'mg', 'lb', 'oz'],
            'temperature': ['C', 'F', 'K'],
            'currency': ['USD', 'EUR', 'RON', 'GBP', 'JPY']
        }

        units = units_map.get(conv_type, ['m', 'km'])
        self.from_unit['values'] = units
        self.to_unit['values'] = units
        self.from_unit.set(units[0])
        self.to_unit.set(units[1] if len(units) > 1 else units[0])
        self.conv_result.config(text="")

    def perform_conversion(self):
        """Perform unit conversion"""
        try:
            value = float(self.conv_value.get())
            conv_type = self.conv_type.get().lower()
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            if conv_type == 'temperature':
                # Temperature conversion
                if from_unit == 'C':
                    if to_unit == 'F':
                        result = value * 9 / 5 + 32
                    elif to_unit == 'K':
                        result = value + 273.15
                    else:
                        result = value
                elif from_unit == 'F':
                    if to_unit == 'C':
                        result = (value - 32) * 5 / 9
                    elif to_unit == 'K':
                        result = (value - 32) * 5 / 9 + 273.15
                    else:
                        result = value
                else:  # Kelvin
                    if to_unit == 'C':
                        result = value - 273.15
                    elif to_unit == 'F':
                        result = (value - 273.15) * 9 / 5 + 32
                    else:
                        result = value
            else:
                # Standard conversion
                rates = self.conversion_rates[conv_type]
                # Convert to base unit first, then to target unit
                base_value = value / rates[from_unit]
                result = base_value * rates[to_unit]

            self.conv_result.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")

            # Add to history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                'expression': f"Convert: {value} {from_unit} to {to_unit}",
                'result': f"{result:.4f} {to_unit}",
                'timestamp': timestamp,
                'type': 'conversion'
            })
            self.save_history()
            self.update_history_display()

            # Update statistics
            self.statistics['conversions'] += 1
            self.save_statistics()

        except Exception as e:
            self.statistics['errors'] += 1
            self.save_statistics()
            self.show_error()

    def update_history_display(self):
        """Update history text widget"""
        self.history_text.delete('1.0', tk.END)
        for item in reversed(self.history[-50:]):  # Show last 50
            entry_type = item.get('type', 'calculation').upper()
            self.history_text.insert(tk.END,
                                     f"[{entry_type}] {item['timestamp']}\n{item['expression']} = {item['result']}\n\n")

    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        self.save_history()
        self.update_history_display()
        trans = self.translations[self.current_language]
        messagebox.showinfo("History", trans.get('clear_history', 'History cleared'))

    def export_results(self):
        """Export history to file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")]
            )
            if filename:
                if filename.endswith('.csv'):
                    with open(filename, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Timestamp', 'Type', 'Expression', 'Result'])
                        for item in self.history:
                            writer.writerow([
                                item['timestamp'],
                                item.get('type', 'calculation'),
                                item['expression'],
                                item['result']
                            ])
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write("Calculator History Export\n")
                        f.write("=" * 60 + "\n\n")
                        for item in self.history:
                            entry_type = item.get('type', 'calculation').upper()
                            f.write(f"[{entry_type}] {item['timestamp']}\n")
                            f.write(f"{item['expression']} = {item['result']}\n\n")

                trans = self.translations[self.current_language]
                messagebox.showinfo("Success", trans.get("export_success", "Export successful!"))
        except Exception as e:
            trans = self.translations[self.current_language]
            messagebox.showerror("Error", trans.get("export_error", "Export failed!"))

    def show_statistics(self):
        """Show usage statistics dialog"""
        trans = self.translations[self.current_language]

        stats_window = tk.Toplevel(self.root)
        stats_window.title(trans.get('stats_title', 'Statistics'))
        stats_window.geometry("300x200")
        stats_window.resizable(False, False)

        frame = ttk.Frame(stats_window, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text=trans.get('stats_title', 'Usage Statistics'),
                  font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text=trans.get('stats_calculations', 'Calculations:')).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        ttk.Label(frame, text=str(self.statistics['calculations']),
                  font=('Arial', 10, 'bold')).grid(row=1, column=1, sticky=tk.E, pady=5)

        ttk.Label(frame, text=trans.get('stats_conversions', 'Conversions:')).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        ttk.Label(frame, text=str(self.statistics['conversions']),
                  font=('Arial', 10, 'bold')).grid(row=2, column=1, sticky=tk.E, pady=5)

        ttk.Label(frame, text=trans.get('stats_errors', 'Errors:')).grid(
            row=3, column=0, sticky=tk.W, pady=5)
        ttk.Label(frame, text=str(self.statistics['errors']),
                  font=('Arial', 10, 'bold')).grid(row=3, column=1, sticky=tk.E, pady=5)

        ttk.Button(frame, text=trans.get('close_button', 'Close'),
                   command=stats_window.destroy).grid(row=4, column=0, columnspan=2, pady=(20, 0))

    def show_error(self):
        """Show error message"""
        trans = self.translations[self.current_language]
        messagebox.showerror(
            trans.get("error_title", "Error"),
            trans.get("error_message", "Invalid expression")
        )

    def show_about(self):
        """Show about dialog"""
        trans = self.translations[self.current_language]
        messagebox.showinfo(
            trans.get("about_title", "About"),
            trans.get("about_message", "Advanced Calculator Pro v2.0")
        )

    def change_language(self, event=None):
        """Change application language"""
        selection = self.lang_combo.get()
        lang_map = {
            "English": "en",
            "Română": "ro",
            "Español": "es",
            "Français": "fr",
            "Deutsch": "de"
        }
        self.current_language = lang_map.get(selection, "en")
        self.apply_localization()

    def change_theme(self, event=None):
        """Change application theme"""
        selection = self.theme_combo.get()
        self.current_theme = "dark" if selection == "Dark" else "light"
        self.apply_theme()

    def apply_theme(self):
        """Apply visual theme"""
        if self.current_theme == "dark":
            # Dark theme colors
            bg_color = "#2b2b2b"
            fg_color = "#ffffff"
            self.root.configure(bg=bg_color)
            # Note: ttk themes are limited, but we set what we can
            style = ttk.Style()
            style.theme_use('clam')  # Use clam theme for better dark mode
        else:
            # Light theme (default)
            bg_color = "#f0f0f0"
            fg_color = "#000000"
            self.root.configure(bg=bg_color)
            style = ttk.Style()
            style.theme_use('default')

    def apply_localization(self):
        """Apply current language translations"""
        if self.current_language not in self.translations:
            self.current_language = "en"

        trans = self.translations[self.current_language]

        # Update window title
        self.root.title(trans.get("app_title", "Advanced Calculator Pro"))

        # Update control labels
        self.lang_label.config(text=trans.get("language_label", "Language:"))
        self.theme_label.config(text=trans.get("theme_label", "Theme:"))
        self.about_btn.config(text=trans.get("about_menu", "About"))
        self.stats_btn.config(text=trans.get("stats_button", "Statistics"))
        self.result_label.config(text=trans.get("result_label", "Result:"))

        # Update notebook tabs
        self.notebook.tab(0, text=trans.get("basic_tab", "Basic"))
        self.notebook.tab(1, text=trans.get("scientific_tab", "Scientific"))
        self.notebook.tab(2, text=trans.get("converter_tab", "Converter"))
        self.notebook.tab(3, text=trans.get("history_tab", "History"))

        # Update converter labels
        self.value_label.config(text=trans.get("value_label", "Value:"))
        self.from_label.config(text=trans.get("from_label", "From:"))
        self.to_label.config(text=trans.get("to_label", "To:"))
        self.convert_btn.config(text=trans.get("convert_label", "Convert"))

        # Update history buttons
        self.clear_history_btn.config(text=trans.get("clear_history", "Clear History"))
        self.export_btn.config(text=trans.get("export_button", "Export"))


def main():
    root = tk.Tk()
    root.title("Advanced Calculator Pro")
    root.geometry("600x650")
    root.resizable(True, True)

    # Locales directory will be created automatically if missing
    app = AdvancedCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()