## 初始化
实例化JPush对象

```
_jpush = jpush.JPush(app_key, master_secret)
```

参数说明

> app_key  https://www.jpush.cn/ 控制台获取

> master_secret  https://www.jpush.cn/ 控制台获取

返回值

>  JPush 实例

## Push api

###  初始化push对象

```
push = _jpush.create_push()
```
参数说明 （无）

返回值

> push 实例

####  audience 设置

##### tag 设置
```
tag(*tags)
```

参数说明

tags 例如：tag("tag1", "tag2")


返回值
> payload 字典

##### tag_and 设置
```
tag_and(*tag_ands)
```

参数说明

tags 例如：tag_and("tag1", "tag2")

返回值
> payload 字典

##### alias 设置
```
alias(*alias)
```

参数说明

alias 例如：alias("alias1", "alias2")

返回值
> payload 字典

##### registration_id 设置
```
registration_id(*reg_ids)
```

参数说明

registration_id 例如：tag("registration_id1", "registration_id2")

返回值

> payload 字典

##### 推送目标说明

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册ID、分群、广播等。

* all

如果要发广播（全部设备），则直接填写 “all”。

* 推送目标

广播外的设备选择方式，有如下几种：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr bgcolor="#D3D3D3">
			<th >关键字</th>
			<th >含义</th>
			<th >类型</th>
			<th >说明</th>
			<th >备注</th>
		</tr>
		<tr >
			<td>tag</td>
			<td>JSON Array</td>
			<td>标签</td>
			<td>数组。多个标签之间是 OR 的关系，即取并集。 </td>
			<td>用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。<ul style="margin-bottom: 0;"><li>有效的 tag 组成：字母（区分大小写）、数字、下划线、汉字。</li><li>限制：每一个 tag 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>tag_and</td>
			<td>JSON Array</td>
			<td>标签AND</td>
			<td>数组。多个标签之间是 AND 关系，即取交集。</td>
			<td>注册与 tag 区分。一次推送最多 20 个。</td>
		</tr>
		<tr >
			<td>alias</td>
			<td>JSON Array</td>
			<td>别名</td>
			<td>数组。多个别名之间是 OR 关系，即取并集。</td>
			<td>用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。<ul style="margin-bottom: 0;"><li>有效的 alias 组成：字母（区分大小写）、数字、下划线、汉字。</li><li>限制：每一个 alias 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>registration_id</td>
			<td>JSON Array</td>
			<td>注册ID</td>
			<td>数组。多个注册ID之间是 OR 关系，即取并集。</td>
			<td>设备标识。一次推送最多 1000 个。</td>
		</tr>
	</table>
</div>


####  notification 设置
```
notification(alert=None, ios=None, android=None, winphone=None)
```
参数说明

* alert

> 通知的内容在各个平台上，都可能只有这一个最基本的属性 "alert"。
这个位置的 "alert" 属性（直接在 notification 对象下），是一个快捷定义，各平台的 alert 信息如果都一样，则可不定义。如果各平台有定义，则覆盖这里的定义。

* ios

