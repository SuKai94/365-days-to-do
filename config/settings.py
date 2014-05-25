#!/usr/bin/env python
# coding: utf-8
import web
from config.url import urls

db = web.database(dbn='mysql', db='kaiyao', user='sk', pw='12345')

render = web.template.render('templates/', cache=False)

web.config.debug = True

replaceList = [
('(1)', '<img src="/static/images/face/1.gif"/>'),
('(2)', '<img src="/static/images/face/2.gif"/>'),
('(3)', '<img src="/static/images/face/3.gif"/>'),
('(4)', '<img src="/static/images/face/4.gif"/>'),
('(5)', '<img src="/static/images/face/5.gif"/>'),
('(6)', '<img src="/static/images/face/6.gif"/>'),
('(7)', '<img src="/static/images/face/7.gif"/>'),
('(8)', '<img src="/static/images/face/8.gif"/>'),
('(9)', '<img src="/static/images/face/9.gif"/>'),
('(10)', '<img src="/static/images/face/10.gif"/>'),
('(11)', '<img src="/static/images/face/11.gif"/>'),
('(12)', '<img src="/static/images/face/12.gif"/>'),
('(13)', '<img src="/static/images/face/13.gif"/>'),
('(14)', '<img src="/static/images/face/14.gif"/>'),
('(15)', '<img src="/static/images/face/15.gif"/>'),
('(16)', '<img src="/static/images/face/16.gif"/>'),
('(17)', '<img src="/static/images/face/17.gif"/>'),
('(18)', '<img src="/static/images/face/18.gif"/>'),
('(19)', '<img src="/static/images/face/19.gif"/>'),
('(20)', '<img src="/static/images/face/20.gif"/>'),
('(21)', '<img src="/static/images/face/21.gif"/>'),
('(22)', '<img src="/static/images/face/22.gif"/>'),
('(23)', '<img src="/static/images/face/23.gif"/>'),
('(24)', '<img src="/static/images/face/24.gif"/>'),
('(25)', '<img src="/static/images/face/25.gif"/>'),
('(26)', '<img src="/static/images/face/26.gif"/>'),
('(27)', '<img src="/static/images/face/27.gif"/>'),
('(28)', '<img src="/static/images/face/28.gif"/>'),
('(29)', '<img src="/static/images/face/29.gif"/>'),
('(30)', '<img src="/static/images/face/30.gif"/>'),
('(31)', '<img src="/static/images/face/31.gif"/>'),
('(32)', '<img src="/static/images/face/32.gif"/>'),
('(33)', '<img src="/static/images/face/33.gif"/>'),
('(34)', '<img src="/static/images/face/34.gif"/>'),
('(35)', '<img src="/static/images/face/35.gif"/>'),
('(36)', '<img src="/static/images/face/36.gif"/>'),
('(37)', '<img src="/static/images/face/37.gif"/>'),
('(38)', '<img src="/static/images/face/38.gif"/>'),
('(39)', '<img src="/static/images/face/39.gif"/>'),
('(40)', '<img src="/static/images/face/40.gif"/>'),
('(41)', '<img src="/static/images/face/41.gif"/>'),
('(42)', '<img src="/static/images/face/42.gif"/>'),
('(43)', '<img src="/static/images/face/43.gif"/>'),
('(44)', '<img src="/static/images/face/44.gif"/>'),
('(45)', '<img src="/static/images/face/45.gif"/>'),
('(46)', '<img src="/static/images/face/46.gif"/>'),
('(47)', '<img src="/static/images/face/47.gif"/>'),
('(48)', '<img src="/static/images/face/48.gif"/>'),
('(49)', '<img src="/static/images/face/49.gif"/>'),
('(50)', '<img src="/static/images/face/50.gif"/>'),
('(51)', '<img src="/static/images/face/51.gif"/>'),
('(52)', '<img src="/static/images/face/52.gif"/>'),
('(53)', '<img src="/static/images/face/53.gif"/>'),
('(54)', '<img src="/static/images/face/54.gif"/>'),
('(55)', '<img src="/static/images/face/55.gif"/>'),
('(56)', '<img src="/static/images/face/56.gif"/>'),
('(57)', '<img src="/static/images/face/57.gif"/>'),
('(58)', '<img src="/static/images/face/58.gif"/>'),
('(59)', '<img src="/static/images/face/59.gif"/>'),
('(60)', '<img src="/static/images/face/60.gif"/>'),
('(61)', '<img src="/static/images/face/61.gif"/>'),
('(62)', '<img src="/static/images/face/62.gif"/>'),
('(63)', '<img src="/static/images/face/63.gif"/>'),
('(64)', '<img src="/static/images/face/64.gif"/>'),
('(65)', '<img src="/static/images/face/65.gif"/>'),
('(66)', '<img src="/static/images/face/66.gif"/>'),
('(67)', '<img src="/static/images/face/67.gif"/>'),
('(68)', '<img src="/static/images/face/68.gif"/>'),
('(69)', '<img src="/static/images/face/69.gif"/>'),
('(70)', '<img src="/static/images/face/70.gif"/>'),
('(71)', '<img src="/static/images/face/71.gif"/>'),
('(72)', '<img src="/static/images/face/72.gif"/>'),
('(73)', '<img src="/static/images/face/73.gif"/>'),
('(74)', '<img src="/static/images/face/74.gif"/>'),
('(75)', '<img src="/static/images/face/75.gif"/>'),
('(76)', '<img src="/static/images/face/76.gif"/>'),
('(77)', '<img src="/static/images/face/77.gif"/>'),
('(78)', '<img src="/static/images/face/78.gif"/>'),
('(79)', '<img src="/static/images/face/79.gif"/>'),
('(80)', '<img src="/static/images/face/80.gif"/>'),
]

config = web.storage(
    site_name = '365 Days To Do',
    site_desc = '',
    static = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
web.template.Template.globals['replaceList'] = replaceList
