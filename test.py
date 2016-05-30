
import unittest
import seuif97


class Region1_Test(unittest.TestCase):

    def setUp(self):
        self.tab5 = [[3, 300, 0.100215168e-2, 0.115331273e3, 0.112324818e3, 0.392294792, 4.17301218, 0.150773921e4],
                     [80, 300, 0.971180894e-3, 0.184142828e3, 0.106448356e3,
                         0.368563852, 4.01008987, 0.163469054e4],
                     [3, 500, 0.120241800e-2, 0.975542239e3, 0.971934985e3, 2.58041912, 4.65580682, 0.124071337e4]]


    def test_specific_volume(self):
        places = 11
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.specific_volume(item[0], item[1]), item[2], places)


    def test_specific_enthalpy(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.specific_enthalpy(item[0], item[1]), item[3], places)


    def test_specific_internal_energy(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.specific_internal_energy(
                item[0], item[1]), item[4], places)


    def test_specific_entropy(self):
        places = 8
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.specific_entropy(item[0], item[1]), item[5], places)


    def test_specific_isobaric_heat_capacity(self):
        places = 8
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.specific_isobaric_heat_capacity(
                item[0], item[1]), item[6], places)


    def test_speed_of_sound(self):
        places = 5
        for item in self.tab5:
            self.assertAlmostEqual(seuif97.speed_of_sound(item[0], item[1]), item[7], places)


class additional_Test(unittest.TestCase):

    def setUp(self):
        self.tab6 = [[0.001, 0, 9.800980612e-4],
                     [90, 0, 91.92954727],
                     [1500, 3.4, 58.68294423]]


    def test_backward_equations(self):
        places = 8
        for item in self.tab6:
            self.assertAlmostEqual(seuif97.backward_equations(item[0], item[1]), item[2], places)


def suite_test():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Region1_Test))
    suite.addTest(unittest.makeSuite(additional_Test))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest = 'suite_test')
