import os
import json
import matplotlib.pyplot
import numpy
import sys
try:
  token = f"""-H 'Authorization: token {open('token.txt', 'r').read()}' """
except:
  token = ""

data = json.loads(os.popen(f"curl -s {token}https://api.github.com/users/{sys.argv[1]}/repos").read())

def normal(num, idk):
	return int(num * 100/idk)

lang = {}

for idk in data:
	for langs in list(json.loads(os.popen(f'curl -s {token}https://api.github.com/repos/NacreousDawn596/{idk["name"]}/languages').read()).keys()):
		if langs == "message" or langs == "documentation_url":
			pass
		else:
			try:
				lang[langs] += 1
			except:
				lang[langs] = 1

lang = dict(sorted(lang.items(),key= lambda x:x[1]))

for idk in range(0, len(list(lang.keys()))): print(f"{list(lang.keys())[idk]}: {list(lang.values())[idk]}")

ax = matplotlib.pyplot.figure()
matplotlib.pyplot.pie(numpy.array([normal(idk, sum(list(lang.values()))) for idk in list(lang.values())]), labels=[f"{idk}: {int(normal(list(lang.values())[list(lang.keys()).index(idk)], sum(list(lang.values()))))}%" for idk in list(lang.keys())])
matplotlib.pyplot.show()
ax.savefig(f'{sys.argv[1]}.png', dpi=200)
