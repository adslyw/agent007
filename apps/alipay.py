from .app import App

class Alipay(App):
	"""docstring for Alipay"""
	def __init__(self):
		super(Alipay, self).__init__('com.eg.android.AlipayGphone')

	def go_home(self):
		self.click(
			'//*[@resource-id="com.alipay.android.phone.openplatform:id/tab_description"]'
		)

	def go_mypage(self):
		self.click(
			'//*[@resource-id="com.alipay.android.phone.wealth.home:id/tab_description"]'
		)

	def go_back(self):
		self.click(
			'//*[@resource-id="com.alipay.mobile.nebula:id/h5_nav_back"]'
		)

	def go_membership(self):
		self.click(
			'//*[@text="支付宝会员"]'
		)

	def checkin(self):
		def baba_farm():
			def collect_baba():
				self.click('//*[@resource-id="root"]/android.view.View[1]/android.view.View[5]/android.view.View[3]/android.view.View[1]/android.view.View[1]')
				self.click('//*[@text="A*ccswT6bSKCsAAAAAAAAAAAAAARQnAQ"]')
				self.click('//*[@text="领取"]')
				self.click('//*[@resource-id="root"]/android.view.View[1]/android.view.View[5]/android.view.View[1]/android.view.View[2]')
				self.click('//*[@resource-id="tmfarm-game-game"]')
			if not self.exists('//*[@text="去芭芭农场给果树施肥"]'):
				return False
			self.click('//*[@text="去芭芭农场给果树施肥"]')
			collect_baba()

		def taobaogold():
			if not self.exists('//*[@text="逛淘金币小镇领金币"]'):
				return False

			# self.click('//*[@text="返回"]')
			self.click('//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]')
			# self.click('')

		def fifteen_point():
			self.click('//*[@text="逛15秒赚积分"]')
			self.wait(20)

		def everyday_point():
			self.click('//*[@text="每日签到"]')
			

		self.go_home()
		self.wait(3)
		self.click('//*[@text="我的小程序"]')
		self.go_membership()		
		self.wait(3)
		everyday_point()
		baba_farm()
		taobaogold()
		fifteen_point()

		self.go_back()
		self.go_back()
		self.go_back()

	def collect_energy(self):
		import random
		import time
		def fetch_energy(cnt):
			print("开始第%d次偷能量！" % cnt)

			# 开始扫描点击有能力出现的区域  
			for x in range(150,1000,150):
				for y in range(600,900,150):
					self.device.long_click(x + random.randint(10,20), y + random.randint(10,20), 0.1)
					time.sleep(0.01)
					if cnt != 1:
						self.device.click(536,1816)
					close_help_dialog()
					return False if return_forest() else True

		def find_more():
			if not self.exists("//*[@resource-id='J_tree_dialog_wrap']"):
				return False

			btn = self.device.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
			# 找能量按钮的坐标
			self.device.click(1000, btn[3] - 80)
			return True

		def close_help_dialog():
			if self.device.xpath('//*[@text="帮好友复活能量"]').exists:
				self.click('//*[@text="关闭"]')


		def return_forest():
			if self.device.xpath('//*[@text="返回蚂蚁森林 >"]').exists:
				self.click('//*[@text="返回蚂蚁森林 >"]')
				return True

			return False

		def close_protect_widow():
			if self.device.xpath('//*[@text="领取保护地"]').exists:
				self.go_back

		self.go_home()
		self.wait(3)
		self.click([
			'//*[@text="我的小程序"]',
			'//*[@text="蚂蚁森林"]',
		])

		count = 1
		while True:
			if not fetch_energy(count):
				break
			if not find_more():
				break

			count += 1


	def do_jobs(self):
		self.checkin()
		self.collect_energy()
		self.go_home()
