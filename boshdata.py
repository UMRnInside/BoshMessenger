import readjson

FORTUNE_CAP = 4096 # 2 ** 12

datafile = "data.json"
data = readjson.readJSON(datafile)

fortune_skel = data["famous"]
before = data["before"]
after = data["after"]

bosh = data["bosh"]
fortunes = []

# Bake fortunes
for af in after:
    for bef in before:
        for forts in fortune_skel:
            # Fortune skeleton goes like: "Mark Twain a, blah blah blah, b"
            baked = forts.replace("a", bef).replace("b", af)
            fortunes.append(baked)

# Avoid changes
fortunes = tuple(fortunes[:FORTUNE_CAP])

def set_topic(topic):
    for s in bosh:
        s.replace("x", topic)

if __name__ == "__main__":
    # Test
    print("\n".join(fortunes))
