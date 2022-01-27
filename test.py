import time
import random
import uiautomator2 as u2

device = u2.connect(
    # '192.168.0.100'
)
print(device.wlan_ip)
print("打开支付宝")
device.app_start("com.eg.android.AlipayGphone")
time.sleep(2) ## 休眠2s等待支付宝完全启动

print("打开蚂蚁森林，等待5s……")
device(text="蚂蚁森林").click()
time.sleep(5) ## 我手机比较卡，进入蚂蚁森林后还需要几秒钟才能完全加载完   

def collect_energy(cnt):
    print("开始第%d次偷能量！" % cnt)

    # 开始扫描点击有能力出现的区域  
    for x in range(150,1000,150):
        for y in range(600,900,150):
            device.long_click(x + random.randint(10,20), y + random.randint(10,20), 0.1)
            time.sleep(0.01)
            if cnt != 1:
                device.click(536,1816)

def lookup_energy(device, timeout=2.0):
	device.xpath('//*[@text="找能量"]').click_exists(timeout)
	device.xpath('//*[@text="找能量"]').click_exists(timeout)

def exit_ant_forest(device, timeout=2.0):
	device.xpath(
		'//*[@resource-id="com.alipay.mobile.nebula:id/h5_nav_options"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]'
	).click_exists(timeout)

cnt = 1
while True:
    collect_energy(cnt)
    a = device.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds 
    device.click(1000, a[3]-80) # 找能量按钮的坐标 

    ## 如果页面出现了“返回我的森林”说明已经没有能量可偷了，结束
    if device.xpath('//*[@text="返回蚂蚁森林"]').click_exists(timeout=2.0):
        break
    cnt += 1
print("###结束###")
exit_ant_forest(device)