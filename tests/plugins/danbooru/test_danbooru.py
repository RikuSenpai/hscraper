import sys
sys.path.append('../../../hscraper/plugins')
sys.path.append('../../../hscraper/plugins/danbooru')
import danbooru_scraper
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.dan = danbooru_scraper.Danbooru()

    def test_clean_url_1(self):
        """
        Tests if clean_url removes weid danbooru extras
        From: https://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags=touhou&ms=1
        To:   https://danbooru.donmai.us/posts?tags=touhou
        """
        weird_url = "https://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags=touhou&ms=1"
        normal_url = "https://danbooru.donmai.us/posts?tags=touhou"
        
        self.assertEqual(self.dan.clean_url(weird_url), normal_url)
        
    def test_clean_url_2(self):
        """
        Tests if clean_url removes weid danbooru extras
        From: https://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags=touhou&ms=1
        To:   https://danbooru.donmai.us/posts?tags=touhou
        """
        weird_url = "https://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags=short_sleeves&ms=1"
        normal_url = "https://danbooru.donmai.us/posts?tags=short_sleeves"
        
        self.assertEqual(self.dan.clean_url(weird_url), normal_url)
        
    def test_scrap_for_pages(self):
        """
        It actually doesnt scrap anything, it only generates links for the pages from a given url.
        Tests if links are correctly generated. Must return a list with the urls.
        """
        given_url = "https://danbooru.donmai.us/posts?tags=short_sleeves"
        
        expected_ouput = ["https://danbooru.donmai.us/posts?tags=short_sleeves",
                          "https://danbooru.donmai.us/posts?page=2&tags=short_sleeves",
                          "https://danbooru.donmai.us/posts?page=3&tags=short_sleeves",
                          "https://danbooru.donmai.us/posts?page=4&tags=short_sleeves"]
        
        out = self.dan.scrap_for_pages(given_url, 4)
        for i in range(4):
            self.assertEqual(out[i], expected_ouput[i])
        
            
    def test_scrap_for_pages_skips_from_2(self):
        """
        Tests if skips pages 1 and 2 from 1 to 4
        """
        given_url = "https://danbooru.donmai.us/posts?tags=short_sleeves"
        
        expected_ouput = ["https://danbooru.donmai.us/posts?page=3&tags=short_sleeves",
                          "https://danbooru.donmai.us/posts?page=4&tags=short_sleeves"]
        
        out = self.dan.scrap_for_pages(given_url, 4, skip_from=2)
        for i in range(2):
            self.assertEqual(out[i], expected_ouput[i])
            
    def test_scrap_for_pages_skip_from_2_to_3(self):
        """
        It actually doesnt scrap anything, it only generates links for the pages from a given url.
        Tests if links are correctly generated. Must return a list with the urls.
        """
        given_url = "https://danbooru.donmai.us/posts?tags=short_sleeves"
        
        expected_ouput = ["https://danbooru.donmai.us/posts?page=2&tags=short_sleeves",
                          "https://danbooru.donmai.us/posts?page=3&tags=short_sleeves",]
            
        out = self.dan.scrap_for_pages(given_url, 4, skip_from=1, skip_to=3)
        print(out)
        for i in range(2):
            self.assertEqual(out[i], expected_ouput[i])
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()