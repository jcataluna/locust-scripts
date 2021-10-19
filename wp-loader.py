from locust import HttpUser, task, between
from pyquery import PyQuery
import random

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    def index_page(self):
        r = self.client.get("/blog/")
        pq = PyQuery(r.content)

        link_elements = pq(".blog-list-post h2 a")
        self.blog_urls = []

        for l in link_elements:
          if "href" in l.attrib:
            self.blog_urls.append(l.attrib["href"])

    def on_start(self):
        self.index_page()

    @task(1)
    def static_content(self):
        # images
        self.client.get("/img/logo/logo.png")
        self.client.get("/img/images/cta_img.png")
        self.client.get("/img/logo/logo.png")
        self.client.get("/img/images/footer_fire.png")
        # styles
        self.client.get("/css/compiled.css?id=629e6d86d0748098936a")
        # scripts
        self.client.get("/js/compiled.js?id=1a927dbcfa8d96520959")

    @task(3)
    def blog_post(self):
        url = random.choice(self.blog_urls)
        r = self.client.get(url)


    @task(3)
    def home_page(self):
        self.client.get("/blog/")   