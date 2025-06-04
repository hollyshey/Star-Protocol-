import unittest
import numpy as np
from star_protocol import combine_bits, harmonic_wave, StarNode, SILENCE, draw_star_pattern

class TestStarProtocol(unittest.TestCase):

    def test_combine_bits(self):
        self.assertEqual(combine_bits(SILENCE, SILENCE), 'هیچ')
        self.assertEqual(combine_bits(0, 1), 'تعامل')
        self.assertEqual(combine_bits(1, 0), 'تعامل')
        self.assertEqual(combine_bits(0, SILENCE), 'نیمه فعال')
        self.assertEqual(combine_bits(SILENCE, 0), 'نیمه فعال')
        self.assertEqual(combine_bits(1, SILENCE), 'نیمه خاموش')
        self.assertEqual(combine_bits(SILENCE, 1), 'نیمه خاموش')
        self.assertEqual(combine_bits(0, 0), 'نامشخص')
        self.assertEqual(combine_bits(1, 1), 'نامشخص')

    def test_harmonic_wave(self):
        t = np.linspace(0, 1, 100)
        np.testing.assert_array_equal(harmonic_wave(t, 'هیچ'), np.zeros_like(t))
        self.assertTrue(np.allclose(harmonic_wave(t, 'تعامل'), np.sin(2 * np.pi * 5 * t)))
        self.assertTrue(np.allclose(harmonic_wave(t, 'نیمه فعال'), 0.5 * np.sin(2 * np.pi * 3 * t)))
        self.assertTrue(np.allclose(harmonic_wave(t, 'نیمه خاموش'), 0.5 * np.sin(2 * np.pi * 7 * t)))
        np.testing.assert_array_equal(harmonic_wave(t, 'نامعلوم'), np.zeros_like(t))

    def test_star_node_pulse_and_evaluate(self):
        star = StarNode(seed="test", freq=1.0)
        initial_wave = star.internal_wave.copy()
        star.pulse()
        self.assertNotEqual(np.sum(initial_wave), np.sum(star.internal_wave))
        status = star.evaluate()
        self.assertIn(status, ['فعال', 'قرنطینه'])

    def test_draw_star_pattern_no_error(self):
        points = [(0,0), (1,0), (1,1), (0,1), (0.5, 1.5)]
        sequence = [1, 3, 5, 2, 4]
        try:
            draw_star_pattern(points, sequence)
        except Exception as e:
            self.fail(f"draw_star_pattern raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
