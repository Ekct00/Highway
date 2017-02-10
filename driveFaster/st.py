key = "苍井空"
page_number = 4
url = []
allow_domains = ["torrentkitty.tv"]
for i in range(0, page_number):
    url.append("https://www.torrentkitty.tv/search/" + key + "/" + str(i + 1))
print(url)