import time
import uiautomator2 as automator


class App(object):
	"""docstring for App"""
	def __init__(self, apk):
		super(App, self).__init__()
		self.device = automator.connect()
		self.apk=apk

	def __str__(self):
		return self.apk

	def start(self):
		self.device.app_start(self.apk)
		print(f"App: {self.__str__()} started!")

	def stop(self):
		self.device.app_stop(self.apk)
		print(f"App: {self.__str__()} closed!")

	def do_jobs(self):
		pass

	def wait(self, peroid=1):
		time.sleep(peroid)

	def exists(self, xpath):
		return self.device.xpath(xpath).exists

	def click(self, xpaths, timeout=2):
		targets = []
		if isinstance(xpaths, str):
			targets.append(xpaths)
		if isinstance(xpaths, list):
			targets.extend(xpaths)

		for xpath in targets:
			self.device.xpath(xpath).click_exists(timeout)


	def run(self):
		self.start()
		self.wait()
		self.do_jobs()
		self.wait()
		self.stop()
