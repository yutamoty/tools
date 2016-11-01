#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pushybullet as pb
import time
import yaml

conf = yaml.load(open('config.yaml'))

pbapi = pb.PushBullet(conf['api_key'])
devices = pbapi.devices()

#ログアウト処理
def logout():
    driver.find_element_by_id("btnLogout").click()
    driver.close()
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    driver.close()
    driver.quit()

def jizenyoyaku():
    try:
        #通常速度に戻すお申し込み(１回分予約)を選択
        select = Select(driver.find_element_by_name("selectedRequestStatus"))
        #事前予約申し込み処理
        select.select_by_value("11")
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[11]/td/table/tbody/tr/td[2]/a").click()
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[9]/td/table/tbody/tr/td[2]/a").click()
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[3]/td/a").click()
        push = pb.NotePush('[OK]事前予約申し込み完了', '305ZT 低速解除')
        for x in devices :
            push.send(x)
    except:
        raise Exception('no jizenyoyaku')

def yoyaku():
    try:
        #通常速度に戻すお申し込み(１回分予約)を選択
        select = Select(driver.find_element_by_name("selectedRequestStatus"))
        #申し込み処理
        select.select_by_value("10")
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[11]/td/table/tbody/tr/td[2]/a").click()
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[9]/td/table/tbody/tr/td[2]/a").click()
        driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[3]/tbody/tr[3]/td/a").click()
        push = pb.NotePush('[OK]申し込み完了', '305ZT 低速解除')
        for x in devices :
            push.send(x)
    except:
        raise Exception('no yoyaku')

#ブラウザオブジェクト作成
driver = webdriver.PhantomJS()

#MyYmobileアクセス
driver.get("https://webmy.ymobile.jp/portal/loginMsn/")

#スクリーンショット作成
#driver.save_screenshot("screen_shot01.png")

#ログイン処理
try:
    driver.find_element_by_id("msisdn").send_keys(conf['userid'])
    driver.find_element_by_id("password").send_keys(conf['password'])
    driver.find_element_by_id("loginBtn").click()
except:
    driver.close()
    driver.quit()
    exit

#オンラインサポートに移動
driver.find_element_by_id("btnOnlineSupport_0").click()

##ウィンドウを移動
for handle in driver.window_handles:
    driver.switch_to_window(handle)

#契約内容照会/変更に移動
try:
    driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[9]/td/a").click()
except:
    push = pb.NotePush('[エラー]契約内容紹介/変更に移動', '305ZT 低速解除')
    for x in devices :
        push.send(x)
    logout()
    exit

#通常速度に戻すお申し込み・ご利用データ通信量の確認に移動
try:
    driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[2]/tbody/tr[8]/td/table/tbody/tr[13]/td[2]/a").click()
except:
    push = pb.NotePush('[エラー]通常速度に戻すお申し込み・ご利用データ通信量の確認に移動', '305ZT 低速解除')
    for x in devices :
        push.send(x)
    logout()
    exit

try:
    #通常速度に戻すお申し込み・予約・キャンセルに移動
    driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr/td/div[1]/a").click()
    yoyaku()
    time.sleep(300)
    #通常速度に戻すお申し込み・予約・キャンセルに移動
    driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr/td/div[1]/a").click()
    jizenyoyaku()
except:
    jizenyoyaku()
finally:
    #ログアウト処理
    logout()
    exit
