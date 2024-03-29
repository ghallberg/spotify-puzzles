import unittest
import zipfsong

class AlbumParserTests(unittest.TestCase):
    def testKnownAlbums(self):
        albums = (((((30,"one"), (30,"two"), (15,"three"), (25,"four")), 2),
                    ["four","two"]),
                (((
                        (197812,"re_hash"),
                        (78906,"5_4"),
                        (189518,"tomorrow_comes_today"),
                        (39453,"new_genious"),
                        (210492,"clint_eastwood"),
                        (26302,"man_research"),
                        (22544,"punk"),
                        (19727,"sound_check"),
                        (17535,"double_bass"),
                        (18782,"rock_the_house"),
                        (198189,"19_2000"),
                        (13151,"latin_simone"),
                        (12139,"starshine"),
                        (11272,"slow_country"),
                        (10521,"m1_a1")
                        ), 3),

                    ["19_2000","clint_eastwood","tomorrow_comes_today"]),
                )
        for input, output in albums:
            result = zipfsong.best_from_album(*input)
            self.assertEqual(result,output)


