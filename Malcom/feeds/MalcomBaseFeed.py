import urllib2
from bson.json_util import dumps, loads
from Malcom.model.datatypes import Ip, Url, Hostname, As 
from Malcom.feeds.feed import Feed
import Malcom.auxiliary.toolbox as toolbox

class MalcomBaseFeed(Feed):
	"""
	This gets data from other Malcom Instances 
	"""
	def __init__(self, name):
		super(MalcomBaseFeed, self).__init__(name, run_every="12h")
		self.enabled = False
		self.apikey = "ENTER-YOUR-API-KEY-HERE"
		self.malcom_host = "malcom.public.instance.com"

	def update(self):
		request = urllib2.Request("http://%s/public/api" % self.malcom_host, headers={'X-Malcom-API-Key': self.apikey})
		feed = urllib2.urlopen(request).read()

		
		self.analyze(feed)
		return True

	def analyze(self, line):
		elements = loads(line)
		test = []
		for elt in elements:
			new = self.model.save(elt, with_status=True)
			if new:
				self.elements_fetched += 1


