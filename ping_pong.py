#/usr/bin/python3

import unittest

def pingpong(entrada):
    saques = entrada.split(':')
    jogador_a = saques[0]
    jogador_b = saques[1]
        
    soma = int(jogador_a) + int(jogador_b)
    
    if soma < 40:
        resultado_div = soma//5
    else:
        resultado_div = soma//2
        
    if resultado_div%2 == 0:
        return "jogador a"
    else:
        return "jogador b"

class PingPongTest(unittest.TestCase):

    def test_saques_1(self):
        self.assertEqual(pingpong("0:0"), "jogador a")
    def test_saques_2(self):
        self.assertEqual(pingpong("3:2"), "jogador b")
    def test_saques_3(self):
        self.assertEqual(pingpong("21:20"), "jogador a")
    def test_saques_4(self):
        self.assertEqual(pingpong("21:22"), "jogador b")

if __name__ == '__main__':
    #main(entrada)
    unittest.main()