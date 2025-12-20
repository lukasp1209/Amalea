import unittest
import os
import sys
import importlib.util
import numpy as np

class TestDeepLearningUnits(unittest.TestCase):
    
    def _import_lab(self, unit_path):
        """
        Hilfsfunktion zum Importieren von lab.py aus einem Unit-Ordner.
        Notwendig, da Ordnernamen mit Zahlen beginnen und nicht direkt importierbar sind.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, unit_path, "code", "lab.py")
        
        if not os.path.exists(file_path):
            self.skipTest(f"Lab file not found: {file_path}")

        spec = importlib.util.spec_from_file_location("lab", file_path)
        module = importlib.util.module_from_spec(spec)
        # Achtung: Dies führt Top-Level Code im Modul aus (Prints etc.)
        spec.loader.exec_module(module)
        return module

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

    def test_unit_05_gradient(self):
        """Testet die Gradienten-Berechnung in Unit 05."""
        lab = self._import_lab("05_Optimierung")
        
        # Funktion ist f(x,y) = x^2 + 10y^2
        # Gradient sollte [2x, 20y] sein
        x, y = 2.0, 1.0
        grad = lab.grad_f(x, y)
        
        self.assertEqual(grad[0], 4.0)  # 2 * 2
        self.assertEqual(grad[1], 20.0) # 20 * 1

if __name__ == '__main__':
    unittest.main()