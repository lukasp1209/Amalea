import unittest
import os
import sys
import importlib.util
import numpy as np
from unittest.mock import patch
from sklearn.linear_model import LinearRegression, Ridge

class TestDeepLearningUnits(unittest.TestCase):
    
    def setUp(self):
        # Verhindert, dass plt.show() blockiert, falls Labs Plots anzeigen
        self.patcher = patch('matplotlib.pyplot.show')
        self.mock_show = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def _import_lab(self, unit_path):
        """
        Hilfsfunktion zum Importieren von lab.py aus einem Unit-Ordner.
        Notwendig, da Ordnernamen mit Zahlen beginnen und nicht direkt importierbar sind.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, unit_path, "code", "lab.py")
        
        if not os.path.exists(file_path):
            self.skipTest(f"Lab file not found: {file_path}")

        spec = importlib.util.spec_from_file_location("lab", file_path)
        module = importlib.util.module_from_spec(spec)
        # Achtung: Dies führt Top-Level Code im Modul aus (Prints etc.)
        spec.loader.exec_module(module)
        return module

    def test_unit_02_sigmoid(self):
        """Testet die Sigmoid-Funktion in Unit 02."""
        # Versuche Import, falls Unit 02 existiert
        try:
            lab = self._import_lab("02_Logistische_Regression")
        except unittest.SkipTest:
            return

        # Sigmoid Eigenschaften prüfen
        if hasattr(lab, 'sigmoid'):
            self.assertAlmostEqual(lab.sigmoid(0), 0.5)
            self.assertAlmostEqual(lab.sigmoid(100), 1.0)
            self.assertAlmostEqual(lab.sigmoid(-100), 0.0)

    def test_unit_03_softmax(self):
        """Testet die Softmax-Implementierung in Unit 03."""
        lab = self._import_lab("03_Softmax_Multiclass")
        
        logits = np.array([1.0, 2.0, 3.0])
        probs = lab.softmax(logits)
        
        # Summe muss 1 sein
        self.assertAlmostEqual(np.sum(probs), 1.0)
        # Werte müssen positiv sein
        self.assertTrue(np.all(probs >= 0))
        # Ordnung muss erhalten bleiben (3.0 > 2.0 > 1.0)
        self.assertTrue(probs[2] > probs[1] > probs[0])

    def test_unit_04_regularization_concept(self):
        """
        Prüft das Konzept von Unit 04: 
        Ridge Regression (L2) sollte kleinere Gewichte haben als Lineare Regression.
        """
        # Wir nutzen hier sklearn direkt, um das Lernziel der Unit zu verifizieren
        X = np.random.rand(10, 5)
        y = np.dot(X, np.array([1, 2, 3, 4, 5])) + np.random.normal(0, 0.1, 10)

        # 1. Ohne Regularisierung
        lin_reg = LinearRegression()
        lin_reg.fit(X, y)
        
        # 2. Mit Regularisierung (Ridge)
        ridge_reg = Ridge(alpha=10.0)
        ridge_reg.fit(X, y)

        # Die Norm der Gewichte sollte bei Ridge kleiner sein
        self.assertLess(np.linalg.norm(ridge_reg.coef_), np.linalg.norm(lin_reg.coef_))

    def test_unit_05_gradient(self):
        """Testet die Gradienten-Berechnung in Unit 05."""
        lab = self._import_lab("05_Optimierung")
        
        # Funktion ist f(x,y) = x^2 + 10y^2
        # Gradient sollte [2x, 20y] sein
        x, y = 2.0, 1.0
        grad = lab.grad_f(x, y)
        
        self.assertEqual(grad[0], 4.0)  # 2 * 2
        self.assertEqual(grad[1], 20.0) # 20 * 1

    def test_unit_06_convolution_shape(self):
        """Testet, ob die Convolution die Bildgröße korrekt reduziert (Valid Padding)."""
        try:
            lab = self._import_lab("06_CNN_Basics")
        except unittest.SkipTest:
            return
            
        # Wenn das Lab feature_map_v berechnet hat
        if hasattr(lab, 'feature_map_v'):
            # Input 10x10, Kernel 3x3, Valid Padding -> Output 8x8
            self.assertEqual(lab.feature_map_v.shape, (8, 8))

    def test_unit_07_attention(self):
        """Testet den Attention-Mechanismus (Unit 07)."""
        try:
            # Versuche den Ordnernamen aus build_book.py oder Standard
            lab = self._import_lab("07_Attention_Transformer")
        except unittest.SkipTest:
            try:
                lab = self._import_lab("07_Attention")
            except unittest.SkipTest:
                return

        if hasattr(lab, 'scaled_dot_product_attention'):
            Q = np.random.randn(4, 8)
            output, weights = lab.scaled_dot_product_attention(Q, Q, Q)
            # Attention Weights müssen sich zu 1 summieren (letzte Achse)
            self.assertAlmostEqual(np.sum(weights[0]), 1.0)

if __name__ == '__main__':
    unittest.main()