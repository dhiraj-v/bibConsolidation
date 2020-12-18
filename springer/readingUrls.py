springerUrlPath = '/content/drive/MyDrive/Tech/IIIT/SecurityVisualizationSLR/springerLinks.txt'
springerURLs = open(springerUrlPath, "r")
content = springerURLs.read()
springerList = content.split(", ")
print(len(springerList))