>  ios payload 字典 查看 [ios payload](https://github.com/jpush/jpush-api-python-client/blob/master/docs/push/push.md#ios-payload)

* android

>  android payload 字典 查看 [android payload](https://github.com/jpush/jpush-api-python-client/blob/master/docs/push/push.md#android-payload)


返回值

> notification payload

#####  ios payload
```
ios(alert=None, badge=None, sound=None, content_available=False,
    extras=None, sound_disable=False)
```

参数说明
<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th width="20%">含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td width="20%">通知内容</td>
			<td>这里指定了，将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。支持 emoji 表情。</td>
		</tr>
		<tr >
			<td>sound</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%">通知提示声音</td>
			<td>如果无此字段，则此消息无声音提示；有此字段，如果找到了指定的声音就播放该声音，否则播放默认声音,如果此字段为空字符串，iOS 7 为默认声音，iOS 8 为无声音。(消息) 说明：JPush 官方 API Library (SDK) 会默认填充声音字段。提供另外的方法关闭声音。</td>
		</tr>
		<tr >
			<td>badge</td>
			<td>int</td>
			<td>可选</td>
			<td width="20%">应用角标</td>
			<td>如果不填，表示不改变角标数字；否则把角标数字改为指定的数字；为 0 表示清除。JPush 官方 API Library(SDK) 会默认填充badge值为"+1",详情参考：<a href="http://blog.jpush.cn/ios_apns_badge_plus/">badge +1</a></td>
		</tr>
		<tr >
			<td>content-available</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">推送唤醒</td>
			<td>推送的时候携带"content-available":true 说明是 Background Remote Notification，如果不携带此字段则是普通的Remote Notification。详情参考：<a href="../../client/ios_tutorials/#ios-7-background-remote-notification">Background Remote Notification</a></td>
		</tr>
		<tr >
			<td>category</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%"> </td>
			<td>IOS8才支持。设置APNs payload中的"category"字段值</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td width="20%">扩展字段</td>
			<td>这里自定义 Key/value 信息，以供业务使用。</td>
		</tr>
	</table>
</div>

返回值

> ios payload 字典

#####  android payload
```
android(alert, title=None, builder_id=None, extras=None)
```
参数说明
<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%" >选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td>通知内容</td>
			<td>这里指定了，则会覆盖上级统一指定的 alert 信息；内容可以为空字符串，则表示不展示到通知栏。</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>通知标题</td>
			<td>如果指定了，则通知里原来展示 App名称的地方，将展示成这个字段。</td>
		</tr>
		<tr >
			<td>builder_id</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏样式ID</td>
			<td>Android SDK 可设置通知栏样式，这里根据样式 ID 来指定该使用哪套样式。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>扩展字段</td>
			<td>这里自定义 JSON 格式的 Key/Value 信息，以供业务使用。</td>
		</tr>
	</table>
</div>


返回值

> android payload 字典

####  message 设置

```
message(msg_content, title=None, content_type=None, extras=None)
```

参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>含义</th>
		</tr>
		<tr >
			<td>msg_content</td>
			<td>string</td>
			<td>必填</td>
			<td>消息内容本身</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>消息标题</td>
		</tr>
		<tr >
			<td>content_type</td>
			<td>string</td>
			<td>可选</td>
			<td>消息内容类型</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>JSON 格式的可选参数</td>
		</tr>
	</table>
</div>

返回值

>message payload

####  smsmessage 设置

```
smsmessage(content,delay_time)
```

*  参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>示例</th>
		</tr>
		<tr >
			<td>content</td>
			<td>string</td>
			<td>必填</td>
			<td>不能超过480个字符。"你好,JPush"为8个字符。超过67个字符的内容（含签名）会被拆分成多条短信下发。</td>
		</tr>
		<tr >
			<td>delay_time</td>
			<td>int</td>
			<td>必填</td>
			<td>单位为秒，不能超过24小时。设置为0，表示立即发送短信。该参数仅对android平台有效，iOS 和 Winphone平台则会立即发送短信</td>
		</tr>
	</table>
</div>

*  返回值

> smsmessage payload

####  platform 设置

```
platform(*types)
```

*  参数说明

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios","winphone"。

*  返回值

> platform tuple

####  options 设置

```
options(options)
```

*  参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>sendno</td>
			<td>int</td>
			<td>可选</td>
			<td>推送序号</td>
			<td>纯粹用来作为 API 调用标识，API 返回时被原样返回，以方便 API 调用方匹配请求与返回。</td>
		</tr>
		<tr >
			<td>time_to_live</td>
			<td>int</td>
			<td>可选</td>
			<td>离线消息保留时长(秒)</td>
			<td>推送当前用户不在线时，为该用户保留多长时间的离线消息，以便其上线时再次推送。默认 86400 （1 天），最长 10 天。设置为 0 表示不保留离线消息，只有推送当前在线的用户可以收到。</td>
		</tr>
		<tr >
			<td>override_msg_id</td>
			<td>long</td>
			<td>可选</td>
			<td>要覆盖的消息ID</td>
			<td>如果当前的推送要覆盖之前的一条推送，这里填写前一条推送的 msg_id 就会产生覆盖效果，即：1）该 msg_id 离线收到的消息是覆盖后的内容；2）即使该 msg_id Android 端用户已经收到，如果通知栏还未清除，则新的消息内容会覆盖之前这条通知；覆盖功能起作用的时限是：1 天。如果在覆盖指定时限内该 msg_id 不存在，则返回 1003 错误，提示不是一次有效的消息覆盖操作，当前的消息不会被推送。</td>
		</tr>
		<tr >
			<td>apns_production</td>
			<td>boolean</td>
			<td>可选</td>
			<td>APNs是否生产环境</td>
			<td>True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。JPush 官方 API LIbrary (SDK) 默认设置为推送 “开发环境”。</td>
		</tr>
		<tr >
			<td>big_push_duration</td>
			<td>int</td>
			<td>可选</td>
			<td>定速推送时长(分钟)</td>
			<td>又名缓慢推送，把原本尽可能快的推送速度，降低下来，给定的n分钟内，均匀地向这次推送的目标用户推送。最大值为1400.未设置则不是定速推送。</td>
		</tr>
	</table>
</div>

*  返回值

> options 字典
